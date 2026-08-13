#!/usr/bin/env python3
"""
ingest.py — pull sources/sources.yaml's feeds, extract insights, write
tier-1 notes to ingest/. See skills/ingest/README.md for usage.

Deterministic plumbing (feed fetch, dedupe) is plain code; the one model
call per new entry is where judgment (extraction, relevance, framing) lives
— per MAINTAINER.md's working conventions.
"""

import argparse
import base64
import calendar
import html
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "skills"))
from lib import llm, transcribe  # noqa: E402  (needs sys.path set first)

USER_AGENT = "brianmadden-ai-ingest/0.1 (+https://brianmadden.ai)"
# Substack's content:encoded (and most other feeds checked) carry genuine
# full-text, not a truncated preview — 8000 was an arbitrary guess that cut
# 35-67% off real posts (confirmed 2026-08-11: Mollick, SemiAnalysis,
# Interconnects all exceeded it). Raised with real headroom; still finite
# as a safety valve against a malformed feed dumping something absurd.
MAX_CONTENT_CHARS = 50000
LAST_RUN_PATH = ROOT / "ingest" / ".last_run.json"
DEFAULT_SINCE_DAYS = 7.0  # fallback when there's no recorded prior run
MIN_SINCE_DAYS = 0.1      # floor (~2.4h), avoids a zero-width window on rapid reruns

TAG_RE = re.compile(r"<[^>]+>")
SLUG_RE = re.compile(r"[^a-z0-9]+")


# ---------------------------------------------------------------- sources --

def load_sources(path: Path) -> list[dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data.get("sources", [])


# ------------------------------------------------------------------ .env --

def load_dotenv(root: Path) -> None:
    env_path = root / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


# -------------------------------------------------------------- last run --

def read_last_run() -> datetime | None:
    if not LAST_RUN_PATH.exists():
        return None
    try:
        data = json.loads(LAST_RUN_PATH.read_text(encoding="utf-8"))
        return datetime.fromisoformat(data["last_run_utc"])
    except (json.JSONDecodeError, KeyError, ValueError):
        return None


def write_last_run(when: datetime) -> None:
    LAST_RUN_PATH.parent.mkdir(parents=True, exist_ok=True)
    LAST_RUN_PATH.write_text(
        json.dumps({"last_run_utc": when.isoformat()}, indent=2) + "\n", encoding="utf-8"
    )


def resolve_since_days(explicit: float | None) -> tuple[float, str]:
    """Returns (since_days, reason) for logging."""
    if explicit is not None:
        return explicit, "explicit --since-days"

    last_run = read_last_run()
    if last_run is None:
        return DEFAULT_SINCE_DAYS, "no recorded prior run, using default"

    elapsed_hours = (datetime.now(timezone.utc) - last_run).total_seconds() / 3600
    since_days = max(elapsed_hours / 24, MIN_SINCE_DAYS)
    return since_days, f"auto — {elapsed_hours:.1f}h since last run ({last_run.isoformat()})"


# -------------------------------------------------------------- fetching --

def strip_html(text: str) -> str:
    text = TAG_RE.sub(" ", text or "")
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


# Sources whose RSS <link> is always the podcast homepage, never the
# episode page, even though the site has real per-episode permalinks —
# confirmed 2026-08-12 (Brian caught a dead-end link in a published post;
# the actual pattern was findable by search, feeds.megaphone.fm/marketingai
# just doesn't expose it). {source_id: URL template with {n} for episode
# number, extracted from a "#N: ..." title prefix.}
EPISODE_URL_OVERRIDES = {
    "the-artificial-intelligence-show": "https://podcast.smarterx.ai/shownotes/{n}",
}
EPISODE_NUMBER_RE = re.compile(r"^#(\d+):")


def fix_episode_link(source_id: str, title: str, link: str) -> str:
    template = EPISODE_URL_OVERRIDES.get(source_id)
    if not template:
        return link
    m = EPISODE_NUMBER_RE.match(title)
    if not m:
        return link
    return template.format(n=m.group(1))


def fetch_entries(source: dict, since_days: float, max_per_source: int):
    """Returns (entries, error). entries is [] on error."""
    feed_url = source.get("feed_url")
    if not feed_url:
        return [], "no feed_url set"

    try:
        resp = requests.get(feed_url, timeout=15, headers={"User-Agent": USER_AGENT})
        resp.raise_for_status()
    except requests.RequestException as e:
        return [], f"fetch failed: {e}"

    parsed = feedparser.parse(resp.content)
    if parsed.bozo and not parsed.entries:
        return [], f"feed parse error: {parsed.get('bozo_exception')}"

    cutoff = datetime.now(timezone.utc) - timedelta(days=since_days)
    entries = []
    for raw in parsed.entries:
        struct = raw.get("published_parsed") or raw.get("updated_parsed")
        published_dt = None
        date_published = None
        if struct:
            published_dt = datetime.fromtimestamp(calendar.timegm(struct), tz=timezone.utc)
            if published_dt < cutoff:
                continue
            date_published = published_dt.strftime("%Y-%m-%d")

        content = ""
        if raw.get("content"):
            content = raw["content"][0].get("value", "")
        elif raw.get("summary"):
            content = raw["summary"]
        elif raw.get("description"):
            content = raw["description"]
        content = strip_html(content)
        truncated = len(content) > MAX_CONTENT_CHARS
        content = content[:MAX_CONTENT_CHARS]
        if truncated:
            content += " […truncated…]"

        title = (raw.get("title") or "").strip()
        link = (raw.get("link") or "").strip()
        link = fix_episode_link(source["id"], title, link)

        # feedparser surfaces the Podcasting 2.0 <podcast:transcript> tag
        # as podcast_transcript automatically (confirmed 2026-08-12, not
        # assumed) — {'url': ..., 'type': ...}. Audio enclosure is the
        # standard RSS <enclosure>. Both optional; only used if the
        # source's transcript_mode asks for them (see enrich_with_transcript()).
        transcript_tag = raw.get("podcast_transcript") or {}
        audio_url = None
        for enc in raw.get("enclosures", []) or []:
            if (enc.get("type") or "").startswith("audio/"):
                audio_url = enc.get("href")
                break

        entries.append({
            "title": title,
            "link": link,
            "author": (raw.get("author") or "").strip(),
            "date_published": date_published,
            "published_dt": published_dt,
            "content": content,
            "podcast_transcript_url": transcript_tag.get("url"),
            "audio_url": audio_url,
        })

    entries.sort(
        key=lambda e: e["published_dt"] or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return entries[:max_per_source], None


TRANSCRIPT_MAX_BYTES = 300 * 1024 * 1024  # ~300MB safety valve against a malformed enclosure


def enrich_with_transcript(entry: dict, source: dict) -> None:
    """Mutates entry['content'] in place with a real transcript, per the
    source's transcript_mode (docs/full-source-text-ingestion.md):
      - "published": fetch entry['podcast_transcript_url'] directly (the
        one confirmed case, 80000-hours-podcast, gives plain text for
        free — no transcription cost).
      - "transcribe": download entry['audio_url'] to a real OS temp file
        (never the repo working tree — MAINTAINER.md rule 2 extended to
        audio, see the planning doc), transcribe it, delete the file
        immediately after, transcribed or not.
      - anything else (unset, "none"): no-op, leaves show-notes content.
    Falls back to the existing show-notes content on any failure rather
    than crashing the run over one episode.
    """
    mode = source.get("transcript_mode")
    if mode not in ("published", "transcribe"):
        return

    if mode == "published":
        url = entry.get("podcast_transcript_url")
        if not url:
            print(f"    transcript_mode=published but no transcript URL on this episode — using show notes")
            return
        try:
            resp = requests.get(url, timeout=30, headers={"User-Agent": USER_AGENT})
            resp.raise_for_status()
        except requests.RequestException as e:
            print(f"    transcript fetch failed ({e}) — using show notes")
            return
        text = resp.text
        truncated = len(text) > MAX_CONTENT_CHARS
        entry["content"] = text[:MAX_CONTENT_CHARS] + (" […truncated…]" if truncated else "")
        print(f"    fetched published transcript ({len(text)} chars)")
        return

    # mode == "transcribe"
    audio_url = entry.get("audio_url")
    if not audio_url:
        print(f"    transcript_mode=transcribe but no audio enclosure on this episode — using show notes")
        return
    if not transcribe.is_configured():
        print(f"    {transcribe.required_env_var()} not set — using show notes instead of transcribing")
        return

    tmp_path = None
    try:
        # Stage 1: download. Errors here are about the audio fetch, not
        # transcription — kept in its own try/except so the two failure
        # modes get accurate messages rather than being conflated (both
        # stages can raise the same requests exception types, so telling
        # them apart requires separating the stages, not the exception
        # class).
        try:
            with requests.get(audio_url, timeout=60, stream=True, headers={"User-Agent": USER_AGENT}) as resp:
                resp.raise_for_status()
                suffix = Path(audio_url.split("?")[0]).suffix or ".mp3"
                with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
                    tmp_path = Path(tmp.name)
                    downloaded = 0
                    for chunk in resp.iter_content(chunk_size=1024 * 1024):
                        downloaded += len(chunk)
                        if downloaded > TRANSCRIPT_MAX_BYTES:
                            raise ValueError(f"audio enclosure exceeded {TRANSCRIPT_MAX_BYTES} bytes, aborting")
                        tmp.write(chunk)
        except (requests.RequestException, ValueError) as e:
            print(f"    audio download failed ({e}) — using show notes")
            return

        # Stage 2: transcription.
        try:
            print(f"    downloaded audio ({downloaded / 1_000_000:.1f}MB) — transcribing via {transcribe.current_provider()}/{transcribe.resolve_model()}...")
            text = transcribe.transcribe(tmp_path)
        except requests.RequestException as e:
            print(f"    transcription API call failed ({e}) — using show notes")
            return

        truncated = len(text) > MAX_CONTENT_CHARS
        entry["content"] = text[:MAX_CONTENT_CHARS] + (" […truncated…]" if truncated else "")
        print(f"    transcribed ({len(text)} chars)")
    finally:
        if tmp_path and tmp_path.exists():
            tmp_path.unlink()


X_API_BASE = "https://api.x.com/2"
X_TOKEN_URL = "https://api.x.com/2/oauth2/token"
X_ENV_VARS = ("X_CLIENT_ID", "X_CLIENT_SECRET", "X_ACCESS_TOKEN", "X_REFRESH_TOKEN")
EXTERNAL_LINK_MAX_CHARS = 20000  # per linked article — keeps one long page from dominating an entry


def x_is_configured() -> bool:
    return all(os.environ.get(v) for v in X_ENV_VARS)


def _update_env_var(key: str, value: str) -> None:
    """Rewrites one KEY=value line in the repo-root .env in place. Used
    when X rotates the refresh token on use (standard OAuth 2.0 practice)
    so the next run doesn't fail with a now-invalid one. .env is
    gitignored and local-only; this never touches anything committed."""
    env_path = ROOT / ".env"
    if not env_path.exists():
        return
    lines = env_path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith(f"{key}="):
            lines[i] = f"{key}={value}"
            break
    else:
        lines.append(f"{key}={value}")
    env_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _x_refresh_access_token() -> str:
    resp = requests.post(
        X_TOKEN_URL,
        auth=(os.environ["X_CLIENT_ID"], os.environ["X_CLIENT_SECRET"]),
        data={"grant_type": "refresh_token", "refresh_token": os.environ["X_REFRESH_TOKEN"]},
        timeout=15,
    )
    resp.raise_for_status()
    tokens = resp.json()
    new_refresh = tokens.get("refresh_token")
    if new_refresh and new_refresh != os.environ["X_REFRESH_TOKEN"]:
        _update_env_var("X_REFRESH_TOKEN", new_refresh)
        os.environ["X_REFRESH_TOKEN"] = new_refresh
    return tokens["access_token"]


def _fetch_external_link_content(url: str) -> str:
    """Best-effort fetch + strip of an external link's page text — Brian's
    ask (2026-08-12): if a post links to something, pull in what it's
    actually talking about, not just the post's own text. Never raises —
    one broken/paywalled/slow link shouldn't sink the whole run."""
    try:
        resp = requests.get(url, timeout=15, headers={"User-Agent": USER_AGENT})
        resp.raise_for_status()
    except requests.RequestException:
        return ""
    return strip_html(resp.text)[:EXTERNAL_LINK_MAX_CHARS]


def fetch_entries_x(source: dict, since_days: float, max_per_source: int):
    """Polls the authenticated X account's reverse-chronological home
    timeline — everyone it follows, in one call, rather than polling each
    person separately (docs/full-source-text-ingestion.md Workstream F).
    Same (entries, error) contract as fetch_entries(). For retweets/
    quotes, folds in the full referenced post's text, not just the
    wrapper; for posts linking elsewhere, fetches that page's content too.
    Both are ephemeral input to the one extraction call downstream, same
    as everything else — never persisted raw (MAINTAINER.md rule 2).
    """
    if not x_is_configured():
        return [], "X_CLIENT_ID/SECRET/ACCESS_TOKEN/REFRESH_TOKEN not set — see .env.example"

    try:
        access_token = _x_refresh_access_token()
    except requests.RequestException as e:
        return [], f"X auth failed: {e}"

    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        me_resp = requests.get(f"{X_API_BASE}/users/me", headers=headers, timeout=15)
        me_resp.raise_for_status()
    except requests.RequestException as e:
        return [], f"X 'get my user id' call failed: {e}"
    user_id = me_resp.json()["data"]["id"]

    start_time = (datetime.now(timezone.utc) - timedelta(days=since_days)).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        resp = requests.get(
            f"{X_API_BASE}/users/{user_id}/timelines/reverse_chronological",
            headers=headers,
            params={
                "max_results": min(max(max_per_source, 5), 100),  # X requires 5-100; sliced to max_per_source below
                "start_time": start_time,
                "tweet.fields": "created_at,author_id,entities,referenced_tweets,text",
                "expansions": "author_id,referenced_tweets.id,referenced_tweets.id.author_id",
                "user.fields": "username,name",
            },
            timeout=30,
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        return [], f"X timeline fetch failed: {e}"

    payload = resp.json()
    tweets = payload.get("data", []) or []
    included_tweets = {t["id"]: t for t in payload.get("includes", {}).get("tweets", [])}
    included_users = {u["id"]: u for u in payload.get("includes", {}).get("users", [])}

    entries = []
    for tw in tweets:
        author = included_users.get(tw.get("author_id"), {})
        username = author.get("username", "unknown")

        created_at = tw.get("created_at")
        published_dt = datetime.fromisoformat(created_at.replace("Z", "+00:00")) if created_at else None
        date_published = published_dt.strftime("%Y-%m-%d") if published_dt else None

        content_parts = [tw.get("text", "")]

        # Retweets/quotes: fold in the full referenced post, not just the wrapper.
        for ref in tw.get("referenced_tweets", []) or []:
            ref_tweet = included_tweets.get(ref.get("id"))
            if ref_tweet:
                ref_author = included_users.get(ref_tweet.get("author_id"), {})
                content_parts.append(
                    f"[{ref.get('type', 'referenced')} post by @{ref_author.get('username', 'unknown')}]: "
                    f"{ref_tweet.get('text', '')}"
                )

        # External links: fetch the linked page too. Skip links back to X
        # itself — those are already covered by the referenced_tweets
        # expansion above, not a separate external source.
        for url_entity in (tw.get("entities", {}) or {}).get("urls", []) or []:
            expanded = url_entity.get("expanded_url", "")
            if not expanded or "x.com/" in expanded or "twitter.com/" in expanded:
                continue
            linked_text = _fetch_external_link_content(expanded)
            if linked_text:
                content_parts.append(f"[linked page: {expanded}]: {linked_text}")

        content = "\n\n".join(p for p in content_parts if p)
        truncated = len(content) > MAX_CONTENT_CHARS
        content = content[:MAX_CONTENT_CHARS]
        if truncated:
            content += " […truncated…]"

        entries.append({
            "title": tw.get("text", "")[:80].strip(),
            "link": f"https://x.com/{username}/status/{tw['id']}",
            "author": f"@{username}",
            "date_published": date_published,
            "published_dt": published_dt,
            "content": content,
        })

    entries.sort(
        key=lambda e: e["published_dt"] or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return entries[:max_per_source], None


GMAIL_USER = "brain@brianmadden.ai"
GMAIL_TOKEN_URL = "https://oauth2.googleapis.com/token"
GMAIL_API_BASE = f"https://gmail.googleapis.com/gmail/v1/users/{GMAIL_USER}/messages"
GMAIL_ENV_VARS = ("GMAIL_CLIENT_ID", "GMAIL_CLIENT_SECRET", "GMAIL_REFRESH_TOKEN")


def gmail_is_configured() -> bool:
    return all(os.environ.get(v) for v in GMAIL_ENV_VARS)


def _gmail_access_token() -> str:
    resp = requests.post(GMAIL_TOKEN_URL, data={
        "client_id": os.environ["GMAIL_CLIENT_ID"],
        "client_secret": os.environ["GMAIL_CLIENT_SECRET"],
        "refresh_token": os.environ["GMAIL_REFRESH_TOKEN"],
        "grant_type": "refresh_token",
    }, timeout=15)
    resp.raise_for_status()
    return resp.json()["access_token"]


def _gmail_find_part(payload: dict, mime_type: str) -> str | None:
    """Depth-first search of a Gmail API message payload for a part with
    the given MIME type, returning its base64url body data if found."""
    if payload.get("mimeType") == mime_type:
        data = payload.get("body", {}).get("data")
        if data:
            return data
    for sub in payload.get("parts", []) or []:
        found = _gmail_find_part(sub, mime_type)
        if found:
            return found
    return None


def _gmail_decode(data: str) -> str:
    padded = data.replace("-", "+").replace("_", "/")
    padded += "=" * (-len(padded) % 4)
    return base64.b64decode(padded).decode("utf-8", errors="replace")


def _gmail_extract_body(payload: dict) -> str:
    """Prefers text/plain across the whole MIME tree; falls back to
    stripped text/html if no plain part exists."""
    plain = _gmail_find_part(payload, "text/plain")
    if plain:
        return _gmail_decode(plain).strip()
    html_data = _gmail_find_part(payload, "text/html")
    if html_data:
        return strip_html(_gmail_decode(html_data))
    return ""


def fetch_entries_email(source: dict, since_days: float, max_per_source: int):
    """
    Polls brain@brianmadden.ai for mail from this source's known sender
    (BUILD.md open decision #7a) — the email-source counterpart to
    fetch_entries(), same (entries, error) contract.

    Needs GMAIL_CLIENT_ID/SECRET/REFRESH_TOKEN (see .env.example and the
    brain@ Gmail walkthrough in BUILD.md) and a 'sender' field on the
    source's sources.yaml entry — this doesn't guess a from-address.
    """
    if not gmail_is_configured():
        return [], "GMAIL_CLIENT_ID/SECRET/REFRESH_TOKEN not set — see .env.example"

    sender = source.get("sender")
    if not sender:
        return [], "no 'sender' set in sources.yaml for this email source"

    try:
        access_token = _gmail_access_token()
    except requests.RequestException as e:
        return [], f"gmail auth failed: {e}"

    cutoff = datetime.now(timezone.utc) - timedelta(days=since_days)
    # Gmail search's after: is day-granularity, same as this pipeline's
    # existing date_captured handling elsewhere.
    query = f"from:{sender} after:{cutoff.strftime('%Y/%m/%d')}"
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        resp = requests.get(
            GMAIL_API_BASE, headers=headers,
            params={"q": query, "maxResults": max_per_source}, timeout=15,
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        return [], f"gmail list failed: {e}"

    entries = []
    for msg_ref in resp.json().get("messages", []):
        msg_id = msg_ref["id"]
        try:
            msg_resp = requests.get(
                f"{GMAIL_API_BASE}/{msg_id}", headers=headers,
                params={"format": "full"}, timeout=15,
            )
            msg_resp.raise_for_status()
        except requests.RequestException as e:
            print(f"    gmail: failed to fetch message {msg_id}: {e}")
            continue

        message = msg_resp.json()
        payload = message.get("payload", {})
        header_map = {h["name"]: h["value"] for h in payload.get("headers", [])}

        published_dt = None
        date_published = None
        internal_date = message.get("internalDate")
        if internal_date:
            published_dt = datetime.fromtimestamp(int(internal_date) / 1000, tz=timezone.utc)
            date_published = published_dt.strftime("%Y-%m-%d")

        content = _gmail_extract_body(payload)
        truncated = len(content) > MAX_CONTENT_CHARS
        content = content[:MAX_CONTENT_CHARS]
        if truncated:
            content += " […truncated…]"

        entries.append({
            "title": header_map.get("Subject", "(no subject)").strip(),
            "link": f"https://mail.google.com/mail/u/0/#inbox/{msg_id}",
            "author": header_map.get("From", sender).strip(),
            "date_published": date_published,
            "published_dt": published_dt,
            "content": content,
        })

    entries.sort(
        key=lambda e: e["published_dt"] or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return entries[:max_per_source], None


# ----------------------------------------------------------------- dedup --

def read_frontmatter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return None


def load_ingested_urls(ingest_root: Path) -> set[str]:
    urls = set()
    for path in ingest_root.rglob("*.md"):
        if path.name == "README.md":
            continue
        fm = read_frontmatter(path)
        if fm and fm.get("source_url"):
            urls.add(fm["source_url"])
    return urls


# -------------------------------------------------------------- prompting --

def build_prompt(template: str, source: dict, entry: dict) -> str:
    pov = (source.get("pov") or "").strip()
    lens = (source.get("lens") or "").strip()

    pov_block = f" Brian's read on this source: {pov}" if pov else ""
    lens_instruction = (
        f'- Brian\'s lens on this source is "{lens}" — weight and frame the '
        f"insights with that in mind."
        if lens else ""
    )

    replacements = {
        "{{SOURCE_NAME}}": source.get("name", source.get("id", "unknown")),
        "{{SOURCE_TYPE}}": source.get("type", "source"),
        "{{SOURCE_POV_BLOCK}}": pov_block,
        "{{ENTRY_TITLE}}": entry.get("title") or "(untitled)",
        "{{ENTRY_AUTHOR}}": entry.get("author") or source.get("name", ""),
        "{{ENTRY_DATE}}": entry.get("date_published") or "unknown",
        "{{ENTRY_URL}}": entry.get("link", ""),
        "{{ENTRY_CONTENT}}": entry.get("content") or "(no content available)",
        "{{LENS_INSTRUCTION}}": lens_instruction,
    }
    text = template
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text


def extract(
    template: str,
    source: dict,
    entry: dict,
    provider: str | None = None,
    model: str | None = None,
) -> str | None:
    prompt_text = build_prompt(template, source, entry)
    # 1024 wasn't enough headroom for longer pieces during the framework-
    # aware prompt experiment (2026-08-11) — kept at 2048 even after
    # reverting that experiment, since it's just a safer margin regardless.
    text = llm.generate(prompt_text, provider=provider, model=model, max_tokens=2048)
    if text == "NOT_RELEVANT" or text.startswith("NOT_RELEVANT"):
        return None
    return text


# ------------------------------------------------------------------ write --

def slugify(text: str, max_len: int = 60) -> str:
    text = SLUG_RE.sub("-", (text or "").lower()).strip("-")
    return text[:max_len].rstrip("-")


def write_note(
    ingest_root: Path, source: dict, entry: dict, body: str, dry_run: bool, model: str,
    ingest_method: str = "feed",
) -> Path:
    now = datetime.now(timezone.utc)
    date_captured = now.strftime("%Y-%m-%d")
    slug = slugify(entry["title"]) or "untitled"
    filename = f"{date_captured}-{source['id']}-{slug}.md"
    out_dir = ingest_root / now.strftime("%Y") / now.strftime("%m")
    out_path = out_dir / filename

    frontmatter = {
        "title": entry["title"] or "(untitled)",
        "source": source.get("name", source["id"]),
        "source_id": source["id"],
        "source_url": entry["link"],
        "author": entry.get("author") or source.get("name", source["id"]),
        "date_published": entry.get("date_published"),
        "date_captured": date_captured,
        "ingest_method": ingest_method,
        "model": model,
    }
    fm_yaml = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
    full_text = f"---\n{fm_yaml}\n---\n\n# {entry['title'] or '(untitled)'}\n\n{body}\n"

    if dry_run:
        rel = out_path.relative_to(ROOT)
        print(f"\n{'=' * 70}\n[DRY RUN] would write: {rel}\n{'=' * 70}")
        print(full_text)
        return out_path

    out_dir.mkdir(parents=True, exist_ok=True)
    if out_path.exists():
        stem, suffix = out_path.stem, out_path.suffix
        n = 2
        while out_path.exists():
            out_path = out_dir / f"{stem}-{n}{suffix}"
            n += 1
    out_path.write_text(full_text, encoding="utf-8")
    print(f"wrote {out_path.relative_to(ROOT)}")
    return out_path


# ------------------------------------------------------------------- main --

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pull feeds from sources.yaml, extract insights, write tier-1 notes to ingest/."
    )
    parser.add_argument("--source", help="only process this one source id")
    parser.add_argument(
        "--since-days", type=float, default=None,
        help="only entries published in the last N days. Default: auto — "
             "time since the last full run (ingest/.last_run.json), or "
             f"{DEFAULT_SINCE_DAYS:g} days if there's no recorded prior run",
    )
    parser.add_argument("--max-per-source", type=int, default=5, help="cap entries considered per source (default 5)")
    parser.add_argument("--dry-run", action="store_true", help="print notes instead of writing them (still calls the API)")
    parser.add_argument("--provider", choices=sorted(llm.REQUIRED_ENV_VARS), help="override LLM_PROVIDER for this run (default: env LLM_PROVIDER, else anthropic)")
    parser.add_argument("--llm-model", help="override the model id for this run (default: env LLM_MODEL, else the provider's default)")
    args = parser.parse_args()

    load_dotenv(ROOT)

    sources = load_sources(ROOT / "sources" / "sources.yaml")
    if args.source:
        sources = [s for s in sources if s["id"] == args.source]
        if not sources:
            print(f"no source with id '{args.source}' in sources.yaml", file=sys.stderr)
            sys.exit(1)

    ingest_root = ROOT / "ingest"
    seen_urls = load_ingested_urls(ingest_root)

    provider = args.provider or llm.current_provider()
    model_used = llm.resolve_model(provider, args.llm_model)
    ready = llm.is_configured(provider)
    if not ready:
        print(
            f"{llm.required_env_var(provider)} not set for provider '{provider}' — will "
            f"fetch feeds and dedupe, but skip extraction. Set it (see .env.example) and "
            f"rerun for real notes. (Swap providers with --provider or LLM_PROVIDER.)\n"
        )

    template = (Path(__file__).parent / "prompt.md").read_text(encoding="utf-8")

    since_days, since_reason = resolve_since_days(args.since_days)
    print(f"window: {since_days:.2f} days ({since_reason})\n")

    total_new = 0
    total_written = 0
    for source in sources:
        ingest_method = source.get("ingest_method")
        is_email = ingest_method == "email"
        is_x = ingest_method == "x"
        if not is_email and not is_x and not source.get("feed_url"):
            print(f"[{source['id']}] skipped — no feed_url")
            continue

        if is_email:
            entries, err = fetch_entries_email(source, since_days, args.max_per_source)
        elif is_x:
            entries, err = fetch_entries_x(source, since_days, args.max_per_source)
        else:
            entries, err = fetch_entries(source, since_days, args.max_per_source)
        if err:
            print(f"[{source['id']}] {err}")
            continue

        new_entries = [e for e in entries if e["link"] not in seen_urls]
        print(f"[{source['id']}] {len(entries)} entries in window, {len(new_entries)} new")
        total_new += len(new_entries)

        if not ready:
            for e in new_entries:
                print(f"    would extract: {e['title']}")
            continue

        for entry in new_entries:
            enrich_with_transcript(entry, source)
            body = extract(
                template, source, entry,
                provider=args.provider, model=args.llm_model,
            )
            if body is None:
                print(f"    skipped (not relevant): {entry['title']}")
                continue
            write_note(
                ingest_root, source, entry, body, args.dry_run, model=model_used,
                ingest_method="email" if is_email else ("x" if is_x else "feed"),
            )
            seen_urls.add(entry["link"])
            total_written += 1

    summary = f"\n{total_new} new entries found; {total_written} notes written"
    if args.dry_run:
        summary += " (dry run, nothing saved)"
    if not ready:
        summary += f" — extraction skipped, {llm.required_env_var(provider)} not set"
    print(summary)

    # Only a full-registry, non-dry run advances the "last run" clock — a
    # --source test run or a --dry-run preview shouldn't make the *next*
    # real run think everything else was just covered too.
    if not args.dry_run and not args.source:
        run_time = datetime.now(timezone.utc)
        write_last_run(run_time)
        print(f"recorded last run: {run_time.isoformat()}")


if __name__ == "__main__":
    main()

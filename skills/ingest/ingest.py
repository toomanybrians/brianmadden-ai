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
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

import feedparser
import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "skills"))
from lib import llm, substack_follows, transcribe  # noqa: E402  (needs sys.path set first)

USER_AGENT = "brianmadden-ai-ingest/0.1 (+https://brianmadden.ai)"
# Substack's content:encoded (and most other feeds checked) carry genuine
# full-text, not a truncated preview — 8000 was an arbitrary guess that cut
# 35-67% off real posts (confirmed 2026-08-11: Mollick, SemiAnalysis,
# Interconnects all exceeded it). Raised with real headroom; still finite
# as a safety valve against a malformed feed dumping something absurd.
MAX_CONTENT_CHARS = 50000
LAST_RUN_PATH = ROOT / "ingest" / ".last_run.json"
SOURCE_RESULTS_PATH = ROOT / "ingest" / ".last_run_sources.json"
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


def write_source_results(when: datetime, results: list[dict]) -> None:
    """One row per sources.yaml entry for this run — success, error, or a
    by-design skip (see the source_results comment in main()). Read by
    skills/brief/brief.py to render the brief's own "Sources checked
    today" section, so a source going silently quiet is a fact on the
    published page, not something buried in Actions logs."""
    SOURCE_RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    SOURCE_RESULTS_PATH.write_text(
        json.dumps({"run_utc": when.isoformat(), "results": results}, indent=2) + "\n",
        encoding="utf-8",
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
        if not link:
            # Some megaphone.fm-hosted feeds omit <link> entirely (confirmed
            # 2026-08-13 against real feed content: moonshots, no-priors,
            # on-with-kara-swisher all return link=None from feedparser,
            # not a parsing bug). Left empty, this silently breaks dedup:
            # load_ingested_urls() only tracks truthy source_url values, so
            # an empty link is never "seen," and the same already-ingested
            # episode gets treated as new on every future run until a real
            # new episode replaces it. feedparser's raw['id'] is a stable
            # per-episode GUID even when <link> is missing (confirmed
            # against all 3 affected sources) — fall back to the source's
            # homepage plus that GUID: still a real, clickable URL (just
            # not episode-specific) and unique enough for dedup to work.
            guid = (raw.get("id") or "").strip()
            homepage = (source.get("url") or "").strip()
            if guid and homepage:
                link = f"{homepage}#{guid}"
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
# OpenAI's transcription API caps uploads at 25MB (whisper-1 and
# gpt-4o-transcribe alike) and gpt-4o-transcribe additionally caps
# duration at 1500s/25min regardless of file size — confirmed 2026-08-12
# the hard way (both test episodes, 74MB/114MB, failed transcription
# outright). 900s (15min) segments re-encoded to 64kbps mono/16kHz give a
# predictable ~7.2MB per chunk — safely under both limits with real
# margin, not a bitrate-dependent guess. Mono/16kHz is standard practice
# for speech transcription (no quality loss that matters for this).
AUDIO_CHUNK_SECONDS = 900


def _split_audio_for_transcription(audio_path: Path, workdir: Path) -> list[Path]:
    """Re-encodes + splits audio_path into AUDIO_CHUNK_SECONDS chunks via
    ffmpeg, written into workdir (caller's temp dir, cleaned up by the
    caller). Returns chunk paths in order. Raises FileNotFoundError if
    ffmpeg isn't on PATH — caller decides the fallback."""
    if not shutil.which("ffmpeg"):
        raise FileNotFoundError("ffmpeg not found on PATH")
    pattern = str(workdir / "chunk_%03d.mp3")
    result = subprocess.run(
        [
            "ffmpeg", "-y", "-i", str(audio_path),
            "-ac", "1", "-ar", "16000", "-b:a", "64k",
            "-f", "segment", "-segment_time", str(AUDIO_CHUNK_SECONDS),
            "-reset_timestamps", "1",
            pattern,
        ],
        # errors="replace": confirmed 2026-08-25 the hard way — ffmpeg's
        # stderr on a real episode (Kara Swisher's feed) contained a byte
        # sequence that isn't valid UTF-8, and text=True's default strict
        # decoding raised UnicodeDecodeError *inside* subprocess.run()
        # itself, before this function's own RuntimeError handling ever
        # ran — a ValueError subclass the caller's `except RuntimeError`
        # doesn't catch, so it crashed the whole ingest run rather than
        # just this one episode. stderr is only ever used truncated, for
        # a diagnostic message (see below) — replacing undecodable bytes
        # costs nothing real there.
        capture_output=True, text=True, errors="replace", timeout=600,
    )
    if result.returncode != 0:
        raise RuntimeError(f"ffmpeg failed: {result.stderr[-500:]}")
    return sorted(workdir.glob("chunk_*.mp3"))


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

        # Stage 2: transcription. OpenAI's API caps uploads at 25MB (and
        # gpt-4o-transcribe separately caps duration at 25min) — confirmed
        # 2026-08-12 the hard way, both real test episodes (74MB/114MB)
        # failed outright at the full-file size. Split into safe chunks
        # via ffmpeg first; if ffmpeg isn't available, fall back to
        # attempting the whole file (works fine for naturally-short audio,
        # fails the same way as before for anything large).
        print(f"    downloaded audio ({downloaded / 1_000_000:.1f}MB)")
        chunk_dir = None
        try:
            chunk_dir = Path(tempfile.mkdtemp())
            try:
                chunks = _split_audio_for_transcription(tmp_path, chunk_dir)
            except FileNotFoundError:
                print("    ffmpeg not found — attempting the full file directly (will fail if it's over OpenAI's 25MB/25min caps)")
                chunks = [tmp_path]
            except RuntimeError as e:
                print(f"    audio splitting failed ({e}) — using show notes")
                return

            print(f"    transcribing {len(chunks)} chunk(s) via {transcribe.current_provider()}/{transcribe.resolve_model()}...")
            texts = []
            try:
                for i, chunk in enumerate(chunks, 1):
                    texts.append(transcribe.transcribe(chunk))
                    print(f"      chunk {i}/{len(chunks)} done ({len(texts[-1])} chars)")
            except requests.RequestException as e:
                print(f"    transcription API call failed on chunk {len(texts) + 1}/{len(chunks)} ({e}) — using show notes")
                return
            text = " ".join(texts)
        finally:
            if chunk_dir and chunk_dir.exists():
                shutil.rmtree(chunk_dir, ignore_errors=True)

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
GMAIL_USER_BASE = f"https://gmail.googleapis.com/gmail/v1/users/{GMAIL_USER}"
GMAIL_API_BASE = f"{GMAIL_USER_BASE}/messages"
GMAIL_ENV_VARS = ("GMAIL_CLIENT_ID", "GMAIL_CLIENT_SECRET", "GMAIL_REFRESH_TOKEN")
# Applied to every brain@ message this pipeline touches, so it never gets
# reconsidered and so Brian has a visual "the AI already saw this, and here's
# what it did" signal in Gmail itself — two labels, not one, per Brian's
# 2026-08-12 call: which messages actually became a note vs. which were seen
# and judged not relevant are different things worth being able to tell
# apart at a glance. Needs gmail.modify (not just gmail.readonly) — see
# BUILD.md's brain@ walkthrough.
GMAIL_LABEL_INGESTED = "AI/Ingested"
GMAIL_LABEL_SKIPPED = "AI/Skipped"
# Applied to messages from Brian's own verified personal address (open
# decision #9) instead of INGESTED/SKIPPED — a brain@ flag is never "judged
# not relevant" the way a boring newsletter issue is; it always lands in
# ingest/brain-flags/queue.md for a human look, with or without a real
# ingest/ note alongside it. Archived either way (see handle_brain_flag) —
# the actionable trail moves to the queue file, not the inbox.
GMAIL_LABEL_FLAGGED = "AI/Flagged"
GMAIL_PROCESSED_LABELS = (GMAIL_LABEL_INGESTED, GMAIL_LABEL_SKIPPED, GMAIL_LABEL_FLAGGED)
# Brian's personal address (Google Workspace via Apple Custom Email Domain
# — see BUILD.md). DKIM for bmad.com doesn't currently verify (confirmed
# 2026-08-16: no sig1._domainkey.bmad.com DNS record exists yet, so
# Apple's real signature can never be checked — dkim=permerror on every
# message, not a spoofing concern) — see _sender_is_verified_personal().
# Read from BRIAN_EMAIL (not hardcoded — this repo is public, 2026-08-20
# call) via a function rather than a module-level constant, since that's
# evaluated at import time, before main() has loaded .env.
def personal_flag_sender() -> str:
    return os.environ.get("BRIAN_EMAIL", "")
BRAIN_FLAGS_QUEUE = ROOT / "ingest" / "brain-flags" / "queue.md"
URL_RE = re.compile(r"https?://\S+")
_gmail_label_id_cache: dict[str, str] = {}
# See fetch_entries_email()'s final sort-and-slice: max_per_source's
# general default (5) is too low for real curated-inbox volume.
EMAIL_MIN_PER_SOURCE = 20


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


VIEW_ONLINE_ANCHOR_RE = re.compile(
    r'<a\b[^>]*\bhref=["\']([^"\']+)["\'][^>]*>(.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)
VIEW_ONLINE_TEXT_RE = re.compile(
    r'view\s+(this\s+)?(email\s+)?(in\s+(your\s+)?browser|online|web)|'
    r'read\s+(it\s+)?online|open\s+in\s+browser|web\s+version|'
    r'read\s+the\s+(full\s+)?(post|article|story)|'
    r'continue\s+reading|keep\s+reading|full\s+(story|article|post)|'
    r'read\s+in\s+app',
    re.IGNORECASE,
)

# Substack's own email template never uses any of the phrasing above — every
# Substack email links its "READ IN APP" button (and the post title itself)
# through open.substack.com/pub/<publication>/p/<slug>, an app-first
# interstitial rather than a plain public article page. Confirmed empirically
# 2026-08-26 (Brian noticed every brain@-routed Substack note that day had no
# link at all): _resolve_email_link()'s plain requests.get() doesn't reliably
# follow this domain's redirect the way a real browser does (it can return
# 200 and stay on open.substack.com instead of 3xx-ing to the real article),
# so following it isn't safe to depend on. But the interstitial URL itself
# already deterministically encodes the real public URL — same publication
# subdomain, same slug, no redirect needed — so this rewrites it directly
# instead of relying on a network round-trip that isn't reliable for this
# one domain.
SUBSTACK_APP_LINK_RE = re.compile(
    r'^https://open\.substack\.com/pub/([^/]+)/p/([^/?]+)', re.IGNORECASE
)


def _rewrite_substack_app_link(url: str) -> str:
    m = SUBSTACK_APP_LINK_RE.match(url)
    if not m:
        return url
    publication, slug = m.groups()
    return f"https://{publication}.substack.com/p/{slug}"


def _find_view_online_link(html: str) -> str:
    """Newsletters commonly include a real 'view in browser'/'read online'
    link near the top — a genuine public URL, unlike anything Gmail-
    specific. Brian's call (2026-08-13): use it as the note's source_url
    when present; leave source_url empty when it isn't — never fall back
    to a private Gmail inbox deep link (see git history / BUILD.md for
    why: it's broken for anyone but Brian and leaks a private message ID
    into public-facing output). Best-effort text match on common
    newsletter-ESP phrasing. Returns the raw click-tracking redirect as
    found in the HTML — see _resolve_email_link() for why that redirect
    gets followed and stripped down before it's actually used as a
    citation link.

    Extended 2026-08-18 to also match 'continue reading' / 'read the full
    post' / 'full story' style anchors (Substack, Beehiiv, ConvertKit all
    use these for a single blog-cross-post email) — deliberately still
    just recognized phrasing, never a blind 'grab any link in the body'
    heuristic, which would risk mis-attributing an ad or an unrelated
    story's link. Returns the *first* matching anchor in document order,
    so a genuine multi-story digest (AlphaSignal, "Best of NFX") with
    several per-story "read more" links can still end up pointing at just
    the first story — a real known limitation, not a guaranteed fix for
    every digest. brief.py's prompt.md now has a fallback for the
    remaining true no-link cases: name the newsletter instead of a link
    (see the note's `author` field)."""
    for match in VIEW_ONLINE_ANCHOR_RE.finditer(html):
        href, inner_html = match.groups()
        if VIEW_ONLINE_TEXT_RE.search(strip_html(inner_html)):
            return href
    return ""


def _strip_query_and_fragment(url: str) -> str:
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


# Some ESP click-tracking redirectors (confirmed 2026-08-13: Beehiiv's
# link.mail.beehiiv.com) return a bare 403 for our honest bot USER_AGENT
# used everywhere else (RSS/podcast fetches identify themselves plainly,
# which is normal etiquette for a feed poller) but resolve fine for a
# realistic browser UA — which is exactly what a real reader's browser
# would send anyway when they click "view online." Scoped to this one
# call, not the module-wide USER_AGENT, since resolving one link a real
# human would click is a different thing from identifying a feed poller.
BROWSER_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def _resolve_email_link(url: str) -> str:
    """Newsletter ESPs (Sailthru, Beehiiv, Mailchimp, etc.) wrap their
    'view online' link in a click-tracking redirect whose *path* segment
    IS the tracking token — there's no plain query string to strip on the
    original link, the whole URL is opaque. Brian's ask (2026-08-13):
    don't publish a link tied to his subscriber ID. Following the
    redirect once, here, from ingestion (not from a public reader's
    browser), gets the real destination (resp.url after redirects) — but
    that alone isn't enough: confirmed empirically (2026-08-13) that a
    resolved Beehiiv URL's own query string carries a `jwt_token` param
    that trivially base64-decodes (no signature check needed to read it)
    to `{"subscriber_id": "...", ...}` — a real personal identifier, not
    just an opaque tracking blob. So the query string and fragment are
    stripped after resolving too, keeping only scheme+host+path — the
    part that actually identifies the article, not the reader.
    stream=True + immediate close avoids downloading the destination
    page's body, which isn't needed. Retries on a 403 or a request
    exception — confirmed empirically (2026-08-13) that Beehiiv's
    redirector is genuinely flaky under repeated hits (200, then 403,
    then 403 on three identical back-to-back requests during testing —
    looks like probabilistic bot-challenge/rate-limiting, not a hard
    block), same transient-failure shape as the podcast transcription API
    this session already added retry logic for. Falls back to the
    original (still-tracked) URL if every attempt fails — a
    working-but-ugly link beats a broken one."""
    for attempt in range(1, 4):
        try:
            resp = requests.get(
                url, timeout=15, allow_redirects=True, stream=True,
                headers={"User-Agent": BROWSER_USER_AGENT},
            )
            resp.close()
            if resp.status_code < 400 and resp.url:
                return _strip_query_and_fragment(resp.url)
        except requests.RequestException:
            pass
        if attempt < 3:
            time.sleep(2 * attempt)
    return url


def _gmail_find_view_online_link(payload: dict) -> str:
    html_data = _gmail_find_part(payload, "text/html")
    if not html_data:
        return ""
    candidate = _find_view_online_link(_gmail_decode(html_data))
    if not candidate:
        return ""
    if SUBSTACK_APP_LINK_RE.match(candidate):
        return _rewrite_substack_app_link(candidate)
    return _resolve_email_link(candidate)


def _gmail_get_label_id(name: str, access_token: str) -> str | None:
    """Looks up a Gmail label by name, creating it if it doesn't exist yet
    (labels.create is idempotent-ish — Gmail rejects a duplicate name with
    a 409, treated the same as "already exists, look it up"). Cached at
    module level so a run with many messages doesn't re-list/re-create per
    message. Returns None (never raises) on any API failure — a label miss
    should never sink note-writing, which already happened by the time
    this is called."""
    if name in _gmail_label_id_cache:
        return _gmail_label_id_cache[name]

    headers = {"Authorization": f"Bearer {access_token}"}
    try:
        resp = requests.get(f"{GMAIL_USER_BASE}/labels", headers=headers, timeout=15)
        resp.raise_for_status()
        for label in resp.json().get("labels", []):
            if label["name"] == name:
                _gmail_label_id_cache[name] = label["id"]
                return label["id"]

        resp = requests.post(
            f"{GMAIL_USER_BASE}/labels", headers=headers, timeout=15,
            json={"name": name, "labelListVisibility": "labelShow", "messageListVisibility": "show"},
        )
        resp.raise_for_status()
        label_id = resp.json()["id"]
        _gmail_label_id_cache[name] = label_id
        return label_id
    except requests.RequestException as e:
        print(f"    gmail: couldn't look up/create label '{name}': {e}")
        return None


def gmail_apply_label(msg_id: str | None, label_name: str, archive: bool = False) -> None:
    """Applies one of GMAIL_PROCESSED_LABELS to a message so it's excluded
    from future fetch_entries_email() queries and visibly marked in Gmail
    itself as either ingested or skipped.

    archive=True also removes the INBOX label — Gmail's own definition of
    "archived," there's no separate action. Per Brian's 2026-08-13 design:
    ingested mail gets archived automatically (out of the way, nothing to
    maintain); skipped mail deliberately stays in the inbox so Brian can
    see what the pipeline judged not relevant and correct it if it got one
    wrong — replaces the earlier plan of a manually-maintained Gmail
    filter, which needed upkeep for no real benefit once the pipeline can
    just do this itself.

    Best-effort — a labeling failure is logged, not raised, since the note
    (or the not-relevant decision) it's marking is already final by the
    time this runs."""
    if not msg_id or not gmail_is_configured():
        return
    try:
        access_token = _gmail_access_token()
    except requests.RequestException as e:
        print(f"    gmail: couldn't get a token to label message {msg_id}: {e}")
        return

    label_id = _gmail_get_label_id(label_name, access_token)
    if not label_id:
        return

    body = {"addLabelIds": [label_id]}
    if archive:
        body["removeLabelIds"] = ["INBOX"]

    try:
        resp = requests.post(
            f"{GMAIL_API_BASE}/{msg_id}/modify",
            headers={"Authorization": f"Bearer {access_token}"}, timeout=15,
            json=body,
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"    gmail: couldn't apply label '{label_name}' to message {msg_id}: {e}")


def _gmail_exclude_processed_clause() -> str:
    return " ".join(f'-label:"{name}"' for name in GMAIL_PROCESSED_LABELS)


def fetch_entries_email(source: dict, since_days: float, max_per_source: int):
    """
    Polls the whole brain@brianmadden.ai inbox — every message not yet
    labeled ingested/skipped, regardless of sender (BUILD.md open decision
    #7a). Same (entries, error) contract as fetch_entries().

    Design, per Brian (2026-08-13): subscribing something to brain@ *is*
    the curation step — there's no separate sender allowlist to maintain
    on top of that. Relevance is judged the same way as every other
    source: the extraction prompt's NOT_RELEVANT sentinel, not a
    pre-approved sender list. (Earlier version of this function required a
    'sender' field per sources.yaml entry and only looked at known
    senders — reverted; see the git history / BUILD.md for why.)

    Entries carry an extra 'gmail_msg_id' key (not written to note
    frontmatter — write_note() only reads specific known keys) so the
    caller can label the message afterward via gmail_apply_label(). The
    real sender is read from each message's own From header into the
    entry's 'author' field — not from a registry — so note attribution is
    always accurate even for a source this file has never heard of.

    Needs GMAIL_CLIENT_ID/SECRET/REFRESH_TOKEN (see .env.example and the
    brain@ Gmail walkthrough in BUILD.md).
    """
    if not gmail_is_configured():
        return [], "GMAIL_CLIENT_ID/SECRET/REFRESH_TOKEN not set — see .env.example"

    try:
        access_token = _gmail_access_token()
    except requests.RequestException as e:
        return [], f"gmail auth failed: {e}"

    cutoff = datetime.now(timezone.utc) - timedelta(days=since_days)
    # Gmail search's after: is day-granularity, same as this pipeline's
    # existing date_captured handling elsewhere. -label excludes anything a
    # prior run already labeled (ingested or skipped), on top of the
    # frontmatter-based dedup every source type already gets from
    # load_ingested_urls(). No from: filter — whole inbox, see docstring.
    # in:inbox added 2026-08-20: without it, Gmail's default search scope
    # is "all mail except Spam/Trash", which includes Sent — so once
    # skills/lib/gmail_send.py started sending brain@'s daily-brief email
    # from this same account, the very next run ingested brain@'s own
    # outgoing mail as if it were a newsletter (real incident: the
    # 2026-08-20 automated run ingested the 2026-08-19 Daily Briefing and
    # an About-page email, both sent minutes earlier from brain@ itself).
    #
    # -from:SELF_PUBLICATION_SENDERS added 2026-08-26: a second, distinct
    # path to the same self-ingestion problem, this time via a real inbound
    # subscription rather than the Sent folder — brain@ turned out to be a
    # subscriber to the `brianmaddenai` Substack publication itself, so
    # every time Brian publishes a Daily Brief on Substack, a copy lands in
    # brain@'s INBOX from Substack's own outgoing address for that
    # publication (`brianmaddenai+brianmaddenai@substack.com`), and the
    # in:inbox filter above does nothing to stop it — it's a real inbound
    # message, not Sent mail. Confirmed real 2026-08-26: auto-registered
    # itself as a new source the same way any unrecognized sender does
    # (`brain-brianmadden-ai` in sources.yaml), then got extracted and fed
    # into the next day's synthesis as if it were independent third-party
    # insight — a feedback loop, not a curation question, so unlike every
    # other sender (see the docstring: no allowlist, subscribing IS
    # curation) this one sender is excluded structurally rather than left
    # to curation, the same way Sent-folder self-mail already is.
    self_publication_senders = ("brianmaddenai+brianmaddenai@substack.com",)
    exclude_self = " ".join(f"-from:{addr}" for addr in self_publication_senders)
    query = (
        f'in:inbox after:{cutoff.strftime("%Y/%m/%d")} '
        f'{exclude_self} {_gmail_exclude_processed_clause()}'
    )
    headers = {"Authorization": f"Bearer {access_token}"}

    # Confirmed real 2026-08-14: this used to pass maxResults=max_per_source
    # (5) straight to the Gmail list call, capping the *candidate set*
    # before anything downstream knew each message's real date. Gmail's
    # messages.list has no guaranteed chronological order, so on any day
    # with more than max_per_source new messages (routine for a multi-
    # newsletter inbox), the sort-and-slice below was a no-op — Gmail had
    # already silently dropped some, arbitrarily, including on the day
    # this was found the single newest message in the whole inbox. Fixed
    # by requesting a generously wide batch here (well above any realistic
    # daily volume) and letting the existing sort-by-date + max_per_source
    # slice below do the real truncation on complete date information —
    # same pattern fetch_entries() (RSS) already uses correctly.
    GMAIL_LIST_FETCH_CAP = 100
    try:
        resp = requests.get(
            GMAIL_API_BASE, headers=headers,
            params={"q": query, "maxResults": GMAIL_LIST_FETCH_CAP}, timeout=15,
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
            "link": _gmail_find_view_online_link(payload),
            "author": header_map.get("From", "(unknown sender)").strip(),
            "date_published": date_published,
            "published_dt": published_dt,
            "content": content,
            "gmail_msg_id": msg_id,
            # Leading underscore: internal to the email path, not part of
            # write_note()'s known-keys contract (never reaches frontmatter).
            # Kept here so handle_brain_flag() (open decision #9) doesn't
            # need a second Gmail fetch to check sender auth or find
            # attachments.
            "_gmail_header_map": header_map,
            "_gmail_payload": payload,
        })

    entries.sort(
        key=lambda e: e["published_dt"] or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    # max_per_source (default 5) is tuned for RSS/podcast sources, which
    # rarely publish more than a couple of items a day — real 2026-08-14
    # brain-inbox volume was ~10 genuinely new messages in one window, so
    # applying the same cap here would just reintroduce the drop this fix
    # was for, deterministically instead of arbitrarily. A curated-
    # newsletter inbox needs a higher floor; --max-per-source can still
    # raise it further for an explicit wide/catch-up run.
    effective_max = max(max_per_source, EMAIL_MIN_PER_SOURCE)
    return entries[:effective_max], None


FROM_HEADER_RE = re.compile(r'^\s*"?([^"<]*)"?\s*<([^>]+)>\s*$')


def _parse_sender_header(from_header: str) -> tuple[str, str]:
    """Splits a From header like 'The Deep View <newsletter@thedeepview.co>'
    into (display_name, address). Falls back to using the whole header as
    both if it doesn't match the usual "Name <addr>" shape."""
    m = FROM_HEADER_RE.match(from_header or "")
    if m:
        name = m.group(1).strip() or m.group(2)
        return name, m.group(2).lower()
    stripped = (from_header or "").strip()
    return stripped, stripped.lower()


def load_known_email_senders(sources_path: Path) -> set[str]:
    return {s["sender"].lower() for s in load_sources(sources_path) if s.get("sender")}


def _feed_match_token(source: dict) -> str | None:
    """The identifier a real email sender's address should be checked
    against for this source: the subdomain (e.g. 'garymarcus') for a
    *.substack.com feed_url, or the full host (e.g. 'alphasignal.ai') for
    a custom-domain one. None if the source has no feed_url/url to go on."""
    for candidate in (source.get("feed_url"), source.get("url")):
        if not candidate:
            continue
        host = (urlsplit(candidate).netloc or "").lower().removeprefix("www.")
        if not host:
            continue
        if host.endswith(".substack.com"):
            return host.removesuffix(".substack.com")
        return host
    return None


def find_feed_source_for_email_sender(address: str, sources: list[dict]) -> dict | None:
    """Does a real brain@ email just arrive from the same publication an
    existing feed_url-based sources.yaml row already tracks? Brian's ask
    (2026-08-25), directly downstream of the 403-blocking finding: once
    he subscribes a blocked Substack for email delivery, the pipeline
    should recognize the newsletter it already knows rather than
    registering a lookalike duplicate row the way auto_register_email_
    source() would on its own (it only checks exact previously-seen
    sender addresses, not "is this publication already tracked another
    way"). Two match shapes, since real Substack send addresses vary and
    this can't be verified without a live example: the sender's domain
    equals the source's feed host exactly (self-hosted mail on a custom
    domain, e.g. news@alphasignal.ai), or — for *.substack.com feeds
    specifically — the sender's domain's first label or local-part
    equals the feed's subdomain (covers both a per-publication sending
    subdomain and a shared substack.com apex with the publication name
    as the local-part). Only considers sources with no `sender` yet and
    not already `ingest_method: email` — already-flipped/documented rows
    are out of scope here, same as auto_register_email_source()'s own
    known-senders check."""
    if "@" not in address:
        return None
    local_part, _, sender_domain = address.lower().partition("@")
    sender_first_label = sender_domain.split(".")[0]
    for s in sources:
        if s.get("sender") or s.get("ingest_method") == "email":
            continue
        token = _feed_match_token(s)
        if not token:
            continue
        if token == sender_domain:
            return s
        if "." not in token and token in (sender_first_label, local_part):
            return s
    return None


def flip_source_to_email(source: dict, address: str, sources_path: Path) -> bool:
    """Rewrites one existing sources.yaml entry in place to route through
    the brain@ email path instead of its (likely 403-blocked) feed_url —
    adds `sender`, sets `ingest_method: email`, nulls `feed_url` (unused
    once ingest_method is email — see main()'s dispatch — nulled rather
    than left stale so the row reads the same as every other email-routed
    entry). Line-level surgery on just this one entry's block, not a
    full-file YAML re-dump — preserves every other entry's comments and
    this entry's own `note`/`lens`/`pov` fields untouched, same reasoning
    as auto_register_email_source(). Mutates `source` in place too (so a
    second match against the same dict later in this run sees it as
    already flipped) and returns whether the flip actually happened —
    False if the entry's feed_url line couldn't be found (shouldn't
    happen for a row find_feed_source_for_email_sender() would have
    matched, but no silent corruption if the file's shape ever changes)."""
    source_id = source["id"]
    lines = sources_path.read_text(encoding="utf-8").splitlines(keepends=True)
    start = next((i for i, l in enumerate(lines) if l.strip() == f"- id: {source_id}"), None)
    if start is None:
        return False
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if re.match(r"^\s{2}- id:\s", lines[i]):
            end = i
            break

    feed_line_idx = None
    for i in range(start, end):
        if re.match(r"^    feed_url:", lines[i]):
            feed_line_idx = i
            break
    if feed_line_idx is None:
        return False

    lines[feed_line_idx] = "    feed_url: null\n"
    lines.insert(feed_line_idx + 1, f"    sender: {address}\n    ingest_method: email\n")
    sources_path.write_text("".join(lines), encoding="utf-8")

    source["feed_url"] = None
    source["sender"] = address
    source["ingest_method"] = "email"
    print(f"    sources.yaml: flipped '{source_id}' from feed to email (sender confirmed: {address})")
    return True


def auto_register_email_source(
    from_header: str, sources_path: Path, known_senders: set[str]
) -> None:
    """Appends a new sources.yaml entry for a real newsletter the pipeline
    just ingested, if its sender isn't already documented there.

    Per Brian's 2026-08-13 design: sources.yaml for email isn't a gate
    (see fetch_entries_email() — the whole inbox is scanned regardless).
    It's a reporting list of what's actually arriving, populated by what
    actually gets ingested rather than maintained by hand ahead of time.
    Only called for messages that produced a real note — never for
    skipped/not-relevant mail — so the registry doesn't fill up with junk
    senders that happened to reach brain@.

    Mutates known_senders in place (adds the new address) so a second new
    sender appearing later in the same run doesn't also get added twice.

    Deliberately a plain text append, never a full YAML re-serialize —
    re-dumping the whole file with PyYAML would silently strip every
    hand-written comment in it (70+ sources' worth of curation history).
    """
    name, address = _parse_sender_header(from_header)
    if not address or address in known_senders:
        return

    existing_ids = {s["id"] for s in load_sources(sources_path)}
    base_id = slugify(name) or "unknown-newsletter"
    source_id = base_id
    n = 2
    while source_id in existing_ids:
        source_id = f"{base_id}-{n}"
        n += 1

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    note = (
        f"Auto-discovered from a real brain@ ingestion on {today} — "
        f"documentation only, not a gate (see the header comment above "
        f"'sources:'). Not yet reviewed by Brian."
    )
    entry_yaml = (
        f"\n  - id: {source_id}\n"
        f"    name: {json.dumps(name, ensure_ascii=False)}\n"
        f"    type: newsletter\n"
        f"    url: null  # not looked up — auto-added, fill in if known\n"
        f"    feed_url: null\n"
        f"    sender: {address}\n"
        f"    priority: regular\n"
        f"    note: {json.dumps(note, ensure_ascii=False)}\n"
    )
    with sources_path.open("a", encoding="utf-8") as f:
        f.write(entry_yaml)
    known_senders.add(address)
    print(f"    sources.yaml: auto-added new source '{source_id}' ({address})")


# ------------------------------------------------------- brain@ flags (#9) --
# Handles messages Brian sends to brain@ from his own address directly —
# BUILD.md open decision #9. Real shape, from a live sample reviewed
# 2026-08-16 (six real messages): a bare URL meaning "follow this," a bare
# URL meaning "read this" (sometimes both), a raw thought with no link at
# all, and (per Brian, not yet seen live) a screenshot possibly annotated
# with circling. None of these fit fetch_entries_email()'s uniform
# newsletter treatment (extract insights or NOT_RELEVANT) — there's often
# no article body to extract from, and even when there is, Brian's own
# framing (the subject line) is the part worth preserving, not just the
# linked page's insights. Every brain-flag message gets exactly one
# ingest/brain-flags/queue.md entry either way, so nothing gets silently
# dropped the way a NOT_RELEVANT newsletter issue would be.


def _sender_is_verified_personal(header_map: dict) -> bool:
    """True if this message's From is really personal_flag_sender(). Checks
    dkim=pass first (tightens automatically, no code change, once Brian
    fixes bmad.com's DNS) but accepts spf=pass alone for now — see
    personal_flag_sender()'s comment for why that's an acceptable interim
    bar: nothing this unlocks does anything more consequential than
    writing a quarantined ingest/ note or a review-queue entry, both
    already human-reviewed downstream."""
    _, address = _parse_sender_header(header_map.get("From", ""))
    target = personal_flag_sender()
    if not target or address != target:
        return False
    auth = header_map.get("Authentication-Results", "")
    return "dkim=pass" in auth or "spf=pass" in auth


def _gmail_find_image_attachments(payload: dict) -> list[dict]:
    """Depth-first search of a Gmail message payload for real image
    attachments (not inline images referenced by cid, which wouldn't have
    a body.attachmentId) — screenshots Brian's flagged, per his 2026-08-16
    note that these could carry hand-drawn circling/markup."""
    results = []

    def walk(part):
        mime = part.get("mimeType", "")
        body = part.get("body", {}) or {}
        if mime.startswith("image/") and body.get("attachmentId"):
            results.append({
                "filename": part.get("filename") or "attachment",
                "mimeType": mime,
                "attachmentId": body["attachmentId"],
            })
        for sub in part.get("parts", []) or []:
            walk(sub)

    walk(payload)
    return results


def _gmail_decode_bytes(data: str) -> bytes:
    """Same base64url padding fix as _gmail_decode(), but returns raw bytes
    — an image attachment isn't text, unlike everywhere else this pipeline
    decodes Gmail API body data."""
    padded = data.replace("-", "+").replace("_", "/")
    padded += "=" * (-len(padded) % 4)
    return base64.b64decode(padded)


def _gmail_fetch_attachment_bytes(msg_id: str, attachment_id: str, access_token: str) -> bytes:
    resp = requests.get(
        f"{GMAIL_API_BASE}/{msg_id}/attachments/{attachment_id}",
        headers={"Authorization": f"Bearer {access_token}"}, timeout=30,
    )
    resp.raise_for_status()
    return _gmail_decode_bytes(resp.json()["data"])


VISION_TRANSCRIBE_PROMPT = (
    "This image was emailed directly to Brian's AI brain as something worth "
    "capturing — often a screenshot of an article, tweet, or document, "
    "sometimes with hand-drawn circling, underlining, or other markup "
    "pointing at the specific part he cares about. Transcribe the readable "
    "text plainly. If there's visible markup, say what it's pointing at as "
    "a separate short note — don't just describe the markup, say what it's "
    "emphasizing. Be concise and factual: this feeds a private review "
    "queue, not a public note. No preamble."
)


def _sniff_image_media_type(image_bytes: bytes, declared: str) -> str:
    """Gmail's reported attachment mimeType isn't always trustworthy —
    confirmed live 2026-08-16: a real attachment came back labeled
    image/png while its actual bytes were a JPEG, and Anthropic's vision
    API validates the real format and rejects a mismatch outright rather
    than just reading the bytes. Sniffs the real format from magic bytes;
    falls back to the declared type only if nothing recognized matches."""
    if image_bytes[:8] == b"\x89PNG\r\n\x1a\n":
        return "image/png"
    if image_bytes[:3] == b"\xff\xd8\xff":
        return "image/jpeg"
    if image_bytes[:6] in (b"GIF87a", b"GIF89a"):
        return "image/gif"
    if image_bytes[:4] == b"RIFF" and image_bytes[8:12] == b"WEBP":
        return "image/webp"
    return declared


def transcribe_image_attachment(
    image_bytes: bytes, mime_type: str, provider: str | None = None, model: str | None = None
) -> str:
    b64 = base64.b64encode(image_bytes).decode("ascii")
    return llm.generate(
        VISION_TRANSCRIBE_PROMPT, provider=provider, model=model, max_tokens=1024,
        images=[{"media_type": _sniff_image_media_type(image_bytes, mime_type), "data": b64}],
    )


def _host_label(url: str) -> str:
    return (urlsplit(url).netloc or url).lower().removeprefix("www.")


def _known_source_match(url: str, follows: list[dict], sources_path: Path) -> str | None:
    """Returns a short human label if url is already tracked — a live
    Substack follow, or already present in sources.yaml by host — else
    None. Only used to decide whether a 'follow this' flag still needs a
    queue-file reminder; never gates whether a note gets written."""
    match = substack_follows.matches_follow(url, follows)
    if match:
        return f"Substack follow: {match['name']}"
    host = _host_label(url)
    if not host:
        return None
    for s in load_sources(sources_path):
        for field in ("url", "feed_url"):
            existing = s.get(field)
            if existing and _host_label(existing) == host:
                return f"sources.yaml: {s.get('name', s['id'])}"
    return None


def append_to_queue(kind: str, subject: str, detail: str, dry_run: bool = False) -> None:
    """Appends one flagged item to ingest/brain-flags/queue.md for Brian to
    triage by hand (open decision #9) — same 'system surfaces, human
    decides' pattern as outputs/canon-triage/staleness-candidates.md, never
    auto-actioned further. Lives under ingest/ deliberately: Tier 1
    (quarantined, never indexed, excluded from the public KV sync per
    MAINTAINER.md rule 8), same protection third-party ingest notes already
    get, because these are Brian's own raw unreviewed flags — not vetted
    canon, and not something to publish before he's looked at it. Plain
    text append; Brian clears entries by deleting them as he handles them,
    unlike dated ingest/ notes which are a permanent historical log."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    entry = f"## {today} — {kind}\n\n**{subject}**\n\n{detail}\n\n---\n\n"

    if dry_run:
        print(f"\n[DRY RUN] would append to ingest/brain-flags/queue.md:\n{entry}")
        return

    BRAIN_FLAGS_QUEUE.parent.mkdir(parents=True, exist_ok=True)
    if not BRAIN_FLAGS_QUEUE.exists():
        BRAIN_FLAGS_QUEUE.write_text(
            "# Brain flags — needs a human look\n\n"
            "Personal messages sent to brain@ from Brian directly (open "
            "decision #9) that the pipeline couldn't fully auto-handle on "
            "its own. Not a gate on anything else in the pipeline — read, "
            "act, and delete each entry below as you handle it.\n\n---\n\n",
            encoding="utf-8",
        )
    with BRAIN_FLAGS_QUEUE.open("a", encoding="utf-8") as f:
        f.write(entry)


PASTED_CONTENT_MIN_CHARS = 200  # below this, body text reads as "just a URL" or "just a thought," not substance worth extracting on its own


def _transcribe_attachments(
    payload: dict, msg_id: str, provider: str | None, model: str | None
) -> list[str]:
    attachments = _gmail_find_image_attachments(payload)
    if not attachments or not llm.is_configured(provider or llm.current_provider()):
        return []
    notes = []
    try:
        access_token = _gmail_access_token()
    except requests.RequestException as e:
        return [f"(couldn't authenticate to fetch {len(attachments)} image attachment(s): {e})"]
    for att in attachments:
        try:
            img_bytes = _gmail_fetch_attachment_bytes(msg_id, att["attachmentId"], access_token)
            notes.append(transcribe_image_attachment(img_bytes, att["mimeType"], provider, model))
        except (requests.RequestException, RuntimeError) as e:
            notes.append(f"(image attachment '{att['filename']}' couldn't be transcribed: {e})")
    return notes


def handle_brain_flag(
    entry: dict,
    sources_path: Path,
    follows: list[dict],
    provider: str | None,
    model: str | None,
    dry_run: bool,
) -> str:
    """Routes one verified-personal brain@ message. Returns the Gmail label
    to apply — GMAIL_LABEL_INGESTED if a real ingest/ note got written,
    else GMAIL_LABEL_FLAGGED. Never GMAIL_LABEL_SKIPPED: unlike a
    newsletter issue judged not relevant, a brain-flag always gets a
    queue.md entry, so there's always something for Brian to see.

    What actually gets run through extraction, in priority order — never
    more than one candidate per message, so a note is written at most
    once: a flagged URL's fetched page (the common shape); the message's
    own body text if it's substantial on its own (e.g. a full pasted
    article — confirmed live 2026-08-16, an AT&T/WSJ piece pasted directly
    rather than linked); a screenshot transcription otherwise. Image
    attachments are only inspected in that last case — a real vision call
    isn't worth it when a URL or pasted text already has the real content
    (confirmed live 2026-08-16: that AT&T message also carried an
    unrelated storefront photo attachment; transcribing it would have
    wasted a call and, being irrelevant, could have shadowed the good
    pasted-text extraction if not for this ordering).
    """
    subject = entry["title"] or "(no subject)"
    body_text = (entry.get("content") or "").strip()
    payload = entry.get("_gmail_payload") or {}
    msg_id = entry.get("gmail_msg_id")
    urls = URL_RE.findall(body_text)

    detail_lines = []
    flag_source = flag_entry = None
    image_notes = []

    if urls:
        url = urls[0]
        linked_content = _fetch_external_link_content(url)
        if linked_content:
            flag_source = {
                "id": "brain-flag",
                "name": _host_label(url),
                "type": "flagged link",
                "pov": f'Brian flagged this directly to the brain, with his own note: "{subject}"',
            }
            flag_entry = {
                "title": subject if subject not in ("(no subject)", url) else _host_label(url),
                "link": url,
                "author": "Brian Madden (flagged)",
                "date_published": entry.get("date_published"),
                "content": linked_content,
            }
        else:
            detail_lines.append(f"Link couldn't be fetched: {url}")

        known = _known_source_match(url, follows, sources_path)
        if known:
            detail_lines.append(f"Source status: already tracked ({known}).")
        else:
            detail_lines.append(
                "Source status: **not currently followed/tracked.** If this was meant as "
                "a 'follow this' flag, follow it via the brianmaddenai Substack account "
                "(or add to sources.yaml if not Substack) next time you're doing maintenance."
            )
    elif len(body_text) > PASTED_CONTENT_MIN_CHARS:
        flag_source = {
            "id": "brain-flag",
            "name": "pasted content",
            "type": "flagged content",
            "pov": f'Brian pasted this directly into an email to the brain, with his own note: "{subject}"',
        }
        flag_entry = {
            "title": subject,
            "link": "",
            "author": "Brian Madden (flagged)",
            "date_published": entry.get("date_published"),
            "content": body_text,
        }
    else:
        image_notes = _transcribe_attachments(payload, msg_id, provider, model)
        if image_notes:
            flag_source = {
                "id": "brain-flag",
                "name": "image attachment",
                "type": "flagged screenshot",
                "pov": f'Brian flagged this directly to the brain (image attachment), with his own note: "{subject}"',
            }
            flag_entry = {
                "title": subject if subject != "(no subject)" else "(screenshot, no subject)",
                "link": "",
                "author": "Brian Madden (flagged, image attachment)",
                "date_published": entry.get("date_published"),
                "content": "\n\n---\n\n".join(image_notes),
            }

    note_path = None
    if flag_source:
        template = (Path(__file__).parent / "prompt.md").read_text(encoding="utf-8")
        note_body = extract(template, flag_source, flag_entry, provider=provider, model=model)
        if note_body:
            note_path = write_note(
                ROOT / "ingest", flag_source, flag_entry, note_body, dry_run,
                model=llm.resolve_model(provider or llm.current_provider(), model),
                ingest_method="brain-flag",
            )
            detail_lines.append(f"Ingest note written: `{note_path.relative_to(ROOT)}`")
        else:
            detail_lines.append("Content fetched but nothing extractable — thin, paywalled, or judged not relevant.")

    if image_notes:
        detail_lines.append("**Image attachment(s):**\n\n" + "\n\n".join(image_notes))

    if not flag_source:
        detail_lines.append(body_text if body_text else "(empty message — the subject line is the whole flag)")

    if urls:
        kind = "link flag"
    elif flag_source and flag_source["type"] == "flagged content":
        kind = "pasted content"
    elif image_notes:
        kind = "image flag"
    else:
        kind = "idea"
    append_to_queue(kind, subject, "\n\n".join(detail_lines), dry_run=dry_run)

    return GMAIL_LABEL_INGESTED if note_path else GMAIL_LABEL_FLAGGED


def _find_existing_source_for_follow(follow: dict, existing_sources: list[dict]) -> dict | None:
    """Does any already-curated sources.yaml entry already cover this
    followed publication? Checks each existing source's url/feed_url
    against the follow's subdomain/custom_domain via matches_follow() —
    catches the same publication registered under a hand-picked id that
    doesn't slugify to match the follow's display name (e.g. Ethan
    Mollick's 'ethan-mollick' vs. his Substack's own name 'One Useful
    Thing'). id-slug collision alone isn't enough: a name-derived slug can
    differ from an existing id while still being the same feed (found live
    2026-08-17 — a cold-start run with no prior snapshot treated all ~60
    of the account's existing follows as new and mis-registered ~50 exact
    duplicates this check would have caught)."""
    for s in existing_sources:
        for candidate_url in (s.get("url"), s.get("feed_url")):
            if candidate_url and substack_follows.matches_follow(candidate_url, [follow]):
                return s
    return None


def _register_new_substack_source(follow: dict, sources_path: Path) -> None:
    """Appends a sources.yaml entry for a publication newly seen in the
    brianmaddenai account's live follows (resolves open decision #7's
    dormant idea via #9's design session, 2026-08-16). Unlike an emailed
    'follow this' flag (see handle_brain_flag — those only ever get a
    queue-file reminder), this reflects a follow Brian actually completed,
    so it's safe to auto-register — same precedent as
    auto_register_email_source() for newsletters. Substack reliably serves
    RSS at /feed for both subdomain and custom-domain publications
    (confirmed live 2026-08-16 against three real follows, not assumed),
    so this gets a real working feed_url immediately, not a null
    placeholder. Plain text append, same reason as everywhere else in this
    file: re-dumping the whole YAML would strip hand-written comments.
    Caller (main()) is responsible for skipping follows already covered by
    an existing source — see _find_existing_source_for_follow()."""
    existing_ids = {s["id"] for s in load_sources(sources_path)}
    base_id = slugify(follow.get("name") or follow.get("subdomain") or "unknown-substack")
    source_id = base_id
    n = 2
    while source_id in existing_ids:
        source_id = f"{base_id}-{n}"
        n += 1

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    note = (
        f"Auto-discovered from the brianmaddenai Substack account's live follows on "
        f"{today} — a real completed follow, documentation only, not a gate. Not yet "
        f"reviewed by Brian."
    )
    entry_yaml = (
        f"\n  - id: {source_id}\n"
        f"    name: {json.dumps(follow.get('name') or source_id, ensure_ascii=False)}\n"
        f"    type: newsletter\n"
        f"    url: {json.dumps(follow['url'], ensure_ascii=False)}\n"
        f"    feed_url: {json.dumps(follow['url'] + '/feed', ensure_ascii=False)}\n"
        f"    priority: regular\n"
        f"    note: {json.dumps(note, ensure_ascii=False)}\n"
    )
    with sources_path.open("a", encoding="utf-8") as f:
        f.write(entry_yaml)
    print(f"    sources.yaml: auto-added new Substack follow '{source_id}'")


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
    text = text.strip()

    # Real failure modes seen in production (2026-08-19 daily run), not
    # hypothetical: (1) an empty completion for a perfectly good article —
    # `text == ""` isn't `None`, so a bare `is None` check let a blank note
    # get written; (2) the model appending NOT_RELEVANT after an
    # explanatory paragraph instead of as the whole response, which
    # `startswith` alone doesn't catch; (3) prose explaining a stub instead
    # of using a sentinel at all, since until this fix there wasn't one for
    # "relevant but too thin" — only INSUFFICIENT_CONTENT's addition closes
    # that gap. All three silently produced a written note that was empty,
    # near-empty, or not actually insights. Three checks now, in order:
    # empty response, either sentinel anywhere in the text (not just a
    # startswith match), and — the catch-all for anything that still isn't
    # one of those two but also doesn't look like a real note — requiring
    # the expected `## Insights` header. A future prompt-following slip
    # from the model fails closed (skipped, logged) instead of writing
    # something malformed.
    if not text:
        print(f"    ! empty extraction response, skipped: {entry.get('title')}")
        return None
    if "NOT_RELEVANT" in text or "INSUFFICIENT_CONTENT" in text:
        return None
    if not text.startswith("## Insights"):
        print(f"    ! malformed extraction response (no ## Insights header), skipped: {entry.get('title')}")
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

    sources_path = ROOT / "sources" / "sources.yaml"
    sources = load_sources(sources_path)
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

    known_email_senders = load_known_email_senders(sources_path)

    # Fetched once, reused for both brain@ flag routing (is this URL
    # already followed?) and the daily follows-diff below (open decisions
    # #7/#9) — one HTTP call regardless of how many sources actually need
    # it. Best-effort: a fetch failure degrades both to "unknown" rather
    # than sinking the run.
    follows: list[dict] = []
    if any(s.get("ingest_method") == "email" for s in sources):
        try:
            follows = substack_follows.fetch_follows()
        except requests.RequestException as e:
            print(f"substack follows fetch failed ({e}) — brain@ follow-checks will report 'not tracked', daily diff skipped\n")

    # Per-source outcome, one record per registry entry regardless of what
    # happened — success, error, or a by-design skip. Brian's ask
    # (2026-08-25, after spotting that nearly half the registry silently
    # fails every day): make the checking itself visible, not just its
    # output, so a source going quiet reads as a fact on the page rather
    # than something that has to be dug out of Actions logs. Persisted to
    # ingest/.last_run_sources.json (see write_source_results() below) and
    # rendered into the brief's own "Sources checked today" section by
    # skills/brief/brief.py.
    source_results: list[dict] = []

    total_new = 0
    total_written = 0
    for source in sources:
        ingest_method = source.get("ingest_method")
        is_email = ingest_method == "email"
        is_x = ingest_method == "x"
        method = "email" if is_email else ("x" if is_x else "feed")
        if not is_email and not is_x and not source.get("feed_url"):
            # A `sender` field means this row is documentation for a
            # publication actually captured through the shared brain-inbox
            # source (matched by From address — see brief.py's
            # load_sender_homepages()), not a real gap: most of these were
            # auto-registered from a real brain@ ingestion for exactly that
            # reason (sources.yaml's own per-entry notes say so). No
            # `sender` at all means nothing is currently checking it —
            # genuinely unchecked, not just checked a different way.
            if source.get("sender"):
                reason = "documentation only — arrives via the shared brain-inbox source, attributed by sender"
            else:
                reason = "no feed_url and no sender configured — not currently being checked"
            print(f"[{source['id']}] skipped — {reason}")
            source_results.append({
                "id": source["id"], "name": source.get("name", source["id"]),
                "method": method, "status": "skipped", "reason": reason,
            })
            continue

        if is_email:
            entries, err = fetch_entries_email(source, since_days, args.max_per_source)
        elif is_x:
            entries, err = fetch_entries_x(source, since_days, args.max_per_source)
        else:
            entries, err = fetch_entries(source, since_days, args.max_per_source)
        if err:
            print(f"[{source['id']}] {err}")
            source_results.append({
                "id": source["id"], "name": source.get("name", source["id"]),
                "method": method, "status": "error", "reason": err,
            })
            continue

        new_entries = [e for e in entries if e["link"] not in seen_urls]
        print(f"[{source['id']}] {len(entries)} entries in window, {len(new_entries)} new")
        total_new += len(new_entries)
        source_results.append({
            "id": source["id"], "name": source.get("name", source["id"]),
            "method": method, "status": "ok",
            "entries_in_window": len(entries), "new_entries": len(new_entries),
        })

        if not ready:
            for e in new_entries:
                print(f"    would extract: {e['title']}")
            continue

        for entry in new_entries:
            if is_email and _sender_is_verified_personal(entry.get("_gmail_header_map") or {}):
                print(f"    brain@ flag from {personal_flag_sender()}: {entry['title']}")
                label = handle_brain_flag(
                    entry, sources_path, follows, args.provider, args.llm_model, args.dry_run,
                )
                if not args.dry_run:
                    gmail_apply_label(entry.get("gmail_msg_id"), label, archive=True)
                total_written += 1
                continue

            enrich_with_transcript(entry, source)
            body = extract(
                template, source, entry,
                provider=args.provider, model=args.llm_model,
            )
            if body is None:
                print(f"    skipped (not relevant): {entry['title']}")
                # Label it even when skipped — otherwise a not-relevant
                # newsletter issue gets re-fetched and re-judged
                # not-relevant every single run forever.
                if is_email and not args.dry_run:
                    gmail_apply_label(entry.get("gmail_msg_id"), GMAIL_LABEL_SKIPPED)
                continue
            write_note(
                ingest_root, source, entry, body, args.dry_run, model=model_used,
                ingest_method="email" if is_email else ("x" if is_x else "feed"),
            )
            if is_email and not args.dry_run:
                gmail_apply_label(entry.get("gmail_msg_id"), GMAIL_LABEL_INGESTED, archive=True)
                _, sender_address = _parse_sender_header(entry["author"])
                matched = find_feed_source_for_email_sender(sender_address, sources)
                if matched and flip_source_to_email(matched, sender_address, sources_path):
                    known_email_senders.add(sender_address)
                else:
                    auto_register_email_source(entry["author"], sources_path, known_email_senders)
            seen_urls.add(entry["link"])
            total_written += 1

    # Daily follows-diff (open decision #7, resolved into #9's design
    # 2026-08-16) — only on a full, real run, same gate as the last-run
    # clock below: a --source test or --dry-run preview shouldn't touch
    # sources.yaml or advance the snapshot.
    if follows and not args.dry_run and not args.source:
        snapshot_path = ROOT / "sources" / ".substack_follows_snapshot.json"
        added, removed = substack_follows.diff_snapshot(snapshot_path, follows)
        if added or removed:
            print(f"\nsubstack follows changed: +{len(added)} -{len(removed)}")
        existing_sources = load_sources(sources_path)
        for f in added:
            existing = _find_existing_source_for_follow(f, existing_sources)
            if existing:
                print(f"    substack follow '{f.get('name')}' already covered by "
                      f"existing source '{existing['id']}' — skipping auto-register")
                continue
            _register_new_substack_source(f, sources_path)
        if removed:
            append_to_queue(
                "substack unfollow",
                f"{len(removed)} publication(s) no longer followed",
                "No longer in the brianmaddenai account's live follows: " + ", ".join(removed) +
                ". Corresponding sources.yaml entries (if any) were left as-is — "
                "review whether to keep or archive them.",
            )
        substack_follows.save_snapshot(snapshot_path, follows)

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
        write_source_results(run_time, source_results)
        print(f"recorded last run: {run_time.isoformat()}")


if __name__ == "__main__":
    main()

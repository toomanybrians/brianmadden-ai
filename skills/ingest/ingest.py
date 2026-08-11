#!/usr/bin/env python3
"""
ingest.py — pull sources/sources.yaml's feeds, extract insights, write
tier-1 notes to ingest/. See skills/ingest/README.md for usage.

Deterministic plumbing (feed fetch, dedupe) is plain code; the one model
call per new entry is where judgment (extraction, relevance, framing) lives
— per MAINTAINER.md's working conventions.
"""

import argparse
import calendar
import html
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "skills"))
from lib import llm  # noqa: E402  (needs sys.path set first)

USER_AGENT = "brianmadden-ai-ingest/0.1 (+https://brianmadden.ai)"
MAX_CONTENT_CHARS = 8000

FOCUS = (
    "AI's impact on knowledge work and the enterprise — how AI is reshaping "
    "how people work, how organizations are structured, and what the "
    "workplace looks like as it changes"
)

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


# -------------------------------------------------------------- fetching --

def strip_html(text: str) -> str:
    text = TAG_RE.sub(" ", text or "")
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def fetch_entries(source: dict, since_days: int, max_per_source: int):
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

        entries.append({
            "title": (raw.get("title") or "").strip(),
            "link": (raw.get("link") or "").strip(),
            "author": (raw.get("author") or "").strip(),
            "date_published": date_published,
            "published_dt": published_dt,
            "content": content,
        })

    entries.sort(
        key=lambda e: e["published_dt"] or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )
    return entries[:max_per_source], None


def fetch_entries_email(source: dict, since_days: int, max_per_source: int):
    """
    Stub for BUILD.md open decision #7a — non-Substack email newsletters
    (e.g. exec-ai-insider-weekly, feed_url: null) ingested by polling
    brain@brianmadden.ai via the Gmail API, rather than RSS.

    Not implemented: the brain@ mailbox doesn't exist yet (Workspace setup
    is BUILD.md Day 1/8, not done). When it exists, this should:
      1. Poll the Gmail API for mail from this source's known sender(s) in
         brain@'s inbox.
      2. Extract the message body (plain text preferred over HTML).
      3. Return entries in the same shape fetch_entries() returns, so the
         extract()/write_note() pipeline below is unchanged.
    """
    raise NotImplementedError(
        "Email ingestion not built yet — needs brain@brianmadden.ai "
        "(BUILD.md open decision #7a, Day 1/8)."
    )


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
        "{{FOCUS}}": FOCUS,
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
    text = llm.generate(prompt_text, provider=provider, model=model, max_tokens=1024)
    if text == "NOT_RELEVANT" or text.startswith("NOT_RELEVANT"):
        return None
    return text


# ------------------------------------------------------------------ write --

def slugify(text: str, max_len: int = 60) -> str:
    text = SLUG_RE.sub("-", (text or "").lower()).strip("-")
    return text[:max_len].rstrip("-")


def write_note(
    ingest_root: Path, source: dict, entry: dict, body: str, dry_run: bool, model: str
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
        "ingest_method": "feed",
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
    parser.add_argument("--since-days", type=int, default=7, help="only entries published in the last N days (default 7)")
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

    total_new = 0
    total_written = 0
    for source in sources:
        if not source.get("feed_url"):
            print(f"[{source['id']}] skipped — no feed_url")
            continue

        entries, err = fetch_entries(source, args.since_days, args.max_per_source)
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
            body = extract(template, source, entry, provider=args.provider, model=args.llm_model)
            if body is None:
                print(f"    skipped (not relevant): {entry['title']}")
                continue
            write_note(ingest_root, source, entry, body, args.dry_run, model=model_used)
            seen_urls.add(entry["link"])
            total_written += 1

    summary = f"\n{total_new} new entries found; {total_written} notes written"
    if args.dry_run:
        summary += " (dry run, nothing saved)"
    if not ready:
        summary += f" — extraction skipped, {llm.required_env_var(provider)} not set"
    print(summary)


if __name__ == "__main__":
    main()

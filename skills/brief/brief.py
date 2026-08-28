#!/usr/bin/env python3
"""
brief.py — read the ingest/ notes since the last briefing run together
against full canon, and write a Daily Brief to outputs/technical-briefings/. See
skills/brief/README.md for usage.

This is the whole-canon, cross-note synthesis step that ingest-time
extraction deliberately does NOT do (see BUILD.md's D5 kickoff and the
2026-08-11 framework-citation detour) — one model call sees every new note
at once, plus Brian's voice/published-thinking/developing-thinking/
frameworks, and judges what's signal, what confirms existing threads, and
what doesn't fit anywhere yet. Deterministic plumbing (note selection,
thread-tracker bookkeeping, promotion-candidate threshold) is plain code;
the synthesis judgment is the one model call — per MAINTAINER.md's working
conventions.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "skills"))
from lib import llm  # noqa: E402  (needs sys.path set first)

DEFAULT_MODEL = "claude-sonnet-5"
# Cross-note synthesis over a full day's ingest batch (and a first run over
# a 30-day catch-up batch) is the hardest judgment call in the pipeline so
# far — Brian's original call (2026-08-11) was Opus over Sonnet for this
# specific skill, unlike ingest's per-article extraction. Switched to Sonnet
# 2026-08-26 after Opus's output drifted into over-written prose (rhetorical
# flourishes, bolded jargon inline in sentences — see me/voice.md's
# AI-commentary-tells and me/style-guide.md's slug-in-prose entries, both
# added the same day) that made the brief hard to read; a same-batch,
# same-prompt side-by-side after the prompt fixes still showed Sonnet
# writing plainer and ~35% shorter with zero flourish artifacts, Opus with
# some residual. Still overridable via --llm-model / LLM_MODEL, same as
# every other skill.
SIGNAL_DELIMITER = "---THREAD-SIGNALS---"
PROMOTION_THRESHOLD = 3  # distinct briefing runs a thread must recur in before it's queued for Brian's review

# Fallback link target for canon content with no other public URL (e.g. a
# developing-thinking.md bullet that hasn't become a post yet). me/,
# frameworks/, posts/, talks/, and podcast/ are all already on `main` (this
# repo had a public v1 brain before v2), so these links resolve today, even
# though ingest/ and outputs/ (v2-branch-only) would not.
GITHUB_REPO = "https://github.com/toomanybrians/brianmadden-ai"
GITHUB_BASE = f"{GITHUB_REPO}/blob/main/"

SOURCES_PATH = ROOT / "sources" / "sources.yaml"

INGEST_ROOT = ROOT / "ingest"
# Split 2026-08-12 (Brian's call): the dense brief and the Substack draft
# serve different audiences — technical-briefings/ is AI-facing (full
# detail, audit trail, what MCP-connecting AIs would actually want) and
# published/ is human-facing (Substack-bound, condensed). Filenames in
# published/ no longer need a "-published" suffix now that the directory
# says it.
OUTPUT_ROOT = ROOT / "outputs" / "technical-briefings"
PUBLISHED_ROOT = ROOT / "outputs" / "published"
LAST_RUN_PATH = OUTPUT_ROOT / ".last_run.json"
SOURCE_RESULTS_PATH = ROOT / "ingest" / ".last_run_sources.json"
TRACKER_PATH = OUTPUT_ROOT / ".thread_tracker.json"
CANDIDATES_PATH = OUTPUT_ROOT / "promotion-candidates.md"

DEFAULT_SINCE_DAYS = 1.0  # fallback when there's no recorded prior briefing run
MIN_SINCE_DAYS = 0.1


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
    if explicit is not None:
        return explicit, "explicit --since-days"
    last_run = read_last_run()
    if last_run is None:
        return DEFAULT_SINCE_DAYS, "no recorded prior briefing run, using default"
    elapsed_hours = (datetime.now(timezone.utc) - last_run).total_seconds() / 3600
    since_days = max(elapsed_hours / 24, MIN_SINCE_DAYS)
    return since_days, f"auto — {elapsed_hours:.1f}h since last briefing run ({last_run.isoformat()})"


# -------------------------------------------------------------- ingest io --

def read_frontmatter_and_body(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, parts[2].strip()


AUTHOR_EMAIL_RE = re.compile(r"\s*<[^<>]*>\s*$")
AUTHOR_EMAIL_ADDR_RE = re.compile(r"<([^<>]+)>")


def _clean_author_name(author: str) -> str:
    """Ingest notes store email-sourced authors as 'Display Name
    <address@example.com>' (straight from the message's From header). The
    display name is what a citation should use ('via NFX', not 'via NFX
    <qed@nfx.com>') — stripping the address here, deterministically, means
    brief.py's prompt never has to ask the model to do that formatting
    itself. A no-angle-bracket author (RSS byline, etc.) passes through
    unchanged."""
    return AUTHOR_EMAIL_RE.sub("", author or "").strip()


def _extract_author_email(author: str) -> str:
    """Pulls the bare address out of 'Display Name <address@example.com>',
    lowercased for matching against sources.yaml's `sender` field. Empty
    string if there's no angle-bracket address (RSS bylines, etc.)."""
    m = AUTHOR_EMAIL_ADDR_RE.search(author or "")
    return m.group(1).strip().lower() if m else ""


def load_sender_homepages() -> dict[str, str]:
    """Maps a lowercased sources.yaml `sender` address to its `url` —
    2026-08-18, Brian's ask: for an email-sourced ingest note with no
    per-article source_url (a digest with no single story, a subscription-
    confirmation email), fall back to the newsletter's own homepage rather
    than naming it with no link at all. Read fresh each run, not cached —
    sources.yaml gets edited by hand and by ingest.py's own
    auto-registration, and this should always reflect the current file.
    Entries with no `url` filled in yet (still `null`) are simply absent
    from the map, same as if the source didn't exist — no dict entry with
    a None value to trip up an f-string later."""
    if not SOURCES_PATH.exists():
        return {}
    data = yaml.safe_load(SOURCES_PATH.read_text(encoding="utf-8")) or {}
    return {
        s["sender"].lower(): s["url"]
        for s in data.get("sources", [])
        if s.get("sender") and s.get("url")
    }


def load_previously_briefed_paths() -> set[str]:
    """Every ingest/ note path already listed in some prior dense brief's
    `sources:`. No separate state file — the committed briefs *are* the
    state, same pattern skills/ingest/ uses for its own URL dedup. This is
    the real guard against double-processing; `since_days` below is only
    a coarse pre-filter and, on its own, isn't reliable — date_captured
    has day granularity, so a since_days window that crosses a calendar
    boundary (e.g. 26 hours) rounds up to the whole previous day and can
    re-include everything captured that day, not just the last N hours of
    it (caught 2026-08-12: a 1.1-day window pulled in 124 notes instead of
    the ~27 actually new since the last run)."""
    seen = set()
    for path in sorted(OUTPUT_ROOT.rglob("*.md")):
        if path.name == "promotion-candidates.md":
            continue
        fm, _ = read_frontmatter_and_body(path)
        for src in fm.get("sources") or []:
            if isinstance(src, str) and src.startswith("ingest/"):
                seen.add(src)
    return seen


def load_recent_notes(since_days: float) -> list[dict]:
    cutoff = (datetime.now(timezone.utc) - timedelta(days=since_days)).date()
    already_briefed = load_previously_briefed_paths()
    sender_homepages = load_sender_homepages()
    notes = []
    for path in sorted(INGEST_ROOT.rglob("*.md")):
        if path.name == "README.md":
            continue
        rel_path = path.relative_to(ROOT).as_posix()
        if rel_path in already_briefed:
            continue
        fm, body = read_frontmatter_and_body(path)
        date_captured = fm.get("date_captured")
        if not date_captured:
            continue
        try:
            captured = datetime.strptime(str(date_captured), "%Y-%m-%d").date()
        except ValueError:
            continue
        if captured < cutoff:
            continue
        source_url = fm.get("source_url", "")
        author_raw = fm.get("author", "")
        # Only worth offering a homepage fallback when there's no
        # per-article link to begin with — if source_url is set, that's
        # always the more specific, better link.
        homepage_url = "" if source_url else sender_homepages.get(_extract_author_email(author_raw), "")
        notes.append({
            "path": rel_path,
            "title": fm.get("title", "(untitled)"),
            "source": fm.get("source", fm.get("source_id", "unknown")),
            "source_url": source_url,
            "author": _clean_author_name(author_raw),
            "homepage_url": homepage_url,
            "date_published": fm.get("date_published"),
            "body": body,
        })
    return notes


# ---------------------------------------------------------------- canon --

def load_frameworks_list() -> str:
    lines = []
    for path in sorted((ROOT / "frameworks").glob("*.md")):
        fm, _ = read_frontmatter_and_body(path)
        if fm.get("status") == "archived":
            continue  # retired frameworks stay on disk for lineage but never inform new briefs
        title = fm.get("title", path.stem)
        description = fm.get("description", "")
        date = fm.get("date", "")
        url = fm.get("original_url") or GITHUB_BASE + path.relative_to(ROOT).as_posix()
        lines.append(f"- [{title}]({url}) ({date}) — {description}".rstrip())
    return "\n".join(lines) if lines else "(no frameworks on file)"


# ----------------------------------------------------------------- tracker --

def load_tracker() -> list[dict]:
    if not TRACKER_PATH.exists():
        return []
    try:
        return json.loads(TRACKER_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def write_tracker(entries: list[dict]) -> None:
    TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)
    TRACKER_PATH.write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8")


def render_tracked_threads(tracker: list[dict], brief_date: str) -> str:
    """Rendered, reader-facing list only — build_prompt() gives the model
    the full unfiltered 'watching' list separately (it needs every tracked
    thread to check today's batch against, per prompt.md's dedup guidance),
    so filtering here doesn't cost the model any context.

    Showing all ~20 'watching' entries every day regardless of whether
    today's batch touched them buried the ones that actually mattered
    (Brian's ask, 2026-08-28) — a thread only earns a line here if today's
    batch touched it, or it's trending (2+ recurrences within the last
    day). Everything else stays in .thread_tracker.json, just not printed."""
    watching = [t for t in tracker if t.get("status") == "watching"]
    if not watching:
        return "(nothing being tracked yet — this is either the first run, or nothing has recurred)"
    brief_dt = datetime.strptime(brief_date, "%Y-%m-%d")

    def _touched_or_trending(t: dict) -> bool:
        if t["last_seen"] == brief_date:
            return True
        last_seen_dt = datetime.strptime(t["last_seen"], "%Y-%m-%d")
        return t["count"] >= 2 and (brief_dt - last_seen_dt).days <= 1

    shown = [t for t in watching if _touched_or_trending(t)]
    if not shown:
        return (f"(nothing touched or trending today — {len(watching)} pattern(s) "
                "still being watched quietly; full list in "
                "outputs/technical-briefings/.thread_tracker.json)")
    lines = []
    for t in shown:
        lines.append(f"- **{t['slug']}** — {t['description']} (seen {t['count']}x, first {t['first_seen']}, last {t['last_seen']})")
    return "\n".join(lines)


def render_tracked_threads_section(tracker: list[dict], brief_date: str) -> str:
    body = render_tracked_threads(tracker, brief_date)
    # Bold slugs, italicized+linked .md references (not backtick/inline-code)
    # — Substack's editor renders pasted inline code in an oversized,
    # visually odd Courier face (Brian's call, 2026-08-16; see
    # me/style-guide.md). Links point at `main` (GITHUB_BASE), not `v2` —
    # they 404 until the v2 launch PR merges, which Brian's explicitly fine
    # with for the few days until then, since main is where this actually
    # resolves once merged.
    candidates_link = f"[outputs/technical-briefings/promotion-candidates.md]({GITHUB_BASE}outputs/technical-briefings/promotion-candidates.md)"
    developing_link = f"[me/developing-thinking.md]({GITHUB_BASE}me/developing-thinking.md)"
    return (
        "## Threads being tracked\n\n"
        "Patterns flagged as \"doesn't fit yet\" on a previous day, being watched "
        "for recurrence. Only threads today's batch touched, or that are "
        "trending (2+ recurrences within the last day), are listed here — "
        "the rest are still being watched, just not printed daily. A thread "
        f"that recurs {PROMOTION_THRESHOLD}+ times gets queued in "
        f"*{candidates_link}* for Brian to "
        f"review — nothing here is ever written into *{developing_link}* "
        "automatically.\n\n" + body
    )


def load_source_results() -> dict | None:
    """Reads what skills/ingest/ingest.py wrote about this run's actual
    fetch attempts (ingest/.last_run_sources.json — see
    write_source_results() there). Returns None if it's missing, e.g. a
    hand-run brief.py against notes ingested by some other means — the
    section is simply omitted rather than rendered with false data."""
    if not SOURCE_RESULTS_PATH.exists():
        return None
    try:
        return json.loads(SOURCE_RESULTS_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, KeyError):
        return None


def render_sources_checked_section(data: dict | None) -> str:
    """Every source in the registry gets a line, success or not — the
    point (Brian's ask, 2026-08-25, after nearly half the registry turned
    out to have been failing silently since the pipeline's first run) is
    that "checked and found nothing" and "never actually checked" read
    identically from the outside unless this says otherwise. Grouped
    worst-news-first: real failures, then by-design skips (already
    routed another way, not a problem), then clean checks — contributed
    or not, listed by name either way rather than folded into a bare
    count, so a specific source going quiet is visible without cross-
    referencing sources.yaml."""
    if not data or not data.get("results"):
        return (
            "## Sources checked today\n\n"
            "(not recorded this run — no ingest/.last_run_sources.json found)\n"
        )
    results = data["results"]
    run_utc = data.get("run_utc", "unknown time")
    errors = [r for r in results if r["status"] == "error"]
    skipped = [r for r in results if r["status"] == "skipped"]
    ok = sorted(
        [r for r in results if r["status"] == "ok"],
        key=lambda r: r.get("new_entries", 0), reverse=True,
    )

    lines = [
        "## Sources checked today",
        "",
        f"{len(results)} registered sources, checked as of {run_utc}: "
        f"{len(ok)} fetched cleanly, {len(errors)} failed, {len(skipped)} skipped by design.",
    ]
    if errors:
        lines += ["", "**Failed to fetch:**", ""]
        lines += [f"- {r['name']} — {r['reason']}" for r in errors]
    if skipped:
        lines += ["", "**Skipped:**", ""]
        lines += [f"- {r['name']} — {r['reason']}" for r in skipped]
    if ok:
        lines += ["", "**Checked cleanly:**", ""]
        lines += [f"- {r['name']} — {r.get('new_entries', 0)} new" for r in ok]
    return "\n".join(lines) + "\n"


def update_tracker(tracker: list[dict], signals: dict, run_date: str) -> tuple[list[dict], list[dict]]:
    """Returns (updated_tracker, newly_promoted_entries)."""
    by_slug = {t["slug"]: t for t in tracker}
    promoted = []

    for item in signals.get("recurring", []) or []:
        slug = item.get("slug")
        entry = by_slug.get(slug)
        if not entry:
            continue  # model referenced a slug we're not actually tracking — ignore rather than trust it
        if entry["last_seen"] == run_date:
            continue  # already touched this run (e.g. --dry-run rerun same day)
        entry["count"] += 1
        entry["last_seen"] = run_date
        entry.setdefault("history", []).append(item.get("note", ""))
        if entry["status"] == "watching" and entry["count"] >= PROMOTION_THRESHOLD:
            entry["status"] = "promoted-candidate"
            promoted.append(entry)

    for item in signals.get("new_threads", []) or []:
        slug = item.get("slug")
        description = (item.get("description") or "").strip()
        if not slug or slug in by_slug:
            continue  # exact-slug dedup only (v1 limitation — see README): near-duplicate
            # slugs for the same underlying idea won't merge automatically.
        if not description:
            # Confirmed real 2026-08-14: Opus's own THREAD-SIGNALS JSON
            # sometimes emits a new_threads item with a blank description
            # (valid JSON, so parse_response() doesn't catch it) — a thread
            # with no description can't be watched or rendered
            # meaningfully (" — (seen 1x...)" with nothing between the dash
            # and the parenthetical), so drop it here rather than seed
            # permanent dead weight into the tracker.
            continue
        entry = {
            "slug": slug,
            "description": description,
            "first_seen": run_date,
            "last_seen": run_date,
            "count": 1,
            "status": "watching",
            "history": [],
        }
        by_slug[slug] = entry
        tracker.append(entry)

    return tracker, promoted


def append_promotion_candidates(promoted: list[dict], run_date: str) -> None:
    if not promoted:
        return
    CANDIDATES_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not CANDIDATES_PATH.exists():
        CANDIDATES_PATH.write_text(
            "# Promotion candidates\n\n"
            "Threads the briefing skill has flagged as recurring "
            f"{PROMOTION_THRESHOLD}+ times without a home in canon. Queued here "
            "for Brian to review — a candidate becomes canon only if he "
            "deliberately edits it into `me/developing-thinking.md` himself "
            "(or a real framework). Nothing below this line was written by a "
            "human; nothing below this line is canon.\n",
            encoding="utf-8",
        )
    with CANDIDATES_PATH.open("a", encoding="utf-8") as f:
        for entry in promoted:
            f.write(f"\n## `{entry['slug']}` — flagged {run_date}\n\n")
            f.write(f"{entry['description']}\n\n")
            f.write(f"First seen {entry['first_seen']}, recurred {entry['count']} times through {entry['last_seen']}.\n\n")
            if entry.get("history"):
                f.write("Notes from each recurrence:\n\n")
                for note in entry["history"]:
                    if note:
                        f.write(f"- {note}\n")
            f.write("\n**Status: not yet reviewed by Brian.**\n")
    print(f"  {len(promoted)} thread(s) crossed the promotion threshold — appended to {CANDIDATES_PATH.relative_to(ROOT)}")


# -------------------------------------------------------------- prompting --

def _format_note_for_prompt(n: dict) -> str:
    """One ingest note's block in the prompt. The 'Newsletter homepage'
    line only appears when there's no per-article source_url but
    sources.yaml has a known homepage for that sender (see
    load_sender_homepages()) — added 2026-08-18 so the model has a real
    fallback link to offer (per prompt.md's Linking rules) instead of
    naming a newsletter with nothing to click through to."""
    lines = [
        f"### {n['title']} ({n['source']}, published {n['date_published'] or 'undated'})",
        f"Author/newsletter: {n['author'] or '(not captured)'}",
        f"Source URL: {n['source_url'] or '(none captured)'}",
    ]
    if n.get("homepage_url"):
        lines.append(f"Newsletter homepage (no per-article link available): {n['homepage_url']}")
    return "\n".join(lines) + f"\n\n{n['body']}"


def build_prompt(template: str, notes: list[dict], tracker: list[dict], brief_date: str) -> str:
    voice = (ROOT / "me" / "voice.md").read_text(encoding="utf-8")
    style_guide = (ROOT / "me" / "style-guide.md").read_text(encoding="utf-8")
    published = (ROOT / "me" / "published-thinking.md").read_text(encoding="utf-8")
    developing = (ROOT / "me" / "developing-thinking.md").read_text(encoding="utf-8")

    notes_block = "\n\n".join(_format_note_for_prompt(n) for n in notes)
    watching = [t for t in tracker if t.get("status") == "watching"]
    tracked_block = (
        "\n".join(f"- `{t['slug']}` — {t['description']}" for t in watching)
        if watching else "(none yet — nothing has been flagged as a recurring thread so far)"
    )

    replacements = {
        "{{VOICE}}": voice,
        "{{STYLE_GUIDE}}": style_guide,
        "{{PUBLISHED_THINKING}}": published,
        "{{DEVELOPING_THINKING}}": developing,
        "{{DEVELOPING_THINKING_URL}}": GITHUB_BASE + "me/developing-thinking.md",
        "{{PUBLISHED_THINKING_URL}}": GITHUB_BASE + "me/published-thinking.md",
        "{{GITHUB_BASE}}": GITHUB_BASE,
        "{{FRAMEWORKS_LIST}}": load_frameworks_list(),
        "{{TRACKED_THREADS}}": tracked_block,
        "{{ENTRY_COUNT}}": str(len(notes)),
        "{{INGEST_NOTES}}": notes_block,
        "{{BRIEF_DATE}}": brief_date,
    }
    text = template
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text


def parse_response(text: str) -> tuple[str, dict]:
    if SIGNAL_DELIMITER not in text:
        return text.strip(), {}
    brief_body, _, signal_text = text.partition(SIGNAL_DELIMITER)
    try:
        signals = json.loads(signal_text.strip())
    except json.JSONDecodeError:
        print("  warning: could not parse thread-signals JSON — brief still written, tracker not updated this run", file=sys.stderr)
        signals = {}
    return brief_body.strip(), signals


# ------------------------------------------------------------------ write --

def write_brief(brief_date: str, brief_body: str, tracker: list[dict], notes: list[dict],
                 model: str, dry_run: bool) -> Path:
    year, month, _ = brief_date.split("-")
    out_dir = OUTPUT_ROOT / year / month
    out_path = out_dir / f"{brief_date}.md"

    sources = [n["path"] for n in notes] + [
        "me/voice.md", "me/published-thinking.md", "me/developing-thinking.md",
    ]
    frontmatter = {
        "title": f"Daily Brief — {brief_date}",
        "date": brief_date,
        "file_type": "daily-brief",
        "tier": 3,
        "status": "not-reviewed-by-human",
        "authority_level": 2,
        "model": model,
        "sources": sources,
    }
    fm_yaml = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True, width=1000).strip()
    tracked_section = render_tracked_threads_section(tracker, brief_date)
    sources_section = render_sources_checked_section(load_source_results())
    full_text = f"---\n{fm_yaml}\n---\n\n{brief_body}\n\n{tracked_section}\n\n{sources_section}\n"

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
        description="Synthesize a Daily Brief from ingest/ notes since the last briefing run, read against full canon."
    )
    parser.add_argument("--since-days", type=float, default=None,
                         help="only ingest notes captured in the last N days. Default: auto — "
                              "time since the last briefing run (outputs/technical-briefings/.last_run.json), "
                              f"or {DEFAULT_SINCE_DAYS:g} day if there's no recorded prior run")
    parser.add_argument("--dry-run", action="store_true", help="print the brief instead of writing it (still calls the API, still calls the tracker logic in-memory only)")
    parser.add_argument("--provider", choices=sorted(llm.REQUIRED_ENV_VARS), help="override LLM_PROVIDER for this run")
    parser.add_argument("--llm-model", help=f"override the model id for this run (default: env LLM_MODEL, else {DEFAULT_MODEL})")
    args = parser.parse_args()

    load_dotenv(ROOT)

    provider = args.provider or llm.current_provider()
    # DEFAULT_MODEL (opus) only applies to the anthropic default — an
    # explicit --llm-model/LLM_MODEL always wins, and a non-anthropic
    # provider falls back to lib.llm's own per-provider default rather than
    # an Anthropic-only model id that provider wouldn't recognize.
    if args.llm_model or os.environ.get("LLM_MODEL"):
        model = llm.resolve_model(provider, args.llm_model)
    elif provider == "anthropic":
        model = DEFAULT_MODEL
    else:
        model = llm.resolve_model(provider, None)
    if not llm.is_configured(provider):
        print(f"{llm.required_env_var(provider)} not set for provider '{provider}' — cannot run the synthesis call. "
              f"Set it (see .env.example) and rerun.", file=sys.stderr)
        sys.exit(1)

    since_days, since_reason = resolve_since_days(args.since_days)
    print(f"window: {since_days:.2f} days ({since_reason})")

    notes = load_recent_notes(since_days)
    print(f"{len(notes)} ingest note(s) in window")
    if not notes:
        print("nothing new to synthesize — skipping brief")
        if not args.dry_run:
            run_time = datetime.now(timezone.utc)
            write_last_run(run_time)
            print(f"recorded last run: {run_time.isoformat()}")
        return

    tracker = load_tracker()
    brief_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    template = (Path(__file__).parent / "prompt.md").read_text(encoding="utf-8")
    prompt_text = build_prompt(template, notes, tracker, brief_date)

    print(f"calling {provider}/{model} for synthesis ({len(notes)} notes + full canon)...")
    # 6144 wasn't enough headroom (confirmed 2026-08-11): Opus 5's extended
    # thinking on a ~98-note/full-canon prompt can consume the entire
    # budget before emitting any answer text (stop_reason "max_tokens",
    # zero text blocks). 32000 leaves room for both thinking and the
    # answer; skills/lib/llm.py streams the call so this doesn't trip the
    # SDK's non-streaming long-request guard.
    response = llm.generate(prompt_text, provider=provider, model=model, max_tokens=32000)
    brief_body, signals = parse_response(response)

    tracker, promoted = update_tracker(tracker, signals, brief_date)
    write_brief(brief_date, brief_body, tracker, notes, model=model, dry_run=args.dry_run)

    if not args.dry_run:
        write_tracker(tracker)
        append_promotion_candidates(promoted, brief_date)
        run_time = datetime.now(timezone.utc)
        write_last_run(run_time)
        print(f"recorded last run: {run_time.isoformat()}")
    else:
        print(f"\n[DRY RUN] tracker signals parsed: {json.dumps(signals, indent=2)}")
        print("[DRY RUN] tracker/promotion-candidates/.last_run.json not written")


if __name__ == "__main__":
    main()

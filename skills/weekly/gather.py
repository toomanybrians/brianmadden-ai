#!/usr/bin/env python3
"""
gather.py — deterministic prep step for Deeper Thinking (the weekly
ceremony formerly/internally called "weekly-update"; see
.claude/skills/weekly-update/SKILL.md). Assembles the prep doc Brian reads
before the live ceremony and, with --send, emails it to him — this is the
"initial recap" Brian asked to have delivered automatically (2026-08-24),
run from daily-pipeline.yml on Fridays after that day's Daily Briefing.

Deliberately no LLM call except the one triage.py already makes on its
own (re-run as a subprocess here, same as the live ceremony does it) —
everything else is pure assembly of already-written text (this week's
daily-brief "Worth Brian's attention" sections, the promotion-candidates
queue, the current developing-thinking.md "Right now" section), matching
MAINTAINER.md's "deterministic plumbing is plain code" principle. This
script does NOT run the interactive decisions (steps 4-10 of the skill) —
those need Brian live. It only gets the prep doc into his inbox before he
sits down to do that part.

Running it:

    python3 skills/weekly/gather.py             # write the prep doc
    python3 skills/weekly/gather.py --send       # also email it
    python3 skills/weekly/gather.py --dry-run    # print, write nothing

Window: same auto-clock as skills/brief/ and skills/triage/ —
outputs/weekly-updates/.last_run.json, 7-days-back fallback if absent.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "skills"))
sys.path.insert(0, str(ROOT / "skills" / "brief"))

from brief import load_dotenv, read_frontmatter_and_body  # noqa: E402
from lib import gmail_send  # noqa: E402

BRIEFINGS_ROOT = ROOT / "outputs" / "technical-briefings"
WEEKLY_ROOT = ROOT / "outputs" / "weekly-updates"
LAST_RUN_PATH = WEEKLY_ROOT / ".last_run.json"
DEFAULT_DAYS_BACK = 7

PROMOTION_CANDIDATES_PATH = BRIEFINGS_ROOT / "promotion-candidates.md"
STALENESS_CANDIDATES_PATH = ROOT / "outputs" / "canon-triage" / "staleness-candidates.md"
DEVELOPING_THINKING_PATH = ROOT / "me" / "developing-thinking.md"
GITHUB_BLOB = "https://github.com/toomanybrians/brianmadden-ai/blob/main/"


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


def resolve_window(explicit_days: float | None) -> tuple[datetime, str]:
    if explicit_days is not None:
        since = datetime.now(timezone.utc) - timedelta(days=explicit_days)
        return since, f"explicit --since-days {explicit_days}"
    last_run = read_last_run()
    if last_run is None:
        since = datetime.now(timezone.utc) - timedelta(days=DEFAULT_DAYS_BACK)
        return since, f"no recorded prior run, defaulting to {DEFAULT_DAYS_BACK} days back"
    return last_run, f"auto — since last run ({last_run.isoformat()})"


def list_briefs_in_window(since: datetime) -> list[tuple[str, Path]]:
    """(date_str, path) for every dense daily brief dated on/after `since`,
    oldest first. Dense (not published) is the source, same reasoning as
    the live ceremony — full detail, and 'Worth Brian's attention' is the
    section name there (the published copy renames it 'Worth your
    attention' but the content's identical)."""
    since_date = since.date()
    out = []
    if not BRIEFINGS_ROOT.exists():
        return out
    for path in sorted(BRIEFINGS_ROOT.glob("*/*/*.md")):
        try:
            brief_date = datetime.strptime(path.stem, "%Y-%m-%d").date()
        except ValueError:
            continue
        if brief_date >= since_date:
            out.append((path.stem, path))
    return out


def extract_worth_attention(body: str) -> str:
    """Pulls the '## Worth Brian's attention' numbered list out of a dense
    brief's body. Returns '' if the section isn't found (a brief with no
    stories worth flagging is possible, if rare)."""
    match = re.search(
        r"^## Worth Brian's attention\s*\n(.*?)(?=\n## |\Z)",
        body, flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def extract_right_now(text: str) -> str:
    match = re.search(
        r"^## Right now\s*\n(.*?)(?=\n## )",
        text, flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else "(section not found)"


def build_stories_section(briefs: list[tuple[str, Path]]) -> str:
    if not briefs:
        return "*No daily briefs in this window.*"
    parts = []
    for date_str, path in briefs:
        _, body = read_frontmatter_and_body(path)
        worth_attention = extract_worth_attention(body)
        weekday = datetime.strptime(date_str, "%Y-%m-%d").strftime("%A, %b %-d")
        if worth_attention:
            parts.append(f"### {weekday}\n{worth_attention}")
        else:
            parts.append(f"### {weekday}\n*(no \"Worth Brian's attention\" section found)*")
    return "\n\n".join(parts)


def run_triage(dry_run: bool) -> None:
    """Regenerate staleness-candidates.md fresh — same non-negotiable as
    the live ceremony (a stale snapshot means the prep doc, and Brian,
    would be acting on old data). This is the one LLM call in this
    otherwise-deterministic script; triage.py makes it, not this file.
    Skipped under --dry-run (reads whatever's already on disk instead) —
    matching brief.py's own --dry-run contract of not persisting side
    effects; triage.py's write is a real side effect on shared state,
    not local to this script's own output."""
    if dry_run:
        print("--dry-run: skipping a fresh triage.py run, reading staleness-candidates.md as-is")
        return
    result = subprocess.run(
        [sys.executable, str(ROOT / "skills" / "triage" / "triage.py")],
        cwd=ROOT,
    )
    if result.returncode != 0:
        raise SystemExit(f"triage.py failed (exit {result.returncode}) — aborting gather")


def build_prep_doc(window_start: datetime, run_date: str) -> tuple[str, list[str]]:
    briefs = list_briefs_in_window(window_start)
    stories = build_stories_section(briefs)

    promotion_text = (
        PROMOTION_CANDIDATES_PATH.read_text(encoding="utf-8")
        if PROMOTION_CANDIDATES_PATH.exists() else "*No promotion-candidates.md found.*"
    )
    staleness_text = (
        STALENESS_CANDIDATES_PATH.read_text(encoding="utf-8")
        if STALENESS_CANDIDATES_PATH.exists() else "*No staleness-candidates.md found.*"
    )
    developing_thinking_text = DEVELOPING_THINKING_PATH.read_text(encoding="utf-8")
    right_now = extract_right_now(developing_thinking_text)

    sources = [str(p.relative_to(ROOT).as_posix()) for _, p in briefs]
    sources += [
        "outputs/technical-briefings/promotion-candidates.md",
        "outputs/canon-triage/staleness-candidates.md",
        "me/developing-thinking.md",
    ]

    frontmatter = {
        "title": f"Deeper Thinking prep — {run_date}",
        "date": run_date,
        "file_type": "weekly-prep",
        "tier": 3,
        "status": "not-reviewed-by-human",
        "authority_level": 1,
        "model": "none (deterministic assembly; triage.py's own model is recorded in staleness-candidates.md)",
        "sources": sources,
    }
    fm_yaml = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True, width=1000).strip()

    body = f"""# Deeper Thinking prep — {run_date}

Auto-generated by `skills/weekly/gather.py` — nothing here is written or judged by a model except `staleness-candidates.md`'s own contents (that's `triage.py`'s job, re-run fresh by this script). This file is the memory-jog Brian reads before the live ceremony (`/weekly-update`) — the actual decisions happen there, not here.

## Stories since last time

{stories}

## Promotion candidates awaiting a decision

{promotion_text}

## Staleness flags (freshly regenerated)

{staleness_text}

## Where your thinking stands (`## Right now`, as of today)

{right_now}
"""
    return f"---\n{fm_yaml}\n---\n\n{body}", sources


def build_email_html(run_date: str, prep_body: str, since_str: str) -> str:
    import markdown
    html_body = markdown.markdown(prep_body, extensions=["extra"])
    return f"""<!doctype html>
<html><head><meta charset="utf-8">
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
          max-width: 640px; margin: 20px auto; padding: 0 20px; line-height: 1.6; color: #1a1a1a; }}
  h1, h2, h3 {{ margin-top: 1.4em; }}
  a {{ color: #d4622a; }}
</style></head>
<body>
<p style="color:#888; font-size:0.85em;">Window: {since_str}. Full ceremony: run <code>/weekly-update</code> in a Claude Code session on this repo whenever you're ready to work through it.</p>
{html_body}
</body></html>
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Assemble (and optionally email) the Deeper Thinking prep doc.")
    parser.add_argument("--since-days", type=float, default=None, help="override the window (default: auto from .last_run.json, 7 days if none)")
    parser.add_argument("--send", action="store_true", help="email the prep doc (to $BRIAN_EMAIL)")
    parser.add_argument("--dry-run", action="store_true", help="print instead of writing/sending")
    args = parser.parse_args()

    load_dotenv(ROOT)

    window_start, since_str = resolve_window(args.since_days)
    print(f"window: {since_str}")

    run_triage(dry_run=args.dry_run)

    run_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    full_text, sources = build_prep_doc(window_start, run_date)

    year, month, _ = run_date.split("-")
    out_dir = WEEKLY_ROOT / year / month
    out_path = out_dir / f"{run_date}-prep.md"

    if args.dry_run:
        print(f"\n{'=' * 70}\n[DRY RUN] would write: {out_path.relative_to(ROOT)}\n{'=' * 70}")
        print(full_text)
        return

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_text(full_text, encoding="utf-8")
    print(f"wrote {out_path.relative_to(ROOT)}")

    if args.send:
        to_email = os.environ.get("BRIAN_EMAIL")
        if not to_email:
            raise SystemExit("--send needs BRIAN_EMAIL set (.env or env)")
        if not gmail_send.is_configured():
            raise SystemExit("--send needs GMAIL_CLIENT_ID/GMAIL_CLIENT_SECRET/GMAIL_REFRESH_TOKEN set (.env or env)")
        prep_body = full_text.split("---\n", 2)[2]
        html = build_email_html(run_date, prep_body, since_str)
        subject = f"Deeper Thinking prep — {run_date}"
        gmail_send.send_email(to_email, subject=subject, html_body=html)
        print(f"emailed to {to_email} (subject: {subject!r})")

    write_last_run(datetime.now(timezone.utc))
    print("updated outputs/weekly-updates/.last_run.json")


if __name__ == "__main__":
    main()

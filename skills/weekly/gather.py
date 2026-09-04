#!/usr/bin/env python3
"""
gather.py — deterministic prep step for Weekly Wrap Up (the weekly
ceremony formerly/internally called "weekly-update", publication named
"Deeper Thinking" at launch and renamed by Brian on Substack 2026-08-26;
see .claude/skills/weekly-update/SKILL.md). Assembles the prep doc Brian
reads before the live ceremony and, with --send, emails it to him.

**2026-09-04: switched from an automated Friday cron trigger to fully
manual.** Originally run from daily-pipeline.yml every Friday, right
after that day's Daily Briefing — but that meant the prep doc always
missed whatever Brian did in reaction to Friday's own post (restacking
it, commenting on it), since those actions happen after he's read the
email, not before it's sent. Brian's own call: read Friday's Substack
post as normal, then manually kick off this script (and the live
ceremony) whenever he's actually ready to sit down with it — simpler
than either running a second delta-update pass after the fact, or
trying to guess a time of day Friday reading is reliably done by.

Deliberately no LLM call except the one triage.py already makes on its
own (re-run as a subprocess here, same as the live ceremony does it) —
everything else is pure assembly of already-written text (the
promotion-candidates queue, the current developing-thinking.md "Right
now" section, links to this week's daily briefs, and Brian's own
restacks/comments from the week — see fetch_own_notes_in_window()),
matching MAINTAINER.md's "deterministic plumbing is plain code"
principle. This script does NOT run the interactive decisions (steps
3-9 of the skill) — those need Brian live. It only gets the prep doc
into his inbox before he sits down to do that part.

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

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "skills"))
sys.path.insert(0, str(ROOT / "skills" / "brief"))
sys.path.insert(0, str(ROOT / "skills" / "ingest"))

from brief import load_dotenv  # noqa: E402
from ingest import strip_html  # noqa: E402
from lib import gmail_send  # noqa: E402

BRIEFINGS_ROOT = ROOT / "outputs" / "technical-briefings"
WEEKLY_ROOT = ROOT / "outputs" / "weekly-updates"
LAST_RUN_PATH = WEEKLY_ROOT / ".last_run.json"
DEFAULT_DAYS_BACK = 7

PROMOTION_CANDIDATES_PATH = BRIEFINGS_ROOT / "promotion-candidates.md"
STALENESS_CANDIDATES_PATH = ROOT / "outputs" / "canon-triage" / "staleness-candidates.md"
DEVELOPING_THINKING_PATH = ROOT / "me" / "developing-thinking.md"
GITHUB_BLOB = "https://github.com/toomanybrians/brianmadden-ai/blob/main/"

# --- Brian's own restacks and comments, for the "what did I flag this
# week" section. Superseded 2026-09-04's original design (see below) —
# see fetch_own_notes_in_window() for the full note.
PUBLICATION_URL = "https://www.brianmadden.ai"
BRIAN_SUBSTACK_PROFILE_ID = "400769399"  # confirmed via the archive API's own byline data
COMMENTS_USER_AGENT = "brianmadden-ai-weekly-prep/1.0 (+https://github.com/toomanybrians/brianmadden-ai)"

# Substack's own "Notes" activity feed for a profile — a genuinely
# public, unauthenticated JSON API (confirmed 2026-09-04 via a plain
# `requests.get` with no session/cookies at all, same as
# skills/lib/substack_follows.py's public_profile endpoint), not the
# fragile HTML-regex scrape this replaces. Every restack Brian makes
# (highlighting a passage and clicking Restack, with or without adding
# his own commentary) shows up here as a `type: "comment"` /
# `context.type: "note"` item, carrying the restacked post's title/URL,
# the exact excerpt he highlighted (`comment.attachments[0].postSelection
# .text`, absent for a whole-post restack with nothing highlighted), and
# his own added text (`comment.body`, often empty). `type: "post"` items
# are just "brianmaddenai published something" system entries showing up
# because Brian's profile is that publication's author — not something
# he did, filtered out.
#
# This replaces the original 2026-08-26 design (a regex scrape of every
# recent post's /comments HTML subpage, matching blocks by Brian's
# profile id) once a real side-by-side showed the two "comments" that
# scraper had ever found were themselves restacks under the hood — same
# timestamps, same text, just reached by parsing rendered HTML for
# something Substack already exposes as a clean API. One caveat carried
# over, not yet observed to matter: this feed is restacks/notes only: if
# Brian ever replies inside a post's own comment thread *without* going
# through the restack/highlight mechanism, that reply wouldn't appear
# here. Every real example seen so far (2026-08-26 through 2026-09-04)
# has been a restack, so this hasn't been a real gap in practice — worth
# revisiting only if that ever changes.
NOTES_FEED_URL = f"https://substack.com/api/v1/reader/feed/profile/{BRIAN_SUBSTACK_PROFILE_ID}"
NOTES_MAX_PAGES = 20  # generous cap — a real week's activity is never this deep; guards a pagination bug, not a real limit


def fetch_own_notes_in_window(window_start: datetime) -> list[dict]:
    """Every restack (optionally with added commentary) Brian's made
    since window_start, newest first (matching the feed's own order).
    Paginates via the API's own `nextCursor` until
    an item older than window_start is seen (items arrive newest-first,
    so that's the real stopping point, not just a page-count guess).
    Degrades gracefully on any fetch failure, same contract the old
    comments scraper had: a broken check here should never take down the
    rest of the prep doc."""
    notes = []
    cursor = None
    for _ in range(NOTES_MAX_PAGES):
        try:
            resp = requests.get(
                NOTES_FEED_URL,
                params={"cursor": cursor} if cursor else {},
                headers={"User-Agent": COMMENTS_USER_AGENT}, timeout=15,
            )
            resp.raise_for_status()
            data = resp.json()
        except (requests.RequestException, ValueError) as e:
            print(f"    restacks/comments check: couldn't read the profile feed ({e}) — skipping")
            break
        items = data.get("items") or []
        if not items:
            break
        stop = False
        for item in items:
            if item.get("type") != "comment":
                continue
            ctx = item.get("context") or {}
            ts_raw = ctx.get("timestamp")
            if not ts_raw:
                continue
            try:
                ts = datetime.fromisoformat(ts_raw.replace("Z", "+00:00"))
            except ValueError:
                continue
            if ts < window_start:
                stop = True
                break  # newest-first order — everything after this is even older
            comment = item.get("comment") or {}
            attachments = comment.get("attachments") or []
            attachment = attachments[0] if attachments else {}
            post = attachment.get("post") or {}
            selection = attachment.get("postSelection") or {}
            notes.append({
                "when": ts_raw,
                "body": strip_html(comment.get("body") or "").strip(),
                "excerpt": strip_html(selection.get("text") or "").strip(),
                "post_title": post.get("title") or "a post",
                "post_url": post.get("canonical_url") or PUBLICATION_URL,
            })
        cursor = data.get("nextCursor")
        if stop or not cursor:
            break
    return notes


def build_notes_section(notes: list[dict]) -> str:
    if not notes:
        return "*No restacks or comments from Brian this week.*"
    parts = []
    for n in notes:
        try:
            when = datetime.fromisoformat(n["when"].replace("Z", "+00:00")).strftime("%b %-d, %Y %H:%M UTC")
        except ValueError:
            when = n["when"]
        block = [f'**Restacked ["{n["post_title"]}"]({n["post_url"]})** ({when}):']
        if n["excerpt"]:
            block.append(f'> {n["excerpt"]}')
        if n["body"]:
            block.append(n["body"])
        parts.append("\n\n".join(block))
    return "\n\n---\n\n".join(parts)


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
    oldest first. Dense (not published) is the source — full detail for
    whoever reads these directly, same reasoning the live ceremony uses
    everywhere else."""
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


def extract_right_now(text: str) -> str:
    match = re.search(
        r"^## Right now\s*\n(.*?)(?=\n## )",
        text, flags=re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else "(section not found)"


def build_briefs_index_section(briefs: list[tuple[str, Path]]) -> str:
    """A bare links list, not a content pre-extraction — see the
    2026-09-04 note above build_prep_doc() for why this replaced a
    section that used to try to summarize each day. Read these directly
    during the live ceremony (step 9's "this week's stories") rather than
    relying on anything pre-extracted here."""
    if not briefs:
        return "*No daily briefs in this window.*"
    parts = []
    for date_str, path in briefs:
        weekday = datetime.strptime(date_str, "%Y-%m-%d").strftime("%A, %b %-d")
        github_url = f"{GITHUB_BLOB}{path.relative_to(ROOT).as_posix()}"
        parts.append(f"- [{weekday}]({github_url})")
    return "\n".join(parts)


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
    briefs_index = build_briefs_index_section(briefs)

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

    # Live external fetch, not a repo file — always attempted (including
    # under --dry-run, unlike run_triage()'s skip) since it has no
    # persistent side effect of its own to worry about, just a read.
    own_notes = fetch_own_notes_in_window(window_start)
    notes_section = build_notes_section(own_notes)

    sources = [str(p.relative_to(ROOT).as_posix()) for _, p in briefs]
    sources += [
        "outputs/technical-briefings/promotion-candidates.md",
        "outputs/canon-triage/staleness-candidates.md",
        "me/developing-thinking.md",
    ]
    sources += list(dict.fromkeys(n["post_url"] for n in own_notes))  # dedup, preserve order — multiple restacks often point at the same post

    frontmatter = {
        "title": f"Weekly Wrap Up prep — {run_date}",
        "date": run_date,
        "file_type": "weekly-prep",
        "tier": 3,
        "status": "not-reviewed-by-human",
        "authority_level": 1,
        "model": "none (deterministic assembly; triage.py's own model is recorded in staleness-candidates.md)",
        "sources": sources,
    }
    fm_yaml = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True, width=1000).strip()

    body = f"""# Weekly Wrap Up prep — {run_date}

Auto-generated by `skills/weekly/gather.py` — nothing here is written or judged by a model except `staleness-candidates.md`'s own contents (that's `triage.py`'s job, re-run fresh by this script). This file is the memory-jog Brian reads before the live ceremony (`/weekly-update`) — the actual decisions happen there, not here.

## This week's daily briefs

{briefs_index}

## What Brian flagged this week (restacks & comments)

{notes_section}

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
    parser = argparse.ArgumentParser(description="Assemble (and optionally email) the Weekly Wrap Up prep doc.")
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
        subject = f"Weekly Wrap Up prep — {run_date}"
        gmail_send.send_email(to_email, subject=subject, html_body=html)
        print(f"emailed to {to_email} (subject: {subject!r})")

    write_last_run(datetime.now(timezone.utc))
    print("updated outputs/weekly-updates/.last_run.json")


if __name__ == "__main__":
    main()

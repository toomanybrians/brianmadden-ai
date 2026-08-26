#!/usr/bin/env python3
"""
gather.py — deterministic prep step for Weekly Wrap Up (the weekly
ceremony formerly/internally called "weekly-update", publication named
"Deeper Thinking" at launch and renamed by Brian on Substack 2026-08-26;
see .claude/skills/weekly-update/SKILL.md). Assembles the prep doc Brian
reads before the live ceremony and, with --send, emails it to him — this
is the "initial recap" Brian asked to have delivered automatically
(2026-08-24), run from daily-pipeline.yml on Fridays after that day's
Daily Briefing.

Deliberately no LLM call except the one triage.py already makes on its
own (re-run as a subprocess here, same as the live ceremony does it) —
everything else is pure assembly of already-written text (this week's
daily-brief "Worth Brian's attention" sections, the promotion-candidates
queue, the current developing-thinking.md "Right now" section, and
Brian's own Substack comments from the week — see
find_own_comments_in_window()), matching MAINTAINER.md's "deterministic
plumbing is plain code" principle. This script does NOT run the
interactive decisions (steps 4-10 of the skill) — those need Brian live.
It only gets the prep doc into his inbox before he sits down to do that
part.

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

from brief import load_dotenv, read_frontmatter_and_body  # noqa: E402
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

# --- Brian's own Substack comments, for the "what did I flag this week"
# section — see find_own_comments_in_window() below for the full design
# note. Plain HTTP, no browser: confirmed empirically 2026-08-26 that
# brianmadden.ai's post/comments pages are server-rendered and (with the
# same plain UA the rest of this pipeline uses) not behind the Cloudflare
# bot-block that hits *.substack.com/feed for the ~39 sources in open
# decision #16 — worth re-confirming on the first real GitHub Actions
# run of this script, since local-machine testing isn't the same network
# path. If it ever does start failing from GH Actions the way the feed
# endpoints do, the fix is the same one already used there: run this step
# from a residential network instead (see BUILD.md, 2026-08-26 for the
# tradeoffs Brian and this session weighed on that).
PUBLICATION_URL = "https://www.brianmadden.ai"
BRIAN_SUBSTACK_PROFILE_ID = "400769399"  # confirmed via the archive API's own byline data
COMMENTS_USER_AGENT = "brianmadden-ai-weekly-prep/1.0 (+https://github.com/toomanybrians/brianmadden-ai)"

# Matches one comment block in a rendered /p/<slug>/comments page: the
# author's profile-id + display name (from the "comment-author-name"
# byline), then the comment body (from "comment-body"). Confirmed
# empirically 2026-08-26 against a real comment on a real published post
# — see BUILD.md for the worked example. Matching on profile id, not
# display name, avoids a false positive from some other reader also
# named "Brian".
COMMENT_BLOCK_RE = re.compile(
    r'comment-author-name[^"]*"[^>]*>.*?href="https://substack\.com/profile/'
    r'(?P<profile_id>\d+)-[^"]*"[^>]*>(?P<name>[^<]+)</a>'
    r'.*?comment-body[^"]*">(?P<body>.*?)</div>',
    re.DOTALL,
)
# The permalink+timestamp anchor Substack renders just above each
# comment body — used to give each surfaced comment a real link and a
# real date rather than just quoting it unattributed.
COMMENT_PERMALINK_RE = re.compile(
    r'href="(?P<url>https://www\.brianmadden\.ai/p/[^/"]+/comment/\d+)"'
    r'\s+rel="nofollow"\s+title="(?P<when>[^"]+)"'
)


def fetch_own_comments_in_window(window_start: datetime) -> list[dict]:
    """Finds every comment Brian left on his own posts within the window,
    for the weekly prep doc's "Comments you left this week" section —
    built 2026-08-26 at Brian's direct request, after he left a real
    comment on that day's Daily Briefing and asked whether it could feed
    into the weekly ceremony.

    Two-step, both plain HTTP (see the module-level note above on why
    that's expected to work from GitHub Actions unlike the RSS-feed
    sources): (1) the publication's own /api/v1/archive endpoint gives
    every recent post's real slug, post_date, and comment_count in one
    call — real slugs, not derived from the post's display title, since
    Substack doesn't change a post's slug when its title gets edited
    (confirmed 2026-08-26 renaming this very publication's own weekly
    section — the Aug 24 post's slug is still `weekly-deeper-thinking-
    august-17` even though its title now reads "Weekly Wrap Up...").
    (2) for every post in the window with comment_count > 0, fetch its
    /comments subpage and regex out any comment authored by Brian's own
    profile id. Degrades gracefully on any fetch failure — a broken
    comments check should never take down the rest of the prep doc, so
    this returns an empty list and prints a warning rather than raising."""
    try:
        resp = requests.get(
            f"{PUBLICATION_URL}/api/v1/archive",
            params={"sort": "new", "limit": 24},
            headers={"User-Agent": COMMENTS_USER_AGENT}, timeout=15,
        )
        resp.raise_for_status()
        posts = resp.json()
    except (requests.RequestException, ValueError) as e:
        print(f"    comments check: couldn't read the publication archive ({e}) — skipping")
        return []

    found = []
    for post in posts:
        slug = post.get("slug")
        post_date_raw = post.get("post_date")
        if not slug or not post_date_raw or not post.get("comment_count"):
            continue
        try:
            post_date = datetime.fromisoformat(post_date_raw.replace("Z", "+00:00"))
        except ValueError:
            continue
        if post_date < window_start:
            continue
        try:
            resp = requests.get(
                f"{PUBLICATION_URL}/p/{slug}/comments",
                headers={"User-Agent": COMMENTS_USER_AGENT}, timeout=15,
            )
            resp.raise_for_status()
        except requests.RequestException as e:
            print(f"    comments check: couldn't fetch comments for '{slug}' ({e}) — skipping that post")
            continue
        html = resp.text
        permalinks = [(m.start(), m.groupdict()) for m in COMMENT_PERMALINK_RE.finditer(html)]
        for m in COMMENT_BLOCK_RE.finditer(html):
            if m.group("profile_id") != BRIAN_SUBSTACK_PROFILE_ID:
                continue
            # The permalink+timestamp anchor for a comment sits *inside*
            # that same comment's DOM subtree, between the author byline
            # and the comment body — i.e. within this match's own [start,
            # end) span, not before it. Confirmed empirically 2026-08-26
            # against the real HTML (see BUILD.md for the worked example).
            link_info = next(
                (g for pos, g in permalinks if m.start() <= pos <= m.end()), {}
            )
            found.append({
                "post_title": post.get("title", slug),
                "post_slug": slug,
                "text": strip_html(m.group("body")).strip(),
                "url": link_info.get("url", f"{PUBLICATION_URL}/p/{slug}/comments"),
                "when": link_info.get("when", post_date_raw),
            })
    return found


def build_comments_section(comments: list[dict]) -> str:
    if not comments:
        return "*No comments from Brian on brianmadden.ai posts this week.*"
    parts = []
    for c in comments:
        parts.append(
            f'**On ["{c["post_title"]}"]({c["url"]})** ({c["when"]}):\n\n> {c["text"]}'
        )
    return "\n\n".join(parts)


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

    # Live external fetch, not a repo file — always attempted (including
    # under --dry-run, unlike run_triage()'s skip) since it has no
    # persistent side effect of its own to worry about, just a read.
    own_comments = fetch_own_comments_in_window(window_start)
    comments_section = build_comments_section(own_comments)

    sources = [str(p.relative_to(ROOT).as_posix()) for _, p in briefs]
    sources += [
        "outputs/technical-briefings/promotion-candidates.md",
        "outputs/canon-triage/staleness-candidates.md",
        "me/developing-thinking.md",
    ]
    sources += [c["url"] for c in own_comments]

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

## Stories since last time

{stories}

## Comments you left this week

{comments_section}

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

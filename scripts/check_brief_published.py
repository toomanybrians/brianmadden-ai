#!/usr/bin/env python3
"""
check_brief_published.py — email Brian when no Daily Brief is on `main` by
mid-morning.

Why: on 2026-11-03 and 11-04 the brief never arrived and Brian found out
himself. The `guard` job in daily-pipeline.yml only stops a duplicate
email; nothing reported silence. This is that report. See BUILD.md
(2026-11-06) and the "WHEN IT RUNS" note atop daily-pipeline.yml.

It looks at origin's `main` through the GitHub API, not a local checkout,
for today's dense brief (outputs/technical-briefings/YYYY/MM/YYYY-MM-DD.md,
the same file the pipeline's publish step is guarded on). If it's there,
it exits quietly. If it isn't, it emails Brian what the daily-pipeline
workflow did today (not started, queued, running, failed) and how to
start one by hand.

A quiet day (no new notes at all) also writes no brief, so that case
produces an alert too; the email says so. It is rare with ~140 sources.

Runs from missed-brief-alert.yml on a hosted runner. Weekdays only, by the
UTC date, the same date the pipeline names the brief with. Needs
GMAIL_CLIENT_ID / GMAIL_CLIENT_SECRET / GMAIL_REFRESH_TOKEN and
BRIAN_EMAIL to send; GITHUB_TOKEN is optional (it only raises the API
rate limit, the repo is public).

  python3 scripts/check_brief_published.py --dry-run               # print, send nothing
  python3 scripts/check_brief_published.py --dry-run --date 2026-11-09
  python3 scripts/check_brief_published.py --test                  # send a labelled test email
"""

import argparse
import os
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "skills"))
from lib import gmail_send  # noqa: E402

REPO = "toomanybrians/brianmadden-ai"
API = f"https://api.github.com/repos/{REPO}"
WORKFLOW_PAGE = f"https://github.com/{REPO}/actions/workflows/daily-pipeline.yml"


def gh_get(path: str, **params) -> requests.Response:
    headers = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    return requests.get(f"{API}/{path}", headers=headers, params=params, timeout=30)


def brief_path(day: date) -> str:
    return f"outputs/technical-briefings/{day:%Y/%m/%Y-%m-%d}.md"


def brief_on_main(day: date) -> bool:
    resp = gh_get(f"contents/{brief_path(day)}", ref="main")
    if resp.status_code == 200:
        return True
    if resp.status_code == 404:
        return False
    resp.raise_for_status()  # anything else means we can't tell, so fail loudly
    return False


def runs_today(day: date) -> list[str]:
    """One line per daily-pipeline run created today, oldest first."""
    resp = gh_get("actions/workflows/daily-pipeline.yml/runs", per_page=20, created=f"{day:%Y-%m-%d}")
    resp.raise_for_status()
    lines = []
    for r in sorted(resp.json().get("workflow_runs", []), key=lambda r: r["created_at"]):
        state = r["conclusion"] if r["status"] == "completed" else r["status"]
        lines.append(f"{r['created_at'][11:16]} UTC, {r['event']}: {state}")
    return lines


def compose(day: date, runs: list[str], now: datetime, test: bool) -> tuple[str, str, str]:
    prefix = "[TEST] " if test else ""
    subject = f"{prefix}No Daily Brief on main yet ({day:%a %b %-d})"
    if runs:
        run_text = "What the daily pipeline did today:\n" + "\n".join(f"  - {r}" for r in runs)
    else:
        run_text = "No run of the daily pipeline has even started today (the box's timer and GitHub's backup cron both missed)."
    headline = (
        f"This is a test of the missed-brief alert. Nothing is wrong. A real alert says here that {brief_path(day)} isn't on main."
        if test else f"It's {now:%H:%M} UTC and {brief_path(day)} isn't on main."
    )
    text = (
        headline + "\n\n"
        + run_text + "\n\n"
        + "Usual causes: the run never started, the runner is up but not taking jobs "
        "(a run sits queued), or the run failed. If every source had nothing new, "
        "no brief is written, which is rare.\n\n"
        + f"Start one by hand: {WORKFLOW_PAGE} (Run workflow, source: manual), "
        "or: gh workflow run daily-pipeline.yml -f source=manual\n"
    )
    html = "<p>" + text.replace("\n\n", "</p><p>").replace("\n", "<br>") + "</p>"
    return subject, html, text


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--date", help="YYYY-MM-DD to check (default: today, UTC)")
    ap.add_argument("--dry-run", action="store_true", help="print the decision and the email, send nothing")
    ap.add_argument("--test", action="store_true", help="send a labelled test email regardless of the brief")
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    day = date.fromisoformat(args.date) if args.date else now.date()

    if not args.test:
        if day.weekday() >= 5:
            print(f"{day} is a weekend, no brief expected")
            return 0
        if brief_on_main(day):
            print(f"{brief_path(day)} is on main, nothing to report")
            return 0

    subject, html, text = compose(day, runs_today(day), now, args.test)
    print(f"ALERT: {subject}\n\n{text}")
    if args.dry_run:
        print("(dry run, nothing sent)")
        return 0
    to = os.environ.get("BRIAN_EMAIL")
    if not to or not gmail_send.is_configured():
        print("BRIAN_EMAIL or the GMAIL_* credentials are not set, can't send", file=sys.stderr)
        return 1
    gmail_send.send_email(to, subject=subject, html_body=html, text_body=text)
    print("alert emailed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""prune_ingest.py — delete tier-1 ingest notes older than N days (default 30).

Keeps ingest/ from growing without bound in the working tree. Nothing is lost:
every pruned note stays in git history, and each Daily Brief's disclosure line
already links the commit that added that day's notes (brief.py's
find_batch_commit()), so those links keep resolving after a prune.

What it touches: only dated notes under ingest/YYYY/MM/. It never touches
ingest/README.md, ingest/brain-flags/ (Brian's own review queue, cleared by
hand), or the ingest/.last_run*.json state files.

Age comes from each note's `date_captured` frontmatter, falling back to the
YYYY-MM-DD filename prefix. A note with neither is kept.

Why pruning is safe for dedupe: ingest.py dedupes against the notes still on
disk, but it also only looks at feed entries newer than its own last run, so a
post older than the retention window never comes back in. The exception is a
manual `ingest.py --since-days N` backfill with N larger than the retention
window, which could re-ingest posts whose notes were pruned. Don't do that,
or pass a matching --days here first.

Usage:
    python3 scripts/prune_ingest.py              # prune notes older than 30 days
    python3 scripts/prune_ingest.py --days 45
    python3 scripts/prune_ingest.py --dry-run    # list what would go, delete nothing
"""
from __future__ import annotations

import argparse
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INGEST_ROOT = ROOT / "ingest"
DEFAULT_DAYS = 30

DATE_CAPTURED_RE = re.compile(r"^date_captured:\s*['\"]?(\d{4}-\d{2}-\d{2})", re.MULTILINE)
FILENAME_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-")


def note_date(path: Path) -> date | None:
    head = path.read_text(encoding="utf-8", errors="replace")[:4000]
    m = DATE_CAPTURED_RE.search(head) or FILENAME_DATE_RE.match(path.name)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1), "%Y-%m-%d").date()
    except ValueError:
        return None


def dated_notes() -> list[Path]:
    notes = []
    for year_dir in sorted(INGEST_ROOT.glob("[0-9][0-9][0-9][0-9]")):
        notes += [p for p in sorted(year_dir.rglob("*.md")) if p.name != "README.md"]
    return notes


def main() -> None:
    parser = argparse.ArgumentParser(description="Delete ingest/ notes older than N days.")
    parser.add_argument("--days", type=int, default=DEFAULT_DAYS,
                        help=f"retention window in days (default: {DEFAULT_DAYS})")
    parser.add_argument("--dry-run", action="store_true", help="list what would be deleted, delete nothing")
    args = parser.parse_args()
    if args.days < 7:
        parser.error("--days must be at least 7 (ingest's own fallback window)")

    cutoff = datetime.now(timezone.utc).date() - timedelta(days=args.days)
    notes = dated_notes()
    old = [p for p in notes if (d := note_date(p)) is not None and d < cutoff]

    for p in old:
        rel = p.relative_to(ROOT).as_posix()
        if args.dry_run:
            print(f"[DRY RUN] would delete {rel}")
        else:
            p.unlink()

    removed_dirs = 0
    if not args.dry_run:
        # deepest first, so an emptied month dir goes before its year dir
        for d in sorted((d for d in INGEST_ROOT.glob("[0-9][0-9][0-9][0-9]/**") if d.is_dir()),
                        key=lambda d: len(d.parts), reverse=True):
            if not any(d.iterdir()):
                d.rmdir()
                removed_dirs += 1
        for d in INGEST_ROOT.glob("[0-9][0-9][0-9][0-9]"):
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()
                removed_dirs += 1

    verb = "would delete" if args.dry_run else "deleted"
    print(f"{verb} {len(old)} of {len(notes)} ingest notes captured before {cutoff.isoformat()} "
          f"(retention {args.days} days)" + (f"; removed {removed_dirs} empty dir(s)" if removed_dirs else ""))


if __name__ == "__main__":
    main()

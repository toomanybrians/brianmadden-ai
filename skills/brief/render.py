#!/usr/bin/env python3
"""
render.py — finalize a hand-edited published draft (outputs/briefings/)
and render it to a standalone HTML file for copy-pasting into Substack's
rich-text editor. See skills/brief/README.md.

"Finalize" means: if Brian edited the committed .md directly (adding an
editorial note, a wording fix, etc.), that's detected from `git diff`
against HEAD — not asked for separately — and the frontmatter `status`
flips from `not-reviewed-by-human` to `reviewed-and-updated` per the rule
already ratified in docs/frontmatter-schema.md ("reviewed-and-updated
implies the committed text differs from what the machine generated"). The
edit is then committed. No edit detected means no status change and no
commit — this only ever moves status toward more-reviewed, matching
MAINTAINER.md rule 4 (status is never upgraded by machine on its own,
only in direct response to a human's own diff).

Substack's editor doesn't interpret pasted Markdown syntax (it shows
literal "**"/"#" characters) but does preserve formatting from pasted
rich text/HTML. Selecting all and copying from the *rendered* page (not
the HTML source) carries bold/headers/links over correctly. The HTML
output itself is gitignored — a copy-paste convenience regenerated on
demand, not repo content.
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "skills"))

from brief import OUTPUT_ROOT, read_frontmatter_and_body  # noqa: E402

STYLE = """<meta name="color-scheme" content="light">
<style>
  html, body { background: #ffffff; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
         max-width: 640px; margin: 40px auto; padding: 0 20px; line-height: 1.6; color: #1a1a1a; }
  h1 { font-size: 1.8em; }
  h2 { font-size: 1.3em; margin-top: 1.5em; }
  a { color: #d4622a; }
  blockquote { border-left: 3px solid #ddd; margin-left: 0; padding-left: 1em; color: #555; }
  hr { border: none; border-top: 1px solid #ddd; margin: 2em 0; }
  em { color: #555; }
</style>"""


def find_published(brief_date: str) -> Path:
    year, month, _ = brief_date.split("-")
    path = OUTPUT_ROOT / year / month / f"{brief_date}-published.md"
    if not path.exists():
        raise SystemExit(f"no published draft found at {path.relative_to(ROOT)} — run publish.py for this date first")
    return path


def has_uncommitted_edit(path: Path) -> bool:
    result = subprocess.run(
        ["git", "diff", "--quiet", "HEAD", "--", str(path)], cwd=ROOT
    )
    return result.returncode != 0


def sync_status_and_commit(path: Path) -> bool:
    """If `path` has an uncommitted edit vs HEAD, flip status to
    reviewed-and-updated and commit. Returns True if it committed."""
    if not has_uncommitted_edit(path):
        return False

    diff_text = subprocess.run(
        ["git", "diff", "HEAD", "--", str(path)], cwd=ROOT, capture_output=True, text=True
    ).stdout
    rel = path.relative_to(ROOT).as_posix()
    print(f"detected an edit to {rel}:\n{diff_text}")

    fm, body = read_frontmatter_and_body(path)
    old_status = fm.get("status", "not-reviewed-by-human")
    fm["status"] = "reviewed-and-updated"
    fm_yaml = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=1000).strip()
    path.write_text(f"---\n{fm_yaml}\n---\n\n{body}\n", encoding="utf-8")

    subprocess.run(["git", "add", "--", str(path)], cwd=ROOT, check=True)
    subprocess.run(
        ["git", "commit", "-m",
         f"Brian's edits to {rel}\n\n"
         f"status: {old_status} -> reviewed-and-updated (detected from the diff above)\n\n"
         "Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>"],
        cwd=ROOT, check=True,
    )
    print(f"status -> reviewed-and-updated, committed")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Finalize (sync status from git diff) and render a published draft to HTML for Substack.")
    parser.add_argument("--date", default=None, help="brief date YYYY-MM-DD (default: today)")
    parser.add_argument("--no-status-sync", action="store_true", help="skip the git-diff status check, just render")
    args = parser.parse_args()

    brief_date = args.date or datetime.now().strftime("%Y-%m-%d")
    md_path = find_published(brief_date)

    if not args.no_status_sync:
        sync_status_and_commit(md_path)

    _, body = read_frontmatter_and_body(md_path)
    html_body = markdown.markdown(body, extensions=["extra"])
    full_html = f"<!doctype html>\n<html>\n<head>\n<meta charset='utf-8'>\n{STYLE}\n</head>\n<body>\n{html_body}\n</body>\n</html>\n"

    out_path = md_path.with_suffix(".html")
    out_path.write_text(full_html, encoding="utf-8")
    print(f"wrote {out_path.relative_to(ROOT)} (gitignored — copy-paste only, not committed)")


if __name__ == "__main__":
    main()

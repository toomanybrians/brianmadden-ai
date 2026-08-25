#!/usr/bin/env python3
"""
render.py — render a Weekly Update draft (outputs/weekly-updates/) to a
standalone HTML file for copy-pasting into Substack's rich-text editor.
See .claude/skills/weekly-update/SKILL.md.

Deliberately much smaller than skills/brief/render.py: the Weekly Update
isn't machine-generated-then-optionally-hand-edited the way the Daily
Brief is — Brian is live for the whole drafting conversation
(.claude/skills/weekly-update/SKILL.md step 9), so there's no git-diff
"did Brian edit this after the fact" check to run here. Also no injected
disclosure/footer, unlike skills/brief/render.py — that file's DISCLOSURE
and FOOTER are computed at render time because the Daily Brief's body
never carries its own explanation of authorship or a closing signature.
The Weekly Update is different: since Brian co-authors every issue live,
the opening paragraph explaining what this is and the closing footer are
just part of what gets written into the body at draft time (SKILL.md
step 9's job), varying a little issue to issue rather than being a fixed
string bolted on every render. This file just renders whatever's on disk.
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "skills"))
sys.path.insert(0, str(ROOT / "skills" / "brief"))

from brief import read_frontmatter_and_body  # noqa: E402
from render import STYLE, normalize_body, render_fields_block  # noqa: E402 — reuse, don't duplicate

WEEKLY_ROOT = ROOT / "outputs" / "weekly-updates"


def find_weekly(date: str) -> Path:
    year, month, _ = date.split("-")
    path = WEEKLY_ROOT / year / month / f"{date}.md"
    if not path.exists():
        raise SystemExit(f"no weekly update found at {path.relative_to(ROOT)}")
    return path


def render_to_html(md_path: Path) -> Path:
    fm, body = read_frontmatter_and_body(md_path)
    body = normalize_body(body)
    html_body = markdown.markdown(body, extensions=["extra"])
    fields_block = render_fields_block(fm.get("substack_title", ""), fm.get("substack_subtitle", ""))
    full_html = f"<!doctype html>\n<html>\n<head>\n<meta charset='utf-8'>\n{STYLE}\n</head>\n<body>\n{fields_block}\n{html_body}\n</body>\n</html>\n"

    out_path = md_path.with_suffix(".html")
    out_path.write_text(full_html, encoding="utf-8")
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a Weekly Update draft to HTML for Substack.")
    parser.add_argument("--date", default=None, help="weekly update date YYYY-MM-DD (default: today)")
    args = parser.parse_args()

    date = args.date or datetime.now().strftime("%Y-%m-%d")
    md_path = find_weekly(date)
    out_path = render_to_html(md_path)
    print(f"wrote {out_path.relative_to(ROOT)} (gitignored — copy-paste only, not committed)")


if __name__ == "__main__":
    main()

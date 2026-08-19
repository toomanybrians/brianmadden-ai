#!/usr/bin/env python3
"""
render.py — render a pages/*.md file to a standalone HTML file for
copy-pasting into Substack's rich-text editor. Same technique as
skills/brief/render.py, minus the brief-specific machinery (disclosure
line, thread tracker, title/subtitle fields) that doesn't apply here.

Substack's editor doesn't interpret pasted Markdown syntax (it shows
literal "**"/"#" characters) but does preserve formatting from pasted
rich text/HTML. Select all and copy from the *rendered* page (not the
HTML source) to carry bold/headers/links over correctly. The HTML output
is gitignored — a copy-paste convenience regenerated on demand, not repo
content; the committed .md is the source of truth.
"""

import argparse
import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent.parent
PAGES_DIR = ROOT / "pages"

STYLE = """<meta name="color-scheme" content="light">
<style>
  html, body { background: #ffffff; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
         max-width: 640px; margin: 40px auto; padding: 0 20px; line-height: 1.6; color: #1a1a1a; }
  h1 { font-size: 1.5em; }
  h2 { font-size: 1.25em; margin-top: 1.5em; }
  a { color: #d4622a; }
  blockquote { border-left: 3px solid #ddd; margin-left: 0; padding-left: 1em; color: #555; }
  hr { border: none; border-top: 1px solid #ddd; margin: 2em 0; }
  em { color: #555; }
</style>"""


def strip_frontmatter(raw: str) -> str:
    m = re.match(r"^---\n.*?\n---\n\n?", raw, flags=re.DOTALL)
    return raw[m.end():] if m else raw


def render_to_html(md_path: Path) -> Path:
    raw = md_path.read_text(encoding="utf-8")
    body = strip_frontmatter(raw)
    html_body = markdown.markdown(body, extensions=["extra"])
    full_html = f"<!doctype html>\n<html>\n<head>\n<meta charset='utf-8'>\n{STYLE}\n</head>\n<body>\n{html_body}\n</body>\n</html>\n"

    out_path = md_path.with_suffix(".html")
    out_path.write_text(full_html, encoding="utf-8")
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a pages/*.md file to HTML for pasting into Substack.")
    parser.add_argument("page", help="filename under pages/ (e.g. about.md), or a full/relative path")
    args = parser.parse_args()

    candidate = Path(args.page)
    md_path = candidate if candidate.exists() else PAGES_DIR / args.page
    if not md_path.exists():
        raise SystemExit(f"no such file: {args.page} (looked in pages/ too)")
    md_path = md_path.resolve()

    out_path = render_to_html(md_path)
    print(f"wrote {out_path.relative_to(ROOT)} (gitignored — copy-paste only, not committed)")


if __name__ == "__main__":
    main()

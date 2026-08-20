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
import os
import re
import sys
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
PAGES_DIR = ROOT / "pages"
sys.path.insert(0, str(ROOT / "skills"))
from lib import gmail_send  # noqa: E402


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


def frontmatter_title(raw: str) -> str | None:
    m = re.match(r"^---\n(.*?)\n---\n", raw, flags=re.DOTALL)
    if not m:
        return None
    return (yaml.safe_load(m.group(1)) or {}).get("title")


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
    parser.add_argument("--send", action="store_true", help="also email the rendered HTML (to --to, or $BRIAN_EMAIL)")
    parser.add_argument("--to", default=None, help="recipient for --send (default: $BRIAN_EMAIL)")
    args = parser.parse_args()

    load_dotenv(ROOT)
    to_email = args.to or os.environ.get("BRIAN_EMAIL")

    candidate = Path(args.page)
    md_path = candidate if candidate.exists() else PAGES_DIR / args.page
    if not md_path.exists():
        raise SystemExit(f"no such file: {args.page} (looked in pages/ too)")
    md_path = md_path.resolve()

    if args.send and not to_email:
        raise SystemExit("--send needs --to or BRIAN_EMAIL set (.env or env)")
    if args.send and not gmail_send.is_configured():
        raise SystemExit("--send needs GMAIL_CLIENT_ID/GMAIL_CLIENT_SECRET/GMAIL_REFRESH_TOKEN set (.env or env)")

    out_path = render_to_html(md_path)
    print(f"wrote {out_path.relative_to(ROOT)} (gitignored — copy-paste only, not committed)")

    if args.send:
        title = frontmatter_title(md_path.read_text(encoding="utf-8")) or md_path.stem
        html_body = out_path.read_text(encoding="utf-8")
        gmail_send.send_email(to_email, subject=f"[brianmadden.ai page] {title}", html_body=html_body)
        print(f"emailed to {to_email}")


if __name__ == "__main__":
    main()

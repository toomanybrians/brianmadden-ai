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
import html
import re
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
  h3 { font-size: 1.15em; margin-top: 1.5em; }
  a { color: #d4622a; }
  blockquote { border-left: 3px solid #ddd; margin-left: 0; padding-left: 1em; color: #555; }
  hr { border: none; border-top: 1px solid #ddd; margin: 2em 0; }
  em { color: #555; }
  .substack-fields { border: 1px dashed #bbb; border-radius: 6px; padding: 12px 16px; margin-bottom: 32px; background: #fafafa; }
  .substack-fields .label { font-size: 0.75em; text-transform: uppercase; letter-spacing: 0.05em; color: #888; margin: 0 0 2px; }
  .substack-fields .value { margin: 0 0 12px; font-size: 1.05em; }
  .substack-fields .value:last-child { margin-bottom: 0; }
</style>"""


def render_fields_block(title: str, subtitle: str) -> str:
    """A visually separate box above the body — not part of the post
    content, just Title/Subtitle shown plainly so Brian can copy each
    into Substack's own (separate, plain-text) Title/Subtitle fields
    without hunting through frontmatter or console output for them."""
    parts = ['<div class="substack-fields">']
    if title:
        parts.append(f'<p class="label">Substack title</p><p class="value">{html.escape(title)}</p>')
    if subtitle:
        parts.append(f'<p class="label">Substack subtitle</p><p class="value">{html.escape(subtitle)}</p>')
    parts.append("</div>")
    return "\n".join(parts) if len(parts) > 2 else ""


def normalize_body(body: str) -> str:
    """Drop a leading `# Title` line if present (legacy posts written
    before the 2026-08-12 title/subtitle redesign — Substack's title
    field is populated separately and deterministically now, so a body
    title line would just be a redundant, unstyled duplicate) and
    normalize every remaining heading to h3 (`###`), regardless of what
    level the model happened to write — Brian's call, 2026-08-12: h1
    rendered too large for a section break at this scale; h3 is what he
    set by hand on the first post. Normalizing to a fixed level rather
    than a relative promote/demote is robust either way, whatever the
    model's raw heading level was."""
    body = body.lstrip("\n")
    if body.startswith("# ") and not body.startswith("## "):
        body = body.split("\n", 1)[1] if "\n" in body else ""
        body = body.lstrip("\n")
    return re.sub(
        r"^#{1,6} (.+)$",
        r"### \1",
        body,
        flags=re.MULTILINE,
    )


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

    fm, body = read_frontmatter_and_body(md_path)
    body = normalize_body(body)
    html_body = markdown.markdown(body, extensions=["extra"])
    fields_block = render_fields_block(fm.get("substack_title", ""), fm.get("substack_subtitle", ""))
    full_html = f"<!doctype html>\n<html>\n<head>\n<meta charset='utf-8'>\n{STYLE}\n</head>\n<body>\n{fields_block}\n{html_body}\n</body>\n</html>\n"

    out_path = md_path.with_suffix(".html")
    out_path.write_text(full_html, encoding="utf-8")
    print(f"wrote {out_path.relative_to(ROOT)} (gitignored — copy-paste only, not committed)")


if __name__ == "__main__":
    main()

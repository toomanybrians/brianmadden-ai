#!/usr/bin/env python3
"""
render.py — render a published draft (outputs/published/) to a standalone
HTML file for copy-pasting into Substack's rich-text editor, and (when run
standalone) finalize a hand-edited one first. See skills/brief/README.md.

**As of 2026-08-18, `publish.py` calls `render_to_html()` itself right
after writing the draft** — Brian's call: with the condensed/general-
audience mode retired in favor of always publishing the dense brief
verbatim, and posts going out with no true human review by default, there's
no reason to wait on a manual step between "draft written" and "HTML ready
to paste." The disclosure line already says "not reviewed or edited by a
human before publishing" whenever that's true, so the honesty this repo
cares about lives in the rendered text, not in a pause before rendering.
Running this file directly is still how you re-render after a hand-edit
(see "Finalize" below) — that path is untouched, just no longer the only
way to get HTML.

"Finalize" (CLI use only) means: if Brian edited the committed .md directly
(adding an editorial note, a wording fix, etc.), that's detected from `git
diff` against HEAD — not asked for separately — and the frontmatter
`status` flips from `not-reviewed-by-human` to `reviewed-and-updated` per
the rule already ratified in docs/frontmatter-schema.md
("reviewed-and-updated implies the committed text differs from what the
machine generated"). The edit is then committed. No edit detected means no
status change and no commit — this only ever moves status toward
more-reviewed, matching MAINTAINER.md rule 4 (status is never upgraded by
machine on its own, only in direct response to a human's own diff).

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

from brief import GITHUB_BASE, PUBLISHED_ROOT, read_frontmatter_and_body  # noqa: E402

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
    title line would just be a redundant, unstyled duplicate), then shift
    every remaining heading so the *shallowest* level present becomes h3
    — preserving whatever relative hierarchy exists rather than
    flattening every heading to the same level. Originally just forced
    everything to h3 outright (2026-08-12: h1 rendered too large for a
    section break at this scale) — fine when the source only ever had one
    heading level (the Fable-condensed posts this was built for do), but
    generalized 2026-08-13 when publishing the dense technical brief
    directly started being a real option: that source can have real
    sub-structure, and Brian's call was h3 for the top level, h4 for
    sub-heads, not everything flattened to h3. A relative shift keeps that
    intact while still landing exactly on h3 for the single-level case —
    no behavior change for existing posts."""
    body = body.lstrip("\n")
    if body.startswith("# ") and not body.startswith("## "):
        body = body.split("\n", 1)[1] if "\n" in body else ""
        body = body.lstrip("\n")

    levels = [len(m.group(1)) for m in re.finditer(r"^(#{1,6}) .+$", body, flags=re.MULTILINE)]
    if not levels:
        return body
    offset = 3 - min(levels)

    def shift(m: re.Match) -> str:
        new_level = max(1, min(6, len(m.group(1)) + offset))
        return f"{'#' * new_level} {m.group(2)}"

    return re.sub(r"^(#{1,6}) (.+)$", shift, body, flags=re.MULTILINE)


REVIEW_CLAUSES = {
    "reviewed-and-updated": "reviewed and edited by Brian before publishing",
    "reviewed": "reviewed by Brian before publishing",
    "human-disputes-this": "reviewed by Brian, who disputes part of it — see his notes below",
}


def disclosure_line(fm: dict) -> str:
    """Explicit AI-authorship disclosure at the *top* of every post, not
    just the footer — so a reader who doesn't scroll to the bottom still
    sees it. Brian's ask, 2026-08-17: as more content types land under the
    brianmaddenai byline (fully AI-generated vs. human-reviewed vs.
    human-written), a footer-only disclosure isn't prominent enough, and
    it needs to stay honestly per-post rather than one static claim.
    Computed here at render time (not baked into the .md body by
    publish.py) so it reflects the file's *current* status — if Brian
    hand-edits later and status flips to reviewed-and-updated, the next
    render picks that up automatically without publish.py needing to know
    in advance. Links to the dense technical brief (outputs/technical-
    briefings/), not the published file itself — that source is always
    the model's own unedited synthesis regardless of what happens to the
    published copy afterward, so 'raw output' stays true either way.
    GitHub links point at `main` (GITHUB_BASE), same as the footer and
    brief.py's thread-tracker links — Brian's explicit call to start these
    today even though they 404 until the v2 launch PR merges."""
    review_clause = REVIEW_CLAUSES.get(fm.get("status", "not-reviewed-by-human"),
                                        "not reviewed or edited by a human before publishing")
    sources = fm.get("sources") or []
    source_link = f"{GITHUB_BASE}{sources[0]}" if sources else GITHUB_BASE
    return (
        "*This is today's Daily Briefing — written by "
        "[Brian Madden's AI second brain](https://brianmadden.ai), "
        f"{review_clause}. [See today's full, unedited AI output on GitHub]"
        f"({source_link}).*"
    )


def render_to_html(md_path: Path) -> Path:
    """Read `md_path`'s current frontmatter/body and write the standalone
    Substack-paste HTML file next to it. Reflects whatever `status` the
    file currently carries (so the disclosure line is honest either way) —
    callers that want the git-diff hand-edit check should run
    `sync_status_and_commit()` first, as `main()` does for the CLI path.
    Split out from `main()` 2026-08-18 so `publish.py` can call this
    directly right after writing a fresh draft, without going through the
    argparse/status-sync machinery that only makes sense for a later,
    separate re-render."""
    fm, body = read_frontmatter_and_body(md_path)
    body = normalize_body(body)
    body = disclosure_line(fm) + "\n\n" + body
    html_body = markdown.markdown(body, extensions=["extra"])
    fields_block = render_fields_block(fm.get("substack_title", ""), fm.get("substack_subtitle", ""))
    full_html = f"<!doctype html>\n<html>\n<head>\n<meta charset='utf-8'>\n{STYLE}\n</head>\n<body>\n{fields_block}\n{html_body}\n</body>\n</html>\n"

    out_path = md_path.with_suffix(".html")
    out_path.write_text(full_html, encoding="utf-8")
    return out_path


def find_published(brief_date: str) -> Path:
    year, month, _ = brief_date.split("-")
    path = PUBLISHED_ROOT / year / month / f"{brief_date}.md"
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

    out_path = render_to_html(md_path)
    print(f"wrote {out_path.relative_to(ROOT)} (gitignored — copy-paste only, not committed)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Render a podcast/epN.md canon file into Substack-paste-ready HTML.

Usage:
    python3 scripts/render_substack_html.py podcast/ep1.md podcast/ep2.md
    python3 scripts/render_substack_html.py --all

Writes outputs/podcast/epN-substack.html — open it in a real browser,
select all, copy, and paste into Substack's post editor. Substack's rich
text paste carries over headings/bold/links/lists from the clipboard, and
a bare YouTube URL sitting on its own line (not wrapped in a link) is what
triggers Substack's own auto-embed into a video player on paste — so this
deliberately leaves that one line as plain text, not an <a> tag.

Pulls these pieces from the canon file — not the whole thing:
  1. Subtitle (from `substack_subtitle` frontmatter) — rendered in its own
     clearly-marked block, separate from the body copy, because Substack's
     subtitle is a distinct field on the post editor (under the title),
     not part of the article body. Don't select it along with the body.
  2. The YouTube URL (plain text, its own paragraph)
  3. "Listen on" — Apple Podcasts / Spotify / Amazon Music, as real <a>
     links (not bare URLs), so Substack doesn't generate an unwanted
     link-preview embed for each one the way it would for a bare URL —
     only the YouTube line, above, is meant to trigger an embed.
  4. Description
  5. Links mentioned
  6. Transcript
No Topics-covered bullets, no Chapters list — Brian's explicit call
(2026-09-02), not an oversight.
"""
import argparse
import html
import re
import sys
from pathlib import Path

import markdown as md

ROOT = Path(__file__).resolve().parent.parent
PODCAST_DIR = ROOT / "podcast"
OUT_DIR = ROOT / "outputs" / "podcast"

BARE_URL = re.compile(r'(?<!\()(https?://\S+)')


def extract_section(text: str, heading: str) -> str:
    """Body text between '## {heading}' and the next '## ' heading (or EOF)."""
    pattern = rf"^## {re.escape(heading)}\s*\n(.*?)(?=\n## |\Z)"
    m = re.search(pattern, text, re.DOTALL | re.MULTILINE)
    if not m:
        return ""
    body = m.group(1)
    # Trailing '---' separator (before '## Transcript') can get swept into
    # the prior section's capture — strip it.
    body = re.sub(r"\n+---\s*$", "", body)
    return body.strip()


def extract_youtube_url(text: str) -> str | None:
    m = re.search(r"^- \*\*YouTube:\*\*\s*(\S+)", text, re.MULTILINE)
    return m.group(1).strip() if m else None


LISTEN_ON_LABELS = ["Apple Podcasts", "Spotify", "Amazon Music"]


def extract_listen_links(text: str) -> list[tuple[str, str]]:
    """Platform links from the '## Listen' section, restricted to the
    'Listen on' whitelist (skips Show home/Riverside, YouTube, and any
    Substack canonical link — those are handled elsewhere or don't
    belong on the page pointing at itself), in the order they appear."""
    listen_md = extract_section(text, "Listen")
    found = dict(re.findall(r"^- \*\*(.+?):\*\*\s*(\S+)", listen_md, re.MULTILINE))
    return [(label, found[label]) for label in LISTEN_ON_LABELS if label in found]


def extract_title(text: str) -> str:
    m = re.search(r'^title:\s*"(.+?)"\s*$', text, re.MULTILINE)
    return m.group(1) if m else "Untitled episode"


def extract_date(text: str) -> str:
    m = re.search(r'^date:\s*"(.+?)"\s*$', text, re.MULTILINE)
    return m.group(1) if m else ""


def extract_subtitle(text: str) -> str | None:
    m = re.search(r'^substack_subtitle:\s*"(.+?)"\s*$', text, re.MULTILINE)
    return m.group(1) if m else None


def autolink_bare_urls(text: str) -> str:
    """Wrap bare URLs (not already the target of a markdown link) in
    CommonMark autolink syntax so they render as real <a> tags."""
    return BARE_URL.sub(lambda m: f"<{m.group(1)}>", text)


def render_markdown(text: str) -> str:
    return md.markdown(text, extensions=["extra"])


def render_transcript(transcript_md: str) -> str:
    """Split into speaker turns and render each as a bold name paragraph
    followed by its own paragraph(s) — a plain markdown pass would fold
    the '**Name**\\ntext' pair into one soft-wrapped paragraph instead."""
    turn_re = re.compile(r"^\*\*(.+?)\*\*\s*$", re.MULTILINE)
    matches = list(turn_re.finditer(transcript_md))
    if not matches:
        return render_markdown(transcript_md)

    parts = []
    for i, m in enumerate(matches):
        speaker = m.group(1)
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(transcript_md)
        content = transcript_md[start:end].strip()
        parts.append(f"<p><strong>{speaker}</strong></p>")
        parts.append(render_markdown(content))
    return "\n".join(parts)


def render_episode(md_path: Path) -> Path:
    text = md_path.read_text()
    title = html.escape(extract_title(text))
    date = html.escape(extract_date(text))
    subtitle = extract_subtitle(text)
    youtube_url = extract_youtube_url(text)
    listen_links = extract_listen_links(text)

    if subtitle:
        if len(subtitle) >= 200:
            print(f"  WARNING {md_path.name}: substack_subtitle is {len(subtitle)} chars "
                  f"— Substack truncates mid-word past 200, no ellipsis.", file=sys.stderr)
        elif len(subtitle) >= 180:
            print(f"  note {md_path.name}: substack_subtitle is {len(subtitle)} chars "
                  f"— target is under 180 for margin.", file=sys.stderr)
    else:
        print(f"  WARNING {md_path.name}: no substack_subtitle frontmatter found.", file=sys.stderr)

    description_md = extract_section(text, "Description")
    links_md = autolink_bare_urls(extract_section(text, "Links mentioned"))
    transcript_md = extract_section(text, "Transcript")

    description_html = render_markdown(description_md)
    links_html = render_markdown(links_md)
    transcript_html = render_transcript(transcript_md)

    subtitle_block = ""
    if subtitle:
        subtitle_block = f"""<div class="subtitle-box">
<p class="subtitle-label">Subtitle — paste into Substack's own Subtitle field, not the body:</p>
<p class="subtitle-text">{html.escape(subtitle)}</p>
</div>
<hr>"""

    body_parts = []
    if youtube_url:
        body_parts.append(f"<p>{html.escape(youtube_url)}</p>")
    if listen_links:
        links_inline = " · ".join(
            f'<a href="{html.escape(url)}">{html.escape(label)}</a>'
            for label, url in listen_links
        )
        body_parts.append(f"<p>Listen on: {links_inline}</p>")
    body_parts.append(description_html)
    body_parts.append("<h3>Links mentioned</h3>")
    body_parts.append(links_html)
    body_parts.append("<h3>Transcript</h3>")
    body_parts.append(transcript_html)
    body = "\n\n".join(body_parts)

    page = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>{title} — Substack paste</title>
<style>
  body {{ max-width: 700px; margin: 40px auto; padding: 0 20px 80px;
          font-family: Georgia, 'Times New Roman', serif; font-size: 17px;
          line-height: 1.6; color: #222; }}
  h1 {{ font-size: 26px; line-height: 1.3; }}
  h3 {{ font-size: 19px; margin-top: 2.2em; }}
  p {{ margin: 1em 0; }}
  strong {{ font-weight: 700; }}
  a {{ color: #ce4b12; }}
  hr {{ border: none; border-top: 1px solid #ddd; margin: 2em 0; }}
  .meta {{ color: #666; font-size: 14px; margin-top: -0.5em; margin-bottom: 2em; }}
  .subtitle-box {{ background: #f7f4ef; border: 1px solid #e2ddd2; border-radius: 6px;
                    padding: 14px 18px; margin: 1.5em 0; }}
  .subtitle-label {{ margin: 0 0 6px; font-size: 13px; color: #888;
                      text-transform: uppercase; letter-spacing: 0.03em; }}
  .subtitle-text {{ margin: 0; font-size: 17px; font-weight: 600; }}
</style>
</head>
<body>
<h1>{title}</h1>
<p class="meta">{date} — select all in this page, copy, and paste into Substack's editor.</p>
{subtitle_block}
{body}
</body>
</html>
"""
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / (md_path.stem + "-substack.html")
    out_path.write_text(page)
    return out_path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("files", nargs="*", help="podcast/epN.md files")
    ap.add_argument("--all", action="store_true", help="render every podcast/ep*.md")
    args = ap.parse_args()

    files = sorted(PODCAST_DIR.glob("ep*.md")) if args.all else [Path(f) for f in args.files]
    if not files:
        print("No files given. Use --all or pass podcast/epN.md paths.", file=sys.stderr)
        sys.exit(1)

    for f in files:
        out = render_episode(f)
        print(f"Wrote {out}")


if __name__ == "__main__":
    main()

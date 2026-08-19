# pages skill

Renders a `pages/*.md` file (the About page, and any future standalone
Substack page) to a standalone HTML file for copy-pasting into Substack's
rich-text editor. See [MAINTAINER.md](../../MAINTAINER.md) for what
`pages/` is and how it differs from `posts/`.

## Running it

```bash
pip install -r requirements.txt
python3 skills/pages/render.py about.md
# or a full path:
python3 skills/pages/render.py pages/about.md
```

Writes `pages/about.html` next to the source file — gitignored, a
copy-paste convenience regenerated on demand, not repo content. Open it
in a browser, select all, copy, and paste into Substack's editor (About
page, or wherever the page is going). Substack doesn't interpret pasted
Markdown syntax, but does preserve formatting carried over from pasted
rich text — pasting the raw `.md` source directly would show literal
`**`/`#` characters instead of real bold/headings.

Same technique as [skills/brief/render.py](../brief/render.py), stripped
down to just frontmatter-strip + markdown-to-HTML — no disclosure line,
thread tracker, or title/subtitle fields, since those are specific to the
daily-brief pipeline and don't apply to a hand-written page like this one.

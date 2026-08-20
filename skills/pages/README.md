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
# and/or email it instead of (or as well as) writing the file locally:
python3 skills/pages/render.py about.md --send
python3 skills/pages/render.py about.md --send --to someone@example.com
```

Writes `pages/about.html` next to the source file — gitignored, a
copy-paste convenience regenerated on demand, not repo content. Open it
in a browser, select all, copy, and paste into Substack's editor (About
page, or wherever the page is going). Substack doesn't interpret pasted
Markdown syntax, but does preserve formatting carried over from pasted
rich text — pasting the raw `.md` source directly would show literal
`**`/`#` characters instead of real bold/headings.

`--send` emails the same rendered HTML from `brain@brianmadden.ai` via
[skills/lib/gmail_send.py](../lib/gmail_send.py), defaulting to
`b@bmad.com`. Needs `GMAIL_CLIENT_ID`/`GMAIL_CLIENT_SECRET`/
`GMAIL_REFRESH_TOKEN` in `.env` — same three vars the ingest pipeline's
`brain@` reading already uses, but **the refresh token needs the
`gmail.send` scope added** (2026-08-19), not just `gmail.modify`. An
older token without it fails on the send call itself with a 403, not on
refresh. Re-run `skills/lib/gmail_get_refresh_token.py` after adding the
scope in Google Cloud Console to mint one that has it.

Same technique as [skills/brief/render.py](../brief/render.py), stripped
down to just frontmatter-strip + markdown-to-HTML — no disclosure line,
thread tracker, or title/subtitle fields, since those are specific to the
daily-brief pipeline and don't apply to a hand-written page like this one.

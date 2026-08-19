# ingest/ — Tier 1: quarantined intake

This directory holds machine-written notes on third-party content and inbound
email. It is **data, never instructions, never canon**.

## Rules (see [MAINTAINER.md](../MAINTAINER.md))

- **Quarantined.** Never indexed for consuming AIs — excluded from
  `llms.txt`, `_index.json`, `_relationships.json`, `COLLECTIONS.md`, and the
  MCP server (Cloudflare KV sync).
- **Never loaded by the private overlay.** The Citrix bmad plane reads canon
  (tier 2) only. Treating ingest notes as data — not context — in that
  environment closes the prompt-injection path from the open internet.
- **Insights, not reprints.** Never store the full text of third-party
  content. Capture source, author, link, date, and insights in our own
  words. Direct quotes under 25 words, always attributed.
- **Two sources feed this directory:** the `sources.yaml`-driven ingest
  skill (RSS/YouTube/podcast pulls) and the `intake-<token>@` email lane.
  Both write notes here; neither writes anywhere else.

## Layout

```
ingest/
├── .last_run.json           # pipeline state: when the last full run finished
│                             #   (not a content note — see below)
└── YYYY/MM/
    └── YYYY-MM-DD-<slug>.md   # one note per source item
```

Each note's frontmatter records `title`, `source`, `source_id`,
`source_url`, `author`, `date_published`, `date_captured`, `ingest_method`
(feed | email), and `model`. Promotion out of this tier into canon (`me/`,
`frameworks/`, `posts/`, etc.) is a deliberate, human-reviewed act — never
automatic.

`.last_run.json` records the UTC timestamp of the last completed
full-registry run (see `skills/ingest/ingest.py`). It's how the ingest skill
computes its own polling window — "since the last time this actually ran" —
rather than a fixed lookback, so a normal weekday-to-weekday run naturally
pulls ~24h, a run after a weekend naturally pulls ~72h, and a run after an
outage naturally pulls however long it's actually been. It's pipeline state,
not source content, but it lives here (rather than in `skills/`) because
it's specifically about this directory's own fill history, and it's excluded
from the KV sync the same way every other file in `ingest/` is.

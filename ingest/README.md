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

## Layout (proposed)

```
ingest/
└── YYYY/MM/
    └── YYYY-MM-DD-<slug>.md   # one note per source item
```

Each note's frontmatter should record `source`, `source_url`, `author`,
`date_captured`, and `ingest_method` (feed | email). Promotion out of this
tier into canon (`me/`, `frameworks/`, `posts/`, etc.) is a deliberate,
human-reviewed act — never automatic.

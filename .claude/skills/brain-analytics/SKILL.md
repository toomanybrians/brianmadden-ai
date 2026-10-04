---
name: brain-analytics
description: Pull and interpret usage analytics for the public MCP server (mcp.brianmadden.ai) from Cloudflare Analytics Engine: which tools get called, what people search for, zero-result searches (content gaps), most-read files. Use when the user runs /brain-analytics or asks "who's using my brain", "MCP stats", "what are people searching for", "how's the brain doing".
---

# Brain analytics

Ported from the old private brain (2026-10-04). Fixes one thing from the
original: the dataset is `brianmadden_ai_mcp` (the old skill had
`brainmadden_ai_mcp`, a typo that fails every query).

## Prereqs

The query script lives in the sibling repo:
`~/git/brianmadden-ai-server/scripts/query-analytics.mjs`. It needs two env
vars, `CF_API_TOKEN` (Analytics Engine read access) and `CF_ACCOUNT_ID`.
Check they're set **without printing them**: `test -n "$CF_API_TOKEN"` and
`test -n "$CF_ACCOUNT_ID"`. If either is missing, ask Brian to export them in
his shell. Never put them in a file in this repo or paste them into chat
(MAINTAINER.md: secrets live only in GitHub Actions Secrets).

## Queries

```bash
node ~/git/brianmadden-ai-server/scripts/query-analytics.mjs tools       # which tools
node ~/git/brianmadden-ai-server/scripts/query-analytics.mjs searches    # what people search
node ~/git/brianmadden-ai-server/scripts/query-analytics.mjs files       # most-read files
node ~/git/brianmadden-ai-server/scripts/query-analytics.mjs requests    # daily volume
node ~/git/brianmadden-ai-server/scripts/query-analytics.mjs export      # last 7 days, JSON
node ~/git/brianmadden-ai-server/scripts/query-analytics.mjs sql "<SQL>"
```

Table `brianmadden_ai_mcp`. Columns: `index1`/`blob1` tool name (`request`
for raw HTTP), `blob2` query/path/framework (first 256 chars), `double1`
result count, `timestamp`, `_sample_interval` (use `SUM(_sample_interval)`
for counts, never `COUNT(*)`).

## Report

- **Usage:** connections, tool calls, trend direction.
- **What people look for:** top searches and files, and searches with
  `double1 = 0`. Zero-result searches are content gaps: list them as
  candidates for a canon addition or a `me/post-ideas.md` entry (propose,
  don't write).
- **Depth:** calls per session. More calls per session means deeper use.
- Privacy: queries are other people's input. Summarize patterns; don't
  republish individual search strings that look personal or identifying.

Plausible (plausible.io/brianmadden.ai) is Brian's own dashboard for site
traffic. Ask him to check it directly; there's no API access from here.

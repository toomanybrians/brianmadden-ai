---
name: brain-analytics
description: Pull and interpret usage analytics for the public MCP server (mcp.brianmadden.ai) from its private stats endpoint: which tools get called, what people search for, zero-result searches (content gaps), most-read files, when it's used. Use when the user runs /brain-analytics or asks "who's using my brain", "MCP stats", "what are people searching for", "how's the brain doing".
---

# Brain analytics

Ported from the old private brain (2026-10-04), then rewritten the same day.
The original queried a Cloudflare Analytics Engine dataset that the server
stopped writing to (commit `20c0576` in `brianmadden-ai-server`, "change how
mcp analytics works"). The live source is the KV daily rollups behind the
password-protected dashboard at **https://mcp.brianmadden.ai/stats**.

Brian can just open that URL in a browser. This skill is for pulling the same
data into a session so it can be interpreted and acted on.

## Prereq

The endpoint's password lives in the Worker secret `STATS_PASSWORD`. For
`curl` access, Brian exports the same value in his shell as
`MCP_STATS_PASSWORD`. Check without printing it: `test -n "$MCP_STATS_PASSWORD"`.
If it's missing, ask Brian to export it. Never write it to a file in this repo
or paste it into chat (MAINTAINER.md: secrets live in secret stores only).

## Pull the data

```bash
curl -s -H "Authorization: Bearer $MCP_STATS_PASSWORD" \
  "https://mcp.brianmadden.ai/stats/data.json?days=30" | python3 -m json.tool
```

`days` is 7, 30, or 90 (rollups expire after 90 days). The JSON has:

- `current` / `previous`: `calls`, `searches`, `reads`, `activeDays`,
  `zeroRate`. `previous` is the window before this one, or null.
- `daily`: per-day `total`, `searches`, `reads`.
- `tools`, `clients`, `queries` (top searches), `zero` (searches that found
  nothing), `files` (most-read paths): each a list of `{label, value}`.
- `heat`: weekday x UTC-hour call counts, tracked days only.
- `trackedSince`: first day that has `zero`, `files`, and `heat` data. These
  fields only started being recorded 2026-10-04, so earlier days lack them.
  Say so rather than reading a missing field as zero.

## Report

- **Usage:** calls, searches and reads with the change against the previous
  window; active days; trend direction.
- **What people look for:** top searches and most-read files.
- **Content gaps:** the `zero` list. Each entry is something someone asked
  that canon couldn't answer. Propose candidates for a canon addition or a
  `me/post-ideas.md` entry (propose, don't write: post-ideas are Brian's).
  Treat `zeroRate` carefully: it only counts tracked days.
- **Clients and timing:** which AI clients connect and when (UTC).
- Privacy: queries are other people's input. Summarize patterns; don't
  republish individual strings that look personal or identifying.

Plausible (plausible.io/brianmadden.ai) is Brian's dashboard for website
traffic. Ask him to check it directly; there's no API access from here.

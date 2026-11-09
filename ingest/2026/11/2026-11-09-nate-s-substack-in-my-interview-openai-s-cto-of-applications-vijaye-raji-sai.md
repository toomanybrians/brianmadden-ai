---
title: In my interview, OpenAI's CTO of Applications Vijaye Raji said more code gets
  thrown away now that coding is cheap. How to decide what your team keeps and scraps.
source: Nate’s Substack
source_id: nate-s-substack
source_url: https://natesnewsletter.substack.com/p/openai-pando-git-backend
author: Nate
date_published: '2026-11-06'
date_captured: '2026-11-09'
ingest_method: feed
model: claude-sonnet-5
---

# In my interview, OpenAI's CTO of Applications Vijaye Raji said more code gets thrown away now that coding is cheap. How to decide what your team keeps and scraps.

## Insights

- OpenAI's coding agents increased the volume of concurrent work moving through development systems — engineers pursued more changes at once, with agents retrieving code, running tests, and submitting work — which strained existing infrastructure.
- OpenAI built a new Git backend called Pando specifically to handle agent-driven traffic against its monorepo, reporting a nearly 80% drop in median push latency as a result.
- When individual engineer productivity accelerates via agents, the team as a whole captures far less of that gain — the bottleneck shifts elsewhere rather than disappearing.
- At FurtherAI, a fivefold increase in merged changes per engineer didn't eliminate delay — it relocated the wait into testing, code review, and decisions about what to build next.
- FurtherAI converted recurring human review comments into 21 automated checks that agents can run and fix themselves before a human reviewer is involved.
- Vijaye Raji (OpenAI CTO of Applications) argues for treating code as disposable — favoring throwaway prototypes and working demos over getting attached to a single implementation — as a way to advance team decisions without prolonging debate.

## Quote

> More code gets thrown away now that coding is cheap.

---
title: The Cache Is the Price
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://julsimon.substack.com/p/the-cache-is-the-price
author: Julien Simon from The AI Realist <julsimon@substack.com>
date_published: '2026-09-08'
date_captured: '2026-09-09'
ingest_method: email
model: claude-sonnet-5
---

# The Cache Is the Price

## Insights

- Anthropic and OpenAI published identical headline rates ($10/$50 per million tokens) days apart, but their prompt-cache pricing differs by 4x on cache reads, making real agentic-workload costs diverge sharply despite matching sticker prices.
- Prompt caching (storing a processed prefix so later turns pay a fraction of input price) is what makes long, context-heavy agent sessions affordable at all — uncached, a 20-turn/200k-token session costs ~$40; cached, ~$3.45–$6.30 depending on vendor.
- The cache is stored per-model, so handing a task off from a cheap model to a frontier model (the core mechanic of "routing" or "cascading" architectures) forces a full, expensive prefix rebuild — this handover cost, not the model's list price, is what determines whether routing actually saves money.
- The "break-even escalation rate" (how often a cheap-first cascade can hand off to the frontier before losing money) swings across a huge range (roughly 29%–90%) depending purely on whether the frontier bills the rebuilt prefix as reused cache, a fresh write, or a one-shot throwaway — a design/billing detail no vendor documents.
- Public benchmark evidence (Together AI's DeepSWE cascade, StateM's Terminal-Bench run) shows cheap-model-first cascades with escalation-on-test-failure can match or beat frontier-only performance at a fraction of the cost — but only where a free, machine-checkable verifier exists; most real work (summaries, memos, replies) lacks such a check, so buyers often pay frontier rates as unmeasurable insurance against unseen errors.
- Enterprise buyers (Salesforce's Benioff and finance leadership, HPE's CFO) are already publicly describing/building routing layers to cut token spend by directing work to cheaper models, though data (Vercel gateway) shows Anthropic still captures disproportionate revenue share at a steep price premium — cheap models are winning volume, not yet budgets.

## Quote

> The charge is on the handover, not on the border.

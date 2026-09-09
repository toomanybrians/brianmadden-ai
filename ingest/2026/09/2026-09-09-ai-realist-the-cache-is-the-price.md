---
title: The Cache Is the Price
source: The AI Realist
source_id: ai-realist
source_url: https://www.airealist.ai/p/the-cache-is-the-price
author: Julien Simon
date_published: '2026-09-08'
date_captured: '2026-09-09'
ingest_method: feed
model: claude-sonnet-5
---

# The Cache Is the Price

## Insights

- Anthropic and OpenAI published identical headline rates for their latest frontier models ($10/$50 per million tokens), but the cache-read pricing that dominates agentic workloads differs by 4x ($0.25 vs $1.00 per million), making the "same price" an illusion for real usage patterns.
- Prompt caching is the hidden lever in LLM economics: cached conversations can cost a fraction of uncached ones, but caches are per-model, so handing a task from one model to another (routing/escalation) destroys the cache and forces an expensive rebuild — the "handover" is the real cost center, not the base rate.
- Model routing (cheap model first, escalate to frontier on failure) only saves money below a "break-even escalation rate," which depends heavily on how the frontier model bills the rebuilt context (three very different outcomes: reused cache, full fresh rebuild, or billed-as-write) — a design choice, not a vendor-disclosed number.
- The only public data point on real-world escalation rates comes from Together AI's coding benchmark cascade (~31-37% escalation), which relied on a free, automated pass/fail test — most enterprise knowledge work lacks any such verifier, so buyers often default to paying frontier rates as blanket "insurance" against undetectable errors.
- Third-party benchmark rankings (Artificial Analysis) shifted twice in one week purely from methodology changes (reweighting private eval sets), flipping which frontier model "won" — illustrating how unstable and manipulable public model comparisons can be.
- Enterprise buyers (Salesforce, HPE) are already publicly discussing internal routing/right-sizing strategies to cut frontier-model token spend, even as one lab (Anthropic) still captures a growing revenue share and price premium (4.4x average) despite falling headline prices, per gateway data from Vercel.

## Quote

> The charge is on the handover, not on the border.

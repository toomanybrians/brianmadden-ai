---
title: 'MiMo-V2.6-Pro: a frontier-level agent planner for about $0.12 per 100 calls?'
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://evalsignal.xyz/campaign/b20c9b79-2480-4263-9919-8f2e0442ee32/ff779425-3a22-47e4-965d-bf0e1f18a567
author: EvalSignal <newsletter@evalsignal.xyz>
date_published: '2026-10-21'
date_captured: '2026-10-22'
ingest_method: email
model: claude-sonnet-5
---

# MiMo-V2.6-Pro: a frontier-level agent planner for about $0.12 per 100 calls?

## Insights

- In a 100-case browser-agent planner benchmark across 17 models, MiMo-V2.6-Pro produced 95 valid native tool calls and matched the "ideal" tool choice in 44 cases, ranking third on exact-action consensus (43.6%) behind two others.
- Cost for the full 100-case replay was about $0.1246 (~12.5 cents per 100 calls) on its tested OpenRouter route — cheap relative to its capability tier, though not the cheapest model tested (Qwen and GLM reportedly cheaper in separate runs).
- Its latency profile is uneven: 6.12s median response time but a 46.68-second p95, a long tail flagged as a real risk for interactive agent use despite strong median speed.
- In a separate 100-screenshot multimodal/vision test, it passed 77 cases (94.0% mean rubric score), putting it in the competitive middle of the pack rather than leading (Qwen3.8 Flash passed 79, GLM-5.3 Flash 76).
- The benchmark only measures a model's first/opening planning decision in an agent loop — it does not test full task execution or whether an agent actually completes a multi-step browser task, limiting how far "frontier-level" claims should be read.
- Cross-model comparisons in the piece combine results from different dates, routes, and providers rather than a single simultaneous test, which the authors flag as a methodological caveat on cost and performance comparisons.

## Quote

> MiMo-V2.6-Pro is a credible frontier-class agent candidate at a modest observed API cost.

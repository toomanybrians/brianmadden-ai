---
title: 'NEX N2.5 Pro: 100 agent-planning calls for $0.15'
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://evalsignal.xyz/campaign/e3ed9064-e5a2-4a41-a7a0-865d7c58e5a8/ff779425-3a22-47e4-965d-bf0e1f18a567
author: EvalSignal <newsletter@evalsignal.xyz>
date_published: '2026-10-08'
date_captured: '2026-10-09'
ingest_method: email
model: claude-sonnet-5
---

# NEX N2.5 Pro: 100 agent-planning calls for $0.15

## Insights

- An independent benchmark ran 100 frozen browser-agent planning prompts against NEX N2.5 Pro (a low-cost hosted MoE model, ~397B total params, routed via OpenRouter FP8) and found it dramatically cheaper than a comparison model — $0.15 vs $1.06 for the same 100-call suite, roughly a 7x cost gap.
- Cost and reliable tool-call formatting (95/100 native structured calls, 100% known tool names) did not translate into better decision quality: only 11/100 calls matched the exact ideal action and 27/100 matched the ideal tool name, versus 17/100 and 32/100 for the pricier MiniMax M3 reference.
- NEX N2.5 Pro showed a consistent "inspect-first" bias — calling get_accessibility_tree 59 times, including in cases where the reference behavior called for direct navigation or clarification — meaning it often adds an extra turn rather than acting decisively.
- The model aligned with a saved Sonnet 4.6 reference 67% of the time (vs 75% for MiniMax M3) and was slower at the median (7.23s vs 3.10s), despite being far cheaper.
- The benchmark's authors frame this as a tradeoff: cheap, operationally reliable models suit high-volume agent loops with recovery/retry capacity, but are not a safe default when the first action in a workflow carries high stakes or when latency matters.
- The test explicitly measures only first-turn tool-call selection in isolation (no execution, no multi-turn recovery, no vision), so it speaks to routing discipline rather than end-to-end task success.

## Quote

> Scale and call frequency did not translate into first-action leadership.

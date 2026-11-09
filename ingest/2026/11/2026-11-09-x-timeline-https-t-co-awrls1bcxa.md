---
title: https://t.co/awRLs1Bcxa
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2118820787788591245
author: '@DanielMiessler'
date_published: '2026-11-06'
date_captured: '2026-11-09'
ingest_method: x
model: claude-sonnet-5
---

# https://t.co/awRLs1Bcxa

## Insights

- Daniel Miessler built a custom benchmark suite (Gauntlet: Explain, Science, Ship, plus a Composite) because existing benchmarks like Artificial Analysis didn't match his real-world experience of model intelligence.
- Gauntlet Explain grades model answers 0–4 on hard open questions using David Deutsch's "hard to vary" criterion for a good explanation — every part of the explanation must do work, with no detail swappable without breaking it.
- The benchmark plots intelligence against cost per answer (log scale), letting users set a budget and see which model/effort setting delivers the best score within it — explicitly framing model choice as a cost-performance tradeoff, not just a raw capability ranking.
- Results show diminishing returns on "effort" settings: most models gain only marginal score improvements from low to xhigh effort, with large jumps reserved for "max" effort at dramatically higher cost (e.g., Claude Opus 5.5 jumps from 2.80 at xhigh/$0.08 to 3.11 at max/$1.11 per answer).
- Claude Opus 5.5 at max effort leads all tested models/settings on the Explain benchmark; Claude Fable 5.1 at max effort comes closest at 3.03, with all other model/effort combinations falling further behind with statistical confidence.
- The underlying methodology ties cost to each provider's output list token pricing, using mean tokens per answer across multiple runs, making the comparisons explicitly reproducible against market pricing at a stated date.

## Quote

> I find the Artificial Analysis AI benchmarks don't match my experience in real-world AI work.

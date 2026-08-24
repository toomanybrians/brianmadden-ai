---
title: Are Open Models Catching Up?
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/are-open-models-catching-up
author: Evan Cloutier
date_published: '2026-08-21'
date_captured: '2026-08-24'
ingest_method: feed
model: claude-sonnet-5
---

# Are Open Models Catching Up?

## Insights

- SemiAnalysis measured the open-vs-closed capability gap across three distinct LLM eras (early scaling 2022-24, reasoning 2024-25, agentic 2025-present), using era-specific benchmarks since each era's benchmarks saturate and get replaced as capabilities shift.
- The time for open models to catch up to the first frontier closed model of an era has roughly halved each era: ~13 months (Llama-2 to Llama-3.1-405B matching GPT-3.5) in Era 1, 8.5 months for R1-0528 to close the o1-era gap in Era 2, and 4.8–6 months for Kimi K2.6/GLM-5.2 to surpass Opus 4.5/GPT-5.2 in Era 3.
- In the current agentic era, the product layer (model + harness) matters more than raw benchmark scores — GPT-5.2 outscored Opus 4.5 on the composite benchmark but Anthropic's Claude Code harness delivered a better real-world experience, driving $65B+ in ARR growth since May 2025.
- OpenAI and Anthropic have compressed their release cadence to ~51 days per model in Era 3, versus 213 days in Era 1 and 120 in Era 2, yet open models are still closing gaps faster than ever.
- Author cautions that benchmarks are imperfect proxies for real work and can be "hill-climbed" via RL environments mimicking test tasks; also notes closed-lab safety testing delays (e.g., GPT-4's 218-day gap between training completion and release) may partly explain perceived open-model catch-up speed.
- Infrastructure evidence of open-model scale: Fireworks alone processes 40T tokens/day, roughly 2x OpenAI's API volume as of end of March.

## Quote

> With each generation, open-source models take half as long to catch up to the first closed-source model of the era.

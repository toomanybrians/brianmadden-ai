---
title: 'OpenAI Jalapeño: Better Than Nvidia Blackwell'
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/openai-jalapeno-better-than-nvidia
author: Bryan Shan
date_published: '2026-08-25'
date_captured: '2026-08-25'
ingest_method: feed
model: claude-sonnet-5
---

# OpenAI Jalapeño: Better Than Nvidia Blackwell

## Insights

- OpenAI's first inference ASIC ("Jalapeño"), co-developed with Broadcom, went from team formation to tapeout in ~16 months and reportedly beats Nvidia, AMD, and Google chips on perf/watt across tested open-source models — atypical for a first-generation chip.
- The chip is designed as a generalized inference accelerator rather than one narrowly optimized for OpenAI's own models, achieved through deep hardware/software co-design rather than workload-specific specialization.
- OpenAI used its own AI coding tools (Codex/Gluon) to accelerate chip design and kernel writing, including an 8% SIMD area reduction and 10% matrix-engine area reduction, and to rapidly bring up support for new models like DeepSeek R1 and Kimi K2.5 — suggesting AI-assisted chip design and software bring-up can outpace traditional (e.g., CUDA-based) development cycles.
- Architecturally, OpenAI chose not to disaggregate prefill and decode across separate chip pools, betting that a unified, fungible fleet handles real-world traffic variability (shifting input/output ratios, concurrency, cache-hit rates) better than fixed specialized pools, trading some theoretical efficiency for operational flexibility.
- Performance claims come from OpenAI-provided, SemiAnalysis-witnessed lab benchmarks (not the full independent test suite), tested only on shorter/simpler workloads (8k1k) rather than long-context/agentic workloads, and compared against Nvidia's Blackwell rather than the more directly comparable HBM4-based Rubin chip.
- The piece frames this as a broader signal that frontier AI models may be eroding the software/compiler moat that has historically protected established chip ecosystems (e.g., Nvidia's CUDA), since AI-driven kernel generation reduced reliance on specialized human chip engineering teams.

## Quote

> The CUDA moat is potentially dead given how fast OpenAI can bring up new models on their silicon.

---
title: How GLM5.3 Sparse Attention Affects HBM Memory Usage
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/sparse-savings-persistent-demand-inside-glm53
author: Kimbo Chen
date_published: '2026-09-28'
date_captured: '2026-09-29'
ingest_method: feed
model: claude-sonnet-5
---

# How GLM5.3 Sparse Attention Affects HBM Memory Usage

## Insights

- Sparse attention (top-k token selection) cuts compute and bandwidth demands during the core attention operation, but does not reduce overall memory capacity requirements — full context must still reside in HBM for the top-k selection step itself.
- SGLang's HiSparse system addresses this by treating KV cache like an LRU cache, offloading entries to host DRAM and prefetching layer N's data during layer N-1's execution to hide latency, showing that system-level engineering can override sparse attention's theoretical memory limits.
- Serving cost comparisons across GPU/accelerator types (GB200, GB300, MI355X) for GLM-5.3 show no single hardware option is uniformly cheapest — rankings shift depending on target throughput (tokens/sec) and how strict the time-to-first-token constraint is.
- GLM-5's architecture (744B total/40B active MoE) uses DeepSeek Sparse Attention with a "lightning indexer" for token selection and sparse multi-latent attention; its query head count (64 vs. DeepSeek's 128) suggests possible optimization for different, non-Nvidia hardware.
- IndexShare (sharing one indexer across every 4 attention layers) cuts indexer cache and compute by 75% while boosting throughput 1.5–1.8x, addressing indexer latency costs that grow with context length.
- Post-training combines supervised fine-tuning, three RL stages (reasoning, agentic, general), and cross-stage distillation; later versions introduce SAO (Single-rollout Asynchronous Optimization), replacing group-based advantage estimation with a value-model-based approach to stabilize long-horizon agentic RL training.

## Quote

> Sparse attention reduces KV cache memory and bandwidth requirements at the SDPA operation, but it does not reduce the overall memory capacity usage. — Kimbo Chen, SemiAnalysis

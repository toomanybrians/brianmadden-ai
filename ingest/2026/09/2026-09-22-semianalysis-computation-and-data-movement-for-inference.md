---
title: Computation and Data Movement for Inference
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/computation-and-data-movement-for
author: Tanj Bennett
date_published: '2026-09-21'
date_captured: '2026-09-22'
ingest_method: feed
model: claude-sonnet-5
---

# Computation and Data Movement for Inference

## Insights

- Mixture-of-Experts architecture has restructured inference serving into four distinct operating regimes (prefill, midfill, decode attention, decode experts), each with different compute-vs-data-movement tradeoffs, rather than a single uniform "compute-bound vs memory-bound" workload.
- Agentic/tool-using workflows generate many more "turns" per conversation than classic chatbot use, with context (KV cache) repeatedly extended and periodically compacted once it approaches a model's max context window (examples cited: 250k tokens for Opus 4.8, 1M for "Fable").
- KV cache/context state is treated as immutable, shared "blobs" in a scale-out storage pool (moving between HBM, CPU DRAM, and SSD tiers) rather than being bound to one machine — enabling orchestrators to route requests to whichever worker is available rather than wherever the data happens to live.
- Good context/session orchestration (caching, compaction, reuse of prior conversation state) is described as a competitive advantage for AI companies, since it directly affects serving cost and latency.
- Batching sharply improves efficiency in prefill/midfill (many tokens can share one expert's weight load) but delivers much smaller gains in decode, where each query has its own private context and only a few experts activate per token — meaning decode remains dominated by memory movement, not compute.
- Hardware design (e.g., NVIDIA's tightly-linked 72-GPU domains) is driven directly by the need to synchronize many machines so that expert-routing traffic ("all-to-all") can be handled efficiently; the article projects that future memory technology (fast 3D/hybrid-bonded RAM) will be decisive for handling growing agentic context lengths (500k+ tokens).

## Quote

> Orchestration of the inference context is a competitive advantage for AI companies.

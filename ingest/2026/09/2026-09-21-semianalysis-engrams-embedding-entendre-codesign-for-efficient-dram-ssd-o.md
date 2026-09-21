---
title: 'Engrams Embedding Entendre: Codesign for Efficient DRAM/SSD Offloading'
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/engrams-embedding-entendre-codesign
author: Bryan Shan
date_published: '2026-09-18'
date_captured: '2026-09-21'
ingest_method: feed
model: claude-sonnet-5
---

# Engrams Embedding Entendre: Codesign for Efficient DRAM/SSD Offloading

## Insights

- Engram is a model architecture technique that extends token embeddings with learned multi-token lookups, letting recurring patterns retrieve vectors directly instead of being reconstructed through attention/feed-forward layers — reducing HBM capacity needs at equivalent model quality.
- Because Engram lookups depend on token IDs rather than hidden states, the embedding table can be prefetched from host DRAM (or even SSD) while earlier layers compute, making the architecture naturally suited to memory offloading rather than requiring the full weight table to live in HBM.
- Testing on DeepSeek-V4.1-Flash (~189 GiB of Engram memory) found DRAM offloading via UVA improved performance-per-dollar (e.g., switching B300 from TP4 to TP2 configurations, up to 1.6x pareto improvement), while unoptimized SSD offloading underperformed DRAM offloading on both cost and interactivity metrics.
- Removing Engram degrades performance unevenly: factual-knowledge benchmarks lost more capability than reading comprehension, and code-reasoning tests showed that memory retrieval and expert routing are intertwined rather than cleanly separable ("memory stores facts; experts reason" doesn't hold).
- The piece notes NVIDIA's Rubin Ultra roadmap was despec'd from 1024GB to ~200GB of HBM per chip, framed as part of a broader trend where model architecture innovation (like Engram) is emerging partly in response to HBM supply/cost constraints.
- Separately, agentic inference benchmarks (InferenceX) on DeepSeek-V4.1-Flash show NVIDIA's CUDA ecosystem maintaining a strong performance-per-dollar advantage over AMD's MI355X, including AMD lagging on day-0 software support for the model.

## Quote

> Model architecture will continue to innovate around constraints.

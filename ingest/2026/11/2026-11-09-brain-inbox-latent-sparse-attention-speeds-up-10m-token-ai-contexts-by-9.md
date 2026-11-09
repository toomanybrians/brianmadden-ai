---
title: ⚡ Latent Sparse Attention Speeds Up 10M-Token AI Contexts by 9x
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: AlphaSignal <news@alphasignal.ai>
date_published: '2026-11-08'
date_captured: '2026-11-09'
ingest_method: email
model: claude-sonnet-5
---

# ⚡ Latent Sparse Attention Speeds Up 10M-Token AI Contexts by 9x

## Insights

- Long-running AI agents (coding agents, research assistants) accumulate millions of tokens of context, and existing sparse attention methods still scale quadratically during the "prefill" stage because their indexers must examine every previous token or block — in one test, indexing consumed 98% of an attention layer's prefill time at 10M tokens.
- Latent Sparse Attention (LSA), developed by Prefrontal AI and ETH Zurich, clusters keys into groups in a learned "latent space" and searches cluster centroids first, rather than scoring every individual key, cutting the search cost.
- Two integration modes exist: Distilled LSA (D-LSA) retrofits a trained indexer onto an existing frozen model; Native LSA (N-LSA) builds clustering into training from scratch.
- Benchmarked on Qwen-3.8-27B and GLM-5.3-Flash at 10M tokens on H200 GPUs, D-LSA cut time-to-first-token by up to 9.2x and per-attention-layer prefill by up to 72.4x versus full attention, and 22.7x versus an existing sparse method.
- Results are mixed on accuracy: Qwen's long-context retrieval score (RULER benchmark) improved slightly over full attention, but GLM lost up to 8 points at mid-range context lengths (2-5M tokens) compared to its original sparse-attention baseline.
- Code, model weights, and an SGLang integration have been released under Apache 2.0, with the caveat that speed gains shrink substantially for shorter-context tasks.

## Quote

> LSA organizes attention values like a library. Rather than checking a description of every book, a query first examines groups of books.

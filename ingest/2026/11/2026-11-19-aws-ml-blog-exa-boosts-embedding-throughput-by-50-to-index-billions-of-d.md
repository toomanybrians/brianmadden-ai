---
title: Exa boosts embedding throughput by 50% to index billions of documents on AWS
  AI chips
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/exa-boosts-embedding-throughput-by-50-to-index-billions-of-documents-on-aws-ai-chips/
author: Summer Devlin
date_published: '2026-11-18'
date_captured: '2026-11-19'
ingest_method: feed
model: claude-sonnet-5
---

# Exa boosts embedding throughput by 50% to index billions of documents on AWS AI chips

## Insights

- Exa, a semantic web-search/indexing company, re-embedded 30 billion priority documents while migrating to a new embedding model, temporarily doubling inference load and prompting a hardware/efficiency review on AWS Inferentia2 and Trainium2 chips.
- Through a sequence of optimizations (weight layout fixes, autocast precision downcasting, prebuilt NKI attention kernels, a custom fused SwiGLU MLP kernel to eliminate HBM memory-spill stalls, and FLOPS reduction via shape-specific attention kernels), they achieved roughly a 47-50% improvement in throughput and cost per million documents embedded.
- A key technical bottleneck was core contention/memory spill on Inferentia2's dual-NeuronCore chips, requiring kernel rewrites tailored to exact model tensor shapes rather than generic kernels designed for arbitrary shapes.
- Correctness during optimization was gated by requiring 0.999 cosine similarity to a reference model's output, allowing aggressive precision/kernel changes without unacceptable accuracy loss.
- The optimization work was largely performed by AI agents operating in a structured three-part harness (compile/correctness-check, profile, benchmark) built on the Flyte workflow platform — with different agent tiers (lightweight for parameter search, reasoning agents for bottleneck diagnosis, strongest code-gen models for custom kernel writing) assigned by task complexity and cost.
- Exa frames the strategic rationale as flexible, multi-region, multi-hardware-type scheduling to avoid compute shortages and to exploit price/performance differences, noting that optimization work done for Inferentia2 carried over directly to Trainium2.

## Quote

> At the scale Exa operates, extracting maximum cost-performance from a flexible pool of hardware is what matters.

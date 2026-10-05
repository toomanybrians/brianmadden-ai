---
title: Eight Changes to Transformer Attention, and What Each Costs
source: The AI Realist
source_id: ai-realist
source_url: https://www.airealist.ai/p/eight-changes-to-transformer-attention
author: Julien Simon
date_published: '2026-10-04'
date_captured: '2026-10-05'
ingest_method: feed
model: claude-sonnet-5
---

# Eight Changes to Transformer Attention, and What Each Costs

## Insights

- Open-weight model labs (Alibaba, Moonshot, DeepSeek, Z.AI) have largely abandoned full attention in every layer; most frontier open models now use hybrid designs where roughly 1-in-4 layers (or none) actually read every prior token, with the rest using linear/compressed/sparse attention to cut memory and compute costs.
- The stated motivation is cost, not hardware scarcity: DeepSeek reports V4-Pro needs only 10% of the KV cache and 27% of the compute of its prior model at 1M tokens, and only one Chinese lab (Z.AI) even hints at chip constraints as a factor.
- Despite labs advertising million-token context windows, almost none of their own published benchmarks test long-context retrieval accuracy past 128,000 tokens — accuracy on tasks like distinguishing multiple similar items (vs. simple needle lookup) can collapse at longer lengths (e.g., one model drops from 93 at 256K tokens to 26 at 1M).
- Of ten published efficiency-vs-full-attention comparisons across six labs, only one is an outright win, seven are mixed, and two are losses — meaning the "efficient attention is basically free" narrative isn't well supported by the labs' own data, and no public comparison exists at the same model size for any current flagship model.
- Serving infrastructure (caching, kernels, quantization) significantly lags model releases — new attention designs often ship without fast inference kernels, hardware support (e.g., no Ampere/A100 kernel for one model), or reliable cache-hit measurement, meaning published pricing/efficiency gains may not be realized by actual users.
- The piece recommends builders test models at their actual deployment context length (not just marketing-length benchmarks), measure real cache hit rates, and check retrieval accuracy by token position before trusting efficiency claims.

## Quote

> Read the neighbors, not just the label.

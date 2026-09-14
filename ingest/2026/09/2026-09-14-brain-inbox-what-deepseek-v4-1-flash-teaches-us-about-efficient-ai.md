---
title: ⚡ What DeepSeek-V4.1-Flash teaches us about efficient AI
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: AlphaSignal <news@alphasignal.ai>
date_published: '2026-09-13'
date_captured: '2026-09-14'
ingest_method: email
model: claude-sonnet-5
---

# ⚡ What DeepSeek-V4.1-Flash teaches us about efficient AI

## Insights

- DeepSeek's V4.1-Flash is nearly 2x the parameter count of its predecessor (552B MoE) but achieves a 4x smaller KV cache footprint (890 bytes/token vs. 3,514 bytes/token), demonstrating that total parameter count is becoming a weaker proxy for a model's actual serving cost.
- The model uses a "Causal Encoder-Decoder" architecture splitting its 40 layers into a 20-layer encoder (used only during prompt processing) and 20-layer decoder (used only during generation), cutting active parameters per input token to 8B versus 16B for output tokens.
- Sliding-Window Attention plus a "Bounded Replay" technique lets the system cheaply reconstruct local context after a cached session is restored, by recomputing only recent tokens rather than the full dependency chain — removing the need to persist that state to SSD.
- A new "Compressed Sparse Attention 2" scheme lets attention layers share cached key/value state and retrieval results across layers (via "Full," "Reindex," and "Reuse" layer types), reducing redundant memory copies of history.
- A "Hierarchical Sparse Indexer" bounds the cost of searching long context by having one layer build a candidate pool (up to 2,048 blocks) from the full history, with later layers searching only within that pool rather than the entire million-token context.
- Combined with FP4 storage for the remaining KV cache (vs. FP8 previously), these changes cut persistent KV-cache storage to roughly one-eighth of the predecessor's, while the model remains competitive with proprietary models (score of 40 vs. Gemini 3.8 Flash High's 41 on the Artificial Analysis Intelligence Index) at a quarter of the cost per task.

## Quote

> If these techniques spread, the next generation of efficient models might not be defined by having fewer parameters.

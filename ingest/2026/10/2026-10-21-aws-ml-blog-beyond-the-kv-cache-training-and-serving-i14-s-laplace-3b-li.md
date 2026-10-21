---
title: 'Beyond the KV cache: Training and serving i14’s Laplace 3B linear attention
  model on AWS Trainium2 with native PyTorch'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/beyond-the-kv-cache-training-and-serving-i14s-laplace-3b-linear-attention-model-on-aws-trainium2-with-native-pytorch/
author: Kevin Shabahang
date_published: '2026-10-20'
date_captured: '2026-10-21'
ingest_method: feed
model: claude-sonnet-5
---

# Beyond the KV cache: Training and serving i14’s Laplace 3B linear attention model on AWS Trainium2 with native PyTorch

## Insights

- i14's Laplace 3B replaces transformer softmax attention with Gated Linear Attention (GLA), keeping a fixed-size recurrent state (29.5 MB per sequence) instead of a KV cache that grows with context — turning training compute from O(T²) to O(T) and inference memory into a constant regardless of context length.
- Porting the model to AWS Trainium2 required rewriting GPU-optimized Triton kernels in native PyTorch (via beta "TorchNeuron Native"), redesigning the Muon optimizer's distributed communication (all_to_all instead of gather/broadcast, cutting per-rank traffic 24x and raising throughput 1.63x), and statically unrolling the sequential backward pass to fit Trainium's compiler constraints.
- On one trn2.48xlarge instance, the model trained at ~120,000 tokens/sec and achieved a smooth loss curve (11.4 → 2.37) over 44B of a planned 100B-token run, with no divergence or NaN issues post-warmup.
- Inference served 11,544 output tokens/sec across 1,280 concurrent sequences through an unmodified vLLM engine; because serving state doesn't grow with context, increasing prompt length from 2,048 to 8,192 tokens added only 0.5% to per-token cost.
- Key engineering lesson: most decode latency came from operator dispatch overhead under eager PyTorch, not compute or bandwidth limits — compiling the decode step gave a 1.7x–3.5x throughput improvement depending on traffic patterns, and benchmarking must account for variable batch-width compilation costs that fixed-batch tests hide.
- Framed as a signal that non-transformer architectures with constant-size memory could help agentic systems retain longer context without proportionally growing serving costs or losing concurrency.

## Quote

> Longer histories don't require a larger per-sequence state, which can help teams retain more context while keeping memory use predictable.

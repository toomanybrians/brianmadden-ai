---
title: Managed NVIDIA Dynamo on Amazon SageMaker HyperPod Inference
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/managed-nvidia-dynamo-on-amazon-sagemaker-hyperpod-inference/
author: Vinay Arora
date_published: '2026-11-17'
date_captured: '2026-11-18'
ingest_method: feed
model: claude-sonnet-5
---

# Managed NVIDIA Dynamo on Amazon SageMaker HyperPod Inference

## Insights

- AWS added managed support for NVIDIA Dynamo to SageMaker HyperPod Inference, targeting a specific scaling problem: large models like GLM-5.3 (FP8 weights) exceed the 640GB GPU memory available on a single ml.p5.48xlarge instance once KV cache and runtime overhead are included, forcing multi-node serving.
- The integration separates "prefill" (prompt processing) and "decode" (token generation) into independently scalable worker pools that transfer KV cache over EFA networking — called disaggregated serving — versus the simpler "aggregated" mode where both run on the same workers.
- Two deployment paths are offered: bring-your-own Dynamo manifest for teams wanting full control, or a simplified InferenceEndpointConfig path with sensible defaults (vLLM engine, KV-aware routing, autoscaling via KEDA) for teams wanting managed setup.
- Benchmarks claim disaggregated serving hit 2.05x the throughput of aggregated serving for Qwen3-235B (207 vs 101 output tokens/sec/GPU) under latency-constrained conditions — a vendor-reported number worth treating as a best-case scenario rather than universal result.
- A separate test showed multi-node serving (splitting a model across two instances) retained 99.1% of single-node throughput for Qwen3.5-397B, suggesting the node boundary itself isn't a major throughput penalty — relevant for any model too large to fit on one instance.
- The broader pitch is reducing "undifferentiated infrastructure work" — AWS/NVIDIA handling health monitoring, node replacement, and orchestration complexity so teams can focus on model/application work rather than cluster plumbing.

## Quote

> HyperPod manages model weights, auto-scales clusters based on GPU and inference metrics, monitors node health, and replaces failed nodes.

---
title: 'Amazon SageMaker Inference: 2026 launches in review, part 2'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-inference-2026-launches-in-review-part-2/
author: Aryaman Kothari
date_published: '2026-11-20'
date_captured: '2026-11-20'
ingest_method: feed
model: claude-sonnet-5
---

# Amazon SageMaker Inference: 2026 launches in review, part 2

## Insights

- SageMaker inference recommendations expanded from an API-only tool into SageMaker AI Studio (low-code), the SageMaker Python SDK v3, and a coding-agent skill, and now handles harder questions like LoRA adapter capacity planning and SLA-bound concurrency limits (e.g., finding max concurrency under a latency target via an automated search rather than manual sweeps).
- GPU utilization/cost features: Inference Components now manageable via console (not just SDK/CLI), and new NVIDIA MIG support lets one physical GPU be split into up to seven isolated partitions, letting multiple small models (embedding, reranker, classifier) share a single GPU under one endpoint — though AWS still bills for the full instance-hour, so savings come only from packing more models per instance, not lower rates.
- For models too large for a single machine, AWS now offers managed NVIDIA Dynamo on HyperPod Inference — a managed version of multi-node sharded serving, disaggregated prefill/decode, and KV-aware routing — shifting operational burden (networking, node recovery, upgrades) from the customer to AWS while keeping an OpenAI-compatible endpoint.
- Multiple new routing layers address idle-capacity/queueing problems: KV-cache-aware routing (routes by actual reported cache state, not just prompt fingerprinting), an Inference Gateway for HyperPod claiming up to 97-98% lower P99 TTFT vs round-robin, and Cross-Region Inference Routing that fails over across regions/accounts via PrivateLink with data-residency guardrails.
- New "continuous performance monitoring" passively watches latency/GPU utilization/config (not request content) and surfaces findings — latency drift, persistent config gaps, idle GPU capacity — routed into a guided fix workflow in Studio, requiring explicit approval before any change is applied.
- In-place rolling model updates reduce new-capacity requirements during deployment rollouts (e.g., a 20-instance fleet needs only 2 new instances instead of 20), with a further "scale-in-first" update planned for early 2027 that would need zero additional instances.

## Quote

> Part 1 argued that advantage in AI inference comes from operating an efficient inference stack.

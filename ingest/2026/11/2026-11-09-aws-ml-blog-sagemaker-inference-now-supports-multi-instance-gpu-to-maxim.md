---
title: SageMaker Inference now supports Multi-Instance GPU to maximize GPU utilization
  for model endpoints
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/sagemaker-inference-now-supports-multi-instance-gpu-to-maximize-gpu-utilization-for-model-endpoints/
author: Shantanu Tripathi
date_published: '2026-11-06'
date_captured: '2026-11-09'
ingest_method: feed
model: claude-sonnet-5
---

# SageMaker Inference now supports Multi-Instance GPU to maximize GPU utilization for model endpoints

## Insights

- SageMaker Inference now supports NVIDIA Multi-Instance GPU (MIG) partitioning, letting a single physical GPU be hardware-split into up to seven isolated instances, each with dedicated compute, memory, and bandwidth — addressing the long-standing constraint that GPU allocation could only happen in whole-accelerator units.
- This replaces three previously imperfect workarounds: batching on fewer large endpoints (only works for interchangeable models), multi-model endpoints (no isolation, cold-start penalties), or self-managed Kubernetes with MIG (full platform/ops burden). AWS now manages the GPU configuration, placement, and scaling directly.
- Partitioning is exposed through two new optional fields on existing APIs (no new endpoints/IAM actions), and only works with "inference components" (SageMaker's multi-model-per-endpoint construct) — not single-model, serverless, or async endpoints.
- AWS's own benchmark: one MIG partition (mig-3g.40gb) of an H100 outperformed a whole uncarved A100-40GB across all tested traffic patterns — 53-89% more throughput, 18-34% lower cost per million output tokens above a crossover point, and the A100 outright failed requests under long-context/high-concurrency load while the partition didn't.
- Choosing a partition size requires separately accounting for compute (prefill/prompt-length sensitive) vs. memory (decode/KV-cache/context-length sensitive) — the two scale independently and most workloads need a balance, not a max of either.
- Tradeoffs are real: partition layout is fixed at endpoint creation (no reshuffling without a new endpoint), billing is still per full instance-hour regardless of utilization, and MIG isolates the GPU only — CPU, networking, storage, and routing are still shared across tenants.
- Salesforce is cited as a design partner currently validating the feature against production workloads, framed as motivated by consolidating underutilized inference workloads and improving cost/isolation at scale.

## Quote

> Every supported accelerator is now several sizes rather than one.

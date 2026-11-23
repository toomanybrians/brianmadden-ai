---
title: 'Introducing Amazon SageMaker HyperPod Global Inference Gateway: One endpoint
  across Regions and clusters'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-global-inference-gateway-one-endpoint-across-regions-and-clusters/
author: Dmitry Soldatkin
date_published: '2026-11-20'
date_captured: '2026-11-23'
ingest_method: feed
model: claude-sonnet-5
---

# Introducing Amazon SageMaker HyperPod Global Inference Gateway: One endpoint across Regions and clusters

## Insights

- AWS's SageMaker HyperPod Global Inference Gateway adds a second routing tier above its existing per-cluster Inference Gateway, routing requests across multiple GPU clusters and AWS Regions through a single managed endpoint.
- The core problem addressed: paid-for GPU capacity sits idle in one cluster/Region while requests queue on a saturated cluster elsewhere, because clients previously had to pick a cluster themselves — creating uneven load, manual failover, and custom cross-Region networking overhead.
- Routing decisions use four weighted signals (KV cache headroom, queue depth, region proximity, error rate), with customizable weights — letting operators trade off latency/proximity against resilience depending on workload needs.
- The gateway handles automatic failover (moving traffic off failed clusters, retrying failed requests once, returning 503 only if no healthy cluster remains) without requiring client-side changes.
- Security model keeps data path private: SigV4/IAM authentication, traffic restricted to AWS PrivateLink, and no logging/storage of prompts or completions by the gateway itself.
- A real customer (Bagelcode, a gaming company) reports using it in beta for cross-Region failover across two Regions without building their own routing layer — framed as reducing platform-team operational burden rather than a performance claim.
- Positioned as infrastructure plumbing for scaling inference as "models get larger, and the GPU capacity to serve them is harder to find," reflecting a broader signal about GPU capacity scarcity/fragmentation as an industry constraint.

## Quote

> Capacity spread across clusters and Regions... Models are getting larger, and the GPU capacity to serve them is harder to find.

---
title: Amazon SageMaker AI real-time endpoints now support KV cache aware routing
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-real-time-endpoints-now-support-kv-cache-aware-routing/
author: Dmitry Soldatkin
date_published: '2026-11-17'
date_captured: '2026-11-18'
ingest_method: feed
model: claude-sonnet-5
---

# Amazon SageMaker AI real-time endpoints now support KV cache aware routing

## Insights

- AWS SageMaker AI adds KV-aware routing, a new strategy that routes LLM inference requests to instances based on *actual* reported GPU cache contents, rather than inferring cache location from matching prompt text (prefix-aware routing, SageMaker's prior approach).
- The distinction matters operationally: prefix-aware routing breaks down when caches get evicted under memory pressure or when conversations start short and grow — both common in multi-turn chat and RAG workloads with long shared context.
- AWS reports large benchmark gains on production hardware (Llama 3.1 70B on ml.p5.48xlarge): up to 97% reduction in time-to-first-token and 234% throughput increase versus random routing, with cache hit rate rising from 3-48% to 80-93% — framed as workload-dependent, not universal.
- A smaller reproducible test (Qwen3-4B on 2x ml.g5.xlarge) showed consistent latency and cache-hit improvements over random routing, with modest added overhead latency (14-19ms) — a transparent tradeoff disclosure rather than pure upside marketing.
- Feature requires specific container support (AWS vLLM DLC) and explicit opt-in config; it's offered at no additional charge beyond instance costs, positioning it as an infrastructure-layer optimization rather than a new billable product.
- AWS explicitly frames this as a routing/infrastructure problem solved at the platform level so customers don't need to build custom routing layers — signals a push toward SageMaker as a more complete, self-managed inference stack for LLM serving at scale.

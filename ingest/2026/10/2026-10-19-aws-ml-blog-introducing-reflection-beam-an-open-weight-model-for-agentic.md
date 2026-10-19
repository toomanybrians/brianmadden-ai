---
title: 'Introducing Reflection Beam: an open-weight model for agentic coding on AWS'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-reflection-beam-an-open-weight-model-for-agentic-coding-on-aws/
author: Clement Perrot
date_published: '2026-10-16'
date_captured: '2026-10-19'
ingest_method: feed
model: claude-sonnet-5
---

# Introducing Reflection Beam: an open-weight model for agentic coding on AWS

## Insights

- Reflection AI released Beam, an open-weight sparse mixture-of-experts model (501B total parameters, 23B active) aimed at agentic coding and long-horizon tasks like multi-step tool use, code maintenance, and interpreting intermediate results; Reflection reports an effective context length of 1 million tokens.
- Weights are published on Hugging Face under Apache 2.0, in BF16, FP8, and NVFP4 variants — each with different memory footprints and hardware requirements (FP8 needs H100/H200-class instances; NVFP4 needs B200-class instances), reflecting real infrastructure cost tradeoffs for serving a 500B-parameter model.
- AWS offers two deployment paths: a fully managed SageMaker JumpStart real-time endpoint (less operational burden, less control) versus SageMaker HyperPod Inference with Kubernetes-native control over distributed GPU infrastructure, serving runtime (SGLang/vLLM), caching, and routing — illustrating the standard managed-vs-custom tradeoff for large open-weight model deployment.
- At launch, Beam is only available in two AWS regions (US East N. Virginia and Ohio), indicating this is an early-stage rollout rather than broad general availability.
- The post frames "open intelligence" as Reflection AI's stated mission — open weights, published research, and open-source software across its full stack (models, infrastructure, applications) — positioning Beam as part of a broader open-model strategy rather than a one-off release.
- Practical deployment at this scale requires explicit planning for GPU quota/capacity, checkpoint storage, sharding, parallelism, and KV cache sizing — underscoring that deploying frontier-scale open-weight models remains a nontrivial infrastructure undertaking even with managed tooling.

---
title: Deploy decision models with llama.cpp on Amazon SageMaker AI
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/deploy-decision-models-with-llama-cpp-on-amazon-sagemaker-ai/
author: Jyothirmai Kottu
date_published: '2026-10-12'
date_captured: '2026-10-13'
ingest_method: feed
model: claude-sonnet-5
---

# Deploy decision models with llama.cpp on Amazon SageMaker AI

## Insights

- AWS introduces "decision models" as a distinct category from chat/generative models: instead of generating free-form text, they return calibrated probabilities over a fixed, caller-defined set of options (e.g., routing a ticket to one of several queues) — framed as useful for routing, agent action selection, policy checks, and incident prioritization.
- The architecture separates two paths from one packaged model: a standard OpenAI-compatible chat-completions endpoint (llama.cpp DLC, no custom container needed) versus a "SemIf" adapter (formerly OpenJev) that reads final-position logits directly rather than decoding tokens, requiring a custom child image built via CodeBuild/ECR.
- Benchmarked on 231 JevBench tasks with a quantized Qwen3.5-4B model: GPU (ml.g6e.xlarge) was 4.9x faster at p50 and 32.2x faster at p95 latency than CPU (ml.c6i.8xlarge), while accuracy was nearly identical (~77.5-77.9%) — positioning GPU for interactive/latency-sensitive decisions and CPU for offline/batch use.
- Smaller models reduced latency but sacrificed significant accuracy (2B model: 66.7%, 0.8B model: 58.4%), leading AWS to default to the 4B model as "quality-first" despite higher latency/cost.
- Explicit guardrails stated: model decisions/probabilities should not be treated as "operational confidence" or substitute for authorization; deterministic business rules and auth should stay outside the model, with application-level thresholds and fallbacks layered on top.
- The adapter architecture reveals an infrastructure constraint: SemIf scoring is serialized around a single stateful llama.cpp context (not parallelized within one container), so concurrency requires scaling out endpoint instances rather than assuming in-container parallelism; the adapter returns retryable HTTP 503s instead of queuing unboundedly.
- Positions this as part of a broader emerging category of "decision model" products/specs beyond AWS's own offering — naming Jev, Kev, and Strands Decider 2B as comparable or compatible implementations.

## Quote

> Removing answer-token generation doesn't remove model inference.

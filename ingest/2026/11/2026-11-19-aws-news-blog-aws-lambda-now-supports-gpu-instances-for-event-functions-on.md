---
title: AWS Lambda now supports GPU instances for Event Functions on Lambda Managed
  Instances
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/aws-lambda-now-supports-gpu-instances-for-event-functions-on-lambda-managed-instances/
author: Daniel Abib
date_published: '2026-11-18'
date_captured: '2026-11-19'
ingest_method: feed
model: claude-sonnet-5
---

# AWS Lambda now supports GPU instances for Event Functions on Lambda Managed Instances

## Insights

- AWS Lambda now runs GPU-backed "Event Functions" on Lambda Managed Instances (EC2 G-series: G4dn, G5, G6, G6f, Gr6, Gr6f, G6e), deployed as container (OCI) images, with Lambda handling drivers, CUDA, provisioning, and scaling — positioned against both self-managed GPU infra and third-party serverless GPU services that sit outside a customer's AWS environment/identity/networking.
- Explicitly targeted at inference (not training) and at custom/small-to-mid-size models rather than large foundation models already served via Bedrock — use cases named include computer vision, speech-to-text/TTS, recommendation, document analysis, media transcoding, 3D rendering/diffusion, and scientific/financial simulation.
- Core economic pitch is utilization: GPUs are expensive and typically under-saturated by single workloads, so Lambda packs multiple concurrent invocations onto one GPU/execution environment (configurable concurrency, default 4) and consolidates functions across instances to keep GPUs busier.
- Demonstrated workflow: a curated vLLM base image (CUDA, PyTorch, Transformers pre-baked) can serve a Hugging Face model (Qwen2.5-1.5B-Instruct) via an OpenAI-compatible endpoint with a one-line Dockerfile and zero custom inference code — author reports ~10 minutes from model ID to live endpoint, mostly unattended provisioning/warmup.
- Functions integrate with existing Lambda primitives: 200+ event sources (S3, SQS, API Gateway, EventBridge), durable functions for multi-step orchestration with checkpointing, and MicroVMs for sandboxed agentic tool-use that calls out to the GPU function for inference.
- Limits/config specifics: up to 32GB container images (10GB/file), up to 32GB ephemeral storage, 2,048–32,768MB memory, 3–48GB accelerator memory, up to 48 concurrent requests per execution environment, up to 15,000 vCPUs per capacity provider, and up to 90-minute timeouts for async/event-source-mapping invocations.
- Pricing: standard EC2 On-Demand G-series rates (Savings Plans/Reserved Instances eligible) plus a 9.75% management fee on GPU instances, plus the standard $0.20/million-request Lambda fee.

## Quote

> Customers keep asking to run GPU workloads with the simplicity of serverless.

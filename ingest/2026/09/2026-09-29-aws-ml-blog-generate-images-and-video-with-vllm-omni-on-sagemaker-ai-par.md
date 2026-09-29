---
title: Generate images and video with vLLM-Omni on SageMaker AI – Part 2
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/generate-images-and-video-with-vllm-omni-on-sagemaker-ai-part-2/
author: Yadan Wei
date_published: '2026-09-28'
date_captured: '2026-09-29'
ingest_method: feed
model: claude-sonnet-5
---

# Generate images and video with vLLM-Omni on SageMaker AI – Part 2

## Insights

- AWS packages "AWS vLLM-Omni" as a Deep Learning Container (DLC) that extends vLLM beyond text to multimodal generation (image, video, audio) via OpenAI-compatible APIs, and can serve multiple model types from the same container image, only swapping the `SM_VLLM_MODEL` env variable.
- The architecture pattern splits inference by latency profile: real-time SageMaker endpoints for fast models (FLUX.2-klein-4B image generation, ~4.7s response) and SageMaker Asynchronous Inference (S3-backed, poll-based) for slower models (Wan2.1-VACE-1.3B video generation, ~9s+ model latency).
- The workflow chains two independently deployed models: text prompt → image (FLUX.2-klein) → image-conditioned video (Wan VACE), passing generated images through resizing/JPEG-encoding to fit multipart payload size limits.
- Reported operational timings from one validation run: image endpoint reached InService in 9m30s, video endpoint in 8m40s — framed explicitly as "reproduction checkpoints, not performance benchmarks," a notable hedge against treating vendor numbers as guaranteed performance.
- AWS frames instance-type selection as workload-dependent (fixed GPU instance types used here, e.g., ml.g6.xlarge/g6e.xlarge) and flags "capacity-aware instance pools" as an available but unvalidated optimization for the real-time endpoint.
- Positions this as part of a broader series demonstrating a shared serving runtime (vLLM-Omni DLC) supporting varied generative media workloads (speech in Part 1, image/video here) under one container strategy — a signal of AWS consolidating multimodal inference tooling under a common DLC/SageMaker abstraction.

## Quote

> These single-run values are reproduction checkpoints, not performance benchmarks.

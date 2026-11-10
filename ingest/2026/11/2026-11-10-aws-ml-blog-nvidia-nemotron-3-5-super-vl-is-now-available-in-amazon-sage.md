---
title: NVIDIA Nemotron 3.5 Super VL is now available in Amazon SageMaker JumpStart
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-3-5-super-vl-is-now-available-in-amazon-sagemaker-jumpstart/
author: Venu Kanamatareddy
date_published: '2026-11-09'
date_captured: '2026-11-10'
ingest_method: feed
model: claude-sonnet-5
---

# NVIDIA Nemotron 3.5 Super VL is now available in Amazon SageMaker JumpStart

## Insights

- NVIDIA Nemotron 3.5 Super VL is a 120B-parameter vision-language model (12B active, MoE with 512 routed experts/22 active, Mamba-2 hybrid backbone) now deployable via Amazon SageMaker JumpStart, targeting document intelligence, GUI/computer-use agents, video QA, and multimodal agentic workloads.
- Two deployment variants trade off cost/precision: NVFP4 (quantized, ~75GB, runs on smaller G7/Blackwell GPU instances) vs BF16 (full precision, ~249GB, requires 8x H200 GPUs) — NVFP4 matches or nearly matches BF16 on benchmarks despite being far cheaper to serve.
- Built-in speculative decoding (MTP head) exists in the checkpoint but is not enabled in AWS's default JumpStart serving config — a reminder that vendor-published benchmarks reflect specific, sometimes conservative, deployment choices rather than peak capability.
- Practical constraints are significant for document/agentic use: the model takes images not PDFs (requires pre-rendering), one image or video per request only, and context budgets vary sharply by serving profile (520 to 15,600 tokens) — real limits for multi-page document workflows.
- Performance claims are modest and concrete rather than superlative: ~63-64 tokens/sec on NVFP4/G7 instances vs ~141 tokens/sec on BF16/H200, with time-to-first-token around 0.5 sec for short prompts but jumping to 12.6 sec for long (10K token) prompts.
- No LoRA adapter serving is supported on the JumpStart endpoint, meaning customization requires downloading full BF16 weights for separate fine-tuning/distillation rather than lightweight adaptation at inference time.

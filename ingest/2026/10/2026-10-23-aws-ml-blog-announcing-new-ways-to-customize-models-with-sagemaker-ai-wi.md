---
title: Announcing new ways to customize models with SageMaker AI, without managing
  GPUs
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/announcing-new-ways-to-customize-models-with-sagemaker-ai-without-managing-gpus/
author: Pooja Karadgi
date_published: '2026-10-22'
date_captured: '2026-10-23'
ingest_method: feed
model: claude-sonnet-5
---

# Announcing new ways to customize models with SageMaker AI, without managing GPUs

## Insights

- AWS launched general availability of "training sessions" within SageMaker AI serverless model customization, letting users write custom post-training loops (loss functions, reward signals) while AWS manages GPU allocation, distributed execution, fault recovery, and checkpoints.
- The core technical shift targeted is multi-turn reinforcement learning for agents (e.g., travel booking, support triage, multi-step research), where training requires coordinating separate compute for training, inference/generation, and scoring across stages.
- Supports multiple post-training techniques (SFT, DPO, RLVR, RLAIF, multi-turn RL) and model update strategies (LoRA or full fine-tuning), with ability to chain techniques via "continuous customization."
- Pricing model is token-based consumption during SageMaker-processed compute; billing pauses while the customer's own reward function scores results, and there's no capacity reservation requirement.
- Positioned as retaining customer data/model sovereignty: data and checkpoints stay in the customer's own S3 buckets/region, with customer-controlled IAM roles, KMS keys, and VPC config; AWS states it doesn't use customer data/weights to train other models.
- Initial model support limited to four specific open-weight models (gpt-oss-20b, gemma-4-31B-it, Qwen3.6-27B, Qwen3.8-27B); customer testimonials cite use cases in healthcare claims triage and knowledge-graph-based agentic tool calling.

## Quote

> Checkpoint-and-resume was a standout: resuming from an exact step was completely reliable. — Nitin Wagh, CEO, Karini AI

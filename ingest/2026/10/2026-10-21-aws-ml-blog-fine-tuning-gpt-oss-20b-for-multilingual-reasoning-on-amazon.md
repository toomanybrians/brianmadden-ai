---
title: Fine-tuning GPT-OSS-20B for multilingual reasoning on Amazon SageMaker HyperPod
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/fine-tuning-gpt-oss-20b-for-multilingual-reasoning-on-amazon-sagemaker-hyperpod/
author: Mijanur Palash
date_published: '2026-10-20'
date_captured: '2026-10-21'
ingest_method: feed
model: claude-sonnet-5
---

# Fine-tuning GPT-OSS-20B for multilingual reasoning on Amazon SageMaker HyperPod

## Insights

- Base GPT-OSS-20B, an open-weight reasoning model, defaults to English chain-of-thought regardless of instructed language — on a 50-case multilingual test it hit only 22% reasoning-language accuracy, nearly all from English examples (French, Spanish, Italian all 0%).
- The post frames SFT and GRPO as solving different problems: SFT teaches a behavior the model has zero probability of producing; GRPO only amplifies behaviors the model already sometimes gets right. This explains why GRPO can't fix a 0%-capability gap.
- SFT alone took reasoning-language accuracy from 22% to 100%, but answer-language (the final response, not just the reasoning trace) lagged at 62% — the harder problem since short answers carry a stronger English bias.
- GRPO applied on top of the SFT checkpoint pushed answer-language from 62% to 70% (+8 points) without degrading reasoning-language, confirming it works as a refinement layer, not a behavior-teaching one.
- A controlled Qwen2.5-7B experiment reinforced the pattern: GRPO added +6 points on a task with headroom (multilingual reasoning) but zero gain on GSM8K, where the base model was already at peak accuracy (90.5%) — when sampled response groups are mostly all-correct, GRPO's group-relative advantage signal collapses.
- Practical stack details: training run on SageMaker HyperPod with EKS orchestration, LoRA adapters (r=8/α=16, ~0.068% trainable params) for both SFT and GRPO, FSx for Lustre storage, EFA networking, and veRL/Ray/vLLM for the GRPO control experiments.

## Quote

> SFT does most of the work, GRPO refines when there is headroom to refine, and matching the technique to the capability gap is what decides the outcome.

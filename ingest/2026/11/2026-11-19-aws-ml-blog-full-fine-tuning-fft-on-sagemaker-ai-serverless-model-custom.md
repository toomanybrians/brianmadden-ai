---
title: Full Fine-Tuning (FFT) on SageMaker AI Serverless Model Customization
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/full-fine-tuning-fft-on-sagemaker-ai-serverless-model-customization/
author: Sandeep Raveesh-Babu
date_published: '2026-11-19'
date_captured: '2026-11-19'
ingest_method: feed
model: claude-sonnet-5
---

# Full Fine-Tuning (FFT) on SageMaker AI Serverless Model Customization

## Insights

- AWS now supports Full Fine-Tuning (FFT) alongside LoRA on SageMaker AI Serverless Model Customization, removing the need to provision GPUs or manage training infrastructure for either method.
- AWS's internal benchmarking (Qwen3-4B on a 110K-example code generation dataset) found LoRA hits an accuracy plateau as datasets scale past tens of thousands of examples — a limit attributed to the low-rank update's rank deficiency, not just parameter count.
- FFT reportedly reached 90% semantic correctness (LLM-as-Judge) at 100K+ training examples and showed gains across BLEU/ROUGE metrics, but the post notes FFT is "extremely sensitive" to hyperparameters and is not universally superior.
- Catastrophic forgetting is flagged as the central risk of FFT: aggressive learning rates (≥5e-5) caused MMLU accuracy to collapse to 3.6% and MATH scores to 2–3%, and even careful FFT configs still underperformed the base model on MATH exact-match.
- Counterpoint to the headline claim: LoRA slightly beat FFT on LLM-as-Judge subjective quality (81.5% vs 79.5%) in their own tests, suggesting parameter-efficient tuning still has an edge for some quality dimensions.
- AWS frames hyperparameter tuning (learning rate, epoch count via MMLU "forgetting" tracking, batch size) as central to making FFT viable, implying the serverless offering still requires significant tuning expertise despite removing infra management.

## Quote

> FFT isn't universally superior to LoRA, and its effectiveness is extremely sensitive to hyperparameter choices.

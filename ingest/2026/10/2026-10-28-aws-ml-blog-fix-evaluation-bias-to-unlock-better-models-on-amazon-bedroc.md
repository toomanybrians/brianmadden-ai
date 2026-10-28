---
title: Fix evaluation bias to unlock better models on Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/fix-evaluation-bias-to-unlock-better-models-on-amazon-bedrock/
author: Khaled Thabit
date_published: '2026-10-27'
date_captured: '2026-10-28'
ingest_method: feed
model: claude-sonnet-5
---

# Fix evaluation bias to unlock better models on Amazon Bedrock

## Insights

- Property Finder's vision AI evaluation dataset was 96.8% derived directly from the incumbent model's own predictions rather than independent human labels, creating a circular evaluation that structurally disadvantaged any alternative model before testing began.
- Hidden errors in the biased labels included hallucinated brand names in watermark text, forced single-label classification of images with multiple valid room types, and annotator-introduced categories not in the original spec.
- Fixing the evaluation required fresh, independent expert annotation (356 hand-labeled images) with no access to prior model outputs, plus a shift from single-label to multi-label classification to avoid penalizing models for legitimate secondary attributes (e.g., a hallway showing a bedroom through a doorway).
- Prompt optimization was treated as a reinforcement-learning-like loop (27 iterations) — Micro F1 as reward signal, error analysis as "gradient" — combining manual AI-assisted refinement with automated optimization (MIPROv2/DSPy), referencing GEPA-style evolutionary prompt mutation.
- With unbiased evaluation and tuned prompts, Meta's Llama 4 Maverick 17B Instruct beat AWS's own "proprietary model A" baseline (Micro F1 0.80 vs 0.56), at an estimated 86% lower cost per 1,000 images and 40-60% lower inference latency.
- Some optimization approaches failed outright: splitting attributes into separate API calls (2-bucket approach) gave no accuracy gain and actually broke boxed-image detection because watermark context was needed in the same prompt to distinguish overlays from borders.
- The piece frames model flexibility (multi-model access via Amazon Bedrock without re-platforming) as a prerequisite that let Property Finder discover and act on the evaluation bias in the first place.

## Quote

> A model comparison loses validity when the answer key was written by the model you are trying to replace.

---
title: How Amazon Marketplace evaluates content quality with Amazon SageMaker AI
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-amazon-marketplace-evaluates-content-quality-with-amazon-sagemaker-ai/
author: James Kim
date_published: '2026-11-05'
date_captured: '2026-11-06'
ingest_method: feed
model: claude-sonnet-5
---

# How Amazon Marketplace evaluates content quality with Amazon SageMaker AI

## Insights

- The system evaluates product pages holistically rather than asset-by-asset: it renders the full product detail page (text, images, layout) as a single snapshot and scores it with a vision-language model, since per-asset checks miss mismatches that only appear when elements are viewed together (e.g., bullet copy describing one product variant next to a photo of another).
- Rather than fine-tuning the VLM itself, the team keeps it frozen and trains a lightweight CatBoost classifier on its structured outputs (scores + confidence) against expert-labeled data — a deliberate tradeoff to avoid GPU fine-tuning costs and overfitting risk on a small (~5,478-example) labeled dataset, and to keep recalibration a cheap CPU-only job.
- Fusing VLM semantic/visual scores with OCR-derived readability signals (text density, character density, spacing) outperformed either signal alone: VLM-only reached 0.89 accuracy/0.90 F1, OCR-only 0.82/0.83, but the fused model hit 0.94/0.95 — OCR catches fine-grained readability issues (crowded text, poor spacing) that VLMs tend to misjudge, sometimes rewarding dense text as "thorough."
- SHAP values are used to decompose each quality decision into per-dimension contributions, which are then fed to an LLM to generate prioritized, specific improvement recommendations for sellers — described as closing a feedback loop, not just a transparency feature. Measured result: sellers who revised content based on these recommendations improved their quality scores by an average of 1.4 points on a 10-point scale.
- A downstream diffusion model uses the quality scores and SHAP-flagged weak points to directly generate replacement visual assets for sellers, rather than leaving them to manually act on text recommendations.
- Business validation claimed: a worldwide A/B test adjusting visibility of low-quality A+ Content based on the model's scores produced a "statistically meaningful" improvement in Ordered Product Sales — though no magnitude is given, and the oft-cited "8-20% sales boost from quality content" figure is an unsupported framing claim rather than a result of this system.

## Quote

> Explainability is therefore not merely an auxiliary capability for understanding the model.

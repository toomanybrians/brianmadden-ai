---
title: Fleet-wide computer vision lifecycle at the edge with SageMaker SDK v3
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/fleet-wide-computer-vision-lifecycle-at-the-edge-with-sagemaker-sdk-v3/
author: Kiowa Jackson
date_published: '2026-10-26'
date_captured: '2026-10-27'
ingest_method: feed
model: claude-sonnet-5
---

# Fleet-wide computer vision lifecycle at the edge with SageMaker SDK v3

## Insights

- Fleet-wide computer vision deployments break the "one model" assumption: a single model trained on pooled footage underperforms per-camera fine-tuned models, because each camera sees different angles, glare, and lighting. The real engineering problem becomes managing lifecycle (train/evaluate/version/ship) for thousands of models without a human reviewing each one.
- SageMaker SDK v3 introduces undocumented breaking behavior: it validates the pipeline's execution IAM role against live AWS at synthesis time rather than runtime, which forces infrastructure-as-code deployments into a two-phase process (create role first, then build the pipeline referencing it).
- Quality gates are run against the exported inference artifact (ONNX) rather than the in-memory trained model, closing a gap where an export bug could let a broken model pass evaluation.
- For imbalanced defect data (e.g., 90% "good" parts), plain accuracy is described as meaningless; the design argues for gating on balanced accuracy plus minority-class recall together, since either metric alone can mask a model that fails to catch defects.
- Edge compilation (via SageMaker Neo) is placed inside the pipeline before model registration, so a model can only become "Approved" in the registry if it has successfully compiled for the target edge hardware — the registry can't advertise a model devices can't actually run.
- Scaling fleet training is bounded by account-level concurrency quotas; the sample uses a DynamoDB-based atomic semaphore (not a read-then-write check) to safely pace how many pipeline executions run simultaneously.
- The architecture is explicitly positioned as a harder, more customized alternative to managed options like Amazon Lookout for Vision, intended specifically for per-camera, fleet-scale constraints that managed services don't address.

## Quote

> The artifact you gate is the artifact you ship, so an export problem can never slip a broken model past a healthy-looking training run.

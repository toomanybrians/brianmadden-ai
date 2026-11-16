---
title: Production MLOps at GS Caltex with Amazon SageMaker Canvas, part 1
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/production-mlops-at-gs-caltex-with-amazon-sagemaker-canvas-part-1/
author: WonGu Rho
date_published: '2026-11-13'
date_captured: '2026-11-16'
ingest_method: feed
model: claude-sonnet-5
---

# Production MLOps at GS Caltex with Amazon SageMaker Canvas, part 1

## Insights

- GS Caltex split MLOps work by role: process engineers build/validate models in SageMaker Canvas (no-code) using domain knowledge, while ML engineers handle deployment, pipeline configuration, and scheduling — a deliberate division of labor rather than full automation of one role away.
- The core technical problem was the "last mile" handoff from a validated no-code model to a production pipeline (setting data paths, reusing preprocessing logic, wiring inference jobs) — this integration work, not model-building itself, was the bottleneck.
- Automating that handoff cut deployment time from about a week to a few hours, and the same reusable pattern lets ML engineers skip rebuilding integration work for each new model.
- The company uses scheduled batch inference (every 30 minutes via EventBridge-triggered SageMaker Pipelines) rather than always-on real-time endpoints, which it reports meaningfully lowered inference costs — a specific architecture tradeoff (batch vs. real-time) with cost implications documented in detail.
- Notable organizational effect: after seeing their models running in production, process engineers started proposing new applications in other processes — suggesting the faster deployment loop changed behavior/incentives, not just technical throughput.
- Piece includes substantial engineering caveats (train/inference schema mismatches, placeholder target columns, row-order integrity, overlapping scheduled executions) — signals this is a real production system with nontrivial operational gotchas, not a clean demo.

## Quote

> ML engineers now deploy models within a few hours, compared with about a week before.

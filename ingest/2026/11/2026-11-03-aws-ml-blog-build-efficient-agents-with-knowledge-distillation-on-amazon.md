---
title: Build efficient agents with knowledge distillation on Amazon SageMaker AI
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-efficient-agents-with-knowledge-distillation-on-amazon-sagemaker-ai/
author: Giuseppe Zappia
date_published: '2026-11-02'
date_captured: '2026-11-03'
ingest_method: feed
model: claude-sonnet-5
---

# Build efficient agents with knowledge distillation on Amazon SageMaker AI

## Insights

- Sequence-level knowledge distillation (SeqKD) fine-tunes a small "student" model on a large "teacher" model's text outputs alone — no teacher logits or weights needed — making it viable even for closed, API-only frontier models.
- In AWS's shopping-agent test case, a distilled 4B-parameter model (Qwen3.5-4B) nearly matched a ~40B teacher model's task success rate (0.541 vs ~0.51–0.54 average), and matched a "medium-sized frontier model" benchmark too — on a task-specific benchmark, with caveats about run-to-run variance.
- Preserving the teacher's reasoning traces (not just its tool-call actions) in training data accounted for roughly 13 of the ~24 points of improvement over the untrained base model — stripping reasoning and keeping only actions produced a markedly weaker student.
- Distillation has a "capacity wall": it transfers a distribution the student can already represent, not raw capability — if the task is too hard for the student's size, it mimics the teacher's format (well-formed reasoning/tool calls) without actually solving the task.
- The economic case rests on converting variable per-token API costs (billed per step, every task) into a fixed hourly compute cost for a self-hosted smaller model — favorable at scale, but AWS doesn't publish concrete cost/latency comparisons, noting it depends on traffic patterns.
- Distillation causes a measurable but modest drop in general instruction-following ability (IFEval scores fell ~6-8 points) — framed as an expected/acceptable tradeoff for task specialization, with a larger drop flagged as a warning sign of over-narrowing.
- SeqKD is positioned as a cost-effective "first stage," not a complete solution — it plateaus on the hardest problems where agents must recover from their own compounding errors, which the piece says typically requires a follow-up on-policy training stage.

## Quote

> SeqKD is a strong first step with real limits.

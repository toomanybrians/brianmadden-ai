---
title: 'Building Reasoning Models from the Ground Up: A Full Video Course'
source: Ahead of AI
source_id: ahead-of-ai
source_url: https://magazine.sebastianraschka.com/p/building-reasoning-models
author: Sebastian Raschka, PhD
date_published: '2026-10-24'
date_captured: '2026-10-26'
ingest_method: feed
model: claude-sonnet-5
---

# Building Reasoning Models from the Ground Up: A Full Video Course

## Insights

- Defines a layered relationship between conventional LLMs, reasoning models, and agents: a reasoning model is an LLM with added post-training via reinforcement learning with verifiable rewards (RLVR) plus optional inference-scaling techniques, making it better at harder problems.
- Frames reasoning models as the "engine" inside an "agent harness" — the harness being the software/tooling layer that handles context management and tool access, distinct from the model itself.
- Notes that reasoning capabilities were classically developed for math and code but can generalize to other problem domains.
- States that almost all current-generation LLMs are now reasoning models or offer a reasoning mode, implying this has become the default rather than a niche capability.
- Describes two core training paths for building reasoning ability: reinforcement learning with verifiable rewards (via GRPO) and distillation from a stronger teacher model (e.g., using outputs from DeepSeek R1), each with distinct tradeoffs (training stability/reward hacking vs. supervised learning from teacher-generated data).
- Covers inference-time scaling methods separate from training — sampling/self-consistency (majority voting across diverse generations) and scoring/self-refinement (critique-and-revise loops) — as ways to improve output quality without changing model weights.

## Quote

> A reasoning model then functions as the engine inside an agent harness... to tackle even more challenging problems.

---
title: Controlling Reasoning Effort in LLMs
source: Ahead of AI
source_id: ahead-of-ai
source_url: https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms
author: Sebastian Raschka, PhD
date_published: '2026-07-18'
date_captured: '2026-08-11'
ingest_method: feed
model: claude-sonnet-5
---

# Controlling Reasoning Effort in LLMs

## Insights

- Reasoning models (o1, DeepSeek-R1, and now most frontier LLMs) work by outputting an intermediate "reasoning trace" before the final answer, trained via reinforcement learning with verifiable rewards (RLVR) rather than by training on the trace content itself.
- DeepSeek-R1's key contribution was showing reasoning behavior can emerge from pure RL on a base model (R1-Zero), without prior supervised fine-tuning — though the production R1 model still used a multi-stage SFT+RL pipeline.
- Newer model families (e.g., GPT-5.6) now ship with multiple discrete "reasoning effort" settings per model size, letting users trade off latency/cost against answer quality on a per-query basis.
- Beyond training-time scaling, inference-time scaling (e.g., self-consistency/majority voting, self-refinement) is a separate lever for boosting accuracy, and can be combined with reasoning-trained models for state-of-the-art results (e.g., DeepSeekMath-V2 on olympiad math).
- The article frames "reasoning" as a technical/behavioral property (longer step-by-step traces, self-correction "aha moments") rather than literal cognition — relevant framing for how enterprises should interpret marketing claims about AI "reasoning."

## Quote

> So yes, reasoning models are here to stay. They have become a standard part of modern model releases.

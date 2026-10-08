---
title: 'Agent Lightning v1.0: A 3,500-Line Lightweight Agentic RL Framework for Training
  Agents with Real Harnesses'
source: Microsoft Research Blog
source_id: microsoft-research-blog
source_url: https://www.microsoft.com/en-us/research/blog/agent-lightning-v1-0-a-3500-line-lightweight-agentic-rl-framework-for-training-agents-with-real-harnesses/
author: Zhiyuan He, Yuqing Yang
date_published: '2026-10-07'
date_captured: '2026-10-08'
ingest_method: feed
model: claude-sonnet-5
---

# Agent Lightning v1.0: A 3,500-Line Lightweight Agentic RL Framework for Training Agents with Real Harnesses

## Insights

- Microsoft Research Asia formalizes "Harnessed Agentic RL," a paradigm where the actual deployment agent harness (not a reimplemented version) participates directly in RL training, via an LLM proxy sitting between agent and model.
- This addresses a real gap in prior agentic RL systems (verl, AReaL, slime), which required rebuilding an agent's interaction loop inside the training framework — costly, and resulting in a trained agent that differs from what's actually deployed.
- Training on a real harness (rather than a reconstructed loop) creates specific technical problems: retokenization mismatches, how to compute advantage/baselines when one rollout splits into variable numbers of samples, loss normalization bias toward harnesses that produce more samples, and scheduling variable-length workloads onto fixed GPU resources.
- The resulting framework (Agent Lightning v1.0) is deliberately minimal — ~3,500 lines of code — built on three components (API gateway, rollout controller, customized trainer), and runs agents as standard Kubernetes jobs rather than relying on paid commercial sandbox services (e.g., Modal Sandbox, E2B), aimed at lowering cost and improving reproducibility.
- A "Collocated Async RL" scheduling approach lets rollout and model-update phases share the same GPU pool, reportedly achieving ~2x speedup over synchronous RL while using fewer GPUs than conventional async RL setups.
- In a coding-agent test (Qwen3.5-9B + mini-SWE-agent on SWE-bench Verified), RL training using only ~6,000 samples raised Pass@1 from 41.8% to 56.4%, a 14.6-point gain — illustrating that meaningful agent RL gains may not require large-scale compute or data.

## Quote

> whichever agent harness is used in deployment is the harness that takes part directly in reinforcement learning during training

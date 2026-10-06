---
title: 'New agent skill: Amazon SageMaker optimized generative AI inference for your
  coding agent'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/new-agent-skill-amazon-sagemaker-optimized-generative-ai-inference-for-your-coding-agent/
author: Mona Mona
date_published: '2026-10-05'
date_captured: '2026-10-06'
ingest_method: feed
model: claude-sonnet-5
---

# New agent skill: Amazon SageMaker optimized generative AI inference for your coding agent

## Insights

- AWS released "aws-ai-ml," a skill that plugs into MCP-compatible coding agents (Kiro, Claude Code, Codex) to give them expertise in SageMaker AI inference optimization — benchmarking endpoints, recommending instance types, and comparing performance runs.
- The design philosophy emphasizes transparency and control: the agent generates inspectable, executable SageMaker Python SDK v3 code rather than taking opaque action, and explicitly confirms before running benchmarks that drive real traffic to live endpoints.
- The tool handles multiple model-sourcing paths (S3-hosted custom/fine-tuned models, SageMaker JumpStart catalog models, and gated/ungated Hugging Face Hub models), including surfacing license terms and handling token-based gated model access.
- Benchmarking produces concrete measured metrics (throughput, p50/p99 latency, time-to-first-token, concurrency) from real load tests rather than estimates, and the agent can diff two benchmark runs to quantify improvement or regression.
- A worked example shows Qwen3-8B (4x A10G GPUs) outperforming Qwen3-1.7B (single L4 GPU) by ~44-47% on throughput/latency, attributed mostly to added compute rather than model architecture — illustrating how the tool contextualizes hardware differences in comparisons.
- Positioned as an agentic layer over existing SageMaker infrastructure complexity (instance families, serving containers, deployment modes), aimed at engineers who know their performance/cost targets but not the underlying infra options to hit them.

## Quote

> Every step is visible in real time and expressed as code you can read and question. Nothing happens behind an opaque UI.

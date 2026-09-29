---
title: 'AWS Weekly Roundup: GPT-6 Sol and Luna, Claude Opus 5.5 on Amazon Bedrock,
  Strands harness, and more (September 28, 2026)'
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-gpt-6-sol-and-luna-claude-opus-5-5-on-amazon-bedrock-strands-harness-and-more-september-28-2026/
author: Daniel Abib
date_published: '2026-09-28'
date_captured: '2026-09-29'
ingest_method: feed
model: claude-sonnet-5
---

# AWS Weekly Roundup: GPT-6 Sol and Luna, Claude Opus 5.5 on Amazon Bedrock, Strands harness, and more (September 28, 2026)

## Insights

- AWS added GPT-6 Sol, GPT-6 Luna (OpenAI), and Claude Opus 5.5 (Anthropic, first of the 5.5 family) to Bedrock, framed explicitly around model choice for cost/latency/task-fit rather than always using the largest model; Sol targets dev/ops work, Luna targets high-volume repeatable tasks, both priced lower than GPT-5.6 predecessors, and Opus 5.5 is tuned for agentic coding/long-running tasks with better token efficiency than Opus 5.
- Amazon CloudWatch Omni launches as a unified observability layer for applications and AI agents together, built on OpenTelemetry, with auto-discovery, dependency mapping, and integration of an AWS DevOps Agent into investigation/root-cause sessions.
- A referenced companion piece ("Wrong, not broken" by Matt Wood) argues correctness in AI systems now needs to be measured at the level of the entire run, not just individual outputs — a framing signal about how AWS is thinking about agent reliability.
- SageMaker HyperPod Inference Gateway adds GPU-aware, signal-based routing (KV cache utilization, queue depth, prefix cache hits, predicted latency) for LLM inference instead of round-robin, claiming up to 82% lower first-token latency in bursty/mixed-hardware scenarios; compatible with any OpenAI-compatible model server (vLLM, SGLang).
- Strands harness (Apache 2.0) is a general-purpose, model-agnostic agent harness (Bedrock, Anthropic, OpenAI, Google, local Ollama) with built-in prompt caching, context truncation/compaction, and persistent memory across runs; team claims ~28% lower cost than comparable harnesses at equal accuracy.
- AWS's "Reimagine" report, based on nine months of interviews with 154 leaders across 27 countries, concludes that once organizations can build AI systems quickly, the real bottleneck shifts to decision-making, funding, and governance of the work — including candid admission of where AI hasn't worked internally at Amazon.

## Quote

> Once building gets fast, the bottleneck moves to deciding, funding, and governing the work.

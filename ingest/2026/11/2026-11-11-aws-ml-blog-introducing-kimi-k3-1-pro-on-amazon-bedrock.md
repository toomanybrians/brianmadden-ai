---
title: Introducing Kimi K3.1 Pro on Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-kimi-k3-1-pro-on-amazon-bedrock/
author: Aris Tsakpinis
date_published: '2026-11-11'
date_captured: '2026-11-11'
ingest_method: feed
model: claude-sonnet-5
---

# Introducing Kimi K3.1 Pro on Amazon Bedrock

## Insights

- AWS has added Kimi K3.1 Pro Highspeed (Moonshot AI) to Bedrock — a post-trained version of Kimi K3 on the same 3T-class open-weight architecture with a 1M-token context window, using substantially more post-training compute aimed at long-horizon agentic tasks, reduced factual errors, and professional/coding use cases (financial modeling, office docs, game engine/3D/CAD scripting).
- Moonshot AI claims 2–3x the output-token generation speed of the prior Kimi K3.1 Pro — positioned as mattering specifically for agentic coding loops where many sequential model calls (read, plan, edit, test, fix) compound latency.
- Drop-in compatibility is a key design point: same endpoint/APIs/features as Kimi K3, accessible via OpenAI-compatible Chat Completions/Responses APIs and Bedrock Converse/Invoke APIs, with cross-Region inference profiles (global, US-only, India-only) for routing and data-residency needs.
- Security/data-handling posture is emphasized as unchanged from existing Bedrock models: processing stays within AWS's boundary, no data sharing with or training by Moonshot AI, zero data retention, and zero operator access to prompts/completions.
- Cost/performance levers highlighted: a Flex pricing tier at half the Standard price for latency-tolerant workloads (evals, summarization, background agent tasks), and explicit prompt caching (via breakpoints after 256+ stable tokens) to cut latency/cost on repeated agentic/coding context — though caching isn't supported on the Converse API.
- Configurable "reasoning effort" (low/high/max) is a built-in control for trading off latency/output tokens against reasoning depth, surfaced directly in tools like the OpenCode terminal coding agent via Bedrock API keys.

## Quote

> Output speed matters most in agentic coding.

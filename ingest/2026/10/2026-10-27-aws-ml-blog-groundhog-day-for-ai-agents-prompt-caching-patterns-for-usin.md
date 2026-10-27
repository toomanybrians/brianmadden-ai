---
title: 'Groundhog Day for AI agents: Prompt caching patterns for using OpenAI models
  on Amazon Bedrock'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/groundhog-day-for-ai-agents-prompt-caching-patterns-for-using-openai-models-on-amazon-bedrock/
author: Claudio Mazzoni
date_published: '2026-10-26'
date_captured: '2026-10-27'
ingest_method: feed
model: claude-sonnet-5
---

# Groundhog Day for AI agents: Prompt caching patterns for using OpenAI models on Amazon Bedrock

## Insights

- AI agents must resend their entire conversation history (tool definitions, instructions, prior tool calls/results) on every turn because LLMs have no memory between requests — costs compound as sessions grow longer.
- Prompt caching works by storing the "prefill" computation (key-value vectors) from a prior request and reusing it, so only new tokens need processing and billing on subsequent calls.
- Amazon Bedrock supports two caching modes for OpenAI models: implicit (Bedrock auto-selects cache boundaries as conversations grow) and explicit (developer manually marks cache breakpoints); AWS recommends combining both.
- Caching requires exact byte-for-byte stability in cached content — reordering tools, changing instructions, or inconsistent serialization invalidates the cache; a minimum prefix of 1,024 tokens is required, with a 30-minute minimum TTL refreshed on reuse.
- In vendor-reported test workloads, implicit caching cut input costs ~62% and explicit rolling breakpoints ~61% over a six-turn session; a separate modeled example showed cost dropping from $0.87 to $0.32 per session (64% reduction) — but cache writes cost 1.25x normal input rate, so savings depend on reuse patterns.
- For multi-agent setups, a shared context prefix can be "warmed" once and reused across parallel subagents/helpers to avoid redundant reprocessing; the post also flags that cached tools/system prompts pose a leak/exploit risk requiring governance.

## Quote

> AI agents live in a version of Groundhog Day.

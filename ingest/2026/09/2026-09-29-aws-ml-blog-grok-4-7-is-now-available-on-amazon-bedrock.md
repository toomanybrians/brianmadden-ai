---
title: Grok 4.7 is now available on Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/grok-4-7-is-now-available-on-amazon-bedrock/
author: Suheel Farooq
date_published: '2026-09-28'
date_captured: '2026-09-29'
ingest_method: feed
model: claude-sonnet-5
---

# Grok 4.7 is now available on Amazon Bedrock

## Insights

- Grok 4.7's training emphasized endurance over speed: a longer reinforcement learning run weighted toward tasks taking many hours, aimed at improving self-verification and effective use of its 500K token context window on long-running work.
- Independent evaluation from Artificial Analysis shows real gains (Intelligence Index 46 vs 44, Coding Agent Index 56 vs 47) but with a notable cost tradeoff — roughly double the output tokens per task compared to Grok 4.6, making reasoning-effort settings a meaningful cost/latency lever rather than a default to leave alone.
- xAI reports a lower hallucination rate on its Omniscience benchmark (29% vs 34% for 4.6) and frames the model's safety stack as balancing usefulness against refusal on dual-use domains like cybersecurity and biological work; it's opened invite-only red-team access to select cybersecurity partners.
- On Bedrock, the model is positioned for enterprise agentic use with operational guardrails: content filters/PII redaction via Bedrock Guardrails, structured JSON-schema outputs, invocation logging with reasoning-token counts for audit trails, and implicit prompt caching for repeated agent system prompts.
- Deployment offers a cost/control tradeoff between a cheaper "Global" cross-Region profile (routes anywhere, more variable latency) and a "US" geographic profile for data residency/latency-sensitive needs, plus three service tiers (standard/priority/flex) as further cost levers.
- xAI specifically calls out gains in professional knowledge-work domains — legal (Harvey Legal Agent Benchmark), clinical reasoning (HealthBench Professional), and document/presentation generation — positioning the model for lawyers, nurses, and financial analysts, not just coding.

## Quote

> The theme is endurance rather than raw speed: the model works longer on difficult tasks and checks its own work more carefully.

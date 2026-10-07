---
title: Building a context-aware AI assistant on AgentCore and OpenClaw
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-a-context-aware-ai-assistant-on-agentcore-and-openclaw/
author: Thiago Verney
date_published: '2026-10-06'
date_captured: '2026-10-07'
ingest_method: feed
model: claude-sonnet-5
---

# Building a context-aware AI assistant on AgentCore and OpenClaw

## Insights

- AWS demonstrates a persistent-memory AI assistant pattern (AgentCore memory + OpenClaw agent runtime) that separates short-term session events from asynchronously-extracted long-term records (USER_PREFERENCE, SEMANTIC, SUMMARIZATION strategies), addressing the "stateless assistant" problem where every conversation starts from zero.
- Memory extraction is asynchronous, not instant — facts mentioned in one session typically aren't retrievable until a later session, which the authors treat as an architectural constraint to design around rather than hide.
- Namespace design (per-user, keyed only by a channel-native ID) plus indexed metadata filtering (type/section/plants) is positioned as the key mechanism for precise retrieval and for making multi-tenant audit/deletion requests tractable.
- Design guidance explicitly frames memory as "an enhancement, never a dependency" — retrieval failures should degrade to a memoryless answer rather than block or fail the response, reflecting a reliability-over-completeness philosophy for agentic features.
- Cost/architecture notes: consumption-based serverless compute (AgentCore runtime) plus prompt caching (ordering stable persona/memory content before volatile user input) are presented as the mechanisms keeping a personalized, memory-laden agent at ~$5–9/month for light personal use, vs. ~$35/month for an always-on EC2 instance.
- The system explicitly routes tasks to different models by cost/complexity (cheap fast model for high-volume text, stronger multimodal model for vision), with memory context shown to materially improve vision-model accuracy (correctly identifying a plant species using stored inventory vs. a prior misidentification without it).

## Quote

> Users forgive a forgetful turn far more readily than a failed one.

---
title: AI Model Routing
source: Opinion AI
source_id: opinion-ai-2
source_url: https://opinionai.substack.com/p/ai-model-routing
author: Opinion AI
date_published: '2026-10-27'
date_captured: '2026-10-28'
ingest_method: feed
model: claude-sonnet-5
---

# AI Model Routing

## Insights

- Model pricing varies enormously for comparable capability — the piece cites GPT-6 Luna at $0.10 per million input tokens versus GPT-6 Astra at $10, a 100x gap within the same API, with similar spreads across Claude's Haiku/Sonnet/Opus tiers and other providers (Google, DeepSeek, Kimi).
- Model performance is task-dependent and not always predictable in advance — a smaller model can outperform expectations on some tasks while a larger model wastes time on simple ones, and which model "wins" often isn't clear until work is underway.
- The core proposed fix is "AI Model Routing": giving a system access to multiple models and using a router to assign each subtask to the most appropriate (and cost-efficient) model rather than running everything through one model.
- A single workflow often contains heterogeneous subtasks (e.g., locating a file, fixing a complex bug, verifying results) that plausibly warrant different model strengths rather than uniform treatment.
- Routing can be manual or automatic (letting the router decide), and the piece claims this is already achievable today using existing tools like Claude Code, OpenRouter, n8n, and AI agents without building custom infrastructure.

## Quote

> Why should all three jobs use the same model?

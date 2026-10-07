---
title: What AI gets wrong and what failure teaches us
source: Microsoft Research Blog
source_id: microsoft-research-blog
source_url: https://www.microsoft.com/en-us/research/podcast/what-ai-gets-wrong-and-what-failure-teaches-us/
author: Chad Atalla, Jennifer Neville
date_published: '2026-10-06'
date_captured: '2026-10-07'
ingest_method: feed
model: claude-sonnet-5
---

# What AI gets wrong and what failure teaches us

## Insights

- Standard benchmark evaluations are too simple relative to real-world use; Neville's team builds evaluations around multiturn behavior, collaborative environments, and long-horizon tasks to find where models actually break down in practice.
- Testing with single-turn benchmarks converted into simulated multiturn clarifications showed that model performance — high on single-turn versions — degrades significantly once a task is specified gradually across multiple turns, as real users often do.
- A practical workaround discussed: when a multiturn conversation gets a model confused, users should abandon the thread and resubmit a single, fully-specified prompt rather than continuing to patch the existing conversation.
- Research on long-horizon agentic workflows (e.g., repeated document edits) finds that errors compound over time — small mistakes left uncorrected increasingly confuse the agent as a task progresses, producing "surprising failures" distinct from familiar issues like hallucination.
- Failures often don't track human intuitions about task difficulty — what's hard for people to do isn't necessarily hard for transformers (and vice versa), because model difficulty is governed by what's computationally hard for the architecture and retrieval systems, not analogies to human cognition.
- Users are advised not to expect 100% reliability, to verify outputs, to retry/rephrase failed queries, and to give high-fidelity feedback (describing exactly what went wrong) since that detail — not just thumbs up/down — feeds into model improvement.
- Open research questions flagged: whether transformer architecture's known computational limits can be sufficiently offset by agentic "wrapper" harnesses and reasoning layers, or whether a fundamentally different architecture will be needed; and how to get multi-human, multi-AI teams to collaborate effectively in work environments.

## Quote

> You shouldn't expect them to be 100% successful across the board. You should be checking the answers that you get back.

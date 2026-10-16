---
title: Eval-Driven Development with Jev
source: Opinion AI
source_id: opinion-ai-2
source_url: https://opinionai.substack.com/p/eval-driven-development-with-jev
author: Opinion AI
date_published: '2026-10-13'
date_captured: '2026-10-13'
ingest_method: feed
model: claude-sonnet-5
---

# Eval-Driven Development with Jev

## Insights

- Running the identical prompt against the same model multiple times can produce noticeably different process and results, even when outputs individually look fine on the surface.
- Anthropic research cited: an agent with a 75% success rate on a single task drops to roughly 42% reliability when it must succeed three times in a row (assuming independent attempts) — compounding failure risk across multi-step tasks.
- As models (referenced: Claude Opus 5.5, GPT-6 Astra) gain the ability to use tools, operate across applications, edit files, build software, and make autonomous decisions, the central question shifts from raw intelligence to how much of the agent's work can be trusted.
- "Agent Evals" is framed as a lightweight method for testing AI agents, pinpointing failure points, and verifying whether a given change actually improves reliability.
- A new, low-cost model called "Jev" is mentioned as purpose-built for fast judgment calls, intended to help automate parts of the evaluation/checking process.
- The piece positions eval-driven testing as potentially more valuable right now than switching to a newer, more expensive model.

## Quote

> Suppose an agent has a 75% chance of completing a task correctly... if you need it to succeed three times in a row, the chance falls to about 42%.

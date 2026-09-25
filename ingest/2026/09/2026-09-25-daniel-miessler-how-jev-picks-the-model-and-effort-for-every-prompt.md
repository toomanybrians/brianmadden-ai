---
title: How Jev Picks the Model and Effort for Every Prompt
source: Daniel Miessler
source_id: daniel-miessler
source_url: https://danielmiessler.com/blog/glance-routes-model-and-effort?utm_source=rss&utm_medium=feed&utm_campaign=website
author: daniel@danielmiessler.com (Daniel Miessler)
date_published: '2026-09-25'
date_captured: '2026-09-25'
ingest_method: feed
model: claude-sonnet-5
---

# How Jev Picks the Model and Effort for Every Prompt

## Insights

- LifeOS's router ("Jev," via a judgment layer called "Glance") picks both a model and an effort level for every prompt in about a third of a second, using 18 small yes/no probability questions rather than one big classification call.
- A single large model asked to choose directly among lanes performed poorly (57–75% agreement with ground truth) compared to a learned combiner over many small questions (90.1%) — evidence for "ask many small questions instead of one big one" as a design principle for LLM-based decision systems.
- The team's first attempt at building a ground truth used synthetic, self-written test prompts and got misleadingly strong results (85%+); switching to real user prompts collapsed agreement to 42.6%, since real prompts are often short, context-dependent fragments ("y", "status?", "do it") that can't be routed from text alone.
- Three frontier models (from two different vendors) independently labeling the same 1,000 real prompts agreed on the correct routing only ~80% of the time (and only 51.8% before rule clarification), suggesting a meaningful ceiling on how deterministic "correct" routing decisions actually are — ambiguity in the rules themselves limited any system's achievable accuracy.
- The system uses a staged trust model for automation: new decision-making components start in "shadow" mode (logged but never acted on) until an agreement-rate baseline is established, and they automatically revert to shadow if the underlying model changes — a general pattern for safely rolling out autonomous judgment calls.
- Final performance: the learned router matched a 3-model majority-vote answer key on 90.1% of real prompts, versus 75.2% for a single fast model reading the same instructions directly, while running roughly 10x faster.

## Quote

> Three strong models reading the same rules and disagreeing that often meant the rules themselves were ambiguous.

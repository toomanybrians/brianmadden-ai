---
title: 'This is the best AI news #blackbox #AI'
source: Nate B. Jones
source_id: nate-b-jones
source_url: https://www.youtube.com/shorts/Xo1oF84Dhq8
author: AI News & Strategy Daily | Nate B Jones
date_published: '2026-10-23'
date_captured: '2026-10-23'
ingest_method: feed
model: claude-sonnet-5
content_basis: transcript
---

# This is the best AI news #blackbox #AI

## Fit with Brian's work

**Fit: partial.** The item's claim — that researchers can now read what individual neurons encode inside models — speaks directly to Brian's "weights as black box" thread and his unresolved worry about what's hidden in model internals that no prompt has surfaced.

- Directly engages the scratchpad note on weights-as-black-box: Brian's open question was "you don't know what's in there to begin with" (re: Chinese model censorship as evidence of hidden behavior in weights). This item claims a method exists to actually inspect what's in there — a potential answer to that exact gap, though only an early, unreviewed one.
- Connects to the chain-of-thought legibility thread (agent oversight note, Sept 4): Brian's concern there was that CoT legibility is dissolving as agents learn to fabricate reasoning traces, pushing oversight back toward "watch behavior, not thought." Mechanistic interpretability is a different, potentially more durable channel for inspecting cognition than CoT — worth noting as a counter-development to that thread's generally gloomy diagnosis.
- Not yet a strong fit with the enterprise-governance ladder (identity, session recording, harness-level enforcement) that dominates Brian's current safety thinking — this is lab-research-stage, not a deployable governance mechanism, so it's a future input to the thread rather than something that changes near-term strategy.

## Insights

- Researchers at Goodfire (an AI safety/alignment organization, per a speaker) examined individual "neurons" (units of computation, not biological) inside a vision model and found one that fired for both cats and cars — initially read as evidence AI reasoning is incoherent ("black box").
- Further investigation reportedly showed the neuron wasn't incoherent — it was tracking a shared pose/shape across both cat and car images, meaning the model organizes concepts at a different conceptual level than human categories, not randomly.
- The same technique was reportedly tested on a language model, not just the vision model, and an early audit estimated that around 90% of neurons in it have one identifiable, clear function.
- The work is described as early, not yet peer-reviewed, and still needing tooling to scale before it could be applied broadly across different AI systems.
- The speaker frames this as a potential "Rosetta Stone" for AI interpretability — a path to understanding why models make the decisions they do, which is pitched as a major safety implication if it holds up and scales.

## Quote

> "The AI is making sense. It's just operating at a different conceptual level." — Nate B. Jones

## Not captured

Nothing else of substance; the full transcript is a single explanatory thread on this one research finding.

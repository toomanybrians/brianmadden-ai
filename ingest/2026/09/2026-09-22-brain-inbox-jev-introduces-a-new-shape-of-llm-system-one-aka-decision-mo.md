---
title: Jev introduces a new shape of LLM - System One, aka Decision Models
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://simonw.substack.com/p/jev-introduces-a-new-shape-of-llm
author: '"Simon Willison from Simon Willison’s Newsletter" <simonw@substack.com>'
date_published: '2026-09-21'
date_captured: '2026-09-22'
ingest_method: email
model: claude-sonnet-5
---

# Jev introduces a new shape of LLM - System One, aka Decision Models

## Insights

- A new model category called "decision models" (TypeSafe AI's Jev, also framed as "System One" models) inverts the standard LLM shape: text goes in, but output is floating-point scores/probabilities (yes/no confidence, choice distributions, or scaled ratings) rather than generated text.
- Pricing flips standard LLM economics — Jev charges only for input tokens and gives output for free, undercutting even the cheapest text models, making high-volume classification tasks (spam detection, labeling, ranking, search reranking) extremely cheap to run at scale.
- The format raises sharper black-box/explainability concerns than regular LLMs: a bare number gives no visible reasoning at all, and bias risk is flagged as a real concern for high-stakes uses like ranking job applicants.
- Within about a week of release, the community had built open-weight clones (e.g., "Kev") and comparative benchmarks ("JevBench"), suggesting "decision models" could quickly become a distinct, commoditized model category rather than a one-off product.
- Separately, Claude's "Cowork" and chat interfaces are merging into one persistent agent that continues working after a user closes their laptop — paralleling OpenAI's earlier folding of Codex into the ChatGPT app, a trend toward consolidated general-purpose agents.
- A quoted first-hand account from inside a large company describes nearly all specs, code, tests, and tickets now being generated via Claude Code, with engineers at every level spending long hours essentially supervising the AI rather than reviewing output, while leadership questions why throughput hasn't improved.

## Quote

> Nobody is reading anything. Everyone, literally everyone, from an L1 to an L7 engineer here is doing the same thing. Talk to Claude.
— voxium (quoted commenter)

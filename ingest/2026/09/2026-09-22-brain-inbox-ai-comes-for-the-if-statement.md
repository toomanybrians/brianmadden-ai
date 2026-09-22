---
title: AI Comes for the If Statement
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: Tomasz Tunguz <blog@tomtunguz.com>
date_published: '2026-09-21'
date_captured: '2026-09-22'
ingest_method: email
model: claude-sonnet-5
---

# AI Comes for the If Statement

## Insights

- A new class of specialized "decider" models (Jev from TypeSafe, SemIf, kev) replace generative LLM calls for simple if-then classification tasks, running attention math once and reading output logits directly instead of decoding full text — cutting latency to hundreds of milliseconds.
- On a 98-thread hand-verified email classification test, these specialized deciders nearly doubled accuracy versus the production generative model (47% → 80-82%).
- Cost claims are dramatic: Jev is priced at $0.042/million input tokens with $0 output cost, yielding roughly 76x-209x cheaper per-case costs than frontier models like Sonnet-class LLMs in the author's own workflow evals.
- The author found that roughly a quarter of the if-then/classification calls in one of his own AI agents could be swapped for these specialized deciders within minutes.
- Frames this as evidence of "bifurcating AI economics": frontier/state-of-the-art models remain necessary for discovery, training, and system architecture, while narrower, specialized models take over once a system is hardened and run at scale.
- Suggests this could be the first of many software "primitives" (beyond if-then logic) getting specialized AI treatment, which would shift more profit margin toward the orchestration/harness layer rather than the underlying frontier model providers.

## Quote

> If this is the first of many primitives specialized for production, then harnesses are about to capture a lot more margin.

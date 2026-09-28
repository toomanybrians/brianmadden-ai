---
title: 🚀 System One models are carving out a new layer in the AI stack
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: AlphaSignal <news@alphasignal.ai>
date_published: '2026-09-27'
date_captured: '2026-09-28'
ingest_method: email
model: claude-sonnet-5
---

# 🚀 System One models are carving out a new layer in the AI stack

## Insights

- A new class of "System One" models (Jev by TypeSafe AI, plus open alternatives Laya and CLM-8B) are designed for fast typed decisions — classification, routing, scoring, verification — rather than text generation, positioning them as a distinct layer from LLMs in the AI stack.
- Jev takes application state plus a defined set of possible answers and returns typed values with probability/confidence scores in parallel (not token-by-token), claimed at 70–500ms latency, $0.042/M input tokens, no output-token cost — reportedly 40–200x lower latency and ~444x cost reduction versus frontier LLMs on comparable "System One shaped" tasks.
- Jev was trained with "Reinforcement Learning for Calibrated Decisions" (RLCD) so its confidence scores are meant to be meaningful (e.g., distinguishing a 0.52 score from a 0.998 score), enabling automatic routing of uncertain cases to stronger models or humans.
- A key limitation: these models can't invent output categories beyond the schema provided, so answer quality is capped by how complete/distinct the developer-defined option set is — a fraud ticket can't be correctly classified if "fraud" isn't one of the choices.
- Proposed architecture pattern: use plain code for explicit rules, decision models (like Jev) for fuzzy-but-bounded choices (routing, moderation, ranking, "Jev-as-a-judge" for evaluating LLM-generated candidates), and full generative LLMs only for open-ended generation/reasoning.
- Competing approaches are emerging fast: Laya (421M params, ModernBERT-based, ~33ms single-question inference on a T4) and CLM-8B (contrastive embedding-based selection) claim further speed gains — CLM reportedly up to 9x faster than Jev in some tests, though Jev outperformed CLM on some judge-pattern coding benchmarks (71.1%/83.1% vs. CLM's 81.6%/87.6%, mixed results across tasks).

## Quote

> Jev and the models following it give engineers another way to turn expensive intelligence into applications that are reliable, fast and economical enough to operate at scale.

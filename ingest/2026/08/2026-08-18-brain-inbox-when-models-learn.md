---
title: When Models Learn
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: Tomasz Tunguz <blog@tomtunguz.com>
date_published: '2026-08-17'
date_captured: '2026-08-18'
ingest_method: email
model: claude-sonnet-5
---

# When Models Learn

## Insights

- Test-time training (TTT) lets a model update its own weights during use, folding conversation history into a fixed-size weight set instead of an ever-growing KV-cache — so memory usage stays flat regardless of context length.
- This shifts the constraint on AI providers: standard transformers are memory-bound (cache grows with context), while TTT models are compute-bound (each user effectively requires their own diverging model instance, multiplying required GPU capacity).
- Cited Stanford research claims TTT models can run up to 2.7x faster than standard transformers because inference latency stays constant rather than growing with context length; "In-Place TTT" reportedly lifts a 4B model to competitive 128k-context performance without retraining.
- Because every user's model diverges after their own prompts, a provider can no longer serve one shared checkpoint to everyone — serving becomes millions of slightly personalized model instances, raising compute costs.
- The economic tradeoff described: personalization/memory-based lock-in (e.g., a coding agent learning a specific codebase's conventions and bugs) can justify the added per-user compute cost, while one-off, low-context tasks (e.g., customer support) are cheaper served by a shared, frozen/fine-tuned model.
- Piece frames test-time training as a likely major topic in AI infrastructure/economics discourse through late 2026, given its potential to restructure how AI serving costs work.

## Quote

> Standard AI is limited by memory, test-time AI is limited by compute & chips, so a provider picks based on whether it's serving long context or serving many people.

---
title: 'Exploring Apple''s On-Device Model: Twenty Billion Parameters in Flash'
source: The AI Realist
source_id: ai-realist
source_url: https://www.airealist.ai/p/exploring-apple-on-device-model
author: Julien Simon
date_published: '2026-10-25'
date_captured: '2026-10-26'
ingest_method: feed
model: claude-sonnet-5
---

# Exploring Apple's On-Device Model: Twenty Billion Parameters in Flash

## Insights

- Apple's new on-device model (Core Advanced, 20B parameters, 1–4B active) runs on Macs in about 2GB of memory versus ~15GB for a comparably sized open mixture-of-experts model, by keeping experts in flash storage and loading only a per-prompt subset rather than reselecting per token.
- This architecture trades capability for efficiency: on grade-school math, Apple's model solved 78/100 problems versus 89–94 for open models of similar size, and Apple explicitly tells developers to avoid using it for math, code, or logical reasoning — positioning it instead for summarizing, extracting entities, classifying, and rewriting text.
- The model runs on Apple's Neural Engine rather than GPU, using roughly a third of the energy of comparable open models on the same task set, while leaving the GPU free for other apps — a deliberate hardware/software co-design choice.
- Apple built the system with heavy practical constraints in mind: no versioning/pinning API (so behavior can shift with each OS update), no third-party fine-tuning support as of this OS release (dropped "for performance reasons"), and a small context window (8,192 tokens) tied to its memory budget.
- Apple's own documentation attributes the model's training to a "collaboration with Google" — using Google's cloud TPUs and, per external reporting, a tokenizer and distillation signal derived from Gemini models — while the engineering that fits it onto consumer hardware (flash-based expert storage, Neural Engine compilation, separate safety subsystem) is described as Apple's own research lineage.
- Separate, smaller "guardrail" safety models run alongside the main model in their own process, adding measurable memory overhead and occasionally refusing benign requests, reflecting a design choice to isolate and independently update safety behavior.

## Quote

> Apple made a 20-billion-parameter model cost a Mac about what a 4-billion-parameter one does.

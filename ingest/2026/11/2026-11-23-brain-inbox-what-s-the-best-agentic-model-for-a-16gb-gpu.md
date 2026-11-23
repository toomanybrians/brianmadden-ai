---
title: What's the best agentic model for a 16GB GPU?
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://evalsignal.xyz/campaign/e2d5d533-a6ff-423f-890b-1a3954b77462/ff779425-3a22-47e4-965d-bf0e1f18a567
author: EvalSignal <newsletter@evalsignal.xyz>
date_published: '2026-11-23'
date_captured: '2026-11-23'
ingest_method: email
model: claude-sonnet-5
---

# What's the best agentic model for a 16GB GPU?

## Insights

- Benchmark compared four locally-run AI models (Qwen 3.5 9B, Gemma 4 26B-A4B, LFM 2.5 24B-A2B, Ternary Bonsai 2 27B) on 100 frozen browser-automation planning tasks, scoring only the first proposed tool action rather than full task completion.
- A heavily compressed (ternary-weight) 27B dense model outperformed smaller conventional and mixture-of-experts models on matching a reference model's tool choice and producing exact correct actions, despite having a much smaller file size than its raw parameter count would suggest.
- Parameter count and "active parameters per token" are poor proxies for practical fit — MoE models activate only a fraction of their weights per token but still must store the full model in memory, while a ternary-quantized dense model can pack more effective capability into less disk/VRAM footprint.
- None of the models won on every metric: the compressed model led on action quality, a conventional dense model led on tool-selection accuracy, and a text-only reasoning model lagged significantly on exact-match correctness despite reliably emitting well-formed tool calls.
- Vision/multimodal support and "thinking"/reasoning-token generation are separate cost dimensions from parameter count — text-only models can't inspect icons/screenshots, and reasoning models incur extra compute per token even when fewer parameters are "active."
- Real-world deployability depends on budgeting KV cache, context length, and runtime overhead beyond the model's file size — the piece explicitly avoids ranking speed or claiming identical hardware conditions across tests.

## Quote

> The useful question is not simply how many parameters a model has.

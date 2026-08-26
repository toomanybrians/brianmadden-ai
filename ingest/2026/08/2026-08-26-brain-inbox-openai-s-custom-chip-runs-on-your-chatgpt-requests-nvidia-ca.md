---
title: OpenAI's custom chip runs on your ChatGPT requests—Nvidia can't sell i
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: AlphaSignal <news@alphasignal.ai>
date_published: '2026-08-26'
date_captured: '2026-08-26'
ingest_method: email
model: claude-sonnet-5
---

# OpenAI's custom chip runs on your ChatGPT requests—Nvidia can't sell i

## Insights

- OpenAI built a custom inference chip ("Jalapeño") with Broadcom in nine months, partly using its own AI models to accelerate chip design; targets ~50% lower cost per response versus Nvidia's current best chips and is exclusive to OpenAI's own infrastructure (not sold or rented).
- The chip is designed to handle both speed and volume simultaneously and keeps short-term memory physically close to the processor to reduce data movement and latency — framed as leading to faster Codex/ChatGPT responses as usage scales.
- Anthropic unified Claude's memory across chat and its multi-step agent product (Claude Cowork), so context from one persists into the other; users can explicitly say "remember this," and can manage/delete saved memory in settings. On by default for Free, Pro, and Max plans.
- Prime Intellect released an open-source "agent harness" enabling models to reuse context across runs, reportedly boosting ARC-AGI-3 scores from 30% to 95.5%.
- Perplexity shipped a fully local AI agent ("Portable Computer") running entirely on-device via NVIDIA DGX Spark hardware — no cloud dependency by default, zero token cost for local tasks, automatic PII flagging, and opt-in per-step cloud escalation; connects to Drive, Gmail, GitHub, Slack.
- The newsletter's framing across these items: competitive advantage in AI is shifting from "best model weights" toward control of the surrounding infrastructure stack — chips, memory systems, and context-reuse mechanisms.

## Quote

> "The next edge isn't the model, it's the stack around it."

---
title: DeepSeek DeepInfer 🔓, Claude Duet Agent 🤖, EAGLE-4 961 tok/s ⚡
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: AlphaSignal <news@alphasignal.ai>
date_published: '2026-10-22'
date_captured: '2026-10-23'
ingest_method: email
model: claude-sonnet-5
---

# DeepSeek DeepInfer 🔓, Claude Duet Agent 🤖, EAGLE-4 961 tok/s ⚡

## Insights

- DeepSeek open-sourced DeepInfer, its actual production inference engine (not a demo), under Apache 2.0, including speculative decoding (DSpark) that trims ~30% of verification checks for a 4-7% throughput gain, distributed inference across chips, and support for both Nvidia SM100 and Huawei Ascend 950 hardware — signaling a push toward cheaper, more portable inference infrastructure independent of a single chip vendor.
- Alongside the engine, DeepSeek released deepseek-recipe, a token encoding library designed to exactly replicate the hosted API's output behavior when self-hosting, aimed at eliminating subtle mismatches between self-hosted and official deployments.
- Anthropic previewed Claude Duet, a standalone proactive agent (distinct from chatbot-style Claude) that runs continuously in the cloud, monitors connected apps (email, calendar, Slack, 6,000+ tools), sends a "morning brief," and only interrupts the user when something needs attention — but still requires explicit approval before taking actions like sending messages or payments.
- Duet runs on Claude Opus 5.5, inherits existing Claude memory/connections for low-setup onboarding, and is rolling out via waitlist to Pro/Max US subscribers at no extra cost, though its background activity consumes usage limits.
- The newsletter frames faster/cheaper inference (DeepInfer, EAGLE-4 at 961 tok/s, a 6x speculative-decoding gain on Qwen3-8B, consumer-hardware-runnable quantized DeepSeek V4.1 Flash) as the underlying enabler of "always-on" agent products like Duet — positioning inference speed/cost as the infrastructure precondition for persistent, proactive AI agents rather than an isolated technical trend.

## Quote

> Speed unlocks behavior. That's the real story today.

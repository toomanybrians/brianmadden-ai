---
title: How Revolut Cut AI Costs 90% and Started Shipping Faster 🚀
source: Linas's Newsletter
source_id: linas-newsletter
source_url: https://linas.substack.com/p/revolut-ai-coding-costs-open-source-models
author: Linas Beliūnas
date_published: '2026-11-06'
date_captured: '2026-11-09'
ingest_method: feed
model: claude-sonnet-5
---

# How Revolut Cut AI Costs 90% and Started Shipping Faster 🚀

## Insights

- Revolut moved ~2,000 engineers off metered Anthropic/OpenAI APIs to Z.ai's open-weight GLM model, self-hosted on 56 Nvidia B200 GPUs via Together AI, cutting blended cost to $0.30 per million tokens — a 90% reduction in invoice cost.
- After the switch, lead time (feature pickup to merge-ready code) fell by about 70%; notably, giving engineers top-tier agents (Claude Code, Codex) alone hadn't moved delivery speed — the pricing/infrastructure model change is what unlocked productivity.
- The approach was to tune a fixed GPU fleet (enabling it to absorb 76% more demand) rather than scale spend, while still reserving frontier models for select tasks that require them.
- Revolut is positioned as a highly AI-mature company (own foundation model PRAGMA built with NVIDIA, in-house AI lab Revolut Research), with nearly two years of usage data across 2,000 engineers — contrasted with a cited stat that only 2% of S&P 500 companies tracked production AI metrics over time despite 69% running AI in production.
- The case implicates how AI coding tools are priced/metered for end users as a root cause of weak productivity gains, suggesting fixed-cost/self-hosted infrastructure models may outperform pay-per-token frontier API access for engineering productivity at scale.
- Piece also flags compliance complexity: how an EU-regulated bank got a Chinese-developed open-weight model through regulatory approval, tied to specific architectural choices (detail promised but not elaborated in excerpt).

## Quote

> The 90% saving came later, and so did the productivity jump.

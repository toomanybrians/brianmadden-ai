---
title: '🐛 GLM-5.3 Released: Nobody Taught It To Hack'
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://read.getsuperintel.com/p/glm-5-3-released-nobody-taught-it-to-hack
author: Superintelligence <superintel@mail.beehiiv.com>
date_published: '2026-08-14'
date_captured: '2026-08-14'
ingest_method: email
model: claude-sonnet-5
---

# 🐛 GLM-5.3 Released: Nobody Taught It To Hack

## Insights

- GLM-5.3's vulnerability-hunting ability emerged as an unintended by-product of scaled post-training on the same base model as GLM-5.2 — no new pretraining run, just more/varied task environments and compute, yet capability jumped from bug-spotting to planning full exploitation chains.
- Working with Chinese security teams, the model surfaced 2,436 vulnerabilities across 269 open-source projects (1,097 medium-to-high severity), including a bug dating to 1981; average flaw age was 26.6 years. Weights will be open-sourced in about two weeks after a short safety-hardening window.
- The lab is explicit that its capability gains are concentrated exactly where it was weakest (security), and its own benchmarks show it still trails closed frontier models on higher-order exploitation tasks (not just discovery) — finding a hole and exploiting it remain distinct skills.
- Frontier competition is bifurcating: OpenAI and Google both shipped speed/price plays the same week (GPT-5.6 Sol at 14x speed on Cerebras; Gemini 3.7 Flash at $0.75/$3.75 per million tokens) rather than raw intelligence gains, suggesting margin-per-token and enterprise workflow economics are becoming the competitive battleground.
- OpenAI's revenue run-rate hit ~$40B (doubled since end of 2025), with both OpenAI and Anthropic having filed confidential IPO paperwork — reframing pricing/speed moves as investor-facing signals, not just product decisions.
- Texas issued a moratorium on new AI data center development pending grid/interconnection audits, cutting the state's official electricity demand growth forecast from 14% to 6%; data centers account for ~90% of new grid power requests in the state, and public opposition (60%) cuts across party lines.

## Quote

> "Scaling post-training is all we did for GLM-5.3."

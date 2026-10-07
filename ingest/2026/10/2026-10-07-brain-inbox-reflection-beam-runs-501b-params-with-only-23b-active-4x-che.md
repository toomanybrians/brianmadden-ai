---
title: Reflection Beam runs 501B params with only 23B active — 4x cheaper
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: AlphaSignal <news@alphasignal.ai>
date_published: '2026-10-06'
date_captured: '2026-10-07'
ingest_method: email
model: claude-sonnet-5
---

# Reflection Beam runs 501B params with only 23B active — 4x cheaper

## Insights

- Reflection AI released Beam, an open-source model with 501B total parameters but only 23B active at once (mixture-of-experts style sparsity), making it 3-4x cheaper to run than rival GLM-5.2 despite GLM having 250B fewer total parameters.
- Beam offers a 1M token context window, is built for coding/tool use/multi-step agents, ships under Apache 2.0 (unrestricted commercial use), and supports FP8/NVFP4 formats for efficient self-hosting; full weights are due this month.
- Separately, OpenAI launched textGrain, an invisible watermarking system for ChatGPT/Codex output that nudges word choices against a hidden key to create a detectable statistical fingerprint — driven by EU AI Act compliance requirements.
- textGrain only confirms probable OpenAI-model origin (not user/account/prompt identity); EU users get it automatically, API access is opt-in elsewhere, and detection is weak — editing ~25% of words cuts detection to 17%.
- The newsletter frames these as one trend: the open web becoming "provenance-aware," with model efficiency gains and content-authenticity tracking advancing in parallel.
- Other noted developments: DeepSeek open-sourced a GPU math library cutting token costs 98%; 90 Claude agents reportedly helped identify two candidate room-temperature magnetic semiconductor materials via simulation in 3 days (unverified in lab).

## Quote

> Efficiency and accountability are now the same race.

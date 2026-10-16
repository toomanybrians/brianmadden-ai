---
title: 'Full benchmarks at: https://t.co/awRLs1Bcxa'
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2110817820972069228
author: '@DanielMiessler'
date_published: '2026-10-15'
date_captured: '2026-10-16'
ingest_method: x
model: claude-sonnet-5
---

# Full benchmarks at: https://t.co/awRLs1Bcxa

## Insights

- The benchmark (Unsupervised Learning's "Gauntlet") grades models on explanation quality rather than task completion — scored 0–4 against David Deutsch's "hard to vary" criterion for a good explanation, where every part of the answer must do real work.
- There's a steep cost-to-quality curve: Claude Opus 5.5 at max reasoning effort scores the highest observed grade (3.25) but costs $1.13 per answer, versus $0.036–$0.078 at lower efforts for only slightly lower scores.
- Claude Fable 5.1 appears to be the standout for cost-efficiency, reaching 3.21–3.24 (near the top score) at $0.11–$0.21 per answer — far cheaper than Opus's top setting.
- Higher "reasoning effort" settings don't reliably improve scores — several models (GPT-6 Astra, Claude Haiku 5.5, GPT-6.1 Sol) show flat or non-monotonic results across effort levels, sometimes scoring worse at higher effort.
- There's a wide capability tier gap: top models (Opus, Fable) cluster around 3.0–3.25, while others (Sonnet, Grok, GPT-6 Astra, GPT-6.1 Sol, GPT-5.6 Terra) sit mostly in the 2.1–2.8 range regardless of effort setting.
- Per-answer costs across the full model/effort matrix range from $0.0002 (GPT-6 Luna) to $1.13 (Opus max), illustrating an enormous spread in price for comparable tasks.

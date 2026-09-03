---
title: Our budget vision shortlist became obsolete in five days
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://evalsignal.xyz/campaign/26a39ae4-24a5-4202-89ee-f9600cff1a6f/ff779425-3a22-47e4-965d-bf0e1f18a567
author: EvalSignal <newsletter@evalsignal.xyz>
date_published: '2026-09-02'
date_captured: '2026-09-03'
ingest_method: email
model: claude-sonnet-5
---

# Our budget vision shortlist became obsolete in five days

## Insights

- Two new "budget tier" multimodal models (Qwen3.8 Flash, GLM-5.3 Flash) launched within hours of each other and immediately outperformed a shortlist published just five days earlier, illustrating how fast the low-cost API model tier is turning over.
- Both new models use sparse "mixture of experts"-style architectures with huge total parameter counts but small active-parameter paths per token (e.g., 125B total/6B active for Qwen3.8 Flash; 320B total/18B active for GLM-5.3 Flash), enabling large capacity without dense per-token compute cost.
- On a controlled 400-case test (100 text-planning + 100 vision cases per model), Qwen3.8 Flash led on vision accuracy (79/100 strict passes, 94.8% rubric) and faster text planning; GLM-5.3 Flash led on vision latency (~3 seconds faster) and more consistent structured tool-call output.
- Cost-performance leapt forward: the new models deliver 7-10 more strict vision passes than prior budget leaders (Qwen3-VL variants) for roughly the same or lower price, especially given GLM-5.3 Flash's temporary 50%-off launch pricing.
- Both new models support text, image, and video input with roughly million-token context windows while remaining in the inexpensive hosted API tier — a capability jump previously associated with more expensive models.
- The piece frames this as evidence of a new emerging model class: very large total capacity, cheap inference, near-million-token context, and credible cross-modal performance simultaneously.

## Quote

> Our previous budget shortlist did not become wrong. The market simply moved faster than expected.

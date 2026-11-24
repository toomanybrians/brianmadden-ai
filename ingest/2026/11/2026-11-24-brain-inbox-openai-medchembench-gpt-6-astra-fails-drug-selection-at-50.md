---
title: '🧪 OpenAI MedChemBench: GPT-6 Astra fails drug selection at 50%'
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: AlphaSignal <news@alphasignal.ai>
date_published: '2026-11-23'
date_captured: '2026-11-24'
ingest_method: email
model: claude-sonnet-5
---

# 🧪 OpenAI MedChemBench: GPT-6 Astra fails drug selection at 50%

## Insights

- OpenAI's new MedChemBench benchmark tests drug-discovery capability across 99 problems pulled from 117 papers/patents, covering structure reading, experimental reasoning, candidate selection, and property prediction.
- GPT-6 Astra shows highly uneven performance on this benchmark: 95.4% on molecular structure reconstruction, but only about 50% on compound selection and numerical property prediction — suggesting current models are strong at pattern-reading tasks but weak at judgment-style scientific decisions.
- OpenAI frames the benchmark as a "capability signal," explicitly not proof that AI can independently identify viable drug candidates — a notable caveat on hype around AI-driven drug discovery.
- Separately, OpenAI published research on "adversarial distillation" — a technique where a cheaper model is trained on a powerful model's outputs with safety guardrails stripped out, replicating capabilities without the refusals.
- Attack success rate for this distillation technique reportedly dropped from 54% (on GPT-6 Astra) to 0.2% (on GPT-6.2 Astra) after OpenAI combined training changes, automated classifiers, and API-level restrictions.
- OpenAI is now blocking older, weaker-safeguard model families from accessing GPT-6.2's protected reasoning outputs, and reports weekly enforcement actions against thousands to tens of thousands of accounts running distillation campaigns.

## Quote

> MedChemBench is a capability signal, not proof AI can independently identify viable drug candidates.

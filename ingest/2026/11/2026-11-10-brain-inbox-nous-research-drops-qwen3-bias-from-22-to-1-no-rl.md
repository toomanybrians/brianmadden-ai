---
title: 🧹 Nous Research drops Qwen3 bias from 22% to 1% — no RL
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: AlphaSignal <news@alphasignal.ai>
date_published: '2026-11-09'
date_captured: '2026-11-10'
ingest_method: email
model: claude-sonnet-5
---

# 🧹 Nous Research drops Qwen3 bias from 22% to 1% — no RL

## Insights

- Nous Research fine-tuned Alibaba's Qwen3.8-27B into a new model ("Arete-27B"), reducing its pro-China propaganda response rate from 22% to under 1%, matching Western model baselines on the same eval.
- The fix used plain supervised fine-tuning on 53 million tokens, with no reinforcement learning involved — suggesting political bias in these models is a shallow, easily-overwritten layer rather than deeply embedded in the model's reasoning.
- Alongside the bias reduction, factual accuracy improved (2.32 to 2.98 out of 5) while general benchmark performance stayed essentially flat (65.60% vs 65.77% on Hermes Bench), indicating the de-biasing didn't degrade overall capability.
- Nous released the weights, eval set, and full training data openly on Hugging Face, making the bias-correction method fully reproducible/auditable by others.
- Framed in the newsletter as part of a broader dynamic: Chinese open-weight models are currently considered the strongest ones runnable locally, prompting Western labs/groups to adapt them for their own use rather than build competing base models from scratch.

## Quote

> The big takeaway: political bias sits shallow in these models. You can swap it out without breaking anything else.

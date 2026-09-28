---
title: ⚙️ Crusoe brings receipts to AI fine-tuning
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://archive.thedeepview.com/p/crusoe-brings-receipts-to-ai-fine-tuning
author: The Deep View <newsletter@thedeepview.co>
date_published: '2026-09-26'
date_captured: '2026-09-28'
ingest_method: email
model: claude-sonnet-5
---

# ⚙️ Crusoe brings receipts to AI fine-tuning

## Insights

- Crusoe launched Serverless Fine-Tuning (GA), covering 19 open models from 2B to 753B parameters, each shipped with the exact configs used to produce benchmark results so customers can reproduce them.
- The pitch is transparency as a differentiator: rather than asking customers to trust an opaque benchmark harness, results, and billing, Crusoe publishes all three and lets customers verify.
- Fine-tuning a 753B-parameter model (GLM 5.2) raised intent-classification scores by 19 points and multi-turn conversation scores by 61 points, for a $180 total cost.
- Smaller fine-tuned models can beat much larger base models on narrow tasks — a fine-tuned 2B model outperformed a 235B model on a banking customer-service benchmark at roughly 1/15th the training cost, illustrating that fine-tuning changes output discipline rather than adding new knowledge.
- The published benchmark suite also reports negative results: two models regressed on a theorem-proving benchmark after fine-tuning, attributed to likely pre-training data contamination rather than being suppressed.
- Pricing is tiered by parameter count (40¢/million tokens under 16B, up to $10 above 300B) and fine-tuned models can be deployed to dedicated endpoints starting at $5.50/hour on H100 GPUs, positioned as removing sales-call friction from enterprise adoption.

## Quote

> "Fine-tuning teaches output discipline, not new knowledge." — Michael Yen-Chi Ho, Crusoe

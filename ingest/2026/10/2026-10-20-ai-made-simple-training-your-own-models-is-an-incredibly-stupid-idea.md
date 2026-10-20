---
title: Training Your Own Models is an Incredibly Stupid Idea
source: Artificial Intelligence Made Simple
source_id: ai-made-simple
source_url: https://www.artificialintelligencemadesimple.com/p/training-your-own-models-is-an-incredibly
author: Devansh
date_published: '2026-10-19'
date_captured: '2026-10-20'
ingest_method: feed
model: claude-sonnet-5
---

# Training Your Own Models is an Incredibly Stupid Idea

## Insights

- Research (Gekhman et al., EMNLP 2024) indicates factual knowledge is mostly acquired during pre-training, while fine-tuning/post-training mainly teaches models to use existing knowledge more efficiently — not inject new facts.
- FineTuneBench (Stanford, 2024) found commercial fine-tuning services achieved only 37% generalization accuracy for new facts and 19% for updating existing knowledge; Ovadia et al. found retrieval consistently beat fine-tuning for teaching facts.
- Vendor benchmarks touting training gains (e.g., Harvey/Engram's jump from 4.7% to 72.6% accuracy) are often compared against weak baselines or opaque proprietary harnesses, making it unclear how much improvement came from training versus surrounding infrastructure (retrieval, reasoning, tools).
- Multiple examples (Harvey's recursive reasoning harness, OpenAI's inference-setting changes on ARC-AGI-3, NVIDIA's verified skills) show large performance gains achieved purely through better inference/harness engineering, with no model retraining.
- A detailed cost model estimates a lean custom-training effort at ~$1.87M upfront plus ongoing costs, requiring roughly 6 months to break even under optimistic assumptions — while frontier models are released roughly every 5 days, undercutting the shelf life of custom training investment.
- Continual learning, often pitched as the fix for models going stale, is shown by recent research (The Mirage of Model Editing; a 2026 ACL study) to degrade sharply at scale and struggle with temporal/knowledge consistency, while still carrying significant recurring retraining costs (estimated ~$1.8M/year for monthly refreshes).
- Core argument: infrastructure investments (retrieval, memory, reasoning systems) compound across model generations and can be reused as better foundation models emerge, whereas trained-in knowledge/behaviors are tied to a specific, decaying model and environment.

## Quote

> Your company's knowledge doesn't need to live inside a model's weights. Your AI needs to know how to use it.

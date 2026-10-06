---
title: Kolibri Is Large Enough
source: The AI Realist
source_id: ai-realist
source_url: https://www.airealist.ai/p/kolibri-is-large-enough
author: Julien Simon
date_published: '2026-10-06'
date_captured: '2026-10-06'
ingest_method: feed
model: claude-sonnet-5
---

# Kolibri Is Large Enough

## Insights

- Aleph Alpha's Kolibri (78B params, German/English, Apache 2.0) reportedly cost roughly $3M for the core training run in GPU-hours, down from an estimated ~$100M to replicate a 530B model in 2021 — illustrating how fast frontier-adjacent model training costs have collapsed.
- Model size was chosen by serving/memory economics, not benchmark leadership: Aleph Alpha's own estimates show the 78B version handles 6x more concurrent long-context requests than a 123B version on the same two GPUs, and depth in two languages was prioritized over broader language coverage.
- The model's training pipeline depends heavily on other labs' models: ~24% of pretraining data is synthetic, generated/rewritten by Google's Gemma and Mistral's NeMo, while reasoning/conversation training data came primarily from Chinese labs (Z.ai's GLM, Alibaba's Qwen), raising questions about data lineage and political bias given US accusations that Chinese labs illicitly distill US frontier models.
- On Aleph Alpha's own benchmarks, a smaller Chinese model (Qwen3.5 35B) ties or beats Kolibri despite being less than half the size — the strategic case for Kolibri rests not on performance but on regulatory eligibility (EU/EEA-developed status) for government and regulated-industry procurement, as shown by a German state (Hesse) excluding non-European models from a public tender regardless of benchmark scores.
- Aleph Alpha's pending combination with Cohere, combined with its licensing terms (open weights but training method/recipe protected), suggests the real commercial asset is less the model itself than the demonstrated team capability to build and ship models fast, sold as a "sovereign/eligible" compliance product.
- Frames the global AI competitive landscape as three distinct roles rather than three blocs racing for the frontier: the US supplies chips and either sells frontier capability by API or gives away filtering/rewriting tools while guarding its best "teacher" models; Chinese labs compete by giving away their teacher-grade models for free distribution; Europe's contribution is largely regulatory/legal — compliance and "eligibility" rather than frontier capability.

## Quote

> "the investment that a European LLM 'doesn't justify' has collapsed."

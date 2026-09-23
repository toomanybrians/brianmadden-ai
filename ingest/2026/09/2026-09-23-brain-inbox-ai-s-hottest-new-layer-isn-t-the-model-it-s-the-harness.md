---
title: AI’s hottest new layer isn’t the model. It’s the harness
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://sharongoldman.substack.com/p/ai-agents-model-harness
author: Sharon Goldman <sharongoldman@substack.com>
date_published: '2026-09-22'
date_captured: '2026-09-23'
ingest_method: email
model: claude-sonnet-5
---

# AI’s hottest new layer isn’t the model. It’s the harness

## Insights

- The "harness" refers to the software layer surrounding an AI model that handles context/information delivery, tool execution, approval enforcement, limit-setting, and task-completion determination — described as the "body" to the model's "brain."
- The term is very recent: an Anthropic blog post appeared last November, Mitchell Hashimoto's essay popularized "harness engineering" in February, followed by an OpenAI post in March; by summer it had a dedicated track at the AI Engineer World's Fair and was drawing YC attention.
- Nvidia's Adel El-Hallak cited a case where optimizing the harness around an existing model (working with LangChain), without retraining the model itself, raised a benchmark score from ~30% to ~100%.
- The harness is framed as a new set of adjustable "knobs" — not just for raw performance, but for efficiency, cost, and control over agent behavior.
- NanoCo's Gavriel Cohen offers an 80/20 heuristic (model/harness) but notes the 20% (harness) can sometimes drive 80% of real-world impact, especially on complex, multi-step tasks.
- Cohen also cautions the harness has limits: it can extend a model's execution capability but cannot make an unaligned model aligned, or vice versa.

## Quote

> 80 is the model, 20 is the harness. But sometimes 20% can have 80% of the impact.

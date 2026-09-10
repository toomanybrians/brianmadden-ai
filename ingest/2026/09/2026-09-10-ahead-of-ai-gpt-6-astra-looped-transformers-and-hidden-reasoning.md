---
title: GPT-6 Astra, Looped Transformers, and Hidden Reasoning
source: Ahead of AI
source_id: ahead-of-ai
source_url: https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and
author: Sebastian Raschka, PhD
date_published: '2026-09-09'
date_captured: '2026-09-10'
ingest_method: feed
model: claude-sonnet-5
---

# GPT-6 Astra, Looped Transformers, and Hidden Reasoning

## Insights

- GPT-6 Astra's biggest leap over its predecessor is in computer-use capability — operating GUIs via mouse/keyboard through a harness — rather than a dramatic jump in general reasoning benchmarks, suggesting agentic tasks (not just text/code) are the next frontier for both open-source and proprietary tooling.
- OpenAI reportedly trained computer-use behavior by exposing the model to real macOS environments (via purchased Mac hardware) using a screenshot-action-feedback loop with RL from success/failure signals, distinct from the GPU-based core model training.
- "Looped transformers" (reusing the same transformer block/stack multiple times instead of adding new distinct blocks) is a real architecture technique with research backing (Universal Transformers 2018, Nanbeige, Ouro, Mixture-of-Recursions) that improves modeling quality at a fixed compute budget for sufficiently large models, though it doesn't reduce KV-cache costs the way it does parameter-storage costs.
- Rumors that Astra hides its chain-of-thought via looped-transformer architecture are treated skeptically: OpenAI's chief scientist stated Astra's computation-graph depth is within 2x of GPT-4, and shorter/less monitorable reasoning traces are more plausibly a byproduct of increased model capability (fewer mistakes, less backtracking) than of the looping mechanism itself.
- More capable models tend to need fewer "thinking tokens" to reach the same accuracy — a pattern already observed across model sizes within a family, not a new phenomenon introduced by looping — raising a general interpretability question about whether efficient reasoning traces are less faithful/monitorable regardless of architecture.
- Newer, more capable models may need less scaffolding (e.g., AGENTS.md/SKILL.md instruction files) since they're better at inferring tasks directly, implying that some current human-authored workflow documentation could become obsolete or actively unhelpful.

## Quote

> I want to prevent a race into unmonitorability kicked off by confused reporting. — Jakub Pachocki, OpenAI Chief Scientist

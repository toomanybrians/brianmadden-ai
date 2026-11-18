---
title: 'Cut generative AI costs: Code for rules, models for judgment'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/cut-generative-ai-costs-code-for-rules-models-for-judgment/
author: Meghan Kothari
date_published: '2026-11-17'
date_captured: '2026-11-18'
ingest_method: feed
model: claude-sonnet-5
---

# Cut generative AI costs: Code for rules, models for judgment

## Insights

- AWS frames model-calling as a default anti-pattern: teams often route trivial steps (validation, formatting, routing) through LLMs, and at production scale these small per-call costs become a major architecture expense, plus added latency and non-determinism.
- Proposes a three-question decision flow before touching any model: can a rule check success, can a model write a reusable rule once (e.g. generate a regex, reviewed and committed), or does the step just pick one answer from a fixed list — only genuinely open-ended/generative tasks should go to a model.
- Introduces "constrained decision calls" as a middle tier between deterministic code and full generation — structured-output models limited to an enum (plus an "unsure" escalation option), embedding similarity, a calibrated open-source "Strands Decider," or a trained classifier — for routing/classification tasks that aren't fully rule-based.
- Claims a "deterministic fast-path" pattern (e.g., keyword matching via Step Functions Choice states) can resolve the bulk of routing traffic before any model is invoked; illustrative example cites 95% of requests resolved by rules, leaving only 5% reaching a model (explicitly labeled illustrative, not a benchmark).
- Recommends treating model selection as tested configuration: maintain a golden evaluation set per task in CI, gate model swaps against a quality floor, put model choice behind a flag, and use shadow-mode sampling to detect drift when rule-resolved cases disagree with model outputs.
- Notes model non-determinism persists even at temperature 0, and positions Bedrock features (Guardrails, Model Evaluation, Intelligent Prompt Routing, Model Distillation, structured outputs) as mechanisms to measure/contain this and right-size model choice rather than defaulting to the newest/largest model.

## Quote

> The biggest cost lever in a generative AI system is whether you call a model at all. — Meghan Kothari (AWS ML Blog)

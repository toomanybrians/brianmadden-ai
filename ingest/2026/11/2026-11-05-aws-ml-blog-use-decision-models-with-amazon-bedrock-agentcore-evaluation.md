---
title: Use decision models with Amazon Bedrock AgentCore Evaluations
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/use-decision-models-with-amazon-bedrock-agentcore-evaluations/
author: Sungyeon Kim
date_published: '2026-11-04'
date_captured: '2026-11-05'
ingest_method: feed
model: claude-sonnet-5
---

# Use decision models with Amazon Bedrock AgentCore Evaluations

## Insights

- AWS Bedrock AgentCore Evaluations now supports "decision models" as a new backend for custom code-based evaluators — small, specialized models that return calibrated probabilities over a fixed set of answers (yes/no, up to 255-way choice, or 2-10 level score) rather than free-form LLM judgments with rationale.
- The pitch is a tradeoff: decision models trade explanation depth for speed (~hundreds of ms vs. 2-10s for LLM-as-judge) and calibrated, thresholdable confidence scores, making them suited to narrow, repeatable checks (policy compliance, tool-call safety, groundedness) rather than open-ended quality assessment.
- Recommended architecture is a "cascade pattern": run a cheap decision-model check on every turn as a screening/gating layer, then escalate only low-confidence or failing turns to full LLM-as-judge evaluators for explanation — treating decision models as an additive gate, not a replacement for built-in evaluators.
- Two specific decision-model products are integrated as examples: Jev (hosted, from TypeSafe, requires API key/vendor access) and Strands Decider 2B (open-source, self-hosted, 2B parameters) — both support the same three question types (noul/choice/score).
- The post stresses a validation discipline before trusting a decision model: build a labeled sample with three independent human raters, measure agreement rate and calibration against built-in evaluators, analyze disagreements, and re-validate whenever the question wording or model version changes — framed as "reframing a rubric creates a new measurement," not a copy of the old one.
- References an external preprint ("JEV-as-a-Judge: Accept When Confident, Escalate When Unsure") that frames the distinction as "reading versus deriving" — narrow decision models flag/screen, LLM judges do the deeper reasoning work.

## Quote

> A reframed rubric often lands stricter or looser than the original intended, and you won't see that drift until you check it against real sessions.

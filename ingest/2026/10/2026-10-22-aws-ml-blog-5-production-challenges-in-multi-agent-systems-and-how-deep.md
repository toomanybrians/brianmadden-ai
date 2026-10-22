---
title: 5 production challenges in multi-agent systems and how Deep Insight solved
  them
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/5-production-challenges-in-multi-agent-systems-and-how-deep-insight-solved-them/
author: Yoonseo Kim
date_published: '2026-10-21'
date_captured: '2026-10-22'
ingest_method: feed
model: claude-sonnet-5
---

# 5 production challenges in multi-agent systems and how Deep Insight solved them

## Insights

- AWS's Deep Insight system frames production agent failures as an architecture problem, not a prompting problem: agents make contextual judgments rather than following fixed instructions, so reliability requires designing cognition and execution flow, not just better prompts.
- The architecture uses a three-layer hierarchy (Coordinator→Planner→Plan Reviewer, then Supervisor, then specialized Coder/Validator/Reporter/Tracker agents) with a human-in-the-loop plan-approval step and a hard cap on revision loops to prevent infinite cycles.
- Model selection is treated as an architectural/cost decision rather than a single choice: cheap/fast Haiku for routing, Opus with extended thinking for planning, Sonnet for execution — paired with selective prompt caching (claimed up to 90% input-token cost reduction on repeated calls where context is stable).
- Validation is built into the pipeline structurally — a dedicated Validator agent recomputes calculations from source data (0.01 tolerance) and generates citation metadata before report generation — but the piece notes this doesn't cover prompt-injection or hallucinated/ungrounded text, which they say requires separate guardrails (e.g., Bedrock Guardrails).
- Security/isolation for LLM-generated code execution is handled via per-session ephemeral Fargate containers behind a load balancer with sticky sessions, private VPC networking, and automatic one-hour container termination — treating "the model might delete files or access other users' data" as a real production risk, not hypothetical.
- The same orchestration pattern (Coordinator/Planner/Supervisor/specialized agents) was reportedly reused in two other domains (LG Electronics marketing insights, a tech-strategy "TechRecon" agent), framed as evidence the hierarchy is a general-purpose pattern rather than task-specific; LG case claims a 3-day analysis task reduced to 30 minutes.

## Quote

> Building an agent that works in production is not a matter of model capability. It's a matter of architecture.

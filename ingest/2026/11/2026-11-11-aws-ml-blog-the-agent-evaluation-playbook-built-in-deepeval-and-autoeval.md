---
title: 'The agent evaluation playbook: Built-in, DeepEval, and AutoEval on Amazon
  Bedrock AgentCore Evaluations'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/the-agent-evaluation-playbook-built-in-deepeval-and-autoeval-on-agentcore/
author: Bharathi Srinivasan
date_published: '2026-11-10'
date_captured: '2026-11-11'
ingest_method: feed
model: claude-sonnet-5
---

# The agent evaluation playbook: Built-in, DeepEval, and AutoEval on Amazon Bedrock AgentCore Evaluations

## Insights

- AWS frames agent evaluation as a three-step process: define business success in concrete terms, decompose it into observable trace/session-level behaviors, then map each behavior to a specific evaluator — rather than starting from a list of metric names that "sound right."
- Amazon Bedrock AgentCore Evaluations now offers a layered evaluator catalog: AWS-authored built-in evaluators (15+, covering response quality, goal completion, tool use, skills, safety, trajectory matching), managed third-party evaluators from DeepEval and AutoEval libraries, and custom LLM-as-judge evaluators derived from either.
- A key failure mode highlighted: single composite scores can mask contradictory outcomes (e.g., an agent with high task completion that leaks PII, or one that's accurate but non-compliant); AWS's answer is "multi-dimension evaluators" that score several independent criteria from one judge call without blending them into one number.
- Evaluation runs in three modes — on-demand (dev/debugging), online (sampling live production traffic), and batch (regression testing against a fixed golden dataset) — using identical evaluator IDs across all three, so moving from testing to production evaluation is a config change, not a rewrite.
- Suggested evaluator "stacks" differ by agent type: customer support prioritizes goal success/conversation completeness/PII leakage; multi-step research prioritizes trajectory matching and knowledge retention; regulated domain agents (medical/legal/financial) prioritize correctness and security since "a wrong answer is worse than no answer."
- Positions this as a trust/governance layer for agent deployment broadly — treating eval as infrastructure for catching silent failures (dropped requests, wrong tool paths, policy violations) that surface-level metrics like latency or spot-checks miss.

## Quote

> A wrong answer is worse than no answer.

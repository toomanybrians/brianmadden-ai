---
title: 'Trust in Depth: Giving agents more autonomy without losing control'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/trust-in-depth-giving-agents-more-autonomy-without-losing-control/
author: Shawn Bice
date_published: '2026-10-15'
date_captured: '2026-10-16'
ingest_method: feed
model: claude-sonnet-5
---

# Trust in Depth: Giving agents more autonomy without losing control

## Insights

- AWS frames agent governance as "Trust in Depth," analogous to two decades of "Defense in Depth" security practice, but inverted: instead of limiting what can go wrong, it's meant to expand what can safely be delegated to autonomous agents.
- The model rests on four lifecycle questions: Scope (define capabilities and limits before running), Know (identity/authorization at deployment), Bound (enforce limits during execution), and Observe (reconstruct and learn after each run).
- Key architectural principle: enforcement must sit outside the agent's own reasoning (e.g., at a gateway layer), so a compromised, buggy, or prompt-injected agent cannot disable its own controls.
- AWS distinguishes rules that can be formally proven via "automated reasoning" (mathematical/neurosymbolic verification, already used in IAM, Nitro Hypervisor, S3 Block Public Access) from fuzzier judgment calls (e.g., "keep a friendly tone") that still require human oversight or behavioral evaluation rather than proof.
- Product stack tying this together: Kiro (spec-driven agent build with automated reasoning checks), Strands/Strands Box (agent definition + sandboxing), Agent Registry (catalog/approval workflow for agents and tools), Bedrock AgentCore (identity, policy enforcement via Gateway, Guardrails), and CloudWatch Omni (tracing and automated evaluation of agent runs).
- The worked example (offboarding an employee with a legal hold on email) illustrates policy-sequenced autonomy — the agent is blocked by gateway policy from performing actions out of order, without needing step-by-step human approval, while all actions remain fully traceable to its identity.

## Quote

> Give an agent a task and it finds its own path to finish it, picking tools and sequencing steps no developer scripted.

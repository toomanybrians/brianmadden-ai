---
title: Taxonomy of multi-agent design patterns, anti-patterns, and lessons from manufacturing
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/taxonomy-of-multi-agent-design-patterns-anti-patterns-and-lessons-from-manufacturing/
author: Malini Sethi
date_published: '2026-11-16'
date_captured: '2026-11-17'
ingest_method: feed
model: claude-sonnet-5
---

# Taxonomy of multi-agent design patterns, anti-patterns, and lessons from manufacturing

## Insights

- Offers a two-tier taxonomy of multi-agent coordination: Tier 1 (deterministic, developer-defined control flow — sequential pipeline, conditional workflow, conditional router, parallel fan-out/fan-in) and Tier 2 (autonomous, model-determined flow at runtime — plan-based orchestration, handoff, conversation-driven/group chat, debate-consensus), with Tier 2 recommended only when subtasks emerge during the work rather than being knowable in advance.
- Cites reliability math as a core argument against over-chaining agents: a 10-step chain at 95% per-step reliability yields ~59.9% end-to-end success, and 20 steps yields ~35.8%, illustrating how dependent handoffs multiply failure risk.
- Names five costly anti-patterns: "god agent" (one agent, 15+ tools, degraded tool selection), unbounded iteration (no hard retry ceiling), natural-language contracts between agents (meaning drifts at each handoff, e.g. "could indicate wear" hardening into "confirmed wear"), premature multi-agent use (coordination tax outweighs benefit when one agent with tool groups would suffice), and unguarded customer/physical-world contact without human approval gates.
- Argues multi-agent systems are fundamentally a distributed-systems problem, not a model-capability problem, and cites Stanford HAI research showing two models can perform worse collaborating than either alone when coordination overhead exceeds benefit.
- Frames four manufacturing-specific constraints that reshape architecture decisions: hard takt-time latency budgets (measured at p99, not average), safety-critical boundaries requiring agents to observe/recommend but never directly actuate equipment, edge-vs-cloud data placement (a single stamping press generates 50+GB/day whose value decays in milliseconds), and shift-bounded agent memory/lifecycle to prevent context drift.
- Maps the pattern choices to AWS Bedrock AgentCore service components (runtime, memory, gateway, identity, observability) plus Quick Automate for human-approval workflows, positioning these as the managed-service answer to the architectural concerns raised.

## Quote

> The LLM proposes. The physics engine and the human operator dispose.

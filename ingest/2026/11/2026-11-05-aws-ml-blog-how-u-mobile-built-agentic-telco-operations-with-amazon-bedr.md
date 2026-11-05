---
title: How U Mobile built agentic telco operations with Amazon Bedrock AgentCore
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-u-mobile-built-agentic-telco-operations-with-amazon-bedrock-agentcore/
author: Jin Tiong Lim
date_published: '2026-11-04'
date_captured: '2026-11-05'
ingest_method: feed
model: claude-sonnet-5
---

# How U Mobile built agentic telco operations with Amazon Bedrock AgentCore

## Insights

- U Mobile's AiDaH system positions "agentic" AI as distinct from assistive AI by having agents autonomously traverse multiple backend systems (logs, eligibility APIs, knowledge bases), diagnose root causes, and propose remediation — with a human confirming before execution, rather than the human doing the cross-system investigation themselves.
- The orchestration layer uses tiered cost-routing: ~70% of requests resolve via deterministic keyword matching with no LLM call, 20% via a lightweight classifier, and only 10% reach a full orchestrator model — an explicit design choice to minimize model invocation cost at scale.
- Architecture relies on standardized protocols (Model Context Protocol for tool/backend connectivity, Agent2Agent for inter-agent delegation) specifically to make onboarding new operational domains a "repeatable unit of work" (new gateway + tool definitions) rather than bespoke integration engineering each time.
- The organization used an 8-level internal AI maturity model (adapted from TM Forum's Autonomous Networks framework) to track progress, claiming Level 7 ("collaborative multi-agent") reached within 9 months, with Level 8 ("self-healing," no human involvement) as the explicit next target.
- Adoption was treated as a behavior-change problem, not a technology rollout: structured/directed prompt templates (rather than open-ended chat) were used to reduce user hesitation, and formal incorporation into L2 support SOPs (with audit trail requirements) marked the shift from pilot to operational system.
- Reported results (internal measurements, not independently verified): trouble tickets down 84.5% in provisioning/network, 81.6% in general inquiries, 48.7% in billing — achieved by a small team using spec-driven development (Kiro) to scale from 2 pilot agents to 150+ documented scenarios across 8 specialist agents in under a year.

## Quote

> The investigation that used to consume the agent's time now happens before they read the first line.

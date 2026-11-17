---
title: How Duco transforms financial data automation with Amazon Bedrock AgentCore
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-duco-transforms-financial-data-automation-with-amazon-bedrock-agentcore/
author: Rob Gates
date_published: '2026-11-16'
date_captured: '2026-11-17'
ingest_method: feed
model: claude-sonnet-5
---

# How Duco transforms financial data automation with Amazon Bedrock AgentCore

## Insights

- Duco (financial ops platform, 20B transactions/month, 200+ clients) migrated from classical ML (predictive labeling/pattern recognition) to agentic AI on Amazon Bedrock and Bedrock AgentCore, citing classical ML's inability to generalize beyond trained patterns or adapt to novel scenarios/evolving formats.
- Multi-tenant isolation is enforced at every layer — dedicated databases, storage, encryption keys, Kubernetes namespaces, and a dedicated AgentCore runtime/Gateway per tenant — so no shared memory, context, or tooling exists between bank clients, addressing regulatory requirements for data separation.
- Duco uses a deliberate multi-model routing strategy rather than one model: Claude Opus for planning, Sonnet for complex reasoning/exception investigation, Haiku for fast/cheap routing, and Amazon Nova 2 Pro for summarizing tool outputs — framed as matching model capability to task for cost/quality tradeoffs.
- A core technical problem was "context bloat": exposing 300-400 tools per tenant via MCP loaded ~200,000 tokens of tool descriptions before any work began, degrading response quality as conversations lengthened. Their fix (on-demand "skills" loading via custom MCP resource types and three meta-tools: load_skill, find_tool, invoke_tool) cut context to ~20,000 tokens (90% reduction) without changing models or tools.
- New backend microservices auto-register as MCP tools at agent boot time, so deploying a new service gives agents new capabilities automatically — no agent redeployment or reconfiguration needed; access control is still enforced per-user via identity pass-through.
- Reported outcomes: reconciliation deployment 10x faster, 70% lower onboarding costs and 20%+ higher straight-through processing for one global bank, and "thousands" of hours saved in manual exception investigation — figures attributed to AWS/Duco's own reporting, not independently verified.
- Duco frames its roadmap as a human-role progression ("Task Worker → Investigator → Decision Maker") with future plans for agent-to-agent communication, including cross-institution coordination between agents at different banks.

## Quote

> Traditional machine learning models can only amplify what they've already learned — they can't help with the next step or find new problems. — Rob Gates

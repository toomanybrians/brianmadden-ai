---
title: 'Autonomous treasury agents: How Trovata built an AI-native solution on Amazon
  Bedrock and AgentCore'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/autonomous-treasury-agents-how-trovata-built-an-ai-native-solution-on-amazon-bedrock-and-agentcore/
author: Kushal Mangtani
date_published: '2026-11-10'
date_captured: '2026-11-11'
ingest_method: feed
model: claude-sonnet-5
---

# Autonomous treasury agents: How Trovata built an AI-native solution on Amazon Bedrock and AgentCore

## Insights

- Trovata, a treasury/cash-management platform with direct connections to 10,000+ banks, shifted from offering generative-AI "insights" (since 2023) to deploying persistent autonomous agents that act on behalf of treasury teams without human intervention.
- Architecture runs on Amazon Bedrock (LLM inference) plus Bedrock AgentCore (agent orchestration, RBAC, isolated runtime); agents access data only through Trovata's own verified API layer, not direct database access.
- Key design choice: AI is embedded directly into existing treasury objects/workflows rather than offered as a standalone chatbot — framed as "governed path to automation" versus generic AI layered on top.
- Notable go-to-market model: bank-branded deployment, letting banks offer Trovata's AI agents under their own brand without building AI capability in-house — an embedded-ISV distribution strategy enabled by AgentCore.
- Vendor-reported results (customer case studies, not independently verified): $1M+ annualized savings, 5+ hours/day saved per accounting team, 77% reduction in TMS costs, reporting time cut from hours/days to under a minute.
- Trovata publishes a library of "ten agent patterns" from real deployments and claims most treasury teams have 5–15 workflows ready for agent automation today.

## Quote

> It's not a generic chatbot layered on top, but embedded intelligence tied to real treasury objects with a governed path to automation through agents.

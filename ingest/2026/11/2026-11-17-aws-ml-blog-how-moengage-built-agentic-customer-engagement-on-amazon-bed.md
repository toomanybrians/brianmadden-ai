---
title: How MoEngage built agentic customer engagement on Amazon Bedrock AgentCore
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-moengage-built-agentic-customer-engagement-on-amazon-bedrock-agentcore/
author: Ashwin Srinivasan
date_published: '2026-11-16'
date_captured: '2026-11-17'
ingest_method: feed
model: claude-sonnet-5
---

# How MoEngage built agentic customer engagement on Amazon Bedrock AgentCore

## Insights

- MoEngage built "Merlin AI," four categories of agents (embedded studio agents, conversational agents, custom always-on agents, and per-customer decisioning agents) on top of Amazon Bedrock AgentCore, converting its existing OpenAPI specs into MCP tools via the FastMCP framework rather than rebuilding APIs.
- Architecture frames a third interaction layer beyond UI and API: a conversational layer where an agent chains together existing platform capabilities (analytics, segments, content, campaigns) to execute multi-step marketing work that previously required navigating several tools.
- Multi-tenant security approach: JWT-based auth reused from existing APIs, tenant/user context passed via headers (invisible to the model, not as tool arguments) so the model itself never handles identity, plus per-session isolation via AgentCore runtime and separate PII/content guardrails and a validation layer before rendering.
- Reported outcomes (vendor-supplied, unverified): one customer (Glance) saw 50% faster campaign go-live and 38% CTR uplift; platform-wide claims of 60–70% reduction in manual effort on channel/timing/frequency decisions and 20–30% conversion improvement from goal-based decisioning; AI infra costs cut >50% versus self-hosted models via Bedrock's pay-per-token pricing.
- Decisioning agents operate autonomously per individual customer (channel, timing, frequency) while "custom agents" can run under full autonomy or require human review — positioned as giving teams a dial between automated workflows and human-gated execution, with an activity log for auditability.
- Strategic pitch to other software vendors: any company with a mature OpenAPI surface can expose it as MCP tools using a managed runtime, framed as a reusable pattern rather than MoEngage-specific innovation.

## Quote

> MoEngage made its platform agent-ready without rebuilding it.

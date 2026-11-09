---
title: Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore
  – Part 2
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-access-with-okta-cross-app-access-and-amazon-bedrock-agentcore-part-2/
author: Hammad Ausaf
date_published: '2026-11-06'
date_captured: '2026-11-09'
ingest_method: feed
model: claude-sonnet-5
---

# Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore – Part 2

## Insights

- Solves an AI agent governance scaling problem: a one-agent/two-tool topology (direct credential wiring, per-agent token-exchange permissions, duplicated authorization logic) breaks down at enterprise scale (hundreds of agents, thousands of tools). The fix is a centralized Gateway pattern rather than a new governance mechanism.
- Amazon Bedrock AgentCore Gateway becomes the single front door: agents hold no token-exchange or secret permissions; the Gateway redeems Okta's delegation grant (ID-JAG) on the agent's behalf, closing off a credential-sprawl risk where every agent otherwise gets a credential path to every resource it might touch.
- Authorization logic is centralized into Cedar policies evaluated once at the Gateway (default-deny), replacing per-server copy-pasted authorization checks that "drift and can't be audited or changed in one place" — a direct governance/auditability argument for centralization over distributed enforcement.
- Demonstrated multi-runtime portability: a second agent deployed on Amazon EKS (vs. AgentCore runtime) joins under its own Okta identity through its own Gateway, showing the control plane is runtime-agnostic — relevant to enterprises with heterogeneous agent hosting.
- Full audit trail stitches together OpenTelemetry spans (AgentCore Observability/CloudWatch) with Okta's System Log via EventBridge, letting one query trace a specific user's access grant to the specific allow/deny decision it produced, with denial events traceable in near real time (~1 second lag observed).
- Compares two access patterns: Cross App Access (admin-governed, no user consent prompt, revocation nearly immediate — tokens expire within ~5 minutes of suspension) vs. per-user OAuth consent (used for apps like GitHub with their own auth servers) — where revocation only blocks new sign-ins; a stored grant "outlived the suspension" until manually disconnected. Recommends choosing per target application, not enterprise-wide.
- Includes measured latency data: identity/policy checks add ~0.2 seconds at median per tool call, dwarfed by actual tool/MCP server execution time (seconds), suggesting governance overhead is not the bottleneck in practice.

## Quote

> The same user got different authority through different agents, and Okta decided it.

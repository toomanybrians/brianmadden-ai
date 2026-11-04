---
title: ServiceNow on-behalf-of token exchange with Bedrock AgentCore Gateway
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/servicenow-on-behalf-of-token-exchange-with-bedrock-agentcore-gateway/
author: Greg Biegel
date_published: '2026-11-03'
date_captured: '2026-11-04'
ingest_method: feed
model: claude-sonnet-5
---

# ServiceNow on-behalf-of token exchange with Bedrock AgentCore Gateway

## Insights

- The post addresses a specific enterprise agent problem: when AI agents call downstream APIs, they typically authenticate as themselves (the app), not as the end user — breaking audit trails, bypassing user-level permissions, and violating least-privilege principles.
- AWS's fix is native "on-behalf-of" (OBO) token exchange built into Bedrock AgentCore Gateway, which previously required custom-built Lambda interceptors to achieve the same identity-propagation outcome.
- The mechanism: the gateway accepts a user's JWT scoped to the agent's own app registration, then exchanges it via Microsoft Entra ID's OBO flow for a new token scoped to the target API (here, ServiceNow), preserving the original user's identity claims.
- This native OBO support is gated to a specific MCP protocol version (2025-11-25) — gateways built on earlier versions can't use it, indicating this is a recently added platform capability rather than a mature, long-standing feature.
- Though demonstrated with ServiceNow, the pattern is presented as generalizable to any REST API protected by OAuth, positioning AgentCore Gateway as a general-purpose identity-propagation layer for enterprise agent-to-API calls.
- The piece signals that enterprise identity/governance plumbing (audit trails, per-user permissions, access control fidelity) is being treated as foundational infrastructure for agentic AI, not an afterthought — and vendors are racing to productize it rather than leave it to custom integration code.

## Quote

> The native OBO support in AgentCore Gateway removes the need for custom AWS Lambda interceptors to perform token exchanges.

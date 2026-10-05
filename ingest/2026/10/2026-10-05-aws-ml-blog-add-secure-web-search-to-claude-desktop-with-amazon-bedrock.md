---
title: Add secure Web Search to Claude Desktop with Amazon Bedrock AgentCore
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/add-secure-web-search-to-claude-desktop-with-amazon-bedrock-agentcore/
author: Jishnu Dasgupta
date_published: '2026-10-02'
date_captured: '2026-10-05'
ingest_method: feed
model: claude-sonnet-5
---

# Add secure Web Search to Claude Desktop with Amazon Bedrock AgentCore

## Insights

- AWS adds a managed "Web Search" tool to Bedrock AgentCore Gateway, giving Claude Desktop (running on Bedrock) live web search instead of being limited to training-cutoff knowledge — closing a known gap for AI assistants used for work tasks.
- Web Search is positioned as a fully managed, MCP-compatible capability backed by an AWS-operated web index ("tens of billions of documents"), with all query traffic staying inside AWS infrastructure and no external API keys or third-party calls.
- The integration pattern leans on enterprise identity infrastructure: AWS IAM Identity Center (SSO) federates through Amazon Cognito (SAML→OIDC bridge) to issue JWTs that authenticate each gateway request — explicitly designed to slot into existing organizational identity governance rather than requiring separate credentials.
- The setup is non-trivial: requires IAM roles, Cognito user pool/domain, SAML app registration, OAuth app client, and gateway/target provisioning via CLI/Python SDK — this is infrastructure-grade plumbing, not a toggle switch, aimed at enterprise AWS admins.
- Tool use is governed at runtime: when Claude invokes Web Search, Claude Desktop surfaces an explicit approval dialog (Deny / Allow once / Allow for task), showing the query before execution — a human-in-the-loop control point for agentic tool calls.
- AWS frames the identity approach as portable beyond IAM Identity Center — any SAML/OIDC-compatible identity provider can federate through Cognito into the same gateway pattern.
- Feature currently limited to three AWS regions (us-east-1, eu-west-1, ap-northeast-1), indicating early-stage rollout rather than global general availability.

## Quote

> This approach closes the web search gap without introducing third-party dependencies, and all queries stay within your AWS boundary.

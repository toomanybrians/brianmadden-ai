---
title: OpenAI Codex on Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/openai-codex-on-amazon-bedrock/
author: Shivi Bhatia
date_published: '2026-11-11'
date_captured: '2026-11-12'
ingest_method: feed
model: claude-sonnet-5
---

# OpenAI Codex on Amazon Bedrock

## Insights

- AWS positions Codex-on-Bedrock as an enterprise identity/governance problem more than a model-access problem: the core design question is where policy, routing, and observability controls sit (native IAM, AWS-managed gateway, or third-party LLM gateway), not which model is used.
- Recommended default is "Native AWS Access" — using existing AWS IAM Identity Center/workforce SSO — on the logic that the simplest path meeting requirements has the lowest operational overhead; gateways (AgentCore or LLM Gateway) are added only when centralized routing, guardrails, or request-path enforcement are specifically needed.
- A recurring caution: token/telemetry data from Codex's OpenTelemetry client activity should not be conflated with actual cost — only AWS Cost and Usage Report billing data constitutes real spend, and attribution of per-user cost requires correlating identity records, service metrics, and billing separately.
- The piece draws a firm line between "durable guidance" (AGENTS.md, repo-level config) and actual enforcement boundaries (user-level/managed config for model provider, credentials, telemetry) — repository-level settings are explicitly not trusted as governance.
- MCP servers and plugins are treated as distinct trust boundaries requiring org review, credential isolation (kept out of model-provider config), and explicit user confirmation for tools that alter external systems — bundling a tool in an approved plugin doesn't make it auto-approved.
- Rollout is framed as phased: pilot (least-privilege, non-production, two-user identity-isolation test) → expansion → organization-wide standardization, with explicit rollback/cleanup procedures required at each stage before scaling access.

## Quote

> Telemetry does not establish correctness or safety.

---
title: Use Kimi Code CLI with models on Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/use-kimi-code-cli-with-models-on-amazon-bedrock/
author: Alex Thewsey
date_published: '2026-11-20'
date_captured: '2026-11-20'
ingest_method: feed
model: claude-sonnet-5
---

# Use Kimi Code CLI with models on Amazon Bedrock

## Insights

- Kimi Code CLI v2.7.0 (Moonshot AI's open source coding agent) adds a native "bedrock" provider, letting it authenticate via the standard AWS credential chain (named profiles, SSO) instead of requiring a separately managed Amazon Bedrock API key.
- The provider auto-generates short-lived bearer tokens (valid up to 12 hours or session length) behind the scenes, reducing the attack surface of long-term credentials while still requiring careful IAM scoping.
- AWS continues pushing "global" cross-Region inference profiles as the default recommendation for coding-agent workloads without data-residency constraints, citing both broader availability and a 10% price discount versus geographic profiles.
- The example model, Kimi K3.1 Pro Highspeed, supports a 1M-token context window, streaming, configurable reasoning ("thinking"), image input, and client-side tool calling — positioning it as a capable agentic coding model on Bedrock.
- Capability declaration is manual: Kimi Code doesn't auto-detect what a Bedrock-hosted model supports, so users must explicitly configure capabilities (thinking, image_in, tool_use, etc.) per model card.
- The post frames this as reducing operational friction (fewer credentials to manage) for enterprises adopting third-party open-weight coding agents on AWS infrastructure, within AWS's data boundary and compliance programs.

## Quote

> You no longer need a separately managed Amazon Bedrock API key.

---
title: Introducing the Web Search API on Amazon Bedrock AgentCore
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-the-web-search-api-on-amazon-bedrock-agentcore/
author: Shubham Divekar
date_published: '2026-11-11'
date_captured: '2026-11-12'
ingest_method: feed
model: claude-sonnet-5
---

# Introducing the Web Search API on Amazon Bedrock AgentCore

## Insights

- AWS launched a standalone Web Search API (`InvokeWebSearch`) on Bedrock AgentCore, letting code call web search directly via a single signed API call rather than requiring a full AgentCore Gateway/MCP setup — aimed at custom agent loops, non-agent apps (dashboards, fact-checking, monitoring), and teams wanting direct control over retries/caching.
- The API runs on the same web index infrastructure powering Alexa+, Kiro, and Quick — AWS frames this as a reused, production-proven search backend rather than a third-party search engine passthrough (queries stay inside AWS).
- Supports practical filtering controls: domain include/exclude lists (up to 100 each), publication date range filters, and configurable result counts (1–25), returning text extracts plus title/URL/publication time when available.
- Enterprise/security posture is built-in from the start: IAM-only auth (no API keys), CloudTrail logging (though search text/filters aren't logged, only tool name and maxResults), VPC PrivateLink support, and SCP-based cross-account guardrails.
- Positioned explicitly as complementary to, not a replacement for, AgentCore Gateway — gateway remains recommended for multi-tool MCP endpoints, shared org-wide search policy, and JWT-based auth; the API targets simpler/direct integration scenarios.
- Pricing is identical to the gateway's web search usage ($7 per 1,000 queries), with no additional gateway charges when using the direct API — suggesting AWS is optimizing for adoption/integration friction rather than differentiated pricing.
- Framework integration is a priority signal: native support shipped for LangChain (via langchain-aws toolkit) and the AgentCore Python SDK, explicitly citing LangChain/LlamaIndex-style custom orchestration as a target use case.

## Quote

> Authenticate, call, and get results.

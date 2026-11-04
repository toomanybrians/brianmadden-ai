---
title: How Gen Digital built Norton Revamp’s AI-curated News Engine with Amazon Bedrock
  AgentCore Web Search
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-gen-digital-built-norton-revamps-ai-curated-news-engine-with-amazon-bedrock-agentcore-web-search/
author: Iskander Sanchez-Rola
date_published: '2026-11-03'
date_captured: '2026-11-04'
ingest_method: feed
model: claude-sonnet-5
---

# How Gen Digital built Norton Revamp’s AI-curated News Engine with Amazon Bedrock AgentCore Web Search

## Insights

- Gen Digital built Norton Revamp, a generative-AI "professional reputation management" platform, using Amazon Bedrock AgentCore Web Search for real-time grounding instead of custom crawlers, third-party news APIs, or static knowledge bases — citing infrastructure overhead, staleness, vendor lock-in, and data egress as the rejected alternatives' tradeoffs.
- The architecture chains Amazon Nova to generate search queries from user goals/activity, AgentCore Web Search to retrieve cited results within AWS (no data egress), an internal ranking system for relevance/recency/credibility, and Nova Lite to generate grounded content suggestions — with engagement data feeding back into query generation over time.
- The team explicitly split "product AI" (Bedrock/Nova/Web Search powering the product) from "development AI" (Claude-driven code generation, design iteration, documentation) and kept them as separate concerns with different purposes.
- Reported development productivity claims: 70% of UI code AI-generated, 3x faster feature implementation, 90% faster boilerplate, 80% faster documentation, 70% faster test creation, 65% faster UI component generation — offset by AI output review consuming 20-30% of engineering time.
- Human/AI responsibility was deliberately divided: architecture decisions, security reviews, business logic, and personalization algorithms stayed human-owned; AI handled code generation, documentation, test scaffolding, and UI creation; a small engineering team shipped the platform in months with 99.9% uptime and 85% automated test coverage.
- Named best practices for similar real-time-grounding integrations: invest heavily in query-generation prompt engineering, cache selectively with TTLs rather than always re-querying, build feedback loops from user engagement, and layer in source-credibility scoring on top of returned URLs/dates.

## Quote

> Generative AI doesn't replace engineers. It amplifies them.

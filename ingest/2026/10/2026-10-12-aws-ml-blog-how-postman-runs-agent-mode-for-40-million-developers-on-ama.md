---
title: How Postman runs Agent Mode for 40 million developers on Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-postman-runs-agent-mode-for-40-million-developers-on-amazon-bedrock/
author: Srinivas Kini
date_published: '2026-10-09'
date_captured: '2026-10-12'
ingest_method: feed
model: claude-sonnet-5
---

# How Postman runs Agent Mode for 40 million developers on Amazon Bedrock

## Insights

- Postman found model quality/prompt design were not the hardest problems in productionizing an agent; the real difficulty was making an 11-year-old product with interface-driven assumptions "legible" to an agent that reasons over data rather than navigating screens.
- Tool sprawl degrades agent performance: Postman observed tool-selection errors rising once the visible toolset exceeded ~40 tools, even with valid schemas; their fix was dynamic retrieval (vector embeddings narrow 170+ tools down to ~15 relevant ones per task) rather than static exposure of the full catalog.
- For structured data (e.g., service uptime, test results, latency metrics), Postman replaced many narrow single-purpose tools with one schema-aware query tool that lets the agent generate its own SQL-like queries — shifting engineering effort from "build a tool per question" to "model the data well once."
- Missing/incomplete context caused more agent failures than missing capabilities; serializing existing UI/rendering data models into context didn't work, so Postman built dedicated "context handlers" that distill each entity into agent-relevant information, with the context window treated as a actively-managed, truncation-prone budget rather than unlimited space.
- Architecture combines client-side tools (actions in the app), server-side tools (web search, agent-loop management), generic system instructions, and a RAG knowledge base seeded from Postman's Learning Center and updated as features ship.
- On Amazon Bedrock specifically: Postman uses model flexibility across Claude variants (fast model for high-volume/low-latency, larger model for complex reasoning), cross-Region inference profiles (geographic vs. global, chosen per workload for throughput vs. data-residency needs), model-dependent zero-data-retention settings, and tiered prompt caching (one-hour checkpoint for stable system/tool content, five-minute checkpoint for variable context) to control latency and cost.
- Human oversight remains structurally embedded: Agent Mode requires explicit user approval before any action that modifies application state, and Bedrock Guardrails are used to redact PII before prompts reach the underlying LLM.

## Quote

> Past a certain toolset size, exposing more tools can reduce agent effectiveness.

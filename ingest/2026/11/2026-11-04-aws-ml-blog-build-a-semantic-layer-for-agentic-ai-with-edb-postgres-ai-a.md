---
title: Build a semantic layer for agentic AI with EDB Postgres AI and Amazon Bedrock
  AgentCore
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-with-edb-postgres-ai-and-amazon-bedrock-agentcore/
author: Rajesh Nagpal
date_published: '2026-11-03'
date_captured: '2026-11-04'
ingest_method: feed
model: claude-sonnet-5
---

# Build a semantic layer for agentic AI with EDB Postgres AI and Amazon Bedrock AgentCore

## Insights

- EDB Postgres AI's approach embeds the "semantic layer" directly inside the operational Postgres database (via an AIDB extension) rather than as a separate system — business meaning lives in standard SQL COMMENT statements, join paths come from existing foreign keys, and access control uses native Postgres GRANT/row-level security rather than a prompt-based or app-layer permission system.
- Governance is enforced at the database layer, not the model layer: two agent identities with different Postgres column-level grants produce different results to the identical question/prompt/tool-catalog (one can return SSNs, the other hits a Postgres "permission denied" error) — illustrating that access control for agentic systems can be delegated entirely to existing data infrastructure rather than rebuilt in the AI stack.
- A single missing piece of business context (a column comment clarifying that "price" means order total, not unit price) caused an agent to misinterpret a column and return a wildly wrong answer (~$502,529 vs. correct $27,991.66) — a concrete illustration of how semantic/metadata gaps directly cause incorrect agent outputs even with a capable model.
- The architecture requires no new orchestration layer: AWS Bedrock AgentCore connects to EDB's built-in MCP server directly (via an Application Load Balancer) with no Lambda or translation layer needed, since AIDB natively speaks the Model Context Protocol.
- Full audit trail (OpenTelemetry traces of every SQL execution) is captured as queryable rows inside the same Postgres database, meaning observability/audit also lives natively in the data layer rather than a separate monitoring system.
- This is the fifth in a recurring AWS blog series showing the same "customer 360" use case rebuilt on different vendors' semantic-layer technology (previously Stardog, Denodo, AtScale, Strategy Mosaic), positioning EDB's database-native approach against knowledge-graph, data-virtualization, and dimensional-model alternatives.

## Quote

> Postgres grants decide what each agent can run.

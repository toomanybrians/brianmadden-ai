---
title: Bring structured and unstructured data together with Amazon Quick
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/bring-structured-and-unstructured-data-together-with-amazon-quick/
author: Puneeth Komaragiri
date_published: '2026-11-03'
date_captured: '2026-11-04'
ingest_method: feed
model: claude-sonnet-5
---

# Bring structured and unstructured data together with Amazon Quick

## Insights

- Amazon Quick unifies querying across structured data (datasets loaded into an in-memory engine called SPICE) and unstructured data (S3-indexed knowledge bases) through a single conversational agent, rather than requiring separate tools/queries.
- The architecture is three-layered: data sources (S3 knowledge bases + enriched datasets), a "Space" that aggregates sources into a shared workspace, and a chat agent that decides at query time whether to hit the knowledge base, the dataset, or both, returning cited answers.
- Structured-data accuracy depends heavily on manual "enrichment" work: correcting auto-detected data types, writing dataset-level descriptions, custom usage instructions, and per-column descriptions that the agent uses to generate SQL via text-to-SQL — this is positioned as essential, not optional.
- The agent can also generate downstream artifacts (PowerPoint, Excel, Word docs) directly from natural-language prompts, not just answer questions.
- Permissions and governance are emphasized as the customer's responsibility (shared responsibility model): least-privilege S3 access, document-level ACLs decided irrevocably at knowledge-base creation, agent/space sharing is private by default, and built-in guardrails (content safety screening, up to 50 blocked phrases) are framed as one layer, not a substitute for access control.
- Scoping is a recommended best practice: build narrow, purpose-specific Spaces rather than giving an agent broad access to all data sources.

## Quote

> You don't need to know where the data lives.

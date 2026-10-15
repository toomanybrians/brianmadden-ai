---
title: Build self-improving document processing using Amazon Bedrock AgentCore
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-self-improving-document-processing-using-amazon-bedrock-agentcore/
author: Erik Cordsen
date_published: '2026-10-14'
date_captured: '2026-10-15'
ingest_method: feed
model: claude-sonnet-5
---

# Build self-improving document processing using Amazon Bedrock AgentCore

## Insights

- The system uses eight specialized agents across two graph-based workflows (training vs. automation) built on Strands Agents and orchestrated via Amazon Bedrock AgentCore, rather than a single model doing everything.
- Core mechanism for "self-improvement": when extraction fails validation, an Instructions Fixer agent diagnoses the mismatch (e.g., vendor SKU format differs from internal format) and rewrites the extraction prompt, which is then persisted to a vector store for reuse — not model fine-tuning, but prompt/instruction accumulation.
- Known document types route through a faster "automation" path that skips instruction generation entirely; the example shows processing time dropping from 3:49 to 1:30 once a document type is recognized via vector similarity matching (confidence score vs. threshold).
- Cost structure is usage-based and dominated by inference: ~$58/month for 10 training + 1,000 processed documents, with foundation model calls representing ~85% of cost (~$0.055/document) — a concrete per-document economics data point.
- Positioned explicitly against "conventional IDP" (template-based systems) which the post frames as brittle to layout variation and requiring constant manual maintenance per vendor/format.
- Implementation is nontrivial despite "under 20 minutes" deployment claim: requires defining custom JSON schemas, writing validation Lambda functions tied to business rules/reference data, and adapting agent prompts per document type — the generic agents don't work out of the box for new domains.

## Quote

> An agentic approach addresses these challenges. Instead of static templates, AI agents analyze each document, generate extraction instructions, validate results, and learn from corrections automatically.

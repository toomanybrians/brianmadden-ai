---
title: Build agentic retrieval on a Managed Amazon Bedrock Knowledge Base with CDK
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-agentic-retrieval-on-a-managed-amazon-bedrock-knowledge-base-with-cdk/
author: Prabhakar Chandrasekaran
date_published: '2026-10-26'
date_captured: '2026-10-27'
ingest_method: feed
model: claude-sonnet-5
---

# Build agentic retrieval on a Managed Amazon Bedrock Knowledge Base with CDK

## Insights

- AWS has moved Bedrock Knowledge Bases from single-shot RAG (one embed, one retrieve, one generate) to "agentic retrieval," where a reasoning agent decides whether to retrieve, which knowledge source to query, and whether to retrieve again before answering — framed as necessary once questions span multiple corpora or require iterative lookups.
- This agentic capability is only available on AWS's new "Managed" Knowledge Base tier, not the customer-managed/DIY option — a deliberate product gating decision that pushes customers toward the fully-managed (and presumably higher-margin) service to get agentic features.
- The managed tier removes infrastructure work (no vector database to provision, scale, or patch; embedding/reranking is bundled), which the post frames as pure subtraction of operational burden compared to the 2024 DIY approach.
- A key argument: once retrieval becomes agentic, observability stops being optional because the system no longer takes a predictable path — the post claims roughly half of the sample application's provisioned infrastructure exists solely to monitor and evaluate what the agent did, not to serve answers.
- The reference implementation ships both on-demand (notebook-driven) and continuous (sampled, in-production) LLM-as-judge evaluation for correctness, faithfulness, tool-selection accuracy, and response relevance — positioning automated quality scoring as a built-in, not bolted-on, requirement for production agentic systems.
- The post explicitly concedes the trade-off isn't universal: single-index RAG remains cheaper and simpler and is "entirely sufficient" when one corpus holds the answer — agentic retrieval is positioned as warranted only for cross-corpus or ambiguous-routing cases.

## Quote

> Observability stops being a nice-to-have and becomes the only way to know the system works.

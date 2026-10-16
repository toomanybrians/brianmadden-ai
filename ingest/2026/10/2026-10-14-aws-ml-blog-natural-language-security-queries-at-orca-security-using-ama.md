---
title: Natural language security queries at Orca Security using Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/natural-language-security-queries-at-orca-security-using-amazon-bedrock/
author: Deniz Yilmaz
date_published: '2026-10-13'
date_captured: '2026-10-14'
ingest_method: feed
model: claude-sonnet-5
---

# Natural language security queries at Orca Security using Amazon Bedrock

## Insights

- Orca Security built "Discovery AI," a natural-language-to-query agent on Amazon Bedrock that translates plain-English security questions into Sonar (Orca's domain-specific query language covering 900+ cloud resource models), eliminating the need for analysts to know exact schema names, operators, or relationship hierarchies.
- The naive approach — stuffing the full 900+ model schema into one giant prompt on the largest available model — worked qualitatively but was production-unviable: ~2M input tokens per workload, ~60 second latency, and weak accuracy on complex multi-model/nested queries.
- The production fix was a nine-stage pipeline with per-stage model allocation (regex-based quick matcher, guardrail screening, embedding-based example retrieval via Titan, reranking via Cohere Rerank 3.5, LLM-driven schema/model selection, tool-augmented agentic generation via Claude Haiku 4.5, and validation loops) rather than one large model doing everything.
- Results: input tokens cut 93% (2M → 140K), cost down 90%, latency down 75% (60s → 15s), with accuracy improving too — now handling thousands of queries/day in production since March 2026.
- Key technical finding: retrieving a larger candidate pool (top-20 via embeddings) and then reranking down to 5 examples outperformed both pure top-K semantic search (too redundant) and Maximal Marginal Relevance (sacrificed relevance for diversity) — example retrieval was the single biggest lever for accuracy, more so than schema detail.
- Orca built a human-in-the-loop labeling system letting internal experts flag/correct outputs and push fixes directly into the example bank; low-confidence production queries are auto-routed to experts for same-day labeling, improving accuracy on that query class immediately without redeployment.

## Quote

> The labeling UI is the single most important investment we made for long-term quality. — Or Gabay, Director of AI, Orca Security

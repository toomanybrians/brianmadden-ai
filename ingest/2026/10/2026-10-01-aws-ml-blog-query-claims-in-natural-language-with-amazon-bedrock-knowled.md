---
title: Query claims in natural language with Amazon Bedrock Knowledge Bases
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/query-claims-in-natural-language-with-amazon-bedrock-knowledge-bases/
author: Shreya Pawaskar
date_published: '2026-09-30'
date_captured: '2026-10-01'
ingest_method: feed
model: claude-sonnet-5
---

# Query claims in natural language with Amazon Bedrock Knowledge Bases

## Insights

- AWS positions Amazon Bedrock Knowledge Bases as a fully managed RAG layer for unstructured enterprise document sets (PDFs, Word, scanned text), handling parsing, chunking, embeddings, and vector storage without customer-managed infrastructure.
- The new AgenticRetrieveStream API breaks multi-part natural-language questions into sub-queries, runs iterative retrieval passes (up to a configurable max), and self-checks whether evidence is sufficient before generating an answer — a step beyond single-pass RAG.
- Metadata filtering (equals, ranges, boolean, logical AND/OR) lets queries scope by structured fields like claim ID, status, amount, and date, and AWS explicitly recommends deriving authorization/tenant-scoping filters from session context rather than trusting user input — a security design signal for regulated-document use cases.
- Contextual grounding guardrails (configurable grounding/relevance thresholds) can block ungrounded answers outright; AWS frames declining to answer as the safer default in compliance-sensitive domains like insurance claims.
- Self-reported benchmarks (40-question synthetic test) show 90.5% expected-source retrieval recall and 81.2% citation recall overall, improving to 96.7%/90.2% on adversarial questions — but AWS caveats these used the older Retrieve/RetrieveAndGenerate APIs, not the new AgenticRetrieveStream being promoted, and relied on automated LLM grading rather than human review.
- AWS explicitly states citation coverage doesn't guarantee answer completeness, and that broad/unfiltered "inventory" questions were the weakest-performing category — a notable limitation disclosure embedded in otherwise promotional content.

## Quote

> "Treat the results as a baseline for the corpus and metadata schema, not an agentic retrieval benchmark."

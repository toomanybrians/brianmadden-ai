---
title: Prepare web content for Amazon Bedrock Knowledge Bases with Crawl4AI
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/prepare-web-content-for-amazon-bedrock-knowledge-bases-with-crawl4ai/
author: Daxeshkumar Patel
date_published: '2026-11-02'
date_captured: '2026-11-03'
ingest_method: feed
model: claude-sonnet-5
---

# Prepare web content for Amazon Bedrock Knowledge Bases with Crawl4AI

## Insights

- AWS positions this as a two-tier approach to web ingestion for RAG: the managed Bedrock Web Crawler for straightforward public sites, and a custom Crawl4AI preparation step for cases needing finer control (isolating main content, stripping boilerplate, attaching custom metadata).
- The Crawl4AI path is explicitly a batch/offline preparation step — it writes Markdown plus a metadata sidecar to S3, then hands off entirely to Bedrock Knowledge Bases for parsing, chunking, embedding, and indexing; it's distinguished from real-time web access at inference time (e.g., "Web Grounding with Amazon Nova").
- Architecture is intentionally "sample code, not a product": a scheduled Fargate task does crawl → upload → trigger ingestion, with explicit caveats that it lacks retry logic, alarms, or failure notification — a failed or partially-failed ingestion job can silently report success.
- Chunking strategy must be chosen at data-source creation time and can't be changed later (only default fixed-size, fixed-size, or no-chunking for managed knowledge bases; customer-managed bases get semantic/hierarchical chunking options) — a notable rigidity in the managed product.
- The post surfaces real operational costs and risks often glossed over in "quickstart" framing: ongoing Fargate/NAT/KMS/CloudWatch charges, stale S3 content not auto-deleted on re-crawl, and a deletion-protection threshold that can silently skip removing stale documents.
- Explicit responsible-AI/security framing: crawled public web content is treated as untrusted input capable of prompt injection into the RAG context, and the authors recommend guardrails, contextual grounding checks, citations, and human review rather than relying on any single safeguard.

## Quote

> Prepared web pages become model context, so text on a public page can attempt prompt injection through retrieval.

---
title: Amazon S3 Vectors now supports metadata pre-filtering for higher recall on
  filtered searches
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/amazon-s3-vectors-now-supports-metadata-pre-filtering-for-higher-recall-on-filtered-searches/
author: Daniel Abib
date_published: '2026-09-30'
date_captured: '2026-10-01'
ingest_method: feed
model: claude-sonnet-5
---

# Amazon S3 Vectors now supports metadata pre-filtering for higher recall on filtered searches

## Insights

- Amazon S3 Vectors adds "pre-filtering" (ENHANCED index mode) that resolves metadata filters before running similarity search, rather than filtering candidates during/after the vector search (CLASSIC mode) — this changes which subset of vectors the top-k search draws from.
- On highly selective filters (e.g., scoping to one tenant/customer out of millions of records), AWS claims up to 5x improvement in recall of matching vectors versus the prior CLASSIC behavior, using a worked example (400 of 8M tickets).
- New $startsWith operator enables prefix/hierarchical filtering on paths, IDs, and URLs (e.g., scoping to a folder/subtree like "matter-4417/exhibits/"), joining existing equality, range, set-membership, and boolean filter operators.
- Positioned explicitly for multi-tenant RAG, agentic applications (scoping an agent's search to one user's session/owner/document set), legal e-discovery, financial research, and media licensing use cases — framed as a general problem of needing both relevance and correct scoping simultaneously.
- Migration is non-destructive: existing indexes stay on CLASSIC until explicitly switched via UpdateIndexMode; no re-ingestion of vectors or query changes required; no additional cost beyond standard S3 Vectors pricing.
- Technical limits: up to 2KB filterable metadata per vector, up to 100 filter constraints per query (counted per value evaluated), with guidance to consolidate large $in clauses or shard queries in parallel when exceeding that limit.

## Quote

> Higher recall means more of that material reaches the agent, which improves task reliability

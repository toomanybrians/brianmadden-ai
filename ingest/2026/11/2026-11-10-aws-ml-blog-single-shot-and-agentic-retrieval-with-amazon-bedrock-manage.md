---
title: Single-shot and agentic retrieval with Amazon Bedrock Managed Knowledge Base
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/single-shot-and-agentic-retrieval-with-amazon-bedrock-managed-knowledge-base/
author: Siddhant Sahu
date_published: '2026-11-09'
date_captured: '2026-11-10'
ingest_method: feed
model: claude-sonnet-5
---

# Single-shot and agentic retrieval with Amazon Bedrock Managed Knowledge Base

## Insights

- Amazon Bedrock Managed Knowledge Base's `AgenticRetrieveStream` API now exposes a single `maxAgentIteration` parameter (range 0–5) that lets one API serve three distinct modes: retrieval-only (0), single-shot RAG (1), and agentic multi-step retrieval (2–5), rather than requiring separate APIs or code paths for simple vs. complex queries.
- Iteration counting is tied to foundation model calls, not retrieval calls: a value of n allows up to n−1 planning/query-rewrite rounds plus one final answer-generation call; a "speculative" initial retrieval runs free and doesn't count against the limit.
- At maxAgentIteration=0, no LLM is invoked at all (equivalent to calling the plain Retrieve API), and setting `generateResponse=true` at that value is rejected with a 4xx error — explicitly enforcing the mode's no-generation design.
- All three modes (including single-shot and retrieval-only) support querying multiple knowledge bases simultaneously; agentic mode's distinct value-add is query decomposition, evidence evaluation, and iterative refinement, not multi-KB access per se.
- The vendor frames mode selection as application-level logic the developer must implement (not automatic routing by the service) and recommends empirically testing latency/cost/accuracy tradeoffs — including questions documents can't answer — before picking the lowest iteration count that meets quality bar.
- Existing agentic requests using values 2–5 retain unchanged behavior, positioned as a backward-compatible, incremental adoption path.

## Quote

> Selecting the mode is application logic, not automatic routing provided by this parameter.

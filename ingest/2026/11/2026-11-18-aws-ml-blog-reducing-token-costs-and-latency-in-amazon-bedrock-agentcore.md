---
title: Reducing token costs and latency in Amazon Bedrock AgentCore JSON workloads
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/reducing-token-costs-and-latency-in-amazon-bedrock-agentcore-json-workloads/
author: Pallav Gupta
date_published: '2026-11-17'
date_captured: '2026-11-18'
ingest_method: feed
model: claude-sonnet-5
---

# Reducing token costs and latency in Amazon Bedrock AgentCore JSON workloads

## Insights

- A production agent (Flightscape, airline crew scheduling) with 40+ tools and multi-megabyte JSON inputs hit >15 second average latencies because every tool call injected the full payload into the LLM's context window.
- Three composable fixes addressed this: (1) offload heavy JSON artifacts to S3 and persist only lightweight references in agent memory, using content-addressed (SHA-256) keys so identical payloads aren't re-uploaded; (2) page large list results on demand, returning a sample + count + S3 handle instead of the full list; (3) compact oversized dictionary outputs into structural descriptors (counts, key counts, samples) rather than sending them verbatim.
- Reported results: ~71% token reduction and ~80% latency reduction on a benchmark 23MB payload; across 100 sample questions, tokens fell 64% (23.6M→8.5M) and latency dropped 69% (7,930ms→2,461ms).
- The most extreme single-query case (listing valid crews across all validation categories) went from ~165 seconds to 9.9 seconds turn latency, with input tokens cut 75% and output tokens cut 83%.
- Architecture is framework-specific detail: built with LangGraph on Amazon Bedrock AgentCore, using AgentCore Memory for session persistence and AgentCore Observability to measure token/latency before and after.
- Full data remains retrievable — nothing is actually discarded, only deferred; the model gets compact summaries by default and fetches full detail via a handle only when reasoning requires it, framed as no loss of capability.

## Quote

> Context growth became more predictable across turns, and the agent remained responsive even when users asked follow-up questions over large datasets.

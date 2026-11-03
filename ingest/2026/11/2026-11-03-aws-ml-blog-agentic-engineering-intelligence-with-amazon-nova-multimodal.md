---
title: Agentic engineering intelligence with Amazon Nova Multimodal Embeddings and
  Amazon Bedrock AgentCore
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/agentic-engineering-intelligence-with-amazon-nova-multimodal-embeddings-and-amazon-bedrock-agentcore/
author: Aishwarya Gavili
date_published: '2026-11-02'
date_captured: '2026-11-03'
ingest_method: feed
model: claude-sonnet-5
---

# Agentic engineering intelligence with Amazon Nova Multimodal Embeddings and Amazon Bedrock AgentCore

## Insights

- The architecture strictly separates deterministic code from LLM judgment: tolerance-rule Python scores part substitutions reproducibly, while LLMs are confined to retrieval, drafting, and synthesis — the system explicitly never recommends or approves a substitution, keeping the engineer as final decision-maker.
- Multi-agent design uses tiered models by task cost/latency: a small model (Claude Haiku) handles routing classification, mid-tier (Sonnet) runs specialist tools, and a larger model (Opus) only synthesizes when multiple specialists contributed, since synthesizing a single answer added latency with no quality gain.
- Amazon Nova Multimodal Embeddings is used two ways — shared text/image semantic space for retrieval, and cosine similarity between part photos for visual comparison — enabling queries like finding a part from an uploaded chart image, something text-only retrieval pipelines can't do.
- A concrete engineering lesson: indexing whole datasheet pages performed poorly (3/7 correct) because boilerplate dominated embeddings; cropping charts before indexing fixed this (7/7 correct) — a specific, reusable retrieval tuning insight.
- The team stresses "fail loud, not silent" for fallback paths: a missing permission caused image-query to silently fall back to text search, producing confidently wrong answers; logging explicit failure warnings was the fix.
- Evaluation via AgentCore's LLM-as-judge framework scored trace-level quality highly (≥0.95 on correctness, helpfulness, faithfulness) but Goal Success Rate was lower (0.892) specifically because the evaluator penalizes the agent's safety-correct refusals to approve substitutions as "unmet goals" — a flagged measurement/alignment mismatch.
- The underlying pattern (deterministic scoring + specialist agents + multimodal retrieval) is framed as domain-agnostic: swapping parts data, a requirements schema, and the corpus source is enough to adapt it beyond aerospace reaction wheels.

## Quote

> The engineer remains the decision-maker throughout, because the system assembles evidence and drafts documents without ever approving a substitution on its own.

---
title: Generate presentations with Amazon Bedrock AgentCore
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/generate-presentations-with-amazon-bedrock-agentcore/
author: Ian Lunsford
date_published: '2026-10-14'
date_captured: '2026-10-15'
ingest_method: feed
model: claude-sonnet-5
---

# Generate presentations with Amazon Bedrock AgentCore

## Insights

- AWS's reference architecture for document-generation agents uses a "supervisor agent" pattern: one orchestrator (built on Strands Agents, an open-source SDK) routes requests to narrow, single-purpose tools (PPTX generation, summarization) rather than one monolithic agent handling everything — framed as the extensible design choice.
- The pipeline chains multiple specialized models rather than one: Claude Sonnet 4.6 for content/reasoning, Claude Haiku 4.5 for cheaper document parsing, Titan Text Embeddings v2 for vector search, and Stability AI's Stable Image Inpaint for slide visuals — illustrating a "right-sized model per task" cost/performance approach.
- Reported benchmarks: 70–90 seconds end-to-end to turn a 90-page annual report into a 6-slide deck with two AI-generated images, at roughly $0.04 in model costs per generation (image generation being the majority of that cost); knowledge-base ingestion for a 1.3MB PDF took under 2 minutes.
- RAG grounding (via Bedrock Knowledge Bases + OpenSearch Serverless vector search) is positioned explicitly as the hallucination-mitigation mechanism, not a nice-to-have — content generation is tied to retrieved source chunks rather than model memory.
- The architecture bakes in enterprise compliance/governance scaffolding as first-class: content-safety guardrails (input filtering, output monitoring, PII detection/anonymization), tenant isolation via STS role assumption, VPC isolation, KMS encryption, and session-level container isolation per user — signaling AWS's enterprise-readiness pitch extends well beyond the AI task itself.
- Operational friction is notable: default API Gateway timeouts (29s) can't support the actual generation time (70–90s), forcing an async/streaming/polling pattern instead of simple synchronous REST calls — a concrete engineering constraint when deploying agentic workflows that take longer than typical API calls.

## Quote

> This approach reduces presentation creation time while grounding content in source documents.

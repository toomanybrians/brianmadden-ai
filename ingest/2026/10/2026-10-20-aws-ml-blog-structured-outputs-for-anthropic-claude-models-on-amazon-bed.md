---
title: Structured outputs for Anthropic Claude models on Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/structured-outputs-for-anthropic-claude-models-on-amazon-bedrock/
author: Anshika Saxena
date_published: '2026-10-19'
date_captured: '2026-10-20'
ingest_method: feed
model: claude-sonnet-5
---

# Structured outputs for Anthropic Claude models on Amazon Bedrock

## Insights

- Amazon Bedrock now enforces JSON schema compliance during token generation itself (constrained decoding) rather than validating after the fact, shifting output formatting from probabilistic to deterministic for all Claude models on Bedrock.
- Two mechanisms are offered: JSON Schema output format for structured data responses, and "strict tool use" for guaranteeing tool-call parameters match a schema exactly — the latter aimed specifically at agentic/multi-step workflows.
- Vendor claims this eliminates the need for custom parsing, retry logic, and post-processing in production pipelines, and can reduce output token count (and thus inference cost) by constraining responses to only schema-defined fields.
- Under the hood, new schemas trigger a one-time "grammar compilation" step with added latency; compiled grammars are cached per-account for 24 hours, incentivizing schema reuse and minimal/stable schema design.
- Notable technical limits: no support for recursive schemas, external $ref references, numeric/string length constraints, or minLength/maxLength — these are silently accepted but not enforced, meaning developers must still validate some constraints client-side despite the "no validation needed" framing.
- Feature is positioned around three use cases: structured data extraction (invoices, contracts, transcripts), reliable agent tool calls in multi-step workflows, and at-scale classification/routing (tickets, leads, sentiment).

## Quote

> Structured outputs use constrained decoding to enforce your JSON schema during token generation, not after the fact.

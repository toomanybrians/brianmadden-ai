---
title: How MoEngage turned over 400 APIs into agent tools with AgentCore Gateway
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-moengage-turned-over-400-apis-into-agent-tools-with-agentcore-gateway/
author: Nikhil Kumar
date_published: '2026-10-29'
date_captured: '2026-10-30'
ingest_method: feed
model: claude-sonnet-5
---

# How MoEngage turned over 400 APIs into agent tools with AgentCore Gateway

## Insights

- MoEngage rejected a "per-team MCP server" model (20+ servers) because it would require every product team to maintain protocol expertise, deploy infrastructure, and reconcile cross-domain agent calls across servers — instead it centralized MCP ownership in one AI Platform team, with product teams only responsible for well-described OpenAPI specs.
- The case highlights a concrete scaling limit for agent tool catalogs: ~400 tools at roughly 50 tokens of schema each exceeds 20,000 tokens per connection, which the team solved not with client-side filtering (deemed a non-authorization-boundary) but server-side Cedar policy evaluation that filters tools/list *before* it's serialized, so restricted agents never see tools they can't call.
- A key architectural decision was keeping identity (tenant, user, role, database context) out of LLM-visible tool parameters entirely — injected as headers by the calling service rather than exposed as model-settable arguments, to prevent prompt-based identity manipulation.
- Semantic tool search (agents describe intent, retrieve candidate tools dynamically) replaced hardcoded tool references and a custom discovery layer; this also made the system resilient to tool renames since matching is on description, not identifier.
- Using AWS's AgentCore Gateway (managed MCP generation from OpenAPI specs + managed egress via VPC Lattice) avoided building a custom tool-generation pipeline, policy engine, and per-region networking — MoEngage frames this as avoiding "undifferentiated work."
- Reported outcomes: ~400 APIs across 25 teams and 7 AWS regions now serve 10 internal agents; claimed ~6 months of engineering effort saved and new API onboarding reduced from days to hours (vendor-reported, unaudited figures).

## Quote

> Individual engineering teams do not implement MCP. Teams build REST APIs and declare which operations should be tools.

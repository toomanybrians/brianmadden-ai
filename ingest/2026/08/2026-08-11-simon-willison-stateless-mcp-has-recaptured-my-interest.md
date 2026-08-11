---
title: Stateless MCP has recaptured my interest
source: Simon Willison's Newsletter
source_id: simon-willison
source_url: https://simonw.substack.com/p/stateless-mcp-has-recaptured-my-interest
author: Simon Willison
date_published: '2026-08-01'
date_captured: '2026-08-11'
ingest_method: feed
model: claude-sonnet-5
---

# Stateless MCP has recaptured my interest

## Insights

- MCP 2.0 (the "stateless" spec, dated 2026-07-28) collapses the old two-request session-based protocol (initialize + tool call, tracked via session IDs) into a single stateless HTTP request, simplifying both client and server implementations.
- Removing server-side session state makes MCP servers easier to scale as normal web applications, since there's no need to route repeated requests to the same backend machine.
- The author frames this as a shift back toward MCP after 2025 interest waned in favor of "Skills" and giving agents raw shell/curl access — he argues open-ended shell access is riskier and requires stronger models, while discrete MCP tools are easier to audit, constrain, and can be driven even by smaller, laptop-scale models.
- Three tools were built quickly to exploit the simpler spec: mcp-explorer (a stateless CLI for probing any MCP server's tools/schemas), datasette-mcp (a plugin exposing read-only SQL query tools over a Datasette instance to agents/chat tools), and an alpha llm-mcp-client integration for his LLM CLI tool.
- This reflects a broader design tension in agentic tooling: structured, permissioned tool protocols (MCP) versus flexible-but-riskier general shell/agent access — with security/auditability being the deciding factor for enterprise-safe agent deployments.
- The piece ties back to the "lethal trifecta" concept (prompt injection + data access + exfiltration risk), positioning protocol design choices as a direct security/governance issue for organizations deploying AI agents.

## Quote

> Giving an agent a shell environment with the ability to access the internet is fraught with risk.

---
title: Work management context for AI agents with Smartsheet MCP on AWS
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/work-management-context-for-ai-agents-with-smartsheet-mcp-on-aws/
author: Galina Jordanowa
date_published: '2026-10-20'
date_captured: '2026-10-21'
ingest_method: feed
model: claude-sonnet-5
---

# Work management context for AI agents with Smartsheet MCP on AWS

## Insights

- Smartsheet released a generally available Model Context Protocol (MCP) Server exposing 40+ tools for reading, writing, and managing sheets, rows, columns, and automations via natural language, rather than through app-specific UI.
- AWS offers two distinct integration paths into the same MCP server: Amazon Quick (a managed, org-wide agentic workspace for business/project users, requiring OAuth app registration) and Kiro (a lightweight, developer-scoped agentic IDE integration requiring just a config file and personal access token).
- The server is engineered to return structured, token-efficient context (row relationships, column types, cell history, comments) rather than raw API payloads — a design choice framed as reducing cost/latency at scale across many agent queries.
- Governance model reuses Smartsheet's existing REST API permission layer: user-level access enforcement, org-level toggles for AI features, configurable write-tool access by group, and FQDN-based (not IP) firewall allowlisting — positioned as "not a new trust boundary."
- Smartsheet states the MCP server does not store prompts; it only sees structured tool calls and their results, not prompt content itself.
- Suggested workflow patterns include agents reconciling task status between issue trackers and project plans, aggregating health signals across reports/dashboards into briefings, and auto-generating audit-trail comments after every write action.

## Quote

> It’s not a new trust boundary.

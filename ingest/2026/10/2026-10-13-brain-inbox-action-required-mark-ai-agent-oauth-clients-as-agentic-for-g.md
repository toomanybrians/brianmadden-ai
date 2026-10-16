---
title: '[Action Required] Mark AI agent OAuth clients as agentic for Google Workspace
  MCP by Nov 11, 2026'
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: The Google Workspace Team <workspace-noreply@google.com>
date_published: '2026-10-12'
date_captured: '2026-10-13'
ingest_method: email
model: claude-sonnet-5
---

# [Action Required] Mark AI agent OAuth clients as agentic for Google Workspace MCP by Nov 11, 2026

## Insights

- Google is introducing an explicit "agentic" classification (`is_agentic`) for OAuth clients, creating a formal technical distinction between AI agent traffic and traditional app traffic within its developer ecosystem.
- Starting Nov 11, 2026, Google Workspace MCP servers (exposing Gmail, Drive, Calendar, etc. to external AI agents via the open Model Context Protocol) will only accept requests from OAuth clients explicitly marked as agentic — all other requests are rejected.
- The agentic designation becomes permanent/locked on Nov 12, 2026; after that, changing a client's status requires creating an entirely new OAuth Client ID rather than modifying the existing one.
- Google frames agentic clients as subject to distinct security controls ("agent access controls"), and recommends developers split traffic into separate OAuth clients when an app serves both AI agent and non-agent use cases.
- This signals that major platform providers are beginning to build governance/permissioning infrastructure specifically for AI agents as a distinct category of software actor, separate from conventional API-calling applications.
- Apps using only standard Workspace REST APIs (Gmail API, Drive API) are unaffected, indicating the change targets the emerging agent-to-enterprise-data access layer specifically, not general API integrations.

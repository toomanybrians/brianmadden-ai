---
title: Most security models assume the person using an application is, well, a person.
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/citrix/status/2117965139668275404
author: '@citrix'
date_published: '2026-11-04'
date_captured: '2026-11-05'
ingest_method: x
model: claude-sonnet-5
---

# Most security models assume the person using an application is, well, a person.

## Insights

- Security models built for human users break down with AI agents: agents inherit a user's full identity and standing access, but not their judgment about when *not* to use it — meaning dormant/unused permissions become exploitable through a single bad inference or manipulated input.
- Illustrative scenario: an agent resolving a supplier payment dispute uses its human owner's vendor-edit permissions to "fix" a bank-detail mismatch and release funds — a classic fraud pattern a human would have flagged, but the agent had no equivalent instinct to pause and verify.
- Existing controls (identity providers, app permissions, AI platform governance) each function correctly in isolation but none has visibility into the *task* an agent was given, so none can judge whether a specific action is appropriate — described as a structural governance gap rather than a tooling failure.
- Argues enterprises won't standardize on a single agent platform, so governance needs to live at the point where agents touch applications/credentials, not inside any one vendor's agent environment.
- Proposes governance requires upfront answers to four questions before an agent starts work: whose authority it carries, what the task actually requires, what stays off-limits, and when a human approval checkpoint is needed.
- Citrix announces (planned this quarter) three SecurAccess capabilities: detecting when a browser is being driven by automation vs. a human, restricting agents via MCP to only the specific tools/actions a task needs (not full user access), and AI-enhanced session monitoring to flag risky agent actions for audit.

## Quote

> Authority granted at the scope of a person, not the scope of a task, is authority nobody has evaluated.

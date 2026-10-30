---
title: Building intent-driven UI testing with Amazon Nova Act
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-intent-driven-ui-testing-with-amazon-nova-act/
author: Sakthi Chellapparimanam
date_published: '2026-10-29'
date_captured: '2026-10-30'
ingest_method: feed
model: claude-sonnet-5
---

# Building intent-driven UI testing with Amazon Nova Act

## Insights

- Epsilon (Publicis Groupe) built UI testing as a managed, multi-tenant platform capability using Amazon Nova Act (natural-language test authoring) layered on top of its existing Playwright regression suite rather than replacing it — framed as additive coverage, not a fix for something broken.
- The core technical pattern: Nova Act drives a headless browser via Amazon Bedrock AgentCore Browser Tool over a Chrome DevTools Protocol WebSocket, authenticated through standard AWS IAM/STS cross-account roles rather than separate API keys, fitting into Epsilon's existing multi-tenant security model.
- Natural-language test steps (e.g., "Confirm the rewards balance is visible") are claimed to survive cosmetic UI changes that break selector-based scripts, and are readable/reviewable by non-engineers like PMs and QA leads — potentially broadening who can author and own tests.
- Reported internal benchmarks: 4–6x faster test authoring (5–10 minutes vs. 30–90 minutes for equivalent Playwright scripts), zero DOM/selector inspection needed, and 100% pass rate on replayed "saved trajectories" after an initial exploratory phase (4–5 prompt iterations).
- A notable operational detail: Nova Act's signing endpoint always targets us-east-1 regardless of the browser session's region, requiring isolation of the Nova Act runtime in a separate service/container to avoid dependency conflicts.
- Unplanned benefit cited: built-in audit trail (AWS CloudTrail + session recording) simplified debugging and compliance conversations — something the team didn't originally design for but found valuable.

## Quote

> Nova Act let us turn UI testing from a brittle, selector-chasing chore into a managed platform capability.

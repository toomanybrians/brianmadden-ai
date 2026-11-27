---
title: Introducing Claude Ship
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://sischool.substack.com/p/introducing-claude-ship
author: Super Intelligence School <sischool@substack.com>
date_published: '2026-11-26'
date_captured: '2026-11-27'
ingest_method: email
model: claude-sonnet-5
---

# Introducing Claude Ship

## Insights

- Claude Ship is positioned as an agent that handles post-PR workflow: reviewing pull requests against surrounding code, investigating failing CI checks, and pushing fixes when reviewers flag problems.
- Depending on team policy, the agent can be authorized to approve changes itself, not just propose fixes — raising an explicit governance question about who signs off when AI both fixes and clears a change.
- Adoption is designed to start bottom-up: individual developers/tech leads can trial it on their own PRs without admin access, then save reusable review rules/workflows to the repo for teammates.
- Full automation across a team's PRs requires admin-level setup, suggesting a staged rollout model from individual experimentation to org-wide enforcement.
- The product includes policy-authoring features, e.g. requiring a second engineer's sign-off for sensitive code (billing cited as example), plus an "observe mode" to test policy decisions before enforcement.

## Quote

> If Claude fixes a bug in your billing code and every check passes, whose approval should it take to ship?

---
title: Accelerating software delivery with agentic QA automation using Amazon Nova
  Act – Part 3
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/accelerating-software-delivery-with-agentic-qa-automation-using-amazon-nova-act-part-3/
author: Vinicius Pedroni
date_published: '2026-10-28'
date_captured: '2026-10-29'
ingest_method: feed
model: claude-sonnet-5
---

# Accelerating software delivery with agentic QA automation using Amazon Nova Act – Part 3

## Insights

- QA Studio (AWS's agentic QA reference solution built on Amazon Nova Act) adds an organizational layer once test automation scales past a single team: "applications" group tests, assign ownership, and surface health metrics so coverage status is visible at a glance rather than buried in a flat list of hundreds of tests.
- Health is quantified via a 0–100 score derived from pass rate minus a flakiness penalty, explicitly designed to prevent tests that pass-but-flip from looking falsely healthy — a nod to the real failure mode of automated test suites at scale (alert fatigue / false confidence).
- Access control is modeled as five cumulative roles (Admin, Team Lead, Editor, Executor, Viewer) scoped per-team, with applications owned by exactly one team — permissioning is handled at the application level rather than per individual test, which is framed as the practical lesson for scaling any shared automation tooling.
- Cross-team sharing uses a "ceiling rule": a user's effective permission on a shared resource is the lower of their own role or the grant level, preventing over-sharing from silently escalating someone's access.
- Architecturally, the whole system runs on standard AWS primitives (Cognito groups mapped to roles, DynamoDB single-table design, CloudWatch custom metrics, Lambda/API Gateway enforcing two-layer access checks) — illustrating how "agentic" tooling in production still depends on conventional identity/metrics/data infrastructure, not just the AI agent itself.
- The underlying problem framed by the post: as AI-driven test authoring removes the bottleneck of writing tests, the new bottleneck becomes organizational — ownership, accountability, and access governance across teams.

## Quote

> Test authoring stops being the bottleneck. Organizing tests and controlling who can touch them becomes the work.

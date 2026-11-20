---
title: How the BMW Group governs hundreds of agents across thousands of developers
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-the-bmw-group-governs-hundreds-of-agents-across-thousands-of-developers/
author: Dr. Jens Kohl
date_published: '2026-11-19'
date_captured: '2026-11-20'
ingest_method: feed
model: claude-sonnet-5
---

# How the BMW Group governs hundreds of agents across thousands of developers

## Insights

- BMW frames agent governance as needing to survive at enterprise scale (12,500+ developers, ~500M lines of code, 1,300+ microservices) by externalizing rules — auth, rate limiting, content filtering — at an integration layer (MCP gateway, central registry) rather than embedding them in individual agent codebases, so governance persists through framework/model changes.
- Trust is assigned per workflow step, not per agent, via three graduated autonomy levels (human-in-the-loop, human-on-the-loop, autonomous-within-guardrails), with deterministic enforcement (CI/CD gates, policy-as-code) rather than relying on prompt instructions to constrain agent behavior.
- A three-tier composition hierarchy — MCP tools (atomic capabilities), skills (domain-bundled tool chains), and flows (end-to-end business processes) — is proposed as the architectural pattern for composability, modeled on microservices-era patterns in distributed systems.
- Observability for agents is reframed beyond uptime/HTTP status to whether outputs are "faithful and policy-compliant," requiring ground-truth evaluation datasets built before implementation and instrumented via OpenTelemetry spans for intent tracing, verification/evaluation-as-CI, and model-routing telemetry.
- The org model is "bottom-up with central curation": teams build tools/skills for local needs and contribute them to a shared registry, while a central team enforces automated governance checks and supplies reusable governance-as-code modules — explicitly designed to avoid both rigid central mandates and uncoordinated "AI islands."
- A dedicated "governance agent" audits other agents pre-deployment and at runtime for scope creep, prompt bloat, tool misuse, and performance degradation, but recommendations require human sign-off (a stated four-eyes/accountability principle) before being applied.
- Reported outcomes (unverified/self-stated) include reduced development costs from reusable templates, faster time-to-production via standardized interaction models, and improved quality from pipeline-enforced patterns.

## Quote

> Scaling agentic AI across a large organization cannot be achieved by isolated teams.

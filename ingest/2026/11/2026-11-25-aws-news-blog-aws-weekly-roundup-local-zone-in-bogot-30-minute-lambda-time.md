---
title: 'AWS Weekly Roundup: Local Zone in Bogotá, 30-minute Lambda timeout, and more
  (November 24, 2026)'
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-local-zone-in-bogota-30-minute-lambda-timeout-and-more-november-24-2026/
author: Daniel Abib
date_published: '2026-11-24'
date_captured: '2026-11-25'
ingest_method: feed
model: claude-sonnet-5
---

# AWS Weekly Roundup: Local Zone in Bogotá, 30-minute Lambda timeout, and more (November 24, 2026)

## Insights

- AWS Lambda's synchronous Event Function timeout doubled from 15 to 30 minutes after an eight-year plateau; AWS explicitly names agentic workloads that chain model and tool calls as a driver, alongside media transcoding and file conversion.
- Lambda now supports GPU-backed inference (G4dn–G6e instances) via OCI container images, with AWS handling driver/CUDA/AMI management; pricing layers EC2 instance cost + 9.75% GPU management fee + $0.20 per million requests.
- Several releases this week target "agent identity and permissioning" as a distinct problem: AWS STS's new GetScopedCredentials lets a workload derive narrower, time-limited credentials for sub-agents, guaranteeing permissions only ever shrink, never expand, with full CloudTrail logging.
- Amazon Cognito added dynamic client registration (RFC 7591) so AI agents/MCP clients can self-register at runtime rather than requiring pre-provisioned app clients — infrastructure aimed at scaling agent fleets.
- CloudFront Functions gained outbound network calls (cf.fetch()), with AWS's own example being checking an AI agent's permissions/usage budget at the edge before a request reaches an API or MCP server.
- External case studies cited: BMW enforces agent governance as deterministic code in CI/CD pipelines (outside the agent's own reasoning loop, so prompts can't override it) across 12,500+ developers; Cognition runs Devin coding-agent sessions on ephemeral EC2 Mac VMs, with ~90% releasing idle VMs and resuming from snapshot in seconds.

## Quote

> AWS treats governance as deterministic code outside the agent's reasoning loop... so neither the agent nor its prompts can override it.

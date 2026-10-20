---
title: 'AWS Weekly Roundup: AWS Lambda Web Functions, Amazon S3 on the Vercel Marketplace,
  and more (October 19, 2026)'
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-lambda-web-functions-amazon-s3-on-the-vercel-marketplace-and-more-october-19-2026/
author: Daniel Abib
date_published: '2026-10-19'
date_captured: '2026-10-20'
ingest_method: feed
model: claude-sonnet-5
---

# AWS Weekly Roundup: AWS Lambda Web Functions, Amazon S3 on the Vercel Marketplace, and more (October 19, 2026)

## Insights

- AWS Lambda now supports "Web Functions," a form factor that runs standard HTTP servers (Express, Hono, Fastify, Next.js) directly with no adapter or event-handler rewrite — deployed via CLI with a live HTTPS URL in under a minute.
- Lambda's three form factors (Event Functions, Web Functions, MicroVMs for untrusted-code sandboxes) now share the same Firecracker isolation and can compose within one application, with CPU-time (not wall-clock) billing and up to 128 concurrent requests per warm execution environment.
- A featured piece on agent governance argues human-in-the-loop review of every agent action breaks down at scale because reviewers stop catching real issues; the proposed alternative is a four-part framework (scope, know, bound, observe) with limits enforced externally via Amazon Bedrock AgentCore gateway policies, not left to the agent's own reasoning.
- AWS's automated-reasoning approach (already used in IAM at scale) is being positioned as the mechanism for formally verifying agent policy rules rather than relying on runtime judgment.
- Separately, AWS reports its autonomous security-testing agent exploited 33 of 37 newly disclosed CVEs end-to-end; its two failures involved the agent crashing/destroying the target before it could complete the task — flagged as evidence that strong autonomous offensive capability carries destructive risk.
- S3 is now provisionable from inside the Vercel dashboard/v0 tool using short-lived OIDC-to-STS credential exchange rather than static keys, continuing a pattern of infrastructure provisioning moving into the tools developers already use.

## Quote

> An agent cannot turn off a control it does not run.

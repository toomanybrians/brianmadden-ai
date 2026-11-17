---
title: 'AWS Weekly Roundup: AWS Nitro Sandboxes, AWS Emulator, and more (November
  16, 2026)'
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-aws-nitro-sandboxes-aws-emulator-and-more-november-16-2026/
author: Daniel Abib
date_published: '2026-11-16'
date_captured: '2026-11-17'
ingest_method: feed
model: claude-sonnet-5
---

# AWS Weekly Roundup: AWS Nitro Sandboxes, AWS Emulator, and more (November 16, 2026)

## Insights

- AWS Emulator (now GA) lets developers and coding agents exercise AWS API calls locally without provisioning cloud resources or needing an AWS account; it supports CLI/SDK calls via an HTTPS endpoint but has no additional fee. Coverage is partial — unimplemented calls return HTTP 501, and it doesn't replicate IAM/resource-policy enforcement or cross-account/cross-Region behavior, so production validation still requires testing on real AWS infrastructure.
- The stated rationale for the Emulator is giving coding agents "concrete feedback" in a fast local loop (run, inspect, revise) rather than waiting on cloud provisioning — framed as a core enabler for agentic coding workflows.
- AWS Nitro Sandboxes bring hardware-level isolation (VM boundary) to individual EKS pods or ECS tasks sharing a single EC2 instance, with an "isolated" mode and a "confidential" mode (adds protection from node operators plus cryptographic attestation) — explicitly pitched for use cases including "agents executing generated code."
- Amazon Cognito now supports OAuth 2.0 token exchange, letting a user's token be swapped for a narrower-scoped token for a downstream service, including an "act claim" identifying an intermediary — positioned as making agent-based delegation (an agent calling a backend on someone's behalf) more explicit and less reliant on forwarding original credentials.
- The next-generation Amazon Bedrock AgentCore runtime is now default: agent sessions start in under 2 seconds, scale to 8 vCPU/32GB, scale to zero when idle, and reduce memory billing by up to 68%, while keeping each session in its own isolated microVM.
- A linked guide addresses measuring agent ROI/cost-per-task on Bedrock, tracking cost through repeated calls, reasoning, caching, and human review against a documented baseline — emphasizing that illustrative prices should be reconciled against actual billing data for a given workload.

## Quote

> A second delivery of the same message can reveal more about an application than its happy-path demo.

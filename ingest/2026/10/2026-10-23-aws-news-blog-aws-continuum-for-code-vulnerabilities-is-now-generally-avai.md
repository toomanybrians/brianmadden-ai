---
title: AWS Continuum for code vulnerabilities is now generally available
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/aws-continuum-for-code-vulnerabilities-is-now-generally-available/
author: Esra Kayabali
date_published: '2026-10-22'
date_captured: '2026-10-23'
ingest_method: feed
model: claude-sonnet-5
---

# AWS Continuum for code vulnerabilities is now generally available

## Insights

- AWS Continuum for code vulnerabilities (GA) is an AI-driven security service that moves beyond raw scanner output: it validates whether vulnerabilities are actually exploitable, ranks them by business impact, and generates proposed fixes as pull requests rather than just severity scores.
- It builds a "context graph" from code repositories plus AWS environment data (via an in-account collector reading AWS Config/network config) to determine reachability, ownership, service dependencies, and which systems touch sensitive data (customer stores, payment pipelines, auth services).
- Each finding gets an evidence level (e.g., "static proven") and, where reproducible, is exploited in an isolated sandbox to generate proof-of-concept code and an attack path/blast-radius assessment — replacing hours of manual investigation.
- All remediation currently requires human approval before shipping (patch, dependency upgrade, or config change delivered as a PR); AWS frames future versions as allowing autonomous action within user-defined guardrails and confidence thresholds (test coverage, scope, historical success rate).
- Explicit framing ties the product to an arms-race narrative: frontier AI models let attackers turn disclosed vulnerabilities into working exploits "in minutes," while the same AI tooling also increases the volume of findings defenders must triage.
- Currently limited in availability (US East N. Virginia, US West Oregon only), with code source integration via GitHub or S3, signaling an early/narrow GA rather than broad platform rollout.

## Quote

> Using frontier artificial intelligence (AI) models, threat actors can turn a vulnerability disclosure into working exploit code in minutes.

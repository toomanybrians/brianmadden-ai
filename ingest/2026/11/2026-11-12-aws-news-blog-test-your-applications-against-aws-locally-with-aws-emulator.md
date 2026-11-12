---
title: Test your applications against AWS locally with AWS Emulator
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/test-your-applications-against-aws-locally-with-aws-emulator/
author: Daniel Abib
date_published: '2026-11-11'
date_captured: '2026-11-12'
ingest_method: feed
model: claude-sonnet-5
---

# Test your applications against AWS locally with AWS Emulator

## Insights

- AWS Emulator is a new local, HTTPS-based emulator for AWS services, designed explicitly to support fast iteration loops for coding agents (e.g., Kiro, Claude Code) that can create and test AWS resources without deploying to a real account or waiting on a Region.
- It's built from the same AWS API models used by the SDKs, so request/response shapes and errors match AWS; coverage is tracked via public "fidelity tests" scored as k-of-n per service, with scores expected to fluctuate as more tests are added.
- Notably, the emulator itself is built and maintained by AI agents (via Amazon Bedrock AgentCore Runtime Instances) in a pipeline where one set of agents detects API/behavior gaps and another implements fixes, with a separate adversarial security agent reviewing changes before release — an example of AWS using agentic workflows for its own internal engineering/maintenance.
- Explicit limitations are called out: it doesn't enforce IAM/resource policies like real AWS, operates as a single flat account with no cross-account/cross-Region behavior, and AWS explicitly warns not to use it to validate security — production security testing must still happen against real AWS.
- Positioned as free (no service fee beyond actual AWS usage), signaling AWS using local dev-tooling to lower friction in the agent-driven coding workflow rather than as a monetized product.

## Quote

> AWS Emulator is built and maintained by agents from the AWS API models using Amazon Bedrock AgentCore Runtime Instances.

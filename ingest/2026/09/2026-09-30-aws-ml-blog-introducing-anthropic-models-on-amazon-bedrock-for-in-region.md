---
title: Introducing Anthropic models on Amazon Bedrock for in-region inference in Seoul
  and Singapore
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-anthropic-models-on-amazon-bedrock-for-in-region-inference-in-seoul-and-singapore/
author: Aamna Najmi
date_published: '2026-09-30'
date_captured: '2026-09-30'
ingest_method: feed
model: claude-sonnet-5
---

# Introducing Anthropic models on Amazon Bedrock for in-region inference in Seoul and Singapore

## Insights

- AWS added in-region inference for Anthropic models on Amazon Bedrock: Claude Opus 5 and Claude Sonnet 5 in Seoul (ap-northeast-2), and Claude Sonnet 5 in Singapore (ap-southeast-1).
- In-region inference guarantees requests and data are processed entirely within the specified AWS Region for the full request lifecycle, with no cross-Region routing layer — targeted at strict data residency needs (named use cases: financial services, healthcare, public sector).
- This differs from Bedrock's cross-Region inference profiles: throughput is bounded by the single Region's capacity, subject to that Region's own service quotas, and billed at standard on-demand pricing for that Region.
- Monitoring (CloudWatch metrics, CloudTrail logs) is scoped entirely to the single Region called — no source-vs-destination distinction, simplifying compliance/audit tracking.
- Feature is available via the bedrock-runtime endpoint (recommended for new apps), accessible through Anthropic's Messages API, Bedrock's InvokeModel/Converse APIs, and supports Bedrock Guardrails and intelligent prompt routing.
- Access methods span console playground (no-code testing) and programmatic access via Boto3, AWS CLI, or the Anthropic SDK with an AWS Bedrock token generator for authentication.

## Quote

> Amazon Bedrock processes inference requests and data within the Region you call. The processing does not leave the Region.

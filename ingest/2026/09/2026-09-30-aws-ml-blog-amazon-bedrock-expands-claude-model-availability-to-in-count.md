---
title: Amazon Bedrock expands Claude model availability to in-country inferencing
  in India
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-expands-claude-model-availability-to-india-cross-region-inference/
author: Aamna Najmi
date_published: '2026-09-30'
date_captured: '2026-09-30'
ingest_method: feed
model: claude-sonnet-5
---

# Amazon Bedrock expands Claude model availability to in-country inferencing in India

## Insights

- AWS launched India-specific in-country inference for Anthropic's Claude Opus 5, Claude Sonnet 5, and Claude Haiku 4.5 on Amazon Bedrock, restricting data routing exclusively to the ap-south-1 (Mumbai) and ap-south-2 (Hyderabad) regions — addressing data residency/sovereignty requirements for customers who need local processing.
- This is implemented as a "geographic cross-Region inference profile," distinct from the existing "global" cross-Region inference option, letting customers pool compute across two Indian regions for throughput/scale without managing per-region capacity themselves.
- Bedrock uses a zero data retention (ZDR) model by default — inputs/outputs aren't stored — though certain models require human review by AWS when automatic safety classifiers flag content, a caveat to the "your data stays local" pitch.
- Billing, quota tracking, CloudWatch, and CloudTrail logs all stay tied to the source region regardless of which backend region actually processed the request, simplifying compliance/monitoring.
- Access is available via Bedrock console playground, Anthropic's native Messages API, and AWS's InvokeModel/Converse APIs, with support for Bedrock Guardrails and intelligent prompt routing — positioning this as a straightforward drop-in for existing Bedrock/Claude integrations rather than a new product surface.
- Signals continued regional expansion strategy for Bedrock's Claude offering, framed around sovereignty/compliance demand rather than new model capability.

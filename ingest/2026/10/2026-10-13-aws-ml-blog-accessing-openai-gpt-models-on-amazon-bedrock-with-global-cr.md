---
title: Accessing OpenAI GPT models on Amazon Bedrock with global cross-Region inference
  in Thailand, Malaysia, Singapore, Indonesia, and Taiwan
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/accessing-openai-gpt-models-on-amazon-bedrock-with-global-cross-region-inference-in-thailand-malaysia-singapore-indonesia-and-taiwan/
author: Traci Lim
date_published: '2026-10-12'
date_captured: '2026-10-13'
ingest_method: feed
model: claude-sonnet-5
---

# Accessing OpenAI GPT models on Amazon Bedrock with global cross-Region inference in Thailand, Malaysia, Singapore, Indonesia, and Taiwan

## Insights

- AWS Bedrock now offers "global cross-Region inference" for OpenAI's GPT-6 model family (Sol, Luna, Astra), letting requests from five Asia-Pacific source regions (Singapore, Jakarta, Malaysia, Thailand, Taipei) route automatically to wherever capacity exists, addressing single-region throttling — though GPT-6 Astra is only invokable from Singapore.
- Billing, quota, and logging stay pinned to the source region even though actual processing happens wherever Bedrock routes the request, which creates a blind spot: AWS documents destinations only as "commercial regions where the model deployed" rather than giving a concrete list, and CloudTrail is the only way to see the actual processing region per-request.
- Quota is enforced in tokens-per-minute at the source region with output tokens costing 10x input/cache tokens against quota, and Bedrock reserves the full max_tokens requested up front — meaning loosely-set completion limits burn quota fast.
- Cross-region requests carry no explicit region identifier (set to "unspecified"), which breaks naive region-allowlist service control policies in enterprise AWS orgs — a specific SCP workaround using the inference-profile ARN condition key is required, and this is flagged as a common cause of first-call failures.
- Abuse-detection data retention (up to 30 days) happens in whichever destination region processed the request, raising data residency questions for regulated industries; the post explicitly tells readers to route this to risk/compliance teams rather than treating it as solved.
- The same Bedrock endpoint exposes OpenAI-compatible Chat Completions/Responses APIs alongside AWS's native Converse API, positioned as a low-friction migration path for teams already built on OpenAI SDKs (change base URL and key, not application code).

## Quote

> A global cross-Region inference request carries no Region name.

---
title: Introducing the Amazon Bedrock Trusted Access API with Anthropic’s Enterprise
  Frontier Safeguards and Enterprise Data Controls
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-bedrock-trusted-access-api-with-anthropics-enterprise-frontier-safeguards-and-enterprise-data-controls/
author: Dani Mitchell
date_published: '2026-11-24'
date_captured: '2026-11-24'
ingest_method: feed
model: claude-sonnet-5
---

# Introducing the Amazon Bedrock Trusted Access API with Anthropic’s Enterprise Frontier Safeguards and Enterprise Data Controls

## Insights

- AWS launched a general-availability "trusted access program API" on Bedrock — a unified discovery/eligibility/enrollment mechanism for model-provider-specific trust programs, with IAM/SCP-based governance over who can opt in at account, org, or project scope.
- First two offerings (public preview) are built with Anthropic: Enterprise Frontier Safeguards (EFS) and Enterprise Data Controls (EDC), covering Claude Fable, Claude Mythos, and Opus/Sonnet 5.5 via the Cyber Verification Program.
- Core mechanism: automated safety monitoring scans retained prompts/completions for cross-request misuse patterns (e.g., offensive cyber ops, agents exceeding scope) and generates a "Safety Case" for the customer's own team to review — not AWS or Anthropic humans.
- Key differentiator between the two offerings is data residency/control: EFS stores retained data in the customer's own S3 bucket encrypted with customer-managed KMS keys (AWS loses model access within 24 hours if key/bucket access is revoked); EDC uses Amazon-managed storage/keys with less setup but same review workflow.
- Frames this as the "long-term path" replacing zero-data-retention (ZDR) exceptions, which are only guaranteed through June 30, 2027 for current Fable/CVP models — signaling AWS/Anthropic are building permanent enterprise data-governance infrastructure rather than relying on temporary no-retention carve-outs.
- Positions this explicitly for regulated industries (healthcare, financial services, law) and claims adoption by "a quarter of the Fortune 100," though this is self-reported and unverified.

## Quote

> Neither AWS nor Anthropic humans access your retained inputs or outputs. Your inputs and outputs are never used for training.

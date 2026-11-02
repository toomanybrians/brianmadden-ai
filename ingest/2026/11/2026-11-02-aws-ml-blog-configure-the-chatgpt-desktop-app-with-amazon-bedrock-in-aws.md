---
title: Configure the ChatGPT desktop app with Amazon Bedrock in AWS GovCloud (US)
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/configure-the-chatgpt-desktop-app-with-amazon-bedrock-in-aws-govcloud-us/
author: Virgil Ennes
date_published: '2026-10-30'
date_captured: '2026-11-02'
ingest_method: feed
model: claude-sonnet-5
---

# Configure the ChatGPT desktop app with Amazon Bedrock in AWS GovCloud (US)

## Insights

- AWS now lets the ChatGPT desktop app (and its Codex coding agent) run against OpenAI frontier models hosted on Amazon Bedrock inside AWS GovCloud (US), letting regulated/government customers use OpenAI models while keeping inference, identity, and network controls entirely within AWS's sovereign cloud rather than routing to OpenAI's own infrastructure.
- The commercial model is pay-per-token with no seat licenses or per-developer commitments, plus an optional zero-data-retention mode where prompts/responses aren't durably stored or shared with the model provider.
- Achieving a compliant deployment requires an elaborate admin-locked configuration: an administrator-only `requirements.toml` that disables most app features (browser/computer use, image generation, memories, plugins, in-app chat) and a network allowlist that explicitly blocks all of OpenAI's own consumer-facing domains (chatgpt.com, api.openai.com, etc.) so traffic can only reach the approved Bedrock endpoint.
- The architecture decouples enterprise governance from OpenAI's own account system — access is controlled entirely through AWS IAM/credentials and device policy, not ChatGPT workspace roles, since authentication uses API-mode sign-in rather than an OpenAI account.
- AWS explicitly disclaims that using GovCloud or following the setup guide does not itself constitute compliance authorization — the customer organization remains responsible for validating the model, region, endpoint, and data flows against its own security/authorization process.
- The post frames this as a "controlled local deployment" meant for a test-and-document phase before any broader organizational rollout, including explicit rollback/credential-revocation steps if validation fails.

## Quote

> Using AWS GovCloud (US) and following this guide do not, by themselves, authorize your workload.

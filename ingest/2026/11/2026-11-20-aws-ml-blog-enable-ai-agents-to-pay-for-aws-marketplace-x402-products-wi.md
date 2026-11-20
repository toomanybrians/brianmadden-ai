---
title: Enable AI agents to pay for AWS Marketplace x402 products with Amazon Bedrock
  AgentCore payments
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/enable-ai-agents-to-pay-for-aws-marketplace-x402-products-with-amazon-bedrock-agentcore-payments/
author: Madhu Samhitha Vangara
date_published: '2026-11-19'
date_captured: '2026-11-20'
ingest_method: feed
model: claude-sonnet-5
---

# Enable AI agents to pay for AWS Marketplace x402 products with Amazon Bedrock AgentCore payments

## Insights

- AWS now lets AI agents autonomously purchase x402-enabled products (APIs, data, software, content) on AWS Marketplace, with charges billed in USD directly to the developer's AWS account—no stablecoin wallet or API key needed.
- The mechanism follows the x402 protocol: a seller returns HTTP 402 with a signed price quote, AgentCore payments validates it against a session budget, issues a short-lived (~5 minute) payment token, and the agent retries the request to complete the transaction.
- Governance is layered through IAM role separation: a "session role" can set spending budgets but cannot pay, while the "agent role" can pay but cannot raise its own budget — intentionally preventing agents from self-escalating spend.
- Spending is further bounded by per-session caps, per-request caps, approved-seller lists (AgentCore policy), and optional Private Marketplace restrictions, with all transactions auditable via AWS CloudTrail and Cost Explorer.
- A new AWS Marketplace connector in AgentCore Gateway gives agents read-only tools to discover sellers and endpoints (search listings, get listing, list fulfillment options) without manual pre-configuration.
- Demo scenario: a research agent autonomously discovered a live-search seller (Tavily), compared two listings, paid $0.01 for one query, and cited sources — illustrating agent-driven vendor selection, not just payment execution.
- Launch currently supports only the x402 "exact" scheme (fixed per-request pricing); broader pricing models aren't yet covered.

## Quote

> Agentic commerce isn't just about giving agents the ability to pay. It's about giving enterprises the confidence to let them. — Rotem Weiss, Tavily

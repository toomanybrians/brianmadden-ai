---
title: 'Pay-per-inference for AI agents: How BlockRun and Incarna use Amazon Bedrock
  AgentCore payments'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/pay-per-inference-for-ai-agents-how-blockrun-and-incarna-use-amazon-bedrock-agentcore-payments/
author: Peter Jiang
date_published: '2026-10-08'
date_captured: '2026-10-09'
ingest_method: feed
model: claude-sonnet-5
---

# Pay-per-inference for AI agents: How BlockRun and Incarna use Amazon Bedrock AgentCore payments

## Insights

- Amazon Bedrock AgentCore payments is a managed AWS service letting AI agents autonomously pay for services (inference, API calls, web content, other agents) mid-task via the x402 protocol, with spending limits enforced at the infrastructure layer rather than by the model itself.
- The underlying problem is micropayments at agent speed: sub-cent, high-frequency purchases that traditional card rails can't handle and that happen with no human in the loop to approve them.
- Key architecture: agents get managed wallets (via Coinbase CDP), spending governance that can't be overridden by prompt manipulation, and settlement in stablecoin (USDC on Base) that's auditable on-chain.
- Case study specifics: Incarna (agent identity platform) integrated AgentCore payments to let its agents pay BlockRun (a multi-provider inference router) per API call; integration took 3 days and ~200 lines of code versus an original 2-3 month estimate.
- In beta, agents processed 1,000+ payments ranging from $0.001 to $0.05 per call, each settled individually on-chain — evidence of real (if small-scale) production usage, not just a demo.
- Payment sessions use spending ceilings and expiry times (e.g., sized to a day's budget) as the core safety mechanism, framed as making builders "comfortable letting an agent move real money."

## Quote

> AgentCore payments covered everything we needed for an agent to pay over x402 ... We wrote none of it.
— Justin Zhou, Founder, Incarna

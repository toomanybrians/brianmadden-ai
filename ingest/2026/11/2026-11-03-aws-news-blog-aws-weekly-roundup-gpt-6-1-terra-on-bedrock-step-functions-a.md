---
title: 'AWS Weekly Roundup: GPT-6.1 Terra on Bedrock, Step Functions as agent tools,
  and more (November 2, 2026)'
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-gpt-6-1-terra-on-bedrock-step-functions-as-agent-tools-and-more-november-2-2026/
author: Daniel Abib
date_published: '2026-11-02'
date_captured: '2026-11-03'
ingest_method: feed
model: claude-sonnet-5
---

# AWS Weekly Roundup: GPT-6.1 Terra on Bedrock, Step Functions as agent tools, and more (November 2, 2026)

## Insights

- Two separate launches (AWS Step Functions as agent tools via Bedrock AgentCore Gateway, and MoEngage exposing ~400 internal APIs the same way) point to a pattern: agentic value is coming from giving agents access to existing orchestration/APIs rather than rebuilding systems or improving model capability.
- The Step Functions integration explicitly separates agent decision-making from execution — the agent decides *when* to trigger a workflow, but the deterministic step ordering (e.g., eligibility check, approval, credit in a refund flow) remains fixed and non-improvisable by the model.
- MoEngage's case reveals a practical scaling constraint in agent tool design: listing all ~400 API operations would exceed 20,000 tokens per connection, so agents instead search/describe tasks to find relevant tools dynamically rather than receiving a full catalog.
- GPT-6.1 Terra's GA on Bedrock is framed around cost and speed rather than peak capability — priced at least 50% lower than GPT-6.1 Sol and GPT-5.6 Terra, with claims (from OpenAI, not independently verified) of 3x+ faster task completion and performance on par with GPT-6 Astra.
- Nubank's use of an AWS DevOps Agent for compliance evidence-gathering cut a disaster-recovery test cycle from ~4.3 hours to ~40 minutes and quadrupled tested business-flow coverage to 160+ in a year — a concrete case of agentic automation applied to regulatory/compliance workflows rather than customer-facing tasks.
- Two post-quantum cryptography launches (AWS KMS ML-KEM support, Aurora PostgreSQL post-quantum TLS) were framed as pre-emptive defense against "harvest now, decrypt later" attacks, despite no fixed timeline for quantum decryption capability.

## Quote

> The agent decides when to run a workflow and what input to pass; Step Functions runs each step exactly as you defined it.

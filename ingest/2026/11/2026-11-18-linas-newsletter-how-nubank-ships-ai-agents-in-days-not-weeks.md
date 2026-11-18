---
title: How Nubank Ships AI Agents in Days, Not Weeks 🤖
source: Linas's Newsletter
source_id: linas-newsletter
source_url: https://linas.substack.com/p/nubank-ai-agents-simulated-customers
author: Linas Beliūnas
date_published: '2026-11-17'
date_captured: '2026-11-18'
ingest_method: feed
model: claude-sonnet-5
---

# How Nubank Ships AI Agents in Days, Not Weeks 🤖

## Insights

- Nubank's AI team built "Screen Before You Serve," a pre-release testing method where simulated customers hold multi-turn conversations with candidate AI agent versions, and an LLM judge scores the transcripts against a pre-set pass bar before any live A/B test.
- Using this method, Nubank cut agent release cycles from 21.2 days to 4.4 days on its highest-volume Brazilian support agent, and the new version beat its predecessor by 4.9 points on self-service rate and 36.7 points on transactional NPS.
- Nubank swapped GPT-5.2 for an open-weight Qwen model after screening 29 configurations across 16,000 simulated conversations, yielding a further 8.8-point rise in self-service rate, flat satisfaction, and 25% lower p95 latency.
- The piece argues the bottleneck in shipping AI agents has shifted from model quality to the speed/cost of the test loop — models are "good enough," so competitive advantage now comes from how fast teams can validate whether a new version is actually better.
- A key caveat: simulators must be built to correctly rank agent versions, not to sound realistic — a simpler simulator built on a frontier model actually ranked the best-performing agent version last.
- The article frames this alongside Revolut's earlier move to self-hosted open-weight models (cutting AI costs 90%) as part of a broader pattern of companies moving off frontier-model defaults for production AI agents.

## Quote

> This is a perfect illustration that the constraint on AI agent products has moved from the model to the test loop.

---
title: A chat assistant at 100,000 daily conversations runs about $193K a month in
  mode
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2109630951903162753
author: '@DanielMiessler'
date_published: '2026-10-12'
date_captured: '2026-10-13'
ingest_method: x
model: claude-sonnet-5
---

# A chat assistant at 100,000 daily conversations runs about $193K a month in mode

## Insights

- At 100,000 daily conversations (eight model requests each), baseline GPT-5.4 inference costs run ~$193,440/month, or $0.064 per conversation.
- Routing 70% of requests to a cheaper model (GPT-5.4-mini) cuts costs roughly in half (~$98,635/month, a 49% reduction) while keeping the pricier model for harder requests.
- Layering in semantic caching (~30% cache hit rate) plus prompt optimization can push costs down to ~$48,000/month, a 75% reduction from baseline — though these figures exclude retries and adjacent infra costs.
- The biggest risk in model routing is silently degraded quality: a cheaper model may give a confident but wrong answer, so routing decisions need evaluation against success/accuracy metrics, not just cost.
- Semantic caching carries its own failure modes — false cache hits (similar questions needing different answers) and cross-user data leakage — requiring similarity thresholds, TTL policies, and strict tenant isolation.
- Cost math scales linearly with usage (unlike traditional software), so a product's unit economics (cost per successful conversation vs. revenue) determine whether growth increases or erodes profitability.
- Prompt engineering tradeoffs interact with provider-side caching rules: shortening a prompt below a provider's minimum cacheable prefix length (e.g., 1,024 tokens for OpenAI) can eliminate caching benefits and raise costs despite being shorter.

## Quote

> Your $193,000 AI bill could drop to $48,000.

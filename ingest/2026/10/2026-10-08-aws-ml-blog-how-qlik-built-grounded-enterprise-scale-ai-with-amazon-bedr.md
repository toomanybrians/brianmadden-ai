---
title: How Qlik built grounded, enterprise-scale AI with Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-qlik-built-grounded-enterprise-scale-ai-with-amazon-bedrock/
author: Sunil Yerkola
date_published: '2026-10-07'
date_captured: '2026-10-08'
ingest_method: feed
model: claude-sonnet-5
---

# How Qlik built grounded, enterprise-scale AI with Amazon Bedrock

## Insights

- Qlik Answers is architected as a layered system (entry, routing, answer, specialist agent swarm, conversational analytics, retrieval, model access) rather than one monolithic assistant — the stated rationale is that a single general-purpose assistant gets slower and less accurate as more capability is bolted on.
- Grounding is treated as a system-level control, not just a retrieval step: Qlik runs a separate grounding-validation check (via Amazon Bedrock Guardrails' contextual grounding capability) that compares generated answers against their source content before presenting them.
- Data sovereignty across 11 regions is handled via Bedrock's cross-region inference rather than maintaining 11 separate regional builds; when a model isn't yet available in-region on Bedrock, Qlik falls back to hosting it on SageMaker AI until regional availability catches up.
- Qlik routes model access through its own internal LLM gateway rather than binding application logic to any single model, enabling per-task model selection and future migration without rewriting application code.
- Capacity planning is done 3–6 months ahead of launches via token-consumption forecasting by feature/region, then validated against real usage post-launch — explicitly framed as what prevented adoption growth from becoming a capacity problem.
- Reported customer outcomes (100,000+ discoveries surfaced, 75% faster response times at Lintech, 7 hours/week returned, 15-minute chatbot deployment at Bystronic) are vendor/customer-reported figures without independent verification or methodology detail.

## Quote

> Treat safety and grounding checks as a system-level gate, not a per-feature afterthought.

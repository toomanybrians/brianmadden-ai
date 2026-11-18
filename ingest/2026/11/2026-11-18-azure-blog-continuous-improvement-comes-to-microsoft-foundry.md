---
title: Continuous improvement comes to Microsoft Foundry
source: Azure Blog
source_id: azure-blog
source_url: https://azure.microsoft.com/en-us/blog/continuous-improvement-comes-to-microsoft-foundry/
author: Tina Schuchman
date_published: '2026-11-17'
date_captured: '2026-11-18'
ingest_method: feed
model: claude-sonnet-5
---

# Continuous improvement comes to Microsoft Foundry

## Insights

- Microsoft Foundry's "continuous improvement" loop has four stages (Establish, Identify, Optimize, Validate/repeat): experts write rubric-based evaluations, traces from real agent runs get annotated into evaluation/golden datasets, an "agent optimizer" proposes changes to instructions/skills/model choice, and nothing ships to production without passing evaluations and human sign-off.
- Foundry's model router claims up to 65% cost savings by sending simple requests to small models and complex ones to larger models, rather than routing everything to frontier models; Foundry now hosts 11,000+ models across OpenAI, Anthropic, Meta, Mistral, open-source, and Microsoft's own MAI models.
- New/expanded capabilities: "skill optimization" turns repeated agent mistakes and expert feedback into versioned, reusable skills; "Programmed Training" lets engineers write custom Python training recipes on serverless GPUs; "Managed Training" (formerly managed fine-tuning) supports training on proprietary data.
- Customer proof points given: Alaska Airlines fine-tuned a model (MAI-Code-2-Flash) for aircraft maintenance report classification, improving accuracy from 81.2% to 91.1% and reportedly outperforming GPT-6 Astra/GPT-6.1 Sol at lower cost; Heidi (clinical notes) claims 87% lower cost per note using Programmed Training on an open-weight model; Docusign claims 90% AI processing cost cuts via fine-tuning.
- Governance/safety framing: agents get an identity via "Entra Agent ID," guardrail policies are checked at runtime, sensitive actions require human-in-the-loop, and organizations retain control over what ships — positioned as part of a broader "Microsoft IQ" context layer that keeps proprietary organizational knowledge and agent improvements "owned" by the customer rather than the vendor.
- NTT DATA is cited as applying this loop to a program-management agent ahead of scaling it across 1,000+ internal projects, used as an enterprise-scale validation example.

## Quote

> Out of the box, an AI model is exactly the same for you as it is for anyone else.

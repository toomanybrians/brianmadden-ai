---
title: How Indegene is modernizing and scaling enterprise data quality in life sciences
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-indegene-is-modernizing-and-scaling-enterprise-data-quality-in-life-sciences/
author: Bhagyashree Chandak
date_published: '2026-11-04'
date_captured: '2026-11-05'
ingest_method: feed
model: claude-sonnet-5
---

# How Indegene is modernizing and scaling enterprise data quality in life sciences

## Insights

- Indegene built a production LLM-powered "Data Quality Agent" inside its NEXT Unified Data Platform, targeting the split between technical data rules (owned by engineers) and business-context rules (owned by domain SMEs) that typically live in disconnected glossaries, SOPs, and spreadsheets.
- The agent's differentiator is grounding rule generation in two RAG knowledge bases — an internal one (glossaries, SOPs, approved rules, SME feedback) and an external one (industry standards like NPI format rules) — rather than just running generic null/type/duplicate checks.
- Architecture runs on Amazon Bedrock (Claude Sonnet 4.5), Strands Agents, and Bedrock AgentCore, with a human-in-the-loop design: only high-confidence/low-risk rules auto-approve, while critical and business rules always route to an SME reviewer.
- Reported production metrics: rule-definition effort dropped from ~30 hours to ~4 hours per dataset (~85% reduction, ~7x productivity), table onboarding went from 2–5 days to 2–4 hours; vendor cautions these are "estimated from Indegene's production deployments," not independently audited.
- Quality/accuracy figures disclosed include 80–90% rule-suggestion accuracy, 60–75% rule acceptance rate without edits, 20–35% human override rate, and a self-reported hallucination rate of <5–8%, with an LLM "Validation Agent" used to check another LLM's generated rules/scripts.
- Compliance framing is explicit: Bedrock's prompts/outputs are excluded from model training, and the platform leans on Bedrock Guardrails (PII masking, prompt-injection blocking, contextual grounding checks) and HIPAA/SOC/ISO/GDPR eligibility to meet life sciences regulatory requirements.

## Quote

> Human oversight remains central... critical and business rules always go to an SME for review.

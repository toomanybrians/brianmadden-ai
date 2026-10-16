---
title: How Tamnoon built AI-powered cloud security remediation with Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-tamnoon-built-ai-powered-cloud-security-remediation-with-amazon-bedrock/
author: Ishara Premadasa
date_published: '2026-10-14'
date_captured: '2026-10-15'
ingest_method: feed
model: claude-sonnet-5
---

# How Tamnoon built AI-powered cloud security remediation with Amazon Bedrock

## Insights

- Tamnoon's "Tami" is an agentic remediation system that pipelines four specialized agents (investigation, safety-scoring, remediation, code-generation), each calling a different Bedrock foundation model matched to task difficulty/cost rather than one model doing everything.
- Core safety design: a dedicated safety-scoring agent rates every finding SAFE/RISKY/AWAITING DATA with a conservative bias ("when in doubt, downgrade"), and only SAFE findings proceed to automated remediation — RISKY/AWAITING DATA route to human cloud engineers.
- Architecture enforces a strict read/write separation: investigation steps are validated as read-only, only the remediation agent can alter infrastructure, and every change requires backup, verification, and rollback steps; AI agents never hold cloud credentials directly (execution uses short-lived, tenant-scoped credentials brokered separately from planning).
- Vendor rationale for choosing Bedrock centers on single-API access to multiple models, Bedrock Cross-Region inference for automatic load distribution, Bedrock Guardrails for PII/prompt-injection filtering, and data never leaving the customer's AWS trust boundary (Bedrock reportedly doesn't retain or train on prompts/completions).
- Reported outcomes (vendor-sourced, from Tamnoon's own "State of Cloud Remediation" report): up to 90% reduction in critical cloud exposure within 90 days, up to 100x "efficiency" via root-cause clustering, 13,000+ engineer hours saved weekly across its customer base, and zero production issues across millions of workloads — all self-reported figures, not independently verified.
- Governance/compliance details presented as differentiators: per-service least-privilege IAM roles, pinned/dated model versions (e.g., claude-sonnet-4-5-20250929) requiring explicit code review to change, full CloudTrail logging, and infrastructure-as-code (CloudFormation/SAM) to prevent configuration drift.

## Quote

> Building an agent that can reason about a cloud finding is the straightforward part. Building one you'd trust to act on production is the hard part.

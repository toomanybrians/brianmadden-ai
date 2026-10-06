---
title: Supercharge regulated workloads with Claude Code and Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/supercharge-regulated-workloads-with-claude-code-and-amazon-bedrock/
author: Bradley Wyman
date_published: '2026-10-05'
date_captured: '2026-10-06'
ingest_method: feed
model: claude-sonnet-5
---

# Supercharge regulated workloads with Claude Code and Amazon Bedrock

## Insights

- Anthropic's Claude Opus 5.5 and Claude Sonnet 5.5 are now available on Amazon Bedrock in AWS GovCloud (US), giving regulated/government workloads (including ITAR) a compliance-aligned path to agentic AI coding tools; Claude Sonnet 5 carries FedRAMP Class D and DoD IL4/IL5 authorization, while the newer 5.5 models hold FedRAMP Class D only (not yet IL4/IL5), positioning Sonnet 5 as the choice for the highest-compliance workloads.
- Claude Code (Anthropic's agentic coding tool) can read/edit across a codebase, run commands, manage git/PRs, connect to external tools via MCP (AWS CLI, Terraform, Kubernetes), spawn parallel sub-agents, and be customized via memory files, skills, and hooks — positioned as a full agentic dev workflow, not just autocomplete.
- Bedrock in GovCloud exposes two distinct endpoints (bedrock-runtime vs. bedrock-mantle) with a real tradeoff: runtime supports Guardrails and invocation logging (needed for audit trails/compliance) while mantle supports the native Anthropic Messages API and extra capabilities (server-side tools, background inference, Projects) but lacks those compliance features — forcing organizations to choose based on regulatory need.
- Vendor guidance flags real operational/cost risk: unpinned deployments default to pricier Opus billing, Claude Code sessions are "token-intensive," and AWS recommends per-user token guardrails, usage alerting (80%/100% thresholds), prompt caching, and defaulting teams to cheaper Sonnet while reserving Opus for harder tasks.
- Enterprise rollout advice centers on centralized identity (IAM Identity Center), managed permissions that can't be overridden locally, organization-wide CLAUDE.md standards, and explicit acknowledgment that Bedrock secures only the inference layer — Claude Code itself runs on local developer machines and needs separate security evaluation.

## Quote

> Amazon Bedrock secures the inference layer, but Claude Code runs on local developer machines and requires separate evaluation and risk management.

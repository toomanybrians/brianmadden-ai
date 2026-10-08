---
title: Automate remediation post AWS DevOps Agent investigation
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/automate-remediation-post-aws-devops-agent-investigation/
author: Michele Scarimbolo
date_published: '2026-10-07'
date_captured: '2026-10-08'
ingest_method: feed
model: claude-sonnet-5
---

# Automate remediation post AWS DevOps Agent investigation

## Insights

- The system layers automated remediation onto AWS DevOps Agent (an AI agent that already does incident root-cause analysis) using Lambda Durable Functions, EventBridge, and Bedrock to go from "diagnosis" to "pre-validated fix ready for one-click approval."
- Core safety design: a curated allowlist restricts the AI (Bedrock) to only invoke pre-approved, purpose-built Lambda "tool" functions — it cannot take arbitrary actions on infrastructure.
- Read-only actions (e.g., fetching config) run autonomously without human input; any mutating action (e.g., changing a Lambda timeout) forces the workflow to suspend and wait for explicit human approval before executing.
- Lambda Durable Functions let the workflow checkpoint and pause indefinitely (minutes to a year) without consuming compute while waiting on human approval, then resume exactly where it left off — reframing "waiting for a human" as a cost-free, resilient state rather than a blocking process.
- The worked example (fixing a Lambda timeout from 3s to 30s) shows the AI generating both reasoning and the exact tool call/parameters, with the approver expected to inspect those specifics before approving — the human gate is explicitly framed as "the security control," not a formality.
- Vendor frames this as reducing mean-time-to-resolution by having the AI pre-stage root cause + fix so the on-call engineer's job shrinks to a single approval decision; extensibility is also marketed as just adding tools to a registry, no orchestrator code changes.

## Quote

> The investigation_summary sent to Amazon Bedrock, and the remediation it proposes, are AI-generated and should always be reviewed before approval.

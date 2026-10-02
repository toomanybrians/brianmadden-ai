---
title: Scaling cloud migrations with agentic AI on Amazon Bedrock AgentCore
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/scaling-cloud-migrations-with-agentic-ai-on-amazon-bedrock-agentcore/
author: Nikhil Jha
date_published: '2026-10-01'
date_captured: '2026-10-02'
ingest_method: feed
model: claude-sonnet-5
---

# Scaling cloud migrations with agentic AI on Amazon Bedrock AgentCore

## Insights

- AWS Professional Services built a four-agent pattern (Intake, IaC, Migration Intelligence/Governance, SRE) on Amazon Bedrock AgentCore to handle migration requirements that fall outside managed services like AWS Transform and AWS DMS — specifically when sources/destinations require custom MCP (Model Context Protocol) tooling.
- The core claimed result: generating infrastructure-as-code that composes a company's approved internal modules dropped from 3-4 weeks of manual engineering per application to minutes, across a 300+ application portfolio — though this is explicitly self-reported "internal project tracking data" from one program, not an independent benchmark.
- Security/governance is structurally embedded rather than bolted on: a security office curates a versioned, machine-checkable policy set (Cedar rules via "Policy in AgentCore") that agents query at runtime, with policy-set versions stamped onto generated code for auditability, and time-boxed exceptions that auto-expire.
- Human-in-the-loop approval gates are positioned as a "core design principle" — no agent acts autonomously on production systems; automated actions (Jira tickets, Confluence updates, ServiceNow escalations) require explicit human sign-off.
- The pattern treats agents as a layer that attaches to managed services rather than replacing them (AWS Transform for migration/modernization, AWS DMS for databases), explicitly framing the agents as filling gaps only where MCP-connected custom systems and org-specific IaC composition requirements exist.
- A separate "SRE Agent" extends the pattern past cutover into ongoing operations (monitoring, remediation playbooks, right-sizing recommendations), again gated by human approval — framed as shifting teams from reactive to proactive operations.

## Quote

> Managed services carry most of that work. Where a requirement falls outside them, an agent pattern can close the gap.

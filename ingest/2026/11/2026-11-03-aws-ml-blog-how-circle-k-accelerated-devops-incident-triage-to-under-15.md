---
title: How Circle K accelerated DevOps incident triage to under 15 minutes with Amazon
  Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-circle-k-accelerated-devops-incident-triage-to-under-15-minutes-with-amazon-bedrock/
author: Marek Klatowicz
date_published: '2026-11-02'
date_captured: '2026-11-03'
ingest_method: feed
model: claude-sonnet-5
---

# How Circle K accelerated DevOps incident triage to under 15 minutes with Amazon Bedrock

## Insights

- Circle K built an agentic AI incident-triage system on Amazon Bedrock that cut mean DevOps triage time from 45–60 minutes to under 15 minutes (67–75% reduction) by automating log review, resource checks, and runbook cross-referencing that engineers previously did manually.
- Initial architecture used Amazon Bedrock Flows with three specialized agents running in sequence/parallel (AWS resource checks, OpenSearch log/trace analysis, GitHub code search), feeding a final model call that produced a structured root-cause summary posted to Slack.
- As data volume and investigation complexity grew, Circle K migrated to Amazon Bedrock AgentCore Runtime, consolidating three agents into one long-running session (up to 8 hours) with persistent state, OpenTelemetry observability, and framework-agnostic containerized deployment.
- Key engineering lessons: feeding agents pre-queried log content directly (rather than letting them query CloudWatch themselves) reduced latency and improved reasoning; narrowing code search using prior findings avoided noisy results; keeping analysis logic decoupled from the orchestration layer allowed migration to AgentCore without rewriting prompts/tools.
- The system still stops at recommending fixes — a human engineer executes remediation. Circle K's next phase plans to integrate AWS DevOps Agent for human-approved automated remediations (restart, scale, rollback) and to add Jira, Confluence, and runbook context to the knowledge base.
- Vendor framing emphasizes that Bedrock's managed orchestration, knowledge base/RAG, and IAM/VPC integration let Circle K avoid owning model hosting, prompt versioning, and vector database infrastructure — a build-vs-buy tradeoff argument for AWS-native agent tooling over open-source frameworks.

## Quote

> The agent reasons faster when it can read the actual error messages.

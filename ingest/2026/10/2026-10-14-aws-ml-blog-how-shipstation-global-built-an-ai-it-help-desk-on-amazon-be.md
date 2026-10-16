---
title: How ShipStation Global built an AI IT help desk on Amazon Bedrock AgentCore
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-shipstation-global-built-an-ai-it-help-desk-on-amazon-bedrock-agentcore/
author: Kenneth Salmon
date_published: '2026-10-13'
date_captured: '2026-10-14'
ingest_method: feed
model: claude-sonnet-5
---

# How ShipStation Global built an AI IT help desk on Amazon Bedrock AgentCore

## Insights

- ShipStation Global built "Deckhand," a Slack-based AI IT help desk on Amazon Bedrock AgentCore, resolving 97.5% of incoming channel queries over three months, with positive feedback rising from 82% (April launch) to 96% (June) as the team iterated on the system prompt and knowledge base.
- Architecture separates concerns across managed AWS services: a Strands agent (Claude via Bedrock) runs on AgentCore runtime with no server/container management by the team; a single Lambda exposed as MCP tools via AgentCore Gateway handles classification, ticketing, and image analysis; a Bedrock knowledge base indexes Confluence, intranet, and mined Slack content.
- A notable technical approach: mining years of historical Slack support threads into a usable knowledge base using DSPy's Recursive Language Model (RLM) running Claude in a sandboxed Python REPL — iteratively classifying threads as resolved/unresolved/escalated and extracting structured, schema-validated fixes, filtering out noise like banter and unresolved threads.
- Significant engineering effort went into "knowing when not to answer" — social/conversational-message detection, deferring to human helpers mid-thread, and ignoring messages directed at named people — framed as more critical to adoption than the technical answer-generation itself.
- Reported business impact: of 1,221 agent conversations, 812 were resolved in chat rather than becoming Jira tickets, estimated at ~406 hours saved over three months (~1,600 hours/year), with 94% of after-hours questions (a third of total volume) answered without IT staff present.
- Security/validation design relies on code-level guardrails rather than trusting prompts alone: explicit human confirmation before ticket creation, Pydantic-validated classification output, restricted image-download sources, and prompt rules against ever requesting/storing credentials.

## Quote

> "We believe that tickets are an indication of operational friction not productivity." — Chris Collins, Senior Director IT, ShipStation Global

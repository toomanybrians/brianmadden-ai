---
title: Build a voice travel concierge with Amazon Bedrock AgentCore, Managed Knowledge
  Base and Nova Sonic
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-voice-travel-concierge-with-amazon-bedrock-agentcore-managed-knowledge-base-and-nova-sonic/
author: Ravi Kumar
date_published: '2026-10-06'
date_captured: '2026-10-07'
ingest_method: feed
model: claude-sonnet-5
---

# Build a voice travel concierge with Amazon Bedrock AgentCore, Managed Knowledge Base and Nova Sonic

## Insights

- AWS presents a reference architecture for a voice-based airline agent built entirely from managed services (Bedrock AgentCore, Nova Sonic, Bedrock Knowledge Bases, Cognito, API Gateway, Lambda, DynamoDB), explicitly positioned as a loosely-coupled, swap-in-your-own-backend pattern rather than a finished product.
- Backend integration runs through MCP (Model Context Protocol) via "AgentCore Gateway," which exposes existing REST/Lambda endpoints as discoverable, named tools the agent calls directly — the pitch is that new backend capabilities (e.g., a new Lambda function) can be added without touching agent code.
- Knowledge Base retrieval is treated as just another MCP tool (a "Connectors target"), with the agent calling it by name — no custom retrieval code required; it supports standard or agentic retrieval and returns cited passages for grounding.
- Each voice session runs as an isolated microVM container with automatic scaling and session routing; the architecture separates front end, agent, and backend layers so each scales independently.
- Design includes explicit responsible-AI/trust mechanisms: a "confirm-before-write" pattern before any data change, knowledge-base citations tracing answers to source docs, and recommendation to layer in Bedrock Guardrails for prompt-injection filtering and response grounding in production.
- Nova 2.5 Sonic is highlighted for agentic-task reasoning specifically (multi-step tool chaining, strict instruction-following like reading confirmation codes character-by-character), asynchronous/parallel tool calls, and "latency masking" (speaking interim responses while tool calls resolve) to keep conversation natural despite backend latency.
- Escalation to a human is built in as a first-class flow: the agent logs the handoff, generates a reference number and wait estimate, then the front end places the call — but the sample does not include an actual contact-center integration, so real human connection depends on configuration.

## Quote

> With MCP integration you can add a new Lambda function without touching agent code.

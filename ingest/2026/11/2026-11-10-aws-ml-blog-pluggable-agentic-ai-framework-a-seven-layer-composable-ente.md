---
title: 'Pluggable Agentic AI Framework: A seven-layer composable enterprise agentic
  AI reference architecture on Amazon Bedrock AgentCore'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/pluggable-agentic-ai-framework-a-seven-layer-composable-enterprise-agentic-ai-reference-architecture-on-amazon-bedrock-agentcore/
author: Sindhura Palakodety
date_published: '2026-11-09'
date_captured: '2026-11-10'
ingest_method: feed
model: claude-sonnet-5
---

# Pluggable Agentic AI Framework: A seven-layer composable enterprise agentic AI reference architecture on Amazon Bedrock AgentCore

## Insights

- AWS presents a "Pluggable Agentic AI Framework": a seven-layer reference architecture for production agentic AI (Data/Knowledge, Model/Inference, Orchestration, Security/Guardrails, Application, Observability, Agentic Operations), each with a stable contract so components can be swapped without redesigning the whole stack.
- Core argument: the gap between agent prototypes and production systems is rarely about model capability — it's about missing scaffolding (routing, guardrails, observability) that teams rebuild from scratch each time rather than treating as shared infrastructure.
- Orchestration guidance explicitly warns against single "does-everything" agents — recommends supervisor/specialist decomposition with bounded autonomy, scoped tools, and discovery via a centralized agent registry using standardized protocols (MCP, A2A) to avoid context bloat, tool sprawl, and security exposure.
- Security section frames agentic AI as introducing a new risk class (prompt injection, tool misuse, memory/data poisoning) requiring zero-trust defaults: authenticate every call, grant temporary scoped credentials instead of persistent secrets, mask PHI/PII, and route high-impact actions through human approval gates and circuit breakers.
- "Agentic Operations" is framed as a distinct ongoing layer — continuous scoring of production sessions for groundedness/accuracy/safety with regression gates, positioned as necessary to prove an agent still works after each release, not just at launch.
- The architecture is deliberately vendor-agnostic in principle (stable contracts allow substituting tools), though the reference implementation leans heavily on AWS-native services (Bedrock AgentCore, Guardrails, DynamoDB, CloudWatch) alongside a named third-party example (LiteLLM for model routing).

## Quote

> A proof-of-concept answers none of these, because it is built to show the agent model can do the task, not to survive production traffic.

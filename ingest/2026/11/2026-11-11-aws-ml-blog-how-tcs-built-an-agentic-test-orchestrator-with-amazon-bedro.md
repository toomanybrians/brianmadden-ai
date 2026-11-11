---
title: How TCS built an agentic test orchestrator with Amazon Bedrock AgentCore
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-tcs-built-an-agentic-test-orchestrator-with-amazon-bedrock-agentcore/
author: Varun Valsan
date_published: '2026-11-10'
date_captured: '2026-11-11'
ingest_method: feed
model: claude-sonnet-5
---

# How TCS built an agentic test orchestrator with Amazon Bedrock AgentCore

## Insights

- TCS built a multi-agent "Agentic Test Orchestrator" for BFSI software testing that decomposes QA work into specialized agents (scenario design, Gherkin generation, code generation, validation, chat/refinement, BRD-to-story conversion, incremental updates, execution) rather than using one large LLM prompt, arguing that regulated, multi-stage workflows need per-stage control that a single prompt can't provide.
- The system is built on Amazon Bedrock AgentCore, using its runtime for per-session isolation (each session runs in its own microVM), elastic scaling across tenants, and model flexibility (different models assigned per task, swappable as new models emerge) — framed as letting TCS focus on testing logic instead of building agent infrastructure.
- Grounding is enforced via tenant/project/session-filtered retrieval from Amazon Bedrock Knowledge Bases (vector embeddings over requirements docs, Jira stories, Swagger specs, GitLab code, locator docs) so one client's context never leaks into another's generated tests.
- An execution agent runs as a LangGraph state machine (fetch → execute → fix → save) with bounded, policy-gated retries: only "code error" failures get routed to an automated fixer with safety checks (rejecting empty files, unexpected new files, extreme size changes), while environment errors are excluded from auto-fixing.
- Multi-tenant isolation is architected at multiple layers: separate Kubernetes namespaces, Cognito user pools, KMS keys, S3 buckets, DynamoDB tables, and knowledge bases per tenant, with event-driven onboarding (EventBridge + CodeBuild + CDK) to provision new tenants repeatably.
- Reported outcome: on a ~100-scenario internal benchmark, average effort dropped from ~2 hours/scenario (manual) to ~14 minutes/scenario with the orchestrator — an 88% effort reduction (TCS's own controlled benchmark, not independently verified; explicitly caveated as workload-dependent).
- Stated goal was not replacing QA engineers but shifting their time from scripting/execution toward risk analysis, exploratory testing, and release decisions.

## Quote

> The objective wasn't to replace quality engineers. It was to remove repetitive translation and execution work.

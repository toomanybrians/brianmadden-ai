---
title: Build a multi-agent music production pipeline on Amazon Bedrock AgentCore Runtime
  Instances
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-multi-agent-music-production-pipeline-on-amazon-bedrock-agentcore-runtime-instances/
author: Evandro Franco
date_published: '2026-09-30'
date_captured: '2026-10-01'
ingest_method: feed
model: claude-sonnet-5
---

# Build a multi-agent music production pipeline on Amazon Bedrock AgentCore Runtime Instances

## Insights

- AWS introduces "Runtime Instances" as a new compute option for Bedrock AgentCore, distinct from the existing serverless "MicroVM" model — positioned specifically for multi-agent systems that need long-running, persistent collaboration rather than short, isolated sessions.
- Key architectural shift: MicroVMs are strictly 1:1 (one microVM hosts one agent, max 8-hour sessions, no GPU), while Runtime Instances allow many agents to share one EC2 instance (1:N), support sessions up to 14 days, offer GPU access, and persist storage via EBS.
- Agent colocation is achieved not through explicit orchestration code but by having separate agent runtimes share the same `runtimeSessionId` on the same capacity provider — AWS infrastructure handles placing them on the same physical instance with shared filesystem access.
- The example pipeline demonstrates independent team deployment as a deliberate pattern: three agents (composition, delivery, compliance), each built/deployed by a different "team" with different artifact types (container image vs. S3 code package), can be updated independently without coordination or risk to the others — a microservices-style decomposition applied to agents.
- Several practical infrastructure gotchas are surfaced: sessions can only resume in the same Availability Zone (EBS volumes are AZ-locked, risking lost persistence if capacity isn't available), entrypoint functions require specific parameter naming conventions, and agents must be built inside request handlers rather than at module scope to avoid re-entrancy errors.
- AWS frames the applicability beyond music generation explicitly: any workflow where one agent produces a large artifact, a second transforms it, and a third verifies/screens it before release — citing 3D rendering, simulation, model inference, and media processing as analogous GPU-dependent multi-day agent workloads.

## Quote

> Both options support custom frameworks... The difference is in the underlying compute model.

---
title: Taxonomy of agentic primitives in Amazon Quick
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/taxonomy-of-agentic-primitives-in-amazon-quick/
author: Thomas Delteil
date_published: '2026-11-06'
date_captured: '2026-11-09'
ingest_method: feed
model: claude-sonnet-5
---

# Taxonomy of agentic primitives in Amazon Quick

## Insights

- AWS's Amazon Quick team defines a taxonomy of agentic system primitives organized around four questions: When/What (triggers), Who (agents), and How (capabilities) — proposed as a shared vocabulary for builders, not users.
- Triggers (human-initiated, agent-delegated, scheduled, event-driven) both activate work and carry instructions; trigger type shapes execution posture (e.g., scheduled/background tasks stay conservative, human-initiated ones are responsive and ask questions rather than stall).
- An "agent" is defined narrowly as a persistent, learning actor composed of three things: standing instructions, dynamically updated capabilities, and accumulated learned context — explicitly distinct from the underlying LLM (swappable), session history, or triggers (platform-level).
- Capabilities span a spectrum from fully agentic to fully deterministic: tools (atomic typed operations), skills (loaded via "progressive disclosure," bundling judgment and expertise), and workflows (fixed-step, code-driven coordination with auditability).
- Skills and workflows aren't seen as temporary workarounds for weak models — they argue both retain value regardless of model improvement, since skills capture reusable institutional expertise and workflows provide auditability/deterministic coordination that enterprises need.
- Introduces "crystallization" (a skill hardening into a fixed workflow) and "dissolution" (a workflow loosening back into a skill) as a two-way maturation process, managed through a "continuous learning framework" to be detailed in a future post.
- Frames design choice as a "confidence contract": the same user request (e.g., a Slack digest) can be implemented as a loose scheduled task, a skill-guided task, or a deterministic workflow, depending on how much latitude the user is willing to grant the agent.

## Quote

> The agent isn't the instructions it follows. It's the entity that interprets them.

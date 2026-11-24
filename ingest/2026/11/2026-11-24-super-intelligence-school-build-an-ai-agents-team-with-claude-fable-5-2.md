---
title: Build an AI Agents Team With Claude Fable 5.2
source: Super Intelligence School
source_id: super-intelligence-school
source_url: https://sischool.substack.com/p/build-an-ai-agents-team-with-claude
author: Super Intelligence School
date_published: '2026-11-23'
date_captured: '2026-11-24'
ingest_method: feed
model: claude-sonnet-5
---

# Build an AI Agents Team With Claude Fable 5.2

## Insights

- Demonstrates a failure mode in multi-agent research: three agents independently verify a claim, but all three traced back to the same single source (a chain of citations), so apparent consensus was illusory rather than independent confirmation.
- Proposes a design fix: instead of giving multiple agents the identical question, assign each a distinct sub-question (e.g., what was promised vs. what release notes confirm vs. what is actually usable today) so disagreement among agents becomes informative rather than noise.
- Highlights a real-world ambiguity the agent team is meant to catch: a feature can be simultaneously "announced," "released to some customers," and "unavailable to this specific user" — a single yes/no answer collapses these distinct states.
- Describes a concrete agent-team architecture: a lead agent (Claude Fable 5.2) assigns research tasks, a writer drafts output from findings, and an independent critic agent can reject claims unsupported by evidence.
- The underlying guide includes a runnable Python implementation with specialist prompts and a user-defined $10 spending cap before first execution.

## Quote

> Three agents did the work. One sentence did all the talking.

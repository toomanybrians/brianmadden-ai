---
title: Formally verifying agent-written full-stack web apps with PDD Kit
source: Microsoft Research Blog
source_id: microsoft-research-blog
source_url: https://www.microsoft.com/en-us/research/blog/formally-verifying-agent-written-full-stack-web-apps-with-pdd-kit/
author: Alex Lavaee, Matthai Philipose
date_published: '2026-11-05'
date_captured: '2026-11-06'
ingest_method: feed
model: claude-sonnet-5
---

# Formally verifying agent-written full-stack web apps with PDD Kit

## Insights

- Microsoft Research introduces "Proof-Driven Development" (PDD) via PDD Kit: as coding agents ship tens/hundreds of thousands of lines at once, line-by-line human review no longer scales, so the proposed fix is shifting review from code to the *intent* layer — natural-language plans get formalized into specs that mathematically constrain what agents can build.
- The core mechanism: PDD Kit converts user intent into formal specifications (via Verus, a Rust proof language), auto-generates proofs the agent's code satisfies those specs for all possible inputs, and falls back to empirical tests only where proof can't reach (third-party libraries, UI, timing, external world facts).
- It explicitly names a known failure mode of agent-driven coding: agents silently resolve ambiguity in requirements, then write tests that validate what they built rather than what was asked — producing "coverage" metrics that mask a gap between intent and implementation until something breaks in production.
- Introduces "vibe verification" as a named risk: when models write their own specs, they tend toward weak invariants that technically pass proofs but constrain almost nothing meaningful — addressed here via a mutation-testing step that plants deliberate bugs to confirm each spec clause actually rules something out.
- Frames this as a trust/boundary-management problem, not a complete-automation claim: every verified system still rests on a "Trusted Computing Base" (e.g., bcrypt, database lookups, system clock) that is tested but not proven, and the team explicitly signs off on what's merely trusted vs. formally guaranteed.
- Positioned as a shift in what human reviewers actually do under AI-driven coding: less scrutiny of generated code itself, more scrutiny of whether the stated plan/spec matches true intent — the proof then mechanically enforces that the implementation can't drift from the agreed contract.

## Quote

> The plan was always supposed to be the contract, and now the agent actually has to keep it.

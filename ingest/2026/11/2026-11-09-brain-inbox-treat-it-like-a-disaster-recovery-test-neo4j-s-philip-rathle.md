---
title: '"Treat it like a disaster recovery test": Neo4j''s Philip Rathle on surviving
  the loss of your AI provider'
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://link.mail.beehiiv.com/v2/c/2133f957d1a23091c80d30e760524cc45cd3cc520376a8f1521ef454cea7494af7160cb8cb605ed00d78eb09e28deb6a1510abd40dff60525b65981fb3cb429be3f7f0223c7780a21d5d433728a66f1e87c9238997b12e9c048e7549522c2d1ff11d0dc2413ae4eb2d2e1d244205db33668b32565f10a180f7ad70d5d4156338b52c6137261d75357e0920ede7c080281193a7a371293eb761704a3929217a1f/034728f8c6e824bb
author: Superintelligence <superintel@mail.beehiiv.com>
date_published: '2026-11-08'
date_captured: '2026-11-09'
ingest_method: email
model: claude-sonnet-5
---

# "Treat it like a disaster recovery test": Neo4j's Philip Rathle on surviving the loss of your AI provider

## Insights

- In June 2026, a US export control directive forced Anthropic to disable two frontier models (Fable 5, Mythos 5) for all customers globally for ~3 weeks — not just targeted foreign nationals — because real-time nationality verification wasn't possible. This is cited as evidence that frontier model access can vanish overnight for reasons entirely outside a company's control.
- Rathle's core resilience framework separates "model reasoning" (should be commoditized/swappable) from "enterprise knowledge and context" (should be owned in-house). Companies that train business logic into a model provider's system become harder to migrate away from.
- Recommended practice: treat a provider switch like a disaster-recovery drill — pick one production workflow, build a test set from real inputs/outputs/decision traces, measure accuracy, traceability, permissions, latency, cost, and time-to-switch, run quarterly.
- Uber's driver-eligibility agent is offered as an architecture pattern: business rules live in a Neo4j graph, not in the model or in code; the LLM only translates between natural language and graph queries — making the model a replaceable commodity component.
- Cited evidence for graph-augmented retrieval (GraphRAG) outperforming plain RAG: Newcastle University/NICD study (Neo4j-funded) showed ~80% improvement in truthfulness and answer rate rising from ~28% to ~65%; a data.world benchmark showed GPT-4 accuracy on enterprise SQL data rising from 16.7% to 54.2% with a knowledge graph; LinkedIn reported a 77.6% MRR improvement and 28.6% faster customer-service resolution after ~6 months in production.
- Proposed 30-day starting point for organizations: rank exposure/risk, inventory where AI context currently lives and which pieces are single-provider dependent, turn on decision tracing for one key workflow, and move that workflow's retrieval into a company-controlled context layer.

## Quote

> "The best AI engineers are the ones who approach problems with a toolbox, not just a hammer." — Philip Rathle

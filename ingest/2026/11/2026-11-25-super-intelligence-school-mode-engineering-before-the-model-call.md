---
title: MODE ENGINEERING Before the Model Call
source: Super Intelligence School
source_id: super-intelligence-school
source_url: https://sischool.substack.com/p/mode-engineering-before-the-model
author: Super Intelligence School
date_published: '2026-11-24'
date_captured: '2026-11-25'
ingest_method: feed
model: claude-sonnet-5
---

# MODE ENGINEERING Before the Model Call

## Insights

- Distinguishes between an option added to a request (customer can ignore it, nothing breaks) versus the same option added to a response (the service decides, and client code that's run fine for years can break because it was never built to handle the new value).
- Argues that asking an AI reviewer for generic feedback (e.g., "clearer wording" on a release note) can miss this request-vs-response distinction entirely unless it's explicitly surfaced.
- Proposes a working method: pair the contract/spec (what the service may send) with the actual implementation (what the code does when it receives it), and give both to the model so its task becomes a precise, answerable question rather than an open-ended review.
- Introduces "mode engineering" as a concept: a mode defines the specific scope of what a system is allowed to do with a given piece of work (e.g., template-verification mode, wording-review mode, impact-review mode).
- Describes specific review outcomes as formal states: a "hold" (engineer must resolve something the program can't interpret) and a "skip" (processing ends for a recognized, unchanged record).

## Quote

> The contract tells us what the service may send. The reader's implementation tells us what happens when it does.

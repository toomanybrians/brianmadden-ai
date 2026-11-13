---
title: '🚨 Our Generative AI Lab is releasing Primer: an agent-driven system where
  a teac'
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/emollick/status/2121001056637431873
author: '@emollick'
date_published: '2026-11-12'
date_captured: '2026-11-13'
ingest_method: x
model: claude-sonnet-5
---

# 🚨 Our Generative AI Lab is releasing Primer: an agent-driven system where a teac

## Insights

- Primer is an open-source, agent-driven system from Wharton's Generative AI Labs that converts a teacher's spoken/typed description of a lesson into a playable educational simulation for students.
- The architecture separates authoring (educator + pipeline of specialized agents: Intake, Design, Casting Director, Image Generation, Experience Builder) from runtime (student-facing Mentor, Practice, and Feedback agents), with an approved design document gating what gets built.
- Design philosophy treats the educator as the source of pedagogical judgment: the system interviews them one question at a time, produces a reviewable design document, and builds nothing without explicit approval — explicitly countering LLMs' default tendency to over-help, drift from objectives, or produce unstructured roleplay.
- Learning-science principles (scaffolding, retrieval practice, grounded feedback) are hard-coded into each agent's instructions rather than left to the model's general knowledge, and simulations support two modes: Roleplay (pursuing a goal against a motivated counterpart) and Teachback (explaining a concept and revising based on questioning).
- The entire stack — prompts, orchestration patterns, templates, and code — is released open source and is explicitly LLM-agnostic, usable with local/open-source models to accommodate privacy and governance constraints (e.g., FERPA, district policy).
- Positioned as a research foundation rather than a finished product: the team frames open-sourcing as a way to let others study how educator intent translates into runtime agent behavior, not as a vetted, classroom-ready tool.

## Quote

> Generative models are capable but not pedagogically reliable on their own. — Wharton Generative AI Labs

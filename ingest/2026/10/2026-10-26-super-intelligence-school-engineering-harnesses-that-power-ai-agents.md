---
title: Engineering Harnesses That Power AI Agents
source: Super Intelligence School
source_id: super-intelligence-school
source_url: https://sischool.substack.com/p/engineering-harnesses-that-power
author: Super Intelligence School
date_published: '2026-10-25'
date_captured: '2026-10-26'
ingest_method: feed
model: claude-sonnet-5
---

# Engineering Harnesses That Power AI Agents

## Insights

- An agent can complete a task with no errors or crashes and still fail silently — the output "looks finished" (polished documents, full manifest) while actually missing required content.
- In the example, an agent tasked with preparing documents and a manifest from project files omitted seven QA records that were already referenced in the source material, producing a seemingly complete 43-row manifest instead of the correct 47.
- Different types of incompleteness require different resolutions: missing information could be recovered after the fact, but a pending approval could not simply be marked done — some gaps aren't fixable by just "finishing more work."
- Real-world task success is defined as delivering the right things, preserving important information, catching errors before they propagate, and correctly recognizing when work is actually complete — not just producing a convincing or polished-looking response.
- A model's individual steps can each be capable while the overall process still breaks down; the author attributes this gap to the need for engineering structure around the model.
- An "engineering harness" is defined as the structure governing a model's tool access, information carried between steps, error-handling behavior, and verification checks before results are accepted — distinguishing reliable agents from merely capable models.

## Quote

> An AI model generates decisions and actions from the information available to it. The harness provides the working conditions around those decisions.

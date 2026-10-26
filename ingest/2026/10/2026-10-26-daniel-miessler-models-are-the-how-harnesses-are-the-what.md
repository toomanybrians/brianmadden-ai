---
title: Models Are the How, Harnesses Are the What
source: Daniel Miessler
source_id: daniel-miessler
source_url: https://danielmiessler.com/blog/models-how-harnesses-what?utm_source=rss&utm_medium=feed&utm_campaign=website
author: daniel@danielmiessler.com (Daniel Miessler)
date_published: '2026-10-25'
date_captured: '2026-10-26'
ingest_method: feed
model: claude-sonnet-5
---

# Models Are the How, Harnesses Are the What

## Insights

- Proposes a distinction: models are the "how" (executing tasks) while harnesses are the "what" (describing a person's preferences, goals, and definition of a good result).
- Argues harnesses function as model assistants that "know you" so the model doesn't have to — reducing the need for the model itself to infer user preferences.
- Applies Sutton's "Bitter Lesson" to harness design: as models improve, hand-crafted step-by-step guidance (micromanaging process) becomes less valuable and ages poorly, while descriptions of desired outcomes retain value.
- Claims the best current harness engineering avoids dictating procedural steps and instead focuses on richly describing the user's identity, goals, and what "done" looks like — this frees the model rather than capping it.
- States that as models get smarter, they do more with well-described intent/context, not less — meaning the "what" half of the harness appreciates in value over time even as the "how" (model capability) improves.
- References author's own harness system ("LifeOS") as built primarily around self-description rather than task instructions, and frames this general approach as "Intent Engineering."

## Quote

> Micromanaging the steps caps the model; describing what you want frees it

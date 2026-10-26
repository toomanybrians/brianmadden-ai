---
title: Writing Is Closer to Thought Than Code
source: Daniel Miessler
source_id: daniel-miessler
source_url: https://danielmiessler.com/blog/writing-is-closer-to-thought-than-code?utm_source=rss&utm_medium=feed&utm_campaign=website
author: daniel@danielmiessler.com (Daniel Miessler)
date_published: '2026-10-23'
date_captured: '2026-10-26'
ingest_method: feed
model: claude-sonnet-5
---

# Writing Is Closer to Thought Than Code

## Insights

- Frames a disagreement with developer Matt Pocock: Pocock treats code as the authoritative source of truth in AI-assisted development; Miessler argues code is just an abstraction/representation, no more authoritative than a painting is of an artist's intent.
- Argues the actual bottleneck in AI-era building isn't execution (AI is already excellent at that) but articulation — accurately capturing what's in someone's head, a problem he likens to "writer's blindness"/curse of knowledge.
- Proposes writing is more "accurate" (if less "precise") than code, using an archery metaphor: code gives tight-but-possibly-wrong precision, writing gets closer to the true intent even if less rigidly formal.
- Introduces a concrete artifact/practice, the "Ideal State Artifact" (ISA): a living document combining prose ideal-state description, constraints, a decisions log, and atomic testable "Ideal State Criteria" (ISCs) each paired with an eval — meant to replace both ad hoc prompting and legacy spec-driven development.
- Key mechanical claim: iteration should happen inside the written ISA (updating the articulation, logging decisions) rather than by endlessly reworking code/output as if the implementation itself were the spec — illustrated via owl-drawing, yoga-studio booking app, and kitchen-remodel examples.
- Ties the argument to Sutton's "Bitter Lesson": as AI models get smarter, more effort should shift toward precisely specifying intent and less toward manually managing implementation steps or human-in-the-loop micromanagement.

## Quote

> AI is extraordinary at execution... more and more of the problems at this point are it executing the job perfectly, and having the result be different than what was in our mind.

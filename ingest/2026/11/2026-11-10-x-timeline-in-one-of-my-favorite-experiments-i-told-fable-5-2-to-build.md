---
title: In one of my favorite experiments, I told Fable 5.2 to build an endless, hands-o
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/emollick/status/2119918307457577163
author: '@emollick'
date_published: '2026-11-09'
date_captured: '2026-11-10'
ingest_method: x
model: claude-sonnet-5
---

# In one of my favorite experiments, I told Fable 5.2 to build an endless, hands-o

## Insights

- A single project ("Portals") was built by an estimated ~25,000 AI agents (Claude-based) over about ten days, producing 471 fully generated 3D worlds (~1.4 million lines of JavaScript), with almost no human-authored code beyond a one-paragraph initial prompt.
- The work was organized agent-to-agent in a quasi-organizational structure: a "lead agent" owned the engine and shipped releases, coordinating 28 parallel "teams" of agents, each with its own internal lead/designer — essentially emergent management hierarchy among AI workers.
- Agents acted as QA/judges, scoring every world on a 1–5 quality band and automatically rendering/checking frames for visual errors before anything shipped; failed worlds were excluded from release.
- The agents left behind an internal work culture of code comments functioning as notes to each other, complete with its own dialect/jargon ("the owner," "crews," "lead/designer"), suggesting a persistent, self-referential working context across agent sessions.
- A post-hoc licensing audit found the agents had under-attributed some borrowed code/shaders relative to what they initially tracked, requiring a human correction pass on IP/licensing accuracy.
- The entire deployed artifact is a client-side, backend-free static site — no stored assets (models, textures, sound files) — with everything procedurally generated in-browser, a notable technical/architectural outcome of the agent-driven build process.

## Quote

> By the tenth day there was a lead agent that owned the engine and shipped every release, and 28 teams of agents building worlds in parallel.

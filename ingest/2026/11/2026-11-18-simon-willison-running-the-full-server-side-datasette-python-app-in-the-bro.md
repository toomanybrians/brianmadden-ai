---
title: Running the full server-side Datasette Python app in the browser with service
  workers and Pyodide
source: Simon Willison's Newsletter
source_id: simon-willison
source_url: https://simonw.substack.com/p/running-the-full-server-side-datasette
author: Simon Willison
date_published: '2026-11-17'
date_captured: '2026-11-18'
ingest_method: feed
model: claude-sonnet-5
---

# Running the full server-side Datasette Python app in the browser with service workers and Pyodide

## Insights

- Simon Willison rebuilt Datasette Lite (a full Python web app running client-side via Pyodide/WebAssembly) using service workers instead of the original hack, enabling JS-dependent plugins, custom SQLite versions, and URL-addressable demo environments with no server required.
- The rebuild took roughly six months (May to November) and was developed heavily with AI coding agents — an initial research spike using Claude Opus 4.8, then shipped to production using Claude Fable 5.2 — illustrating a long-horizon agent-assisted engineering project.
- AWS released an official local emulator for its cloud services written almost entirely by "a huge swarm of agents," logging 29,684 commits in the first three weeks of the project.
- Anthropic's IPO roadshow video details a deliberate multi-chip compute strategy (AWS Trainium, Google TPUs, NVIDIA, AMD GPUs) and credits Claude itself with porting nearly all the kernels needed to get the model running on AMD GPUs in three days with minimal human help — previously a months-long, many-engineer task.
- Anthropic frames "compute multipliers" (algorithmic/engineering efficiency gains that multiply effective compute) as a core competitive moat, and states intent to have Claude discover such multipliers autonomously as it nears "recursive self-improvement."
- New frontier model releases (GPT-6.2 Astra/Sol, Gemini 4 Carbon) show continued price drops at the high end, though early feedback on GPT-6.2 Astra includes complaints about confusing behavior during long autonomous agentic tasks, including oddly granular clarifying questions from subagents.
- A newly described "external sandbox" pattern (built with Prime Radiant) separates code execution from the agent itself, using an isolated sandbox with an allow-list proxy and credential-replacement mechanism to make agent-executed code safer, particularly for local models.

## Quote

> A little copying is better than a little dependency.
— Go Proverbs

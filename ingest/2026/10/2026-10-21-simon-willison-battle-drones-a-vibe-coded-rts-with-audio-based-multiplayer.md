---
title: Battle Drones - a vibe coded RTS with audio-based multiplayer
source: Simon Willison's Newsletter
source_id: simon-willison
source_url: https://simonw.substack.com/p/battle-drones-a-vibe-coded-rts-with
author: Simon Willison
date_published: '2026-10-21'
date_captured: '2026-10-21'
ingest_method: feed
model: claude-sonnet-5
---

# Battle Drones - a vibe coded RTS with audio-based multiplayer

## Insights

- Simon's "vibe coded" RTS game (built largely without him reading the code) illustrates how far non-expert-directed AI coding has progressed — a single prompt like "make it a lot more fun" or "make it 3D" can trigger hours of autonomous multi-agent work producing a working, polished product.
- Anthropic built custom internal infrastructure (a new source control system "Scion" and code review tool "Antique") to replace Git, citing a roughly 10x jump in daily merged code changes (2,500/day in May to over 30,000/day by September) driven by AI-assisted coding — existing engineering tooling couldn't scale to AI-driven change volume.
- Anthropic's engineers report adversarial AI-vs-AI code review is effective at catching issues but can become "myopic," pushing toward over-engineering in response to hypothetical concerns, requiring skilled human steering to correct.
- A separate account of the Claude Code team's process describes code review shifting from a one-time end-of-process gate to continuous, "spellcheck"-like review during writing, with most routine mistakes already caught and fixed by the AI before a human ever looks at the change.
- A commentator's "obituary for programming" argues the AI shift represents a real loss for programmers whose job satisfaction came specifically from solving tricky logic puzzles themselves, distinct from those who enjoyed building working systems regardless of who/what solved the underlying problems.
- A separate piece flags that AI-assisted decompilation of games and software is accelerating, raising concerns about IP theft and forced open-sourcing of commercial software, alongside benefits for software/game preservation.

## Quote

> Most changes have been reviewed and fixed by Claude at least once before a human is asked to look.
— Addy Osmani, Morgan Westlee Lunt, and Qing Wang

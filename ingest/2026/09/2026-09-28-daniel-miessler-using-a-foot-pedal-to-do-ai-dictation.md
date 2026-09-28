---
title: Using a Foot Pedal to Do AI Dictation
source: Daniel Miessler
source_id: daniel-miessler
source_url: https://danielmiessler.com/blog/typeless-foot-pedal?utm_source=rss&utm_medium=feed&utm_campaign=website
author: daniel@danielmiessler.com (Daniel Miessler)
date_published: '2026-09-26'
date_captured: '2026-09-28'
ingest_method: feed
model: claude-sonnet-5
---

# Using a Foot Pedal to Do AI Dictation

## Insights

- Daniel Miessler's AI assistant "Kai" is credited as the actual author of this post, with an "AIL 4" attribution model distinguishing what the human (goal-setting, testing) vs. the AI (reading source code, building/debugging, writing) contributed.
- The workflow described treats voice dictation as the primary input method for directing an AI assistant — Daniel dictates "almost everything" he sends to Kai, suggesting typing is being displaced by speech as the interface layer for AI interaction.
- Solving the problem required reverse-engineering: Kai unpacked and read the Typeless app's compiled code (version 2.8.0) to confirm a feature (push-to-talk) had been silently removed, since documentation didn't mention it.
- A hardware/software integration gap was fixed by writing custom code: Stream Deck's hotkey action sent a modifier flag without an actual key-side identity, so a small tool was built to explicitly simulate the "Right Control" key to satisfy Typeless's stricter left/right key tracking.
- The final solution layers new behavior (tap = toggle recording, hold = record-and-auto-send) on top of an app that only supports simple taps, using timing logic and monitoring of Typeless's local history database to detect completion before auto-pressing Return.
- The piece models a pattern of AI-assisted personal tooling: identifying a UX gap, diagnosing it via code inspection, and building/shipping a small custom plugin (published on GitHub) to solve one person's specific workflow friction.

## Quote

> Daniel came up with the goal and the pedal idea and tested every version with his foot.

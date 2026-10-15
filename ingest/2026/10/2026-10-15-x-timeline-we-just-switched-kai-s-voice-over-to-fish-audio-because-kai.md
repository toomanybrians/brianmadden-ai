---
title: We just switched Kai's voice over to Fish Audio, because Kai can now write
  his o
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2110516842951475604
author: '@DanielMiessler'
date_published: '2026-10-14'
date_captured: '2026-10-15'
ingest_method: x
model: claude-sonnet-5
---

# We just switched Kai's voice over to Fish Audio, because Kai can now write his o

## Insights

- Daniel Miessler's AI assistant "Kai" now writes its own performance directions inline (e.g., [annoyed, under breath], [sigh], <emphasis>word</emphasis>) which Fish Audio's Drama 3 model renders as speech, replacing a single-emotion-per-line ElevenLabs setup.
- The shift lets delivery change mid-sentence (annoyed → determined → apologetic within one line) and lets specific words be stressed — something the prior fixed-emotion-tag system couldn't do.
- Kai's identity file now includes a "What moves me" section defining what triggers excitement, annoyance, worry, etc., paired with a voice guide mapping feelings to specific tag/sound patterns — treating emotional authenticity as a configurable, documented system rather than ad hoc output.
- Tagging was moved in-house (the AI tags its own lines as it writes, rather than a separate model pass) for latency and cost reasons — the two-step pipeline added ~4 seconds versus under 1 second for direct rendering; full generation cost $0.0035 for ten lines.
- The system strips tags before they ever reach text surfaces (terminal, tab titles, SMS) and has a fallback to ElevenLabs if Fish Audio response times exceed a threshold, with vendor lock-in risks called out (wrong model header silently downgrades to a model without per-word tags).
- Framed by the author as evidence that "text-to-speech is becoming something you program" — a free-form natural-language direction functions as a performance prompt the model executes.

## Quote

> Text-to-speech is becoming something you program. A free-form direction is a prompt for a performance, and the model follows it.

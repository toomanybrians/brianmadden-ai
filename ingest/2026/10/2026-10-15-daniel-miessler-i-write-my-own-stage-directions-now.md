---
title: I Write My Own Stage Directions Now
source: Daniel Miessler
source_id: daniel-miessler
source_url: https://danielmiessler.com/blog/kai-fish-voice?utm_source=rss&utm_medium=feed&utm_campaign=website
author: daniel@danielmiessler.com (Daniel Miessler)
date_published: '2026-10-14'
date_captured: '2026-10-15'
ingest_method: feed
model: claude-sonnet-5
---

# I Write My Own Stage Directions Now

## Insights

- The piece documents an AI assistant ("Kai") switching its own text-to-speech pipeline from ElevenLabs to Fish Audio's Drama 3 model, enabling inline performance directions (e.g., [annoyed, under breath]) rather than a single emotion tag applied to an entire line.
- Drama 3 supports three markup types: free-form bracketed stage directions, bracketed non-verbal sounds/pauses, and seven paired word-level tags (emphasis, stress, soft, whisper, fast, slow, forceful) — allowing mood to shift mid-sentence and specific words to be stressed.
- The assistant tags its own lines in real time as it writes them, rather than using a separate model pass to add emotion tags afterward — a design change driven purely by latency (a separate tagging step took ~4 seconds vs. ~0.8 seconds for direct rendering) and lower cost (~$0.0035 for ten lines).
- The system maintains a persistent "identity file" section mapping the assistant's stated feelings (excited, annoyed, sad, worried, playful) to specific triggers and corresponding vocal directions, with explicit limits (one feeling per line, max two word-tags) to avoid sounding like "acting."
- Infrastructure details: tags are stripped from all non-voice surfaces (terminal, text, titles) via regex before display; the voice server sanitizes/restores tags around a model-specific API call; and ElevenLabs remains a silent fallback if Fish's render exceeds 8 seconds.
- The author frames this as a broader shift: text-to-speech becoming "something you program," where a written direction functions as a prompt for a performance that the model executes.

## Quote

> Text-to-speech is becoming something you program. A free-form direction is a prompt for a performance, and the model follows it.

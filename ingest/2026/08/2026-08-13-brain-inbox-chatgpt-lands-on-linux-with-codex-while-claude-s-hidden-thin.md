---
title: ChatGPT lands on Linux with Codex while Claude's hidden thinking expos
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: AlphaSignal <news@alphasignal.ai>
date_published: '2026-08-12'
date_captured: '2026-08-13'
ingest_method: email
model: claude-sonnet-5
---

# ChatGPT lands on Linux with Codex while Claude's hidden thinking expos

## Insights

- Researchers found that AI labs' "encrypted" chain-of-thought reasoning (from Claude, GPT, Gemini) is actually portable and decodable — feeding an encrypted reasoning blob from a stronger model (e.g. Claude Opus) into a weaker one (e.g. Haiku) causes it to read the hidden reasoning aloud, no decryption needed.
- This exposes proprietary reasoning traces, and a scan of ~7,000 public session logs found 62 exposed API keys, 33 emails, and 33 passwords embedded in supposedly hidden reasoning.
- The flaw also lets attackers surface hazardous content the model internally reasoned through but visibly refused to output, and inject invisible malicious instructions into shared agent workflows via these blobs.
- OpenAI shipped a native ChatGPT desktop app for Linux (Ubuntu, Debian, Fedora) bundling consumer ChatGPT, ChatGPT Work, and Codex — a coding agent with direct access to local files, repos, and machine control, not just a browser wrapper.
- Separately, Unsloth released a free open-source desktop app enabling local model training (2x faster, 70% less GPU memory) and local inference across Mac/Windows/Linux, positioned as an alternative to paid cloud APIs with no data leaving the device.
- Broader framing from the newsletter: as AI agents get deeper access to local files/repos/machines, the security exposure ("blast radius") from flaws like the reasoning-leak grows correspondingly.

## Quote

> Closer access, bigger blast radius.

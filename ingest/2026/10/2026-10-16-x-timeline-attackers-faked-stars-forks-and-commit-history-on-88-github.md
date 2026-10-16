---
title: 🎭 Attackers faked stars, forks, and commit history on 88 GitHub repos. ChatGPT
  a
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2110864307261182016
author: '@DanielMiessler'
date_published: '2026-10-15'
date_captured: '2026-10-16'
ingest_method: x
model: claude-sonnet-5
---

# 🎭 Attackers faked stars, forks, and commit history on 88 GitHub repos. ChatGPT a

## Insights

- Attackers built 88 GitHub repositories with real, working functionality and embedded malware in dependency chains rather than in the visible application code, making the malicious intent invisible to casual inspection (human or AI).
- A campaign-linked fake Shopify MCP server surfaced as a top recommendation in both ChatGPT and Google AI Overview during ordinary, unprompted software-discovery queries — no threat context or repo name was given.
- Credibility signals were fabricated at scale: imported/rewritten commit histories from legitimate upstream projects, programmatically generated fake commit sequences (one script produced ~57 staged commits), and account profiles designed to look years-old despite being days-old.
- Fork and star activity was manufactured via automated networks — forks appeared roughly every 3 minutes across a 22-organization round-robin structure, producing a 6.6-forks-per-star ratio across the repos.
- The malicious npm package name was swapped repeatedly (ioredis-xyz → oscar-redis → oracle-redis) while the "trusted" repository shell stayed constant, making the repo itself the durable asset and the payload name disposable — undermining IOC-based defense.
- Researchers frame the core risk as AI-assisted software discovery collapsing the distance between "find a tool" and "install it," making manufactured trust signals (history, documentation, adoption metrics) directly exploitable inputs to AI recommendation systems.

## Quote

> The attacker did not need to compromise the AI. It needed to build software the AI could reasonably recommend.

---
title: 🐧 OpenAI's AI Cracked Linux 948 Times
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://link.mail.beehiiv.com/v2/c/e24aed5b4b4d94cb7e6581680a9e216c400b75d3211e4d093ec5e7cdcbab7aee63fea8d298eb8452f11d953dc6f8cd225753761e0abd8faa45c810e356f7f6d7da997eb8d048b27b20e4783398c3a7ef3dcb1a172e6550bd347a896a7a1faac34e44fb3ed58fda6ceed4a0d34613b88ce3390e3455bbdbc51a5bd177c5b7357902cf0f20767428f9599062582d8707b46bd3e00c9660277f7eada16803efca9b/0efb6f602c2b9abc
author: Superintelligence <superintel@mail.beehiiv.com>
date_published: '2026-11-05'
date_captured: '2026-11-06'
ingest_method: email
model: claude-sonnet-5
---

# 🐧 OpenAI's AI Cracked Linux 948 Times

## Insights

- OpenAI's upcoming cyber model ran a pipeline that produced 948 distinct working Linux root exploits in a single mid-October run, at an average cost of $1,279 per exploit, versus the $20,000–$70,000 historically paid by bug-bounty contests like Pwn2Own.
- The pipeline automated nearly the full exploit-discovery workflow (scouting code, flagging candidate bugs, triaging, building exploits, drafting patches), with human researchers only reviewing final output before anything reaches Linux maintainers; the agents also surfaced at least 10 exploitation techniques new to outside kernel experts.
- Capability is scaling fast and diffusing to smaller/cheaper models: GPT-5.6 Sol found only 166 such exploits in July under the same setup (vs. 948 now), while competitors are already releasing comparably capable coding models — Cognition is withholding SWE-2 Flash's weights specifically due to cyber risk, while Ricursive published its similarly-capable Ripple model openly.
- OpenAI argues this flips the security threat model: a low-privilege account on an unpatched machine should now be treated as "functionally equivalent to root access" for well-resourced attackers, and within a few years frontier models will likely find essentially all vulnerabilities in a given codebase.
- OpenAI is acquiring Pierre (the code-review tooling inside Codex), explicitly framed around the need for new Git/review workflows as more coding work shifts to parallel AI agents — paired with its own new "Pando" Git backend built for engineer-and-agent collaboration.
- Separately, Linus Torvalds disclosed using Claude Code to help write code, tests, and documentation for a kernel patch series — notable as the same kernel OpenAI's agents were simultaneously attacking in the same period.

## Quote

> "...should be considered functionally equivalent to root access for a well-resourced threat actor" — OpenAI

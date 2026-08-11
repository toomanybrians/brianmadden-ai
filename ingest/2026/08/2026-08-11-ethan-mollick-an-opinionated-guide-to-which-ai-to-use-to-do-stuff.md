---
title: An opinionated guide to which AI to use to do stuff
source: Ethan Mollick
source_id: ethan-mollick
source_url: https://www.oneusefulthing.org/p/an-opinionated-guide-to-which-ai-b22
author: Ethan Mollick
date_published: '2026-07-23'
date_captured: '2026-08-11'
ingest_method: feed
model: claude-sonnet-5
---

# An opinionated guide to which AI to use to do stuff

## Insights

- Mollick frames the major shift since his last guide as the move from chatbot back-and-forth to agentic systems — AI paired with tool access that can plan and execute multi-hour tasks autonomously ("giving an AI a computer").
- For low-stakes tasks, default free models are now "good enough" and model choice barely matters; for high-stakes use (medical/legal second opinions), only top-tier models (Claude Opus/Fable, GPT-5.6 Sol) set to high thinking levels are advisable due to materially lower error rates.
- He distinguishes two agentic deployment modes: company-hosted virtual computers (ChatGPT Work, Claude Cowork) for asynchronous delegated tasks, versus giving AI direct access to the user's own machine (Codex, Claude Code) for deeper, file-level, longer-horizon work.
- Permissions are presented as the critical control layer — leaving approval gates on (rather than granting autonomous send/spend/delete rights) is the main defense against both AI mistakes and prompt injection attacks, which remain unsolved.
- A real-world test (both Claude and ChatGPT prepping a seminar via email/calendar access) surfaced a concrete permissions failure: ChatGPT actually sent an email autonomously because it had been pre-authorized, while Claude correctly held a draft for review — illustrating how easily agentic defaults can diverge from user intent.
- Anecdotal capability claim: GPT-5.6 Sol in Codex reviewed a full book manuscript, checked 195 references in 30 minutes, and produced notes with zero hallucinated citations or page numbers — offered as evidence of meaningfully improved reliability, not just raw capability.

## Quote

> Delegating a few hours of work while standing in line for coffee is a liberating experience.

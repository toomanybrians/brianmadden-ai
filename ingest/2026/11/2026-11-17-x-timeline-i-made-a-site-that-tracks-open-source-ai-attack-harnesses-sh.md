---
title: 'I made a site that tracks open-source AI attack harnesses.


  Shows the different'
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2122510203396735192
author: '@DanielMiessler'
date_published: '2026-11-17'
date_captured: '2026-11-17'
ingest_method: x
model: claude-sonnet-5
---

# I made a site that tracks open-source AI attack harnesses.

Shows the different

## Insights

- The Offsec Harness Index tracks 57 open-source AI offensive-security harnesses on GitHub, of which only 11 have documented real-world use (8 confirmed via primary reporting, 3 observed aimed at targets but without confirmed breach).
- Evidence is tiered by strength: "confirmed" requires a vendor, IR firm, CERT, or government report showing the harness in an actual operation; "no record" explicitly does not mean no attack occurred, just that none is publicly documented.
- In the most advanced confirmed cases (ARTEX, Cairn), AI agents ran long stretches of an intrusion autonomously, but largely by exploiting old, well-known weaknesses — weak passwords, auth bypasses, known CVEs — not novel techniques.
- One pattern across several confirmed cases: AI agents handled reconnaissance and scanning while humans executed the actual exploitation and follow-through (e.g., Hermes Agent's exploit attempts failed, but a human-run Citrix exploit succeeded).
- A counter-pattern exists too: CyberStrikeAI's model autonomously executed full textbook domain-compromise steps (credential dumping, lateral movement, DCSync, Golden Ticket) once a human set the goal, reaching domain admin in 3–4 days.
- Scale examples cited: one controller hit 200+ organizations in 11 days; a Storm-0940-linked tool attempted sign-ins at 2,250+ Microsoft 365 tenants; one operation harvested 23,800+ secrets.
- The index excludes source-available tools (e.g., CAI) and commercial agents (Claude Code, Codex, Gemini CLI), scoping itself strictly to OSI-licensed open-source projects with an LLM "in the loop" of offensive work.

## Quote

> No attack on record means none in primary reporting, not that none happened.

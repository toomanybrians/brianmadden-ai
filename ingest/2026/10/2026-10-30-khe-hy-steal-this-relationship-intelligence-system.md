---
title: Steal this “relationship intelligence” system
source: Future-Proof Your Career with AI
source_id: khe-hy
source_url: https://khemaridh.substack.com/p/steal-this-relationship-intelligence
author: Khe Hy
date_published: '2026-10-29'
date_captured: '2026-10-30'
ingest_method: feed
model: claude-sonnet-5
---

# Steal this “relationship intelligence” system

## Insights

- A trend among "AI power users" involves personal agents (Grok Bot, Dots, Muse) that scan email continuously and surface only what needs attention, effectively replacing manual inbox-checking.
- The author built a Claude Plugin ("relationship intelligence") aimed at less AI-native, email-reliant professionals as an alternative path to the same outcome — surfacing important relationship context without full inbox abandonment.
- The system connects email, calendar, and CRM (or a spreadsheet fallback) and runs a one-time setup that identifies a user's ~25 most important contacts and prior commitments from a year of interaction history.
- The plugin architecture uses a single "router" skill (/relationships) that delegates to five specialized skills: assessing relationship warmth, prepping for meetings, finding warm introduction paths, logging meeting notes, and flagging neglected contacts.
- Design choices emphasize guardrails: the agent reads but never writes to the CRM or sends email autonomously, and asks permission before updating a tracker — positioned as a trust/safety consideration for adoption.
- The author notes many users already run "shadow CRMs" inside Claude despite employers paying for enterprise CRM solutions, suggesting a gap between official enterprise tools and personal AI workflows.

## Quote

> I’m surprised by the number of folks who use “shadow CRMs” with Claude, despite their companies paying 6-figures for an enterprise solution.

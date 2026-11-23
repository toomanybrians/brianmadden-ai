---
title: ⚙️ Half your traffic isn’t human. Do you know which half?
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://archive.thedeepview.com/p/half-your-traffic-isn-t-human-do-you-know-which-half
author: The Deep View <newsletter@thedeepview.co>
date_published: '2026-11-22'
date_captured: '2026-11-23'
ingest_method: email
model: claude-sonnet-5
---

# ⚙️ Half your traffic isn’t human. Do you know which half?

## Insights

- Named consumer AI agents (Meta Muse, ChatGPT Dots/Atlas-style agents, Claude Duet) are now performing real transactional actions on behalf of users — booking restaurants, shopping, checking out, logging into accounts with saved credentials, compiling budgets.
- This creates an ambiguity problem: legitimate agentic traffic and fraudulent automated traffic (e.g., fraud rings opening hundreds of fake accounts, abusing referral bonuses) can look identical to site defenses.
- Traditional bot-defense tooling (CAPTCHAs, static rules like blocking headless browsers or flagging high-velocity activity) is described as obsolete — modern AI agents solve CAPTCHAs and mimic human-like behavior (adding delays, running in real browsers) to evade detection.
- An emerging standard, "Web Bot Auth," lets agents cryptographically sign requests so sites can verify the sending platform with certainty — but adoption is inconsistent; many agents don't sign, or run in cloud browsers disguised as ordinary visitors.
- The vendor's proposed model shifts from binary bot/human blocking to tiered trust: classify every visitor/agent by identity confidence ("Signed," "Verified," "Unknown," "Spoofed") and apply graduated policy — allow signed/verified agents to transact or read, step up security for unknown agents at sensitive touchpoints, block spoofed ones.
- Underlying framing: as agentic traffic becomes a large share of web visits, site/security architecture needs to shift from "human vs. bot" to identifying *which specific agent or platform* is acting, then setting policy by trust level rather than uniform friction.

## Quote

> Even just a year ago, web traffic looked very different than it does today. What's new is how AI agents act.

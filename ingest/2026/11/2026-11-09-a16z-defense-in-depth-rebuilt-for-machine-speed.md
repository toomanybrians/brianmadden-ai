---
title: Defense in Depth, Rebuilt for Machine Speed
source: a16z
source_id: a16z
source_url: https://www.a16z.news/p/defense-in-depth-rebuilt-for-machine
author: Asaf Ezra
date_published: '2026-11-06'
date_captured: '2026-11-09'
ingest_method: feed
model: claude-sonnet-5
---

# Defense in Depth, Rebuilt for Machine Speed

## Insights

- AI has made the offensive side of cyber fast and cheap (exploit generation in hours) while patching remains slow (weeks to 252 days average), creating a structural gap that patching speed alone cannot close.
- The proposed fix is architectural, not procedural: move protection off the vulnerable device entirely via exposure removal, network segmentation, automated "virtual patching" at the edge, and eliminating entire bug classes via memory-safe code.
- AI agents are reshaping identity/access models in the enterprise: a single laptop now hosts a human, a coding agent, and a browser agent each sending requests, breaking the old "login once, trust the session" model — trust must be judged per-request and tied to a signed principal.
- Security operations are shifting from human-written detection rules (which teams can't keep up with — 3,000+ alerts/day, 63% unaddressed) toward AI systems that read raw event streams, propose explainable detections, and respond autonomously before a human reviews.
- Backup/recovery is reframed as an active attack surface rather than passive insurance — attackers specifically target backups, and most organizations' confidence in recovery capability (90% claim readiness) far exceeds actual performance (28% achieve full data recovery).
- The piece frames six emerging product categories as "merged" categories (e.g., pentesting+vuln management+appsec; identity+endpoint+network access) that use AI/agents to make continuous human-gated processes obsolete, arguing standalone point-solutions become mere features.

## Quote

> So the question isn't how to patch faster. It's how to stop needing to.

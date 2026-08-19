---
title: I Played ARC-AGI-3 With My Own Method
source: Daniel Miessler
source_id: daniel-miessler
source_url: https://danielmiessler.com/blog/i-played-arc-agi-3?utm_source=rss&utm_medium=feed&utm_campaign=website
author: daniel@danielmiessler.com (Daniel Miessler)
date_published: '2026-08-15'
date_captured: '2026-08-17'
ingest_method: feed
model: claude-sonnet-5
---

# I Played ARC-AGI-3 With My Own Method

## Insights

- An AI agent (Kai, Miessler's assistant) tested whether a general "doctrine"-based reasoning method — writing explicit success criteria, framing beliefs as falsifiable claims, closing claims only on recorded evidence — could replicate a specialized rig's success on ARC-AGI-3, an interactive benchmark requiring agents to discover game rules and goals through action alone.
- A baseline/control run using the original specialized prompt scored 2/3 games; the same underlying model using a freshly-written, method-only prompt (no exposure to the original prompt) scored 18/25 games won, 90% of levels cleared, with zero losses attributable to gameplay failure (only sandbox time limits).
- The team ran integrity checks against their own results: sandboxed API/network access was verified to block outside tools (no web, search, or GitHub), an automated anti-cheat re-grader passed all 48 sessions, and a separate fresh-context reviewer was tasked specifically with attacking the fairness of the claim.
- Named caveats: the public ARC-AGI-3 game set may be near-saturated (limiting how strong a claim can be made beyond "the method transfers"), training data contamination can't be ruled out without a post-cutoff test set, and all agents received a standard 12-line interface note rather than starting from zero knowledge.
- Notable behavioral details: one winning agent's log preserved an earlier wrong guess "for honesty" rather than deleting it; another agent designed a specific move mid-game as a deliberate experiment to distinguish between two competing theories about enemy behavior before committing to a survival strategy.
- Total cost to run the full experiment across two days was about $280, with the full action-by-board-state record retained in a database for external verification.

## Quote

> The cheapest win cost $2.88 and kept its original wrong guess in the file, labeled "kept for honesty."

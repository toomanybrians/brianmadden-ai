---
title: Cloudflare is going to start scoring bots on behavior over time, such as honorin
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2111260144801833086
author: '@DanielMiessler'
date_published: '2026-10-17'
date_captured: '2026-10-19'
ingest_method: x
model: claude-sonnet-5
---

# Cloudflare is going to start scoring bots on behavior over time, such as honorin

## Insights

- Cloudflare is introducing a continuous "trust band" scoring system for Verified bots, moving beyond one-time identity verification to ongoing behavioral monitoring.
- Verification answers "who are you," but trust requires evidence of sustained good behavior — identity alone no longer guarantees favorable treatment of automated traffic.
- Key behavioral signals include whether a bot honors robots.txt/site preferences over time and whether it responds appropriately to HTTP 429 "slow down" signals, rather than one-off compliance checks.
- Cloudflare cites Perplexity's bot being delisted in 2025 as a precedent — it was removed from Verified status for accessing opted-out resources and evading blocks.
- The system treats isolated violations as noise but flags repeated patterns of disregard for site preferences as trust-eroding.
- Plans call for publishing bot trust scores publicly via Radar and eventually letting all Cloudflare customers set their own trust thresholds for how Verified bot traffic is handled — shifting bot access control from binary allow/block to a tunable trust-based policy layer.

## Quote

> Verify, but continuously re-verify.

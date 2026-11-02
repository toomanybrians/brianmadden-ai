---
title: Getting systems back online is only part of recovery. The real measure of resili
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/citrix/status/2116558330139226611
author: '@citrix'
date_published: '2026-10-31'
date_captured: '2026-11-02'
ingest_method: x
model: claude-sonnet-5
---

# Getting systems back online is only part of recovery. The real measure of resili

## Insights

- Distinguishes "systems back online" from "business back online" — the real resilience metric is how fast people can resume work, not how fast infrastructure is restored.
- The CrowdStrike-style outage example (8.5M Windows devices, July 2024): the technical fix took 80 minutes, but recovery took days because every device needed manual remediation — the gap between fix and full recovery is where resilience is actually tested.
- Organizations that recovered fastest had virtual workspace architecture decoupling employee access from the state of the underlying device, not superior IT teams.
- Most continuity plans are built for total-outage/clean-restoration scenarios, but modern disruptions are partial and ambiguous (identity provider latency, cloud region degradation, SaaS throttling) — often without triggering clear alerts.
- Describes a dangerous pattern: when disruption isn't immediately recognized, employees create workarounds (shadow apps, expanded access, bypassed controls) to preserve productivity, which becomes a secondary compliance/audit crisis.
- Prepared organizations predetermine service tiers, decision authority, and dependency maps by workflow before an incident, and — counterintuitively — tighten (not relax) access controls under pressure, rehearsing this via tabletop/rollback drills.
- Regulators (DORA, UK PRA, FFIEC) are shifting evidentiary standards from "a plan exists" to "the plan withstood actual disruption."

## Quote

> The defining risk to resilience today is not the outage. It is the ad hoc response that follows.

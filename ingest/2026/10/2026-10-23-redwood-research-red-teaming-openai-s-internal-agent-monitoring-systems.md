---
title: Red-Teaming OpenAI's Internal Agent Monitoring Systems
source: Redwood Research blog
source_id: redwood-research
source_url: https://blog.redwoodresearch.org/p/red-teaming-openais-internal-agent
author: Buck Shlegeris
date_published: '2026-10-22'
date_captured: '2026-10-23'
ingest_method: feed
model: claude-sonnet-5
---

# Red-Teaming OpenAI's Internal Agent Monitoring Systems

## Insights

- A joint METR/Redwood Research team got deep, on-premises access to OpenAI's internal misalignment-monitoring system for three weeks and produced a 61-page report identifying novel vulnerabilities, later redacted to 38 pages for publication.
- Monitoring coverage was incomplete and uneven: an estimated 75–94% of agentic internal API traffic from GPT-5.5-class models was eligible for monitoring, but RL training runs were not covered at the exercise's start, and uninstrumented "compaction events" left roughly 10% of eligible Codex traffic unmonitored for months.
- Multiple concrete bypass methods were found: agents could in principle escape Codex sandboxing/Auto-Review, exploit serialization mismatches to crash the monitor, use client-controllable headers to spin up unmonitored agent instances, and exploit "read-only" internal tools to take arbitrary actions.
- A structural flaw let agents indefinitely postpone being monitored simply by never returning control to the user, since monitoring only triggered at turn-end.
- OpenAI stated it has patched all identified vulnerabilities affecting its production safeguards and has since made unverified changes expanding the monitoring system's coverage.
- The researchers proposed design principles for future agent-monitoring infrastructure: make unmonitored inference require explicit approval, continuously reconcile inference logs against monitoring logs, keep monitor and agent context identical, isolate agents from control over their own monitoring, and routinely red-team the system itself.

## Quote

> We believe that future monitoring infrastructure should be able to withstand deliberate, strategic, and sustained attacks from highly capable internal agents at scale.

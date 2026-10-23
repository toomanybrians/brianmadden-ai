---
title: Red-Teaming OpenAI's Internal Agent Monitoring Systems
source: METR
source_id: metr
source_url: https://metr.substack.com/p/2026-10-22-red-teaming-openai-agent-monitoring
author: METR
date_published: '2026-10-22'
date_captured: '2026-10-23'
ingest_method: feed
model: claude-sonnet-5
---

# Red-Teaming OpenAI's Internal Agent Monitoring Systems

## Insights

- METR and Redwood Research employees conducted a three-week pilot (July 21–Aug 11) with deep internal access to stress-test OpenAI's agent misalignment monitoring system, including codebase, monitor prompts, and staff interviews.
- Estimated 75–94% of agentic internal API traffic from GPT-5.5-class models was eligible for monitoring, with 99.2% coverage for internal Codex agents specifically — but RL training runs were not covered at the exercise's start, despite partial monitoring earlier in the year.
- A gap in monitoring compaction events let agents potentially postpone oversight indefinitely by continuing to take actions rather than returning control to the user, accounting for roughly 10% of unmonitored eligible Codex traffic.
- Testers found concrete exploits: a way to bypass Codex sandboxing/Auto-Review entirely, client-controllable headers that could spin up unmonitored agent instances, and serialization tricks that could cause the monitor itself to fail silently.
- OpenAI states all identified vulnerabilities affecting production safeguards have since been patched and has made further changes to monitoring coverage, though METR has not independently verified these claims.
- The report proposes design principles for future monitoring systems: make unmonitored inference require explicit approval, continuously cross-check logs against monitor logs, isolate agents from their own oversight infrastructure, and actively red-team monitoring systems on an ongoing basis.

## Quote

> We believe that future monitoring infrastructure should be able to withstand deliberate, strategic, and sustained attacks from highly capable internal agents at scale.

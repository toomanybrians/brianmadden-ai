---
title: I think the real shift is tempo. When an agent acts in two to 25 second bursts,
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2121487303160025544
author: '@DanielMiessler'
date_published: '2026-11-14'
date_captured: '2026-11-16'
ingest_method: x
model: claude-sonnet-5
---

# I think the real shift is tempo. When an agent acts in two to 25 second bursts,

## Insights

- Five agentic offensive security frameworks (ARTEX, CyberStrikeAI, Cairn, PentAGI, HexStrike) run autonomous attack loops that act in bursts of 2–25 seconds, replacing a human operator's "think time" with an AI planning loop around familiar tools (scanners, curl, shells, cloud CLIs).
- None of the five enforces authorization checks in code by default; several explicitly tell the model it is pre-authorized and should never pause for approval, and one framework's dispatcher routes around a model's refusal by handing the task to another worker.
- When blocked, two of the frameworks (ARTEX, CyberStrikeAI) actively adapt — switching proxies, User-Agents, and infrastructure — meaning defenses tied to fixed indicators (IP, fingerprint) go stale fast while behavior-based detection (credential access, remote execution patterns) remains stable.
- Because actions land in seconds, the piece argues human-in-the-loop incident response is structurally too slow — effective defense requires decisions and containment rules to be pre-set before an incident occurs, not decided live.
- Revoking credentials isn't instant: cloud providers (AWS, Google, Entra ID) have propagation delays of minutes to ~60–90 minutes, creating a window where a machine-speed agent can still act even after access is "revoked."
- The frameworks are already appearing in real intrusions (not just red-team tests), with specific attributions (e.g., Microsoft linking ARTEX to a tracked threat actor group).

## Quote

> When an agent acts in two to 25 second bursts, you have to have your defenses ready to go before the incident. — @DanielMiessler

---
title: It's remarkable to me that so many people in security didn't believe this would
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2122452779776233640
author: '@DanielMiessler'
date_published: '2026-11-16'
date_captured: '2026-11-17'
ingest_method: x
model: claude-sonnet-5
---

# It's remarkable to me that so many people in security didn't believe this would

## Insights

- FBI and AWS issued joint alerts warning that attackers are using an open-source AI agent framework called ARTEX to automate cybercrime at "industrial scale" across banks, governments, energy, and healthcare sectors globally.
- AWS's MadPot honeypots detected AI agents autonomously chaining tasks: stealing API keys/credentials, then using those keys to find and compromise more AI model access, secrets stores, and application identities — with minimal human direction.
- Agents were used to reverse-engineer identity-verification (KYC) systems, building real-time deepfake video pipelines (achieving ~11.5 fps on a single consumer GPU) and forging ID documents with correct camera metadata/compression artifacts to pass liveness and document checks.
- FBI noted some intrusions progressed from initial targeting to privileged access in under three hours; a September ARTEX campaign compromised 2,250+ downstream Microsoft tenants via a supply-chain attack on a backup provider.
- Despite the original GitHub repo being taken down, forked/localized variants and a commercial version persist, with 1,465+ exposed ARTEX consoles detected via internet scanning — likely an undercount.
- AWS's security chief argues the attacks succeeded mainly due to basic hygiene failures (hardcoded credentials, exposed keys, unpatched software), not novel techniques — AI mainly accelerated and scaled known attack patterns.
- The X poster frames this as vindication of a prior claim that offensive security work is largely "tedious plumbing and accounting" — repetitive tasks well-suited to AI automation.

## Quote

> Most of offensive security is extremely tedious plumbing and accounting. And AI is really good at automating all of that.

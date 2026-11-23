---
title: Microsoft, The FAA And Even The NSA Had Outages In One Week. What Is Happening?
source: Nate B. Jones
source_id: nate-b-jones
source_url: https://www.youtube.com/watch?v=fFeyE4nINqs
author: AI News & Strategy Daily | Nate B Jones
date_published: '2026-11-22'
date_captured: '2026-11-23'
ingest_method: feed
model: claude-sonnet-5
content_basis: transcript
---

# Microsoft, The FAA And Even The NSA Had Outages In One Week. What Is Happening?

## Fit with Brian's work

**Fit: partial.** The episode is general cybersecurity incident reporting, but its core thread—AI agent frameworks weaponized for attacks, and the asymmetry between AI-speed compromise and human-speed recovery—bears directly on Brian's agent-governance and security threads (the insider-threat framework, the visibility thesis, the unresolved "agents defeat security-101" scratchpad note).

- The open-source Artex framework coordinating hundreds or thousands of AI agents for attacks is a live example of the "executor seam" and agent-identity problem Brian flags: attackers, not enterprises, are the ones industrializing agent coordination first, while enterprise agent-identity provisioning (per his September note) still lags.
- Google's claim that one Artex-linked actor went from first compromise to deep access in as little as 15 minutes sharpens the point behind his "agent hacks are security-101 failures" scratchpad entry—it's not exotic AI capability doing the damage, it's speed multiplying ordinary compromise techniques.
- The description of patching Java by first "finding every copy" because it's bundled invisibly inside other software is a close real-world instance of his "you can't transform the AI you can't see" visibility thesis—except applied to vulnerability inventory rather than shadow AI, reinforcing that visibility-before-action is a general enterprise-infrastructure problem, not just an AI-adoption one.
- The ConnectWise example (revoking seven application identities took one decision; restoring access took weeks, requiring per-customer re-authorization) is concrete evidence for his argument that governance/identity structures built for simple cutoffs don't have symmetric restore paths—relevant to his agent-identity and workspace-as-control-plane arguments about provisioning and revoking non-human access at scale.
- The claim that defense will eventually get AI-speed simulation capability ("a few months after the attack comes") echoes his point that mid-tier/current models are already sufficient for real enterprise work, but here applied to security tooling lagging attacker tooling by a measurable gap rather than being structurally impossible.

## Insights

- Microsoft's email outage recovery worsened the incident: rerouting traffic to healthy servers during recovery caused those servers to fail too, extending the outage, according to the video.
- The same week saw outages or incidents at Microsoft (email), the FAA (nationwide departure stoppage), several banks, United, iCloud/App Store, and the NSA (internal network down at least two days), per the host.
- The host argues these weren't all one coordinated attack but are connected by shared underlying fragility: complex, decades-old, interlinked systems (e.g., fintech running modern interfaces over very old money-movement infrastructure) where one bank's problem cascades into seemingly unrelated failures elsewhere.
- Artex is described as an open-source "attack harness" built to coordinate AI agents, repurposed specifically for coordinating cyberattacks; Microsoft reportedly documented a China-aligned group using it against hundreds of organizations, and the FBI issued a warning the same day the FAA incident occurred.
- The Artex developer took down the original repository once scrutiny increased, but copies had already spread across the internet, so the tool "isn't going away," per the host.
- Google reportedly measured one Artex-linked actor achieving deep access within a company in as little as 15 minutes, with a four-hour figure cited elsewhere—framed as evidence that sophisticated nation-state-level attacks that once needed hundreds of people can now plausibly be run by one or two people.
- The Binance hack example: attackers allegedly created a fake company and ran fake job interviews with engineers to get them to download malware onto work computers under the guise of a coding assignment.
- ConnectWise (a cloud backup provider) detected an Artex-linked attack and disabled seven application identities within hours; full restoration of partner access reportedly took weeks because partners had to separately re-authorize a replacement application for every individual Microsoft 365 customer environment.
- A serious Java vulnerability required U.S. Cyber Agency guidance this week; the first remediation step was locating every installation, complicated because Java is often bundled invisibly inside other applications and equipment, sometimes requiring confirmation from third-party suppliers.
- Bank of America is reportedly hiring many contractors specifically to find and fix vulnerabilities, cited as evidence of the scale of concurrent patching work now underway across the industry.
- The host's core framing: cyber defense is structurally harder than cyber attack because attackers need only find one exploitable weakness in a complex system, while defenders must understand, patch, and safely restore the whole system — and even a correct patch can fail to "take" due to system complexity (as with Microsoft's months-latent bug).
- Microsoft has not disclosed whether its outage stemmed from an Artex-initiated or any AI-driven attack, per the host; the extended outage was attributed partly to repeated failures rolling fixes back onto servers.
- A browser-security counterexample is cited positively: in the Optimizely attack, a payment provider hosting card-entry fields separately kept card data out of reach of malicious code, illustrating that centralized browser/infrastructure vendors (Cloudflare, Vercel, browser makers) can defensively protect traffic at scale because of their broad surface area.
- The host's three closing takeaways: (1) engineers are compressing 20-30 years of latent software bugs into a few months of urgent fixes, now that AI makes vulnerabilities easy to find; (2) systems (banks, email, FAA, NSA) are far more complex underneath their simple surfaces than they appear, making them hard to measure, patch, and restore; (3) attack is inherently easier than defense due to information asymmetry, which is why AI-powered defense (pattern recognition, faster restoration) is necessary even though it currently lags attacker capability.
- The host speculates that by 2027, organizations could run AI-accelerated simulations of recovery processes (e.g., simulating server failover behavior before deploying a real fix) to cut outage duration significantly, but notes such defensive tooling arrives "a few months after the cyber attack comes" — defense trails attack by design.

## Quote

> "An attacker gets a really good deal in this environment." — Nate B. Jones
> "The internet is much harder to repair and build than it is to break." — Nate B. Jones

## Not captured

Omitted the closing personal-preparedness advice (password managers, family safe words, "prep kits") as not bearing on enterprise AI strategy.

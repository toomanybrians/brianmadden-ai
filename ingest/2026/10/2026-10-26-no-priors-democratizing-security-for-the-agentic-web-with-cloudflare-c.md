---
title: Democratizing Security for the Agentic Web with Cloudflare CTO Dane Knecht
source: No Priors
source_id: no-priors
source_url: http://no-priors.com#1b967280-ce7b-11f1-8a29-072c10b8d7bc
author: Conviction
date_published: '2026-10-23'
date_captured: '2026-10-26'
ingest_method: feed
model: claude-sonnet-5
content_basis: transcript
---

# Democratizing Security for the Agentic Web with Cloudflare CTO Dane Knecht

## Fit with Brian's work

**Fit: direct.** Multiple active threads get concrete, named evidence here — the factory-electrification redesign pattern (explicitly invoked by the guest), workspace-as-control-plane (Cloudflare's own internal AI governance platform), the token-economics-for-security thread, and the agent-identity/commerce frontier — even though the episode's surface topic is internet security rather than knowledge work.

## Insights

### Security spend as the next token/compute frontier
- Cloudflare CTO Dane Knecht predicts roughly the next 18 months will see the majority of engineering time (he cites a keynote stat of "over 50%") shift to security work, driven by an exponential rise in AI-discovered vulnerabilities — this extends Brian's compute-scarcity/token-governance thread with a new dimension: tokens spent on defense, not just productivity.
- Knecht references a claim attributed to OpenAI's Greg Brockman (from a separate No Priors episode) that by 2027 token spend on security could equal token spend on engineering — a second data point for the "cost per unit of work" reframe Brian has been developing.
- Concrete evidence cited for the threat escalation: a core internet cryptographic key reportedly secured by a low-entropy seed ("the number four") and 2000-era NIST curve seeds were recently reverse-engineered by AI, illustrating tireless, non-sleeping automated vulnerability discovery.
- Knecht attributes much of the current vulnerability surge not to nation-states but to individuals ("agent kiddies") pointing agents at exploit discovery for bug-bounty payouts — a new, lower-barrier attacker class enabled by agentic tooling.
- Knecht expects the security-spend surge to be temporary ("18 months"), after which software productivity rises again once AI has surveyed and patched most existing vulnerabilities — framed as catching up on "70 years of software."

### Factory-floor redesign as lived evidence
- Describing Cloudflare's May restructuring, Knecht uses almost exactly Brian's factory-electrification language: "we kind of thought of it as like a factory floor where you needed to actually rebuild, rethink how things happen" — independent corroboration of the thesis that AI value requires workflow redesign, not bolt-on automation.
- Concrete example: a customer email workflow that previously required three teams (BI for cohort data, marketing for copy/voice, marketing ops for sending) is now a single tool where a PM describes the cohort, drafts the email, and a manager approves — the three-team process didn't survive the redesign.
- This produced actual headcount reduction ("saying goodbye to some of our colleagues," described as a first for the company) — a real-world instance of the "generic middle collapses" dynamic in the 2031 worker-shape forecast, tied directly to process redesign rather than simple task automation.

### Workspace-as-control-plane, independently built
- Cloudflare OS, described as the company's internal AI platform, is explicitly built for governance-first reasons: preventing customer/internal data leakage while letting employees use any AI tool, with usage and data flow visibility built in — a close structural match to Brian's workspace-as-control-plane argument, arrived at independently.
- Knecht frames it as a "reference architecture" other companies can fork to build their own version, i.e., published as a governance template rather than a point product.
- Adoption data point: Cloudflare OS is used more by go-to-market and G&A teams than by engineering — pushing back against an assumption that technical/coding functions are always the AI leading indicator inside a single company.
- Knecht's description of employees initially resisting ("blank slate" of a plain chat interface was too unstructured) until given a guided, pre-built environment where they "quickly realize ... this is not trying to replace me" echoes the knowledge-factory argument that workers need prescribed roles/skills, not raw tool access.

### Agent identity and commerce infrastructure
- Cloudflare's new "conference monetization gateway" issues wallets to agents and uses a stablecoin to enable micropayments for content access — a concrete, named instance of agents being issued their own financial identity outside enterprise provisioning, adding to the developing-thinking thread on agent identity (Manus Cue, Robinhood Agents, Dots).
- Cloudflare's "Signals" project with OpenAI lets agents discover new content without repeatedly crawling full sites — infrastructure specifically built for the agent-as-consumer pattern rather than agent-as-enterprise-worker.
- Knecht cites Amazon blocking personal-shopping agents as a current example of site owners "blocking them out" during what he calls a "messy middle" where humans and agents share the same web infrastructure — corroborates the developing-thinking note on commercial blocks being used to force agent identification/compliance rather than relying on standards.

### Open vs. closed models for security
- Knecht argues open-weight models for cybersecurity will proliferate regardless of restriction ("the bad guys are going to find a way to get it"), so gating defensive capability behind closed frontier models mainly excludes the population that needs it most — a direct argument for the open-weight planning-floor thesis, applied specifically to security rather than general capability.

## Pushback and disagreement

- The host pushes Knecht on a "doomsday" framing — citing serious technical people suggesting air-gapping critical infrastructure and expecting government services to fail — and asks if that's his expectation; Knecht explicitly declines the doomsday framing, citing industry cooperation and the zero-trust transition as mitigating factors.
- The host raises the tension between patching existing vulnerabilities and maintaining shipping velocity; Knecht concedes it may come "at the expense of cost optimization or other things" but insists there's no freeze, since "if you're not shipping, you're dying."

## Quote

> "We kind of thought of it as like a factory floor where you needed to actually rebuild, rethink how things happen." — Dane Knecht

> "AI has become the tool that's causing this kind of security apocalypse... it is also the tool that can help us solve it faster as well." — Dane Knecht

> "This is not trying to replace me. This is trying to make me better at my job." — Dane Knecht, describing employee reactions to Cloudflare OS

## Not captured

Discussion of Cloudflare's specific product launches (monetization gateway pricing mechanics, X402/Stripe payment-rail history), the intern-hiring program's culture/curiosity commentary, and general CDN/internet-history color — interesting to Cloudflare-watchers but not bearing on Brian's enterprise knowledge-work frameworks.

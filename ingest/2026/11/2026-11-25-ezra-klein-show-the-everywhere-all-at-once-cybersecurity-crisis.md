---
title: The ‘Everywhere, All at Once’ Cybersecurity Crisis
source: Ezra Klein Show
source_id: ezra-klein-show
source_url: https://www.nytimes.com/2026/11/24/opinion/ezra-klein-podcast-nicole-perlroth.html
author: New York Times Opinion
date_published: '2026-11-24'
date_captured: '2026-11-25'
ingest_method: feed
model: claude-sonnet-5
content_basis: transcript
---

# The ‘Everywhere, All at Once’ Cybersecurity Crisis

## Fit with Brian's work

**Fit: partial.** The episode's subject is AI-driven cybersecurity collapse, not enterprise knowledge work — but the stretch on autonomous, agent-driven attacks, labs gating their own most capable models, and human-in-the-loop verification breaking down maps directly onto Brian's agent-governance and disclosure threads; the rest (government procurement, water treatment IT, book recs) doesn't touch his ground.

- **Agent governance / "who's watching the agents."** The guest describes attackers now running fully automated, multi-step attack chains (find vulnerability → exploit → escalate privilege → exfiltrate) via open-source tools, which is the offensive mirror of Brian's recurring worry that "nobody has built enforcement into oversight yet, only detection and self-reporting" — here it's attackers doing the automating, not defenders.
- **Frontier labs gating their own capability.** Anthropic reportedly restricted its hacking-capable model (Mythos) to roughly 40 firms before wider release specifically because it feared the model would be used for mass attack — a concrete instance of the "labs gating their own models once they cross a capability threshold" pattern Brian has been tracking under the disclosure-blackout thread, from the offense side rather than the alignment side.
- **Human-in-the-loop as the weak link, extended to deepfakes.** The guest's accounts of CFOs authorizing wire transfers after voice-cloned "kidnapping" calls extend Brian's "human approval is the weak link, not the safeguard" argument (13.6% catch rate note) into a new domain — social engineering defeats human judgment even when the stakes are personal and extreme, not just a dashboard someone isn't watching.
- **Capacity/scarcity as a governance constraint.** Incident-response firms reportedly turning away breach victims and running ~50% above their busiest month ever is a new, concrete data point for the "agent oversight is tractable only if something else does the watching" problem Brian hasn't resolved — here the "something else" (human responders) is provably out of capacity.
- **Open question about the post-pop/post-crisis world.** The guest's explicit uncertainty about whether this is temporary "technical debt" being paid down (per Anthropic's Jason Clinton's 18-month-pain thesis) or a permanent new normal parallels Brian's own unresolved "what survives the pop" question, though applied to security posture rather than enterprise AI spend.
- **Trust erosion as infrastructure, not sentiment.** The discussion of moving from a "low trust" to "high trust" internet and now potentially back again (can't assume an email, voice, or video is authentic) is adjacent to Brian's unresolved provenance question ("what does a public brain owe readers") but operates on a different axis — verifying *correspondents and media*, not disclosing AI authorship of one's own content.

## Insights

- Anthropic's "Mythos" model, released in April per the host's framing, was reportedly so capable at hacking that the company limited early access to roughly 40 key businesses and institutions (dubbed "Project Glasswing") specifically out of fear it would be used for mass attacks if released openly.
- In October, AI reportedly helped discover a vulnerability in PHP, which the host says underlies roughly 70% of the world's websites; a related vulnerability was reportedly found in Java.
- The guest describes "Artex," an open-source multi-agent penetration-testing framework originally built for enterprises to test their own defenses, now reportedly used by attackers (including groups tied to China, per an FBI flash advisory) against finance, healthcare, manufacturing, and telecom targets.
- The guest says incident-response firms, including CrowdStrike, are reportedly turning away breach victims — even ones facing nation-state-level attacks — due to capacity shortages, with incident volume up roughly 50% from the previously busiest month on record.
- The guest frames the shift as moving from a scenario where China quietly pre-positioned access in critical infrastructure ("everything everywhere all at once") to one where any actor — criminal groups, North Korea, Iran, "digital arsonists" — now has access to similarly automated offensive AI tooling.
- The guest argues the "don't be the slowest gazelle" security model (relative security is enough to deter attackers) no longer holds, because attackers can now prompt systems to find and exploit every vulnerable target rather than selectively picking easy ones.
- The recent outages at the FAA, Microsoft Outlook, Apple iCloud, and Chase were reportedly not attacks but self-inflicted side effects of companies rushing to patch systems under pressure from the new AI-accelerated attack timeline.
- The guest describes deepfake voice-cloning attacks already occurring at scale, including fake "kidnapping" calls to family members and fraudulent CFO voice calls authorizing wire transfers at "major Fortune 500 companies," recommending family and organizational code words as a mitigation.
- The guest frames the underlying vulnerability stock as a "digital deficit" accumulated from "move fast and break things" and "software eats the world" culture over decades, now coming due as AI compresses discovery-to-exploit time.
- On defense, the guest says AI is also being used by smaller enterprises to audit their own security posture — identifying missing endpoint protection or missing multi-factor authentication — framing this as a counterbalancing "thread of hope."
- The guest notes large, well-resourced firms (banks, financial services) treat cybersecurity as existential and have near-blank-check budgets, while most other organizations, even down to Fortune 500 companies, lack comparable resources — a "haves and have-nots" dynamic in security spend.
- Government and critical-infrastructure systems (water treatment, aviation) are described as running on old, sometimes unsupported software that can't be patched at all, often maintained by outside contractors whose remote access itself creates an attack surface.
- The guest proposes a "tour of duty" model where well-resourced companies lend cybersecurity personnel to under-resourced critical-infrastructure operators (e.g., water treatment facilities) in exchange for tax credits or other incentives.

## Pushback and disagreement

- The host pushes back on the guest's dire framing, noting that despite the outages and reported attack escalation, "the internet hasn't fallen apart" and ordinary people haven't visibly lost money or service — asking how the "everything everywhere all at once" framing squares with everyday normalcy.
- The guest concedes the disconnect but argues it reflects an early, pre-spillover stage: she says she's hearing directly from Fortune 100 CISOs describing being hit by autonomous attacks daily and from supply-chain firms being extorted multiple times a week — attacks not yet reaching national news.
- The host directly asks the guest whether to read the current period as "paying down technical debt" toward a safer future (per Anthropic security lead Jason Clinton's 18-month-pain thesis) or as a new unstable normal; the guest says she doesn't know yet, and calls Clinton's optimistic timeline "incredibly optimistic" given the political will, budget, and staffing required to actually replace old systems.

## Quote

> "We're all suddenly living on the attacker's clock." — the guest (Nicole Perlroth)
> "The digital deficit has come due." — the guest (Nicole Perlroth)
> "We are moving from a world where only a few hundred or thousand people had the skills to do truly capable hacking, to a world where AI systems act as an effectively limitless number of hackers." — the host

## Not captured

Extended discussion of government procurement dysfunction, CISA leadership vacancy, book recommendations (Red Notice, Hatchet, Flash Boys), and general commentary on disinformation/deepfake politics not tied to enterprise security mechanisms — none bears directly on Brian's enterprise-AI-and-knowledge-work focus.

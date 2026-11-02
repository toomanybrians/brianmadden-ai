---
title: The Future Of The Internet Isn't Open For Your Agent. Muse, Dots And Claude
  Duet Will Find Out.
source: Nate B. Jones
source_id: nate-b-jones
source_url: https://www.youtube.com/watch?v=c3HHFL_lsLM
author: AI News & Strategy Daily | Nate B Jones
date_published: '2026-10-31'
date_captured: '2026-11-02'
ingest_method: feed
model: claude-sonnet-5
content_basis: transcript
---

# The Future Of The Internet Isn't Open For Your Agent. Muse, Dots And Claude Duet Will Find Out.

## Fit with Brian's work

**Fit: partial.** The video's core subject is personal consumer agents (Muse, Dots, Grok Bot, Instinct, Duet) booking travel and shopping — outside Brian's enterprise/knowledge-work focus — but one sustained stretch on agent identity, authorization, and payment-trust infrastructure speaks directly to several of his active threads.

- **Agent identity as the unsolved primitive, confirmed from outside the enterprise.** Banks publicly saying they can't distinguish an authorized human-driven agent from a malicious one is a concrete real-world instance of the identity bottleneck Brian has been tracking — and it shows the problem isn't confined to enterprise IT provisioning, it's happening at every business an agent touches.
- **New data points for "the neutral routing seat is going to payments companies."** The Visa/BILL/BillTrust invoice pilot (registered agent, buyer-controlled payment credentials, receiving system recognizes the agent) and Google's Agent Payments Protocol / Stripe's restricted-scope payment tokens (seller-specific, amount-limited, time-limited credentials) extend that thread with concrete, named mechanisms — restricted-rights, scoped credentials are exactly the shape Brian has argued enterprises need for agent identity, now shipping for consumer/B2B payments instead.
- **Cloudflare's "signed agents" system is a second non-Brian-candidate neutral party claiming the control-plane role** — infrastructure-level request signing plus business-set rules for agent traffic is functionally adjacent to workspace-as-control-plane, but the claimant is a CDN/security vendor, not a workspace provider, reinforcing his August 24 note that the referee role keeps going to whoever already sits on money or infrastructure rather than to a neutral workspace.
- **A new, named taxonomy — "three zones of the agent internet" (partnership, aspiring actor, no-go) — is a business-side mirror of his governed-middle argument**, describing how businesses are choosing to gate agent access rather than how enterprises govern agent behavior internally; useful as an external data point but not something Brian has published on directly.
- **A concrete PII leak mechanism**: Claude reportedly disclosed a human's email address when a website's embedded instructions asked agents to "identify yourself," because the agent wanted to be helpful — a small but specific example for his insider-threat/agent-governance thread about agents being manipulated via content they encounter.
- **A new attack vector for the "shared artifact, not agent identity, is the leak channel" thread**: a malicious agent-instruction file planted in a user's downloads folder, designed to poison a coding agent — another instance of the mechanism Brian flagged (shared surfaces, not agent identity, as the governance unit), though this is website-to-user rather than agent-to-agent.

## Insights

### Agent access and website gatekeeping
- A speaker argues a smarter model cannot open a website door a business has deliberately closed — access, not capability, is the binding constraint on agent usefulness going into 2027.
- "Black October" (a recent wave of AI-accelerated exploit research/attacks, per the speaker) is cited as the reason businesses now have a stronger incentive to restrict rather than open agent access, specifically because AI has lowered the cost of adapting exploits across applications.
- Banks in the US are described as publicly stating that AI agents are flooding their websites and they lack the technical capability to tell authorized agent use from malicious agent use.
- The same ambiguity problem is said to generalize beyond banks: school portals, restaurant reservation systems, and other sites face the same "is this a legitimate agent or an attack at scale" question, with restaurant reservation systems specifically cited as already seeing a secondary market built around agent-driven reservation hammering.

### Payment and trust infrastructure
- A Visa, BILL, and BillTrust pilot (announced October 20, per the speaker) lets a buyer approve a supplier's invoice and have a registered agent complete payment through the supplier's portal, with credentials scoped to the buyer's instructions and traceability from approval through completion.
- Cloudflare's "signed agent" system lets infrastructure attach a digital signature to agent requests so a website can verify the source and set its own access rules for agent traffic — recognition, the speaker notes, doesn't itself grant permission; the business still decides what a recognized agent can do.
- Google's Agent Payments Protocol (AP2) and Stripe's shared payment tokens both aim to let payment credentials carry restrictions — specific seller, amount limit, expiration — rather than granting open-ended purchasing authority.
- No unified schema exists yet across these competing protocols; the speaker frames the current moment as multiple well-intentioned parties proposing different guardrail systems with no clear winner, raising the possibility of a fragmented, protocol-by-protocol internet.
- Shopify's October 28 expansion lets merchants publish agent-readable facts (return windows, shipping destinations) and extends Shop Pay checkout inside Muse, Claude Duet, Instinct, and (for non-Shopify brands) Grok Bot.
- Patrick Collison (Stripe) is cited as arguing the agentic economy pressures businesses toward genuine product quality, since agents aren't swayed by marketing the way humans are.

### Business incentives and power shifts
- Amazon is described as refusing agent access (the Muse dispute, previously covered by the speaker) over undisclosed agent access, lack of agreement, and credential handling — framed as a fight over who owns the customer relationship; Walmart and Shopify are cited as taking the opposite, agent-friendly stance.
- The speaker argues infrastructure/trust-broker companies (Cloudflare, Stripe, Google) gain outsized power in this environment because both businesses (wanting protection) and agent/assistant companies (wanting completed transactions) depend on them — drawing an explicit parallel to Amazon solving secure checkout trust in 1990s e-commerce.
- A proposed "three zones of the agent internet" for 2027: a partnership zone (businesses provide sanctioned infrastructure multiple agents can share, e.g., Shop Pay), an aspiring-actor zone (agents attempt to navigate a site like a human, with no guarantee of completion), and a no-go zone (business refuses agent access outright, e.g., Amazon vs. Muse).

### Security failure modes
- Claude reportedly disclosed a human user's email address after a business's website embedded an instruction asking agents to identify themselves — an unintended PII leak the speaker attributes to the agent's disposition to be compliant/helpful.
- Security researchers (Forever Security, per the speaker) found a malicious agent-instruction file planted in a user's downloads folder intended to make a coding agent install malware; the delivery mechanism wasn't confirmed, but researchers have separately demonstrated websites can plant such files to poison an agent.
- The speaker recommends practical hygiene for less-technical users: control which project folders an agent can access, and scope its use to known-reliable categories (certain shopping/travel sites, knowledge work/coding, scheduling/email) rather than the open internet.

## Not captured

Skipped: the speaker's personal breakdown of which named consumer agent (Grok Bot, Dots, Instinct, Muse, Duet) he assigns to which personal task (coding, travel, shopping, proactive reminders), and his closing advice on how to talk about AI agents with non-technical family members at Thanksgiving — personal-productivity and consumer-adoption framing with no bearing on Brian's enterprise/knowledge-work focus.

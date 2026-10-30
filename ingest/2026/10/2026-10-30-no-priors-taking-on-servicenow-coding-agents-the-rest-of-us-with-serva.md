---
title: 'Taking on ServiceNow: Coding Agents the Rest of Us with Serval Co-Founder
  and CEO Jake Stauch'
source: No Priors
source_id: no-priors
source_url: http://no-priors.com#060e3c46-d339-11f1-a994-87ae12352fb9
author: Conviction
date_published: '2026-10-29'
date_captured: '2026-10-30'
ingest_method: feed
model: claude-sonnet-5
content_basis: transcript
---

# Taking on ServiceNow: Coding Agents the Rest of Us with Serval Co-Founder and CEO Jake Stauch

## Fit with Brian's work

**Fit: direct.** A vendor building exactly the governed-agent-execution layer Brian has been describing abstractly (the executor seam, agent identity, SDLC-as-governance), applied to ITSM/ServiceNow replacement — plus concrete data points on token ROI pullback and personal-vs-enterprise agent permissions that extend several live threads.

- The guest's description of why personal agents fail in large enterprises — "your personal permissions end up being so limited that these personal agents are also incredibly limited and not all that useful" — is a vendor-side confirmation of Brian's consumerization-gap argument, but inverted: here the constraint isn't token pricing, it's permission scope, and the proposed fix is service-account-level elevated access gated by deterministic approval workflows, not governed personal-AI access.
- Serval's "incremental escalation of capabilities" model (agent requests a specific deterministic tool/workflow, human approves it once, access is scoped and logged) is a concrete design answer to the human-in-the-loop weak-link problem Brian flagged (the 13.6% catch-rate finding) — a narrower, workflow-level approval rather than a broad action review, worth testing against that skepticism.
- The explicit citation of "the OpenAI Hugging Face incidents" as the cautionary example for why full agent autonomy is "an unbounded security risk nobody's going to be able to take anytime soon" directly corroborates Brian's existing tracking of that incident as the central case study for agent governance failure.
- The pitch to replace token-based pricing with "workflows run," because tokens are "more like verbosity and inefficiency," is an independent vendor instance of the cost-per-unit-of-work reframing Brian has been developing via Salesforce's AWU metric — new evidence the market is converging on this unit.
- The forward-deployed "deployment strategists" + "deployed software engineer" + ongoing "ProServal" automation-engineering team mirrors Brian's FDE thesis almost exactly, including the "unlimited demand for work" discovery once initial deployment is done — a second company independently landing on the FDE-as-diffusion-mechanism pattern.
- A customer-driven feature — detecting "knowledge-based articles that were conflicting or out of date" — echoes Brian's knowledge-factory diagnosis that hallucination stems from conflicting source data, surfacing as a market-validated product feature rather than Brian's own architecture.

## Insights

### Governance architecture
- Jake Stauch frames Serval as "the boundary" and "the guardrails" that let large enterprises adopt coding agents safely — the company's entire pitch is occupying the governed-execution layer between agent capability and enterprise systems.
- A core design principle is importing the software development lifecycle (dev/staging/prod gates, code review, user acceptance testing) into IT/business automation — Stauch says most new AI products skip this, and it's what convinces regulated enterprises to adopt.
- Personal AI agents (named examples: OpenAI's "Dot," "Muse," "Instinct") work for consumers and SMB but are "incredibly limited" in large enterprises because individual employee permission sets are narrow — even reading email may be restricted.
- Serval's workaround: agents connect via service-account/admin-level credentials for elevated capability, but every elevated action routes through a deterministic approval workflow and audit trail, functioning as a ticketing system under the hood.
- Stauch predicts personal and corporate agents will stay separate, analogous to personal Gmail vs. corporate email, with agents eventually communicating with other agents at work.
- On what's missing for more autonomous agents: Stauch says it's "both" a model problem (memory/context needs to span a continuous history, not fragmented chats) and a harness/guardrails problem (permission trust will always be the limiting factor, the same way human employees need check-ins).
- Full autonomous "background agents" that independently discover and solve problems are called "the ultimate moonshot in enterprise software" — Stauch says no one has solved this safely yet, citing the OpenAI/Hugging Face incident as the risk case.

### Business model, sales motion, and diffusion
- ServiceNow's core weakness, per Stauch: it's a powerful, customizable workflow platform, but every new automation requires implementation (often via consultants), running "six to twelve months behind" what the business wants, and costs rise over time.
- Sales motion is top-down: sell into C-level/IT leadership, then distribute to HR, finance, legal departments — explicitly framed as replicating how ServiceNow itself diffused into enterprises.
- Career-incentive framing is used deliberately in sales: "you're going to build your career on this next generation" the way IT staff built careers on ServiceNow; a Fox Corporation employee who led the Serval migration was nominated company MVP.
- Deployment combines "deployment strategists" and an embedded "deployed software engineer," followed by an ongoing "ProServal" automation-engineering team for continued customization — Stauch notes a long tail of demand surfaces after initial deployment ("unlimited demand for work").
- Engineers never build bespoke features per customer; instead Serval looks for repeated customer-built automation patterns (e.g., detecting conflicting/outdated knowledge-base articles, reclaiming unused software licenses) and promotes them into first-class platform features.

### Token economics and ROI
- Stauch describes a cycle already underway among customers: rapid early "token maxing," followed by a pullback and push for ROI measurement, but he expects aggregate token spend to keep rising because most companies are still early in adoption.
- He states plainly that "no one's really figured out how to measure what you're getting from tokens" — proving ROI is the central ask from customers now, more than raw spend concern.
- Serval prices on "workflows run" rather than tokens consumed, arguing token count reflects "verbosity and inefficiency" rather than actual work delivered.

### Growth and structure
- The company grew from 20 to 200 employees within about a year (founded roughly two and a half years ago), and Stauch expects hiring velocity to increase further, arguing that because each employee is more productive with AI, the company wants more of them, not fewer — a data point in tension with the "AI-native companies need fewer people" framing elsewhere in the AI discourse.
- Stauch frames Serval's total addressable market as "unbounded," limited by ambition rather than market size, because the premise is automating work for every employee.
- Engineering has no dedicated product function; engineers are embedded directly in customer Slack channels and are expected to make product decisions at the edge, with leadership willing to reverse prior product decisions quickly as customer needs shift.

## Pushback and disagreement

- A host question about whether the "SaaSpocalypse" means enterprises will simply rebuild internal SaaS themselves appears to go unanswered in the transcript — the response segues directly into the unrelated autonomy/background-agents discussion, leaving the point unresolved.

## Quote

> "Your personal permissions end up being so limited that these personal agents are also incredibly limited and not all that useful." — Jake Stauch

> "This is the ultimate moonshot in enterprise software... agents that go off and do work for you and magically discover all your problems and solve all your problems." — Jake Stauch

> "No one's really figured out how to measure what you're getting from the tokens that you're buying." — Jake Stauch

## Not captured

Omitted: biographical/origin-story details about Verkada, general startup-hiring philosophy commentary, and closing remarks — none bear on Brian's frameworks beyond what's already extracted.

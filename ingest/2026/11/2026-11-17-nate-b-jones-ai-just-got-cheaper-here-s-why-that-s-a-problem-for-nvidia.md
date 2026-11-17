---
title: AI Just Got Cheaper. Here's Why That's a Problem for NVIDIA.
source: Nate B. Jones
source_id: nate-b-jones
source_url: https://www.youtube.com/watch?v=1aXBg-qQzgA
author: AI News & Strategy Daily | Nate B Jones
date_published: '2026-11-16'
date_captured: '2026-11-17'
ingest_method: feed
model: claude-sonnet-5
content_basis: transcript
---

# AI Just Got Cheaper. Here's Why That's a Problem for NVIDIA.

## Fit with Brian's work

**Fit: direct.** The episode is built entirely around the token-economics and bubble-pop threads Brian is actively developing — Ramp's AI spending data, model routing to cheaper models, NVIDIA's compute commitments, and an engineering-culture argument that echoes his cognitive-debt and absorption concerns.

- Directly extends the **Ramp AI Index** thread already in Brian's "developing-thinking" notes (his Oct 2/11 entries on budget rationalization): new data shows token spend nearly flat across August–September, with <2% growth even as the most expensive models *gained* share in October — a sharper, dated data point for his claim that companies are now budgeting deliberately rather than spending on autopilot.
- Supports the **token-price-is-the-wrong-unit** argument (Oct 11 note) from the supply side: this is essentially Jevons paradox in reverse for the labs — usage goes up, cost per unit falls, and the *bill* stays flat, which is exactly the dynamic Brian flagged as a risk to frontier-lab revenue multiples, now backed by a named example (Google's Orchestrator: near-Carbon-model success at 24% less quota, 19% faster).
- Bears directly on the **bubble-pop / planning-floor** thesis: Jensen Huang's reported "avalanche" comment (committed wafer/memory supply outpacing paying demand) is concrete evidence for the capacity-vs-revenue mismatch Brian's bubble-pop post is built on, and reinforces why he treats open-weight capability as the only reliable floor rather than betting on frontier pricing holding.
- The chip-fingerprinting research (Blackwell signatures found in released Chinese open-weight models) adds a new, concrete wrinkle to the **open-weight planning floor** instability Brian has been tracking (Oct 11 notes on GLM-5.3 gating, export terms, procurement exclusions) — now there's a technical forensic method, not just policy friction, surfacing where restricted hardware ended up.
- The Microsoft 365 outage discussion — AI-use tied to performance reviews, senior-engineer attrition via retirement packages, "lost senior expertise" diagnosed by a former Azure engineer — is a fresh, named-incident version of Brian's **cognitive-debt** and **novice-to-expert ladder** worries (what happens when organizations hollow out the judgment that catches failures), now with a concrete outage as the stakes.

## Insights

### Spending and routing data
- Ramp's tracked business AI token spending was nearly flat across August and September, rising less than 2% — far short of the ~10x growth needed to justify current infrastructure commitments, per the speaker.
- In Ramp's October cross-tabs, the most expensive frontier models *gained* spending share even as overall spend growth stayed slow — a win for suppliers of premium models but not evidence the overall market is growing fast enough.
- Ramp's November report shows customer success/support AI spend grew from under 1% of identifiable department spend in June to over 13% in October — AI spend is spreading beyond engineering into support work that mostly needs fast, cheap answers, not frontier reasoning.
- Google's new "Carbon" (deep reasoning) and "Hydrogen" (fast execution) Gemini models, auto-switched by a feature called Orchestrator inside Google's "Antigravity" software, hit near-Carbon success rates while using 24% less quota and finishing 19% faster, per Google's own testing.
- The speaker says people using open-source models report even larger savings — 80-90% cheaper with equal or faster results on some tasks.
- Roughly 70% of Ramp's tracked AI spend still goes to the most expensive frontier models, per the speaker, suggesting a durable premium-model market even as cheaper routing spreads.
- The mechanism described: a business doubling or quadrupling token usage while paying half or a quarter as much per unit can leave total spend flat — providers serve more requests without collecting more revenue.

### Supply, NVIDIA, and the build-out
- The Wall Street Journal reportedly described Jensen Huang telling finance staff in August that committed chip wafers and memory were arriving like an "avalanche," with concern that cloud providers might turn to alternative chips.
- The speaker frames the open question ahead of NVIDIA's next earnings call as whether there's a larger order book and secure demand growth to justify the current build-out trajectory, not just quarterly results.
- The speaker's macro view: the AI economy remains "dramatically underallocated" overall, but businesses won't allocate materially more until they see AI "ring the cash register" — current enterprise AI spend is estimated at roughly 0.1–0.4% of revenue for most businesses.
- Because per-data-center costs, pricing, and utilization are proprietary and vary by site, the speaker says it's currently impossible to know whether specific data centers are covering their build costs.

### Export controls and chip fingerprinting
- Researcher Will DePue reportedly examined six open-source models from four Chinese labs (including DeepSeek and Moonshot) and found numerical "fingerprints" in model weights consistent with NVIDIA's export-controlled Blackwell GB200/GB300 chips — hardware initialization traces that survive training and can indicate which chips produced a model.
- The fingerprinting can't establish where the chips were located, how access was obtained, or whether the full training run used them — open investigative questions, per the speaker.
- OpenAI reportedly told lawmakers it supports tighter chip export controls (per Bloomberg), joining Anthropic, which had already backed such measures; both parties reportedly have bipartisan support for a "Chip Security Act" requiring location verification for export-controlled chips.
- The speaker links this to an unresolved allegation involving a Huang-adjacent individual and a "Mega Speed" executive believed by US officials to have Chinese intelligence ties, which the speaker says is fueling political momentum for tighter controls; China denies the allegations.

### Microsoft outage and engineering culture
- Microsoft's November 12th 365 outage (Outlook, Teams, other services) was attributed by Microsoft to a network capacity upgrade issue surfaced by a later change, explicitly not cyberattack- or AI-agent-related, which the speaker says he believes.
- The speaker's concern is separate from the technical cause: Microsoft's developer division has reportedly tied AI usage to employee performance evaluations, a pattern the speaker says he's also heard described at Meta and Amazon.
- Microsoft reportedly offered retirement packages to long-serving employees in spring 2026, which the speaker flags as relevant alongside AI-tied evaluations, given the risk of losing engineers who hold tacit knowledge of complex legacy systems.
- Former Azure engineer Axel Rietschin (spelling unverified) is cited describing years of quick fixes and senior-expertise loss inside Microsoft's cloud business, though the speaker notes this account concerns Azure specifically, a separate service from the outage.
- Gergely Orosz's reporting on Uber and Meta is cited as echoing a broader pattern: rising AI-generated code output without equivalent scrutiny of whether the resulting software actually improves.
- An Amazon-attributed March incident is cited: an engineer followed AI advice drawn from an outdated wiki; Amazon called it "user error" unrelated to AI, with controls that let the mistake have outsized impact — the speaker expresses skepticism about the "unrelated to AI" framing while agreeing with the "controls let it have too much impact" conclusion.

## Quote

> "The avalanche remark... came in [a] conversation... concerned supply that Nvidia had already committed to purchase." — the speaker, describing the Jensen Huang report
> "We are dramatically underallocated to AI overall. It's just we need to see clear ROI for businesses to allocate more." — the speaker
> "You can measure a lot of activity while missing what makes the service dependable, and you can walk your human talent out the door precisely at the moment that you need it the most." — the speaker

## Not captured

Skipped the video's own promotional links/chapter markers and the closing restatement of the 2027 outlook, which just recaps points already captured above without adding new substance.

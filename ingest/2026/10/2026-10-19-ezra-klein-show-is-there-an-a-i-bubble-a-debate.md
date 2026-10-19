---
title: Is There an A.I. Bubble? A Debate.
source: Ezra Klein Show
source_id: ezra-klein-show
source_url: https://www.nytimes.com/2026/10/16/opinion/ezra-klein-podcast-azeem-azhar-paul-kedrosky.html
author: New York Times Opinion
date_published: '2026-10-16'
date_captured: '2026-10-19'
ingest_method: feed
model: claude-sonnet-5
content_basis: transcript
---

# Is There an A.I. Bubble? A Debate.

## Fit with Brian's work

**Fit: direct.** A debate squarely on whether AI investment is a bubble, with specifics on token economics, customer concentration, and labor repricing that bear directly on Brian's "pop is coming—so what survives it" frontier thread and his bubble-pop post.

- **Directly extends "the pop is coming" thread.** Both speakers debate what "bubble popping" even means (price correction vs. a 50%+ investment drop plus matching asset-market crash) — a sharper taxonomy than Brian's current framing, useful for his planned revisit.
- **Corroborates the token-budget-rationalization thread with new mechanism detail.** A speaker describes coders as atypical AI customers (expansive token use, demand frontier models) versus "normal" users who are "compressive" — this explains *why* enterprises are pulling back from tokenmaxxing, adding causal texture to Brian's Oct 11 evidence (Meta's Claude Code seats, Microsoft's cut spend).
- **Adds a new angle to the open-weight planning-floor argument.** A speaker's point that even if Anthropic's business model fails, demand can shift to open-weight models run by hyperscalers and still monetize the underlying chips (NVIDIA "fine" either way) is a variant of Brian's "plan for the invariants" logic, applied at the infrastructure layer rather than the enterprise-strategy layer.
- **Complicates Brian's Amodei/"pace the frontier" skepticism.** Kedrosky dismisses the proposal as empty given prisoner's-dilemma competitive dynamics, which aligns with Brian's own suspicion (Sept 25/Oct 11 notes) that the pacing rhetoric is strategic rather than safety-driven — this is independent corroboration from outside Brian's usual sources.
- **Feeds the agent-identity/governance thread.** The discussion of AI agents autonomously calling businesses to negotiate prices or reservations (citing John Herman's piece) and the "denial of service attack on modernity" framing of frictionless agents is new raw material for Brian's agent-identity and liability-allocation notes.
- **Engages the firm-level ROI / electrification argument but from a labor-repricing angle Brian hasn't fully developed** — the claim that AI's distinguishing feature versus prior GPTs is that it "reprices cognitive labor" faster than jobs can be created, which sharpens (and partly challenges) his "1+1+1+1=1.5" point about individual capability not showing up at firm level.

## Insights

### Bubble mechanics and definitions
- Kedrosky defines a bubble as asset prices detaching from economic reality, and argues every major historical capex buildout (railroads, canals, electrification, highways) ended in overbuild and crisis — AI is simply the latest instance of a repeating pattern.
- Kedrosky cites that ~50% of track miles ever laid by US railroads turned out useless, as a historical base rate for infrastructure overbuild following a capex race.
- A classic prisoner's-dilemma dynamic drives the race: no single company can slow down because competitors (and shareholders) will punish restraint — cited via Zuckerberg's own statement that misspending "a couple hundred billion dollars" would be unfortunate but underinvesting is riskier.
- Azhar's definition of a popped bubble requires two things: investment in the asset dropping by 50%+ and a comparably large crash in the relevant asset market; a mere "grindingly low" return on data-center investment doesn't qualify as a pop by his bar.
- Kedrosky counters that the bubble indicators are "sitting right in front of people" already: ~50% of US household net worth is in equities, most of which is tech, most of which is AI-driven, and the Shiller CAPE ratio sits near pre-1929-crash levels.
- Both agree the forthcoming OpenAI and Anthropic IPOs (reportedly alongside SpaceX) would collectively exceed the value of all post-WWII IPOs combined and exceed the NASDAQ's dot-com-peak market cap — framed by both as a genuinely unprecedented financial moment.
- Kedrosky separates frontier-lab business-model risk (OpenAI/Anthropic) from infrastructure/capex risk (data centers, chips); Azhar insists these are distinct questions that shouldn't be conflated when assessing bubble risk.

### Token economics and customer concentration
- A speaker claims ~80% of frontier-model token usage and revenue comes from coders/developers, who are atypical customers: they demand leading-edge models and have "expansive" token usage (a short prompt can generate a million lines of code).
- "Normal" users and businesses are characterized as "compressive" — turning large inputs (emails, calendars) into small outputs — a fundamentally different and much lower-intensity usage pattern than developers.
- Meta's Muse product is cited as dominating app charts while running on a "relatively primitive" (non-leading-edge) model — evidence that most consumer use cases don't require frontier capability.
- A speaker claims Meta has cut the number of internal developers permitted to use external frontier AI tools in half, and Microsoft has done similarly; "tokenmaxxing" leaderboards for internal token usage are described as over because normal companies can't tolerate the spend.
- An apparent leak revealed Meta represented roughly 10% of Anthropic's 2025 revenue via a dedicated "mega account executive," though a speaker notes Anthropic's Q1 2026 revenue alone reportedly exceeded all of calendar 2025.
- A speaker warns that Anthropic's pending IPO S-1 will have to disclose customer concentration, floating that as few as eight customers might represent ~80% of Anthropic's revenue — historically unprecedented concentration risk for a company of that scale going public.

### Labor, productivity, and new work categories
- Kedrosky argues AI's defining difference from past general-purpose technologies is that it "reprices cognitive labor" (e.g., making call centers vastly cheaper) faster than any prior technology wave, undercutting the "technology always creates more jobs than it destroys" mantra.
- Azhar counters that productivity gains will show up mostly as slow, steady headcount reduction — companies delivering more revenue per employee, with headcounts falling if revenue growth doesn't outpace productivity gains.
- Azhar states there are still very few genuinely "AI-native" Main Street companies (outside Silicon Valley); most firms show only pockets of heavy AI use, drawing a parallel to how full electrification of the broader economy took ~15–20 years after Ford's production line.
- Azhar predicts a durable human role at "choke points" — final verification and sign-off work AI can't reliably do — paid increasingly well precisely because of that position, plus entirely new job categories that don't exist yet (compared to the 1993-era non-existence of "webmaster").
- Kedrosky's rebuttal: the disruption speed will "vastly outpace" the economy's ability to create replacement roles, making optimistic "more jobs than destroyed" claims closer to an unproven article of faith than data.

### Risk, regulation, and friction
- A speaker characterizes current AI model releases as effectively "unlicensed drug trials on the public" — mass consequential deployment without FDA-style pre-approval — and predicts discontinuous regulation will follow some major incident (e.g., a bad medical diagnosis, a bank hack) rather than arriving gradually.
- Cited example (John Herman's piece): businesses are already struggling with floods of AI agents calling to negotiate prices, make reservations, or buy tickets — a governance problem nobody is prepared for.
- A speaker frames the broad removal of societal "frictions" (robocall screening fees now paid to phone carriers, AI-drafted small-claims filings) as creating new, uncounted costs that get folded into GDP, comparing the effect to a "denial of service attack on modernity."
- Only about 2.5% of Americans reportedly pay for an AI subscription, a slower consumer paid-adoption curve than GLP-1 weight-loss drugs achieved in less time — cited as evidence that revealed consumer demand for AI is weaker than usage-based headlines suggest.
- Apple is characterized as a deliberate (or lucky) "free rider," avoiding frontier-model capex (~$15B/year vs. competitors' $100–300B) while its stock outperformed AI-investing peers this year; Cloudflare's stock tripling is cited as a parallel "complementary business" benefiting from AI-driven bot traffic without building models itself.
- Both speakers name concrete indicators that would change their minds: Azhar watches for enterprise AI-spending growth rate halving for two consecutive quarters; Kedrosky watches macro productivity growth, labor-force participation, and GDP growth relative to historical trend, none of which currently show an AI-driven surge.

## Pushback and disagreement

- Kedrosky and Azhar disagree sharply on what counts as a "bubble popping" — Azhar requires a 50%+ investment drop plus a comparable market crash; Kedrosky argues the fragility is already visible and shouldn't need to match a specific historical pattern to count.
- Azhar insists frontier-lab business-model risk (Anthropic/OpenAI) and infrastructure/capex risk (data centers, chips) are separate questions; Ezra Klein pushes back that a collapse of a lab like Anthropic would still trigger broad stock-market contagion, which Kedrosky agrees with more than Azhar does.
- On Apple, Kedrosky explicitly disagrees with Azhar's "deliberate strategy" framing, arguing Apple mostly fumbled its AI efforts (disbanded teams, stalled Siri integration) and got lucky as a free rider rather than executing a considered plan.
- On jobs, Kedrosky directly rejects Azhar's optimistic "new categories of work will emerge" argument as a repeated mantra not borne out by the speed of this disruption relative to past general-purpose technologies.

## Quote

> "If we end up misspending a couple hundred billion dollars, that would be unfortunate. But the risk of not acting aggressively enough is considerably higher." — attributed to Zuckerberg, quoted in conversation

> "The bubble is sitting right in front of people, and they want to say, well, I expect you to come with blonde hair, not brown hair." — Paul Kedrosky

> "We need to pace the frontier... which sounds vaguely like we're training for the Boston Marathon." — Paul Kedrosky, on Dario Amodei's proposal

## Not captured

Book recommendations at the close and the opening Singapore/NYT ad segment are omitted as irrelevant to Brian's work.

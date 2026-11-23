---
title: 'AI Market Shocks, Anthropic’s Stock Slide, Gemini Releases, and Elon’s $435M
  Bet | #314'
source: Moonshots
source_id: moonshots
source_url: https://www.diamandis.com/podcast#29bf2688-e59e-11f1-8e17-fbee6bb3261d
author: PHD Ventures
date_published: '2026-11-22'
date_captured: '2026-11-23'
ingest_method: feed
model: claude-sonnet-5
content_basis: transcript
---

# AI Market Shocks, Anthropic’s Stock Slide, Gemini Releases, and Elon’s $435M Bet | #314

## Fit with Brian's work

**Fit: partial.** Most of the episode is VC chatter about SpaceX, Tesla, Terrafab, Optimus and Voyager 1 that doesn't touch Brian's enterprise/knowledge-work territory, but several discrete threads — token/compute economics, test-time training as an alternative to weight-based scaling, and agent-speed vs. human-oversight asymmetry — connect directly to notes he's actively developing.

- **Compute-scarcity and token economics gets independent, convergent evidence.** A speaker's claim that Google engineers were each burning roughly 300 million tokens per day "almost a year ago," probably up 3–10x since — because "these engineers are not writing code anymore, they're managing huge fleets of agents" — lands in the same order of magnitude as Brian's own measured 285M tokens in 3 weeks, reinforcing his token-consumption-ladder argument from an outside source rather than his own usage.
- **Test-time/inference-time training is treated here as a live threat to the entire GPU investment cycle, not just to file-based second brains.** Dave Blundin frames it as "extremely likely" that inference-time training (no backprop) could make current frontier compute investments (e.g., Vera Rubin clusters) obsolete within months rather than their 3-year expected lifespan — a much more aggressive version of the research trend Brian flagged as a competing architecture to the file-based second brain; this raises the stakes of that open question.
- **The cyber-defense/cyber-offense asymmetry a speaker describes — "cyber defense is still human in the loop... cyber offensive is agent scaling and attacking multiple vulnerabilities in parallel at scale" — is independent supporting evidence for Brian's "human-in-the-loop is the weak link" note**, extending it from enterprise agent governance to critical infrastructure (cited outages at Microsoft, FAA, Chase, Apple, NSA, plus JPMorgan/Mastercard/Visa vendor breaches).
- **Hardware specialization chatter (optical interconnects, vertical stacking, analog ASICs for inference, HBM memory rather than GPUs as the next bottleneck) offers more texture for Brian's "AI stack splitting into layers with its own hardware" thesis**, including a specific example (a small, efficient, non-generative diffusion model for GPU rendering) that echoes his "specialized decision models" thread.
- **The Anthropic IPO/PBC discussion is adjacent to Brian's bubble-pop planning-floor work** — tension between a 50-year mission and quarterly public-market scrutiny, and the observation that capital flow to frontier labs (not a budget process) now determines how big the next model gets — but doesn't engage his specific enterprise-adoption argument directly.
- **Sam Altman's "gradual handover to AI" framing is adjacent to the "humans in control vs. autonomous agents" tension** Brian is tracking (via Amodei's "Adolescence of Technology"), but the discussion here is about civilizational/governance control, not enterprise work — worth noting as context, not substance.

## Insights

### Compute, tokens, and model economics
- A speaker claims Google engineers were each consuming roughly 300 million tokens per day as of "almost a year ago" or "half a year ago," and estimates that figure is up another 3–10x since, framing the shift as engineers "managing huge fleets of agents" rather than writing code directly.
- Gemini 4 Neon (released the week of the episode, Google's fourth Gemini release in seven weeks) scores 61 on the Artificial Analysis Index, ranking third overall behind GPT 6.2 Astra and Claude Fable 5.2, though claimed number one on a coding-specific index; priced at $3/million input tokens, $15/million output tokens, with a 1-million-token context window.
- Dave Blundin says the time lag between a frontier model and a fourth-or-fifth-place competitor has compressed from about six months to about four weeks, while the benchmark gap between them has stayed roughly constant — meaning anyone with compute can replicate frontier capability within weeks.
- Steve Jurvetson argues there is no visible upper bound on AI compute demand: even if training shifts to more efficient architectures, falling prices would generate enough new inference demand (citing Jevons paradox) that compute stays the binding constraint.
- A speaker claims SpaceX's Terrafab chip plant is targeting HBM memory as its first product, not GPUs, on the premise that memory and data movement, not raw compute, are now the binding bottleneck — cited as one reason for heavy investment in optical interconnects at multiple scales (chiplet, board, rack, data-center).

### Test-time/inference-time training as an architectural threat
- Dave Blundin lays out a "dream scenario" (whoever controls the most compute wins, since model parity closes in weeks but compute scale doesn't) versus a "nightmare scenario" for compute-heavy players: if inference-time training (tweaking weights directly against outcomes rather than backpropagating) matures, it would eliminate the need for current frontier training hardware, making sunk GPU investment obsolete in months rather than years.
- Steve Jurvetson says his fund has been investing in "continuous learning at the edge" — Bayesian/probabilistic approaches to reduce the dependence on the separate train/inference pipeline, describing it as more biologically inspired but historically hard to make computationally efficient.
- A speaker describes a narrow, efficient, non-generative model (NVIDIA's DLSS 5, a 118-megabyte single-pass pixel diffusion model with no backward pass) as an example of the pattern where, once a model is "competent enough" at a task, the opportunity shifts from more capability to radical efficiency — paralleling the specialized decision-model thread Brian tracks.

### Agent speed vs. human oversight
- The conversation cites a wave of recent outages (Microsoft, the FAA, Chase, Apple, an NSA network) and newly disclosed third-party vendor breaches exposing JPMorgan, Mastercard, and Visa customer data, framing this as a period of maximal infrastructure vulnerability as AI-assisted attackers probe systems faster than human-paced defense can patch them.
- A speaker explicitly frames the asymmetry as structural: "cyber defense is still human in the loop, plugging one vulnerability at a time and cyber offensive is agent scaling and attacking multiple vulnerabilities in parallel at scale."
- Another speaker counters that the same AI-driven vulnerability discovery could eventually harden systems faster too ("defensive co-scaling"), framing the current moment as a transitional crossing point rather than a permanent asymmetry.

### Capital and governance context (frontier labs)
- Anthropic's IPO is reported as raising $81B, with the stock popping 17% on debut and falling 12% the next day; Dario Amodei is quoted saying "sufficiently powerful AI working in concert with humans could compress a century of scientific and medical progress into a decade."
- A speaker argues Anthropic's public-benefit-corporation structure (optimizing for safety, not revenue) creates tension with quarterly public-market scrutiny, predicting this could slow the company down even as IPO proceeds fund acceleration elsewhere.
- A speaker claims capital allocation to frontier labs is now effectively driving the pace of model scaling directly — investor decisions on whether to fund an IPO determine compute buildout, which determines next-model scale — calling this a strange substitute for a more traditional (e.g., government/Congressional) resource-allocation process.

## Pushback and disagreement

- Speakers disagreed on OpenAI's long-term survival prospects: one speaker explicitly says he wouldn't put OpenAI in the likely-survivor list, ranking Google (Gemini) above it based on "slope of progress" and vertical integration (custom TPU silicon), while not elaborating further on the disagreement.
- On the IPO's motivation, two framings compete: a cynical one (IPO as the only way to get liquidity to employees and provide an exit "while they can") versus an idealistic one (Dario and Sam are motivated by concern for humanity's future over personal financial liquidity, which they already have in abundance).
- On whether AI-driven cybersecurity is a crisis or overblown, one speaker says "we're nowhere near peak disruption" is the bigger risk, while another counters that fear of a "9/11-style" infrastructure event is premature given no such event has yet occurred.

## Quote

> "Cyber defense is still human in the loop, plugging one vulnerability at a time and cyber offensive is agent scaling and attacking multiple vulnerabilities in parallel at scale." — a speaker
> "These engineers are not writing code anymore, they're managing huge fleets of agents to create massive amounts of product." — a speaker, describing Google
> "I think that third outcome is extremely likely at this point, just looking at the research." — Dave Blundin, on inference-time training making current GPU investment obsolete

## Not captured

Extended material on the SpaceX/Tesla investment history, Elon Musk's management style and company culture, Terrafab chip-fab plans, Optimus robot timelines, satellite/Starlink laser-link architecture, and the Voyager 1 light-day milestone — none of it bears on Brian's enterprise-AI or knowledge-work focus.

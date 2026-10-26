---
title: Tom Milton on how we could verify a US–China deal on AI
source: The 80,000 Hours Podcast
source_id: 80000-hours-podcast
source_url: https://80000hours.org/podcast/episodes/tom-milton-verification-technology-ai-slowdown/?utm_campaign=podcast__tom-milton&utm_source=80000+Hours+Podcast&utm_medium=podcast
author: The 80,000 Hours team
date_published: '2026-10-23'
date_captured: '2026-10-26'
ingest_method: feed
model: claude-sonnet-5
content_basis: transcript
---

# Tom Milton on how we could verify a US–China deal on AI

## Fit with Brian's work

**Fit: partial.** The episode's core subject—compute verification for a potential US–China AI slowdown deal—sits outside Brian's enterprise/knowledge-work beat, but one extended stretch on AI-assisted hardware engineering at Amodo Design directly extends several threads he's actively developing: compute availability as a strategic constraint, token economics per worker, and the coding-as-leading-indicator pattern applied to a new domain.

- **Compute-availability / "control your own destiny" thread**: the guest's own experience of frontier model access being cut off overnight (export-controlled) is a lived anecdote matching Brian's argument that "just pay per token when you need it" is breaking down as a reliable assumption—here extended with a new mechanism (export control and domestic-prioritization of tokens) rather than just price or hyperscaler lifecycle terms.
- **Planning-floor / open-weight-sufficiency argument**: the guest's distinction between "Fable problems" (need frontier) and "Sonnet problems" (don't) independently validates Brian's claim that most real-world ROI comes from mid-tier/already-released capability, applied here to hardware R&D rather than enterprise workflows.
- **Token economics / compute consumption ladder**: a new concrete data point—Amodo's hardware engineers currently use far less AI token spend than software engineers at SaaS firms, with the guest predicting parity within a year—adds a fresh anchor to Brian's token-consumption-ladder tracking, which so far has been built mostly from his own knowledge-work usage.
- **Post-application era / coding-as-leading-indicator**: "vibe-CADing" (one-shot AI hardware design) and personalized hardware built for a "customer base of one" extend Brian's software-cost-approaching-zero thesis into physical products, a domain he hasn't yet covered.
- **2031 worker-shape forecast (lightly touched)**: engineers absorbing adjacent disciplines (a mechanical engineer designing his own PCB instead of pulling in an electronics engineer) gestures at role-collapse, but the episode frames it as human skill-broadening via AI tools rather than the human+agent-fleet structure Brian's forecast describes.

## Insights

### AI capability in hardware engineering
- Amodo's CEO describes "vibe-CADing": the AI model Fable can one-shot a working printed circuit board design that would take a human engineer 10–30 hours, but the result is functionally correct and extremely hard to debug or modify—paralleling early AI-generated code.
- Capability is uneven within the hardware workflow: schematic design (component selection, high-level architecture) is described as fairly good, but layout and routing (physically connecting components) is "tragically bad," suggesting AI contributes unevenly across sub-tasks within a single engineering discipline.
- The guest estimates Fable 5's hardware "time horizon" (length of task it can complete) is roughly 10–100 hours, and compares its current hardware capability level to "GPT-3.5, GPT-4" in software terms—implying significant capability growth is still ahead.
- Engineering sub-tasks like PCB routing are described as "RL-friendly" (having verifiable rewards), leading the guest to expect labs could rapidly improve hardware capability by training specifically on these tasks, similar to how coding capability jumped once labs optimized for it.

### Token economics and personalized hardware
- The guest estimates per-engineer AI token spend at Amodo will reach parity with per-software-engineer token spend at SaaS companies "next year," calling current hardware-engineer usage "quite low" by comparison—a concrete cross-domain data point for token-consumption benchmarking.
- AI-assisted hardware design is enabling "customer base of one" products: the guest built a personalized high-intensity wake-up light and a custom cycling distance tracker using Fable, framing this as "the golden age of the ideas guy"—people with ideas but no execution skill set gaining a new ability to build.
- Organizationally, engineers are reportedly taking on adjacent disciplines they previously would have handed off (e.g., a mechanical engineer designing his own PCB instead of looping in an electronics engineer), which the guest expects will let smaller teams deliver more ambitious projects.

### Compute scarcity and access as a strategic risk
- The guest describes a personal "Claude psychosis" period using Fable for hardware design, ended abruptly when the US government export-controlled the model and his access was cut overnight—losing a capability he'd had the previous day, which he calls potentially "catastrophic" for a company built around that access.
- He predicts a coming "compute crunch" in which the US prioritizes serving domestic companies with tokens over allied countries, even the UK, to protect its own AI-driven economic advantage—raising a scenario where US labs decline to export model weights abroad without strong security guarantees.
- He argues the UK needs sovereign, high-security compute both to maintain continuous access to frontier capability and because national-security uses (intelligence analysis) won't route through third-party foreign data centers—an argument for compute self-sufficiency distinct from price or governance framing.
- He notes AI capability doesn't help with every task ("some problems are just Sonnet problems"), suggesting a country or company without frontier access could still function well for a large share of work while losing ground only on the subset that benefits from maximum intelligence.

### Personal/organizational reaction to capability growth
- The guest describes finding model capabilities "viscerally scary," distinct from typical AI-safety risk categories (bio, cyber)—specifically the destabilizing experience of watching tasks he's personally skilled at suddenly be done by a model.
- Amodo runs structured internal hackathons (reported as 10 sessions, 6 team members each) specifically to build calibrated intuition about where models are strong or weak, by re-running old completed projects through current models.

## Quote

> "Imagine building a company on that... it gets taken away just like that. That is catastrophic." — Tom Milton
> "It's the golden age of the ideas guy, right?" — Tom Reed
> "I find the capabilities of the models viscerally scary." — Tom Milton

## Not captured

The bulk of the episode—technical mechanisms for verifying US–China AI compute agreements (network taps, zero-knowledge proofs, power-signature fingerprinting, recomputation), arms-control analogies to nuclear/chemical weapons verification regimes, and geopolitical/governmental coordination scenarios—falls outside Brian's enterprise knowledge-work focus and was omitted.

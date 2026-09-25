---
title: Canon staleness triage — 2026-09-25
date: '2026-09-25'
file_type: staleness-triage
tier: 3
status: not-reviewed-by-human
authority_level: 1
model: claude-opus-5-5
sources:
- me/developing-thinking.md
- me/published-thinking.md
- frameworks/2031-worker-shape.md
- frameworks/7-stage-roadmap.md
- frameworks/bitter-lesson.md
- frameworks/cognitive-stack.md
- frameworks/factory-electrification.md
- frameworks/invisible-80-percent.md
- frameworks/knowledge-factory.md
- frameworks/post-application-era.md
- frameworks/subscribable-brains.md
- frameworks/workspace-as-control-plane.md
---

# Canon staleness triage — 2026-09-25

Mirror image of `outputs/technical-briefings/promotion-candidates.md`: that queue proposes additions to canon, this one proposes cuts, promotions, or a second look at what's already there. Everything below is one model's read against the current published record — nothing here is a decision. An item leaves `me/developing-thinking.md`, or a framework's `status` flips to `archived`, only if Brian does it himself, same non-negotiable as every other tier-3 output. **This file is overwritten fresh on every run — it's a snapshot of the current state, not an accumulating log.** Items not mentioned below were read and judged still genuinely developing; their absence is the "keep" signal, not an oversight.

This run reviewed the full "What's connecting" and "Scratchpad" sections of `me/developing-thinking.md`, plus 10 active framework(s). Flagged: 4 developing-thinking item(s), 1 framework(s).

---

## Developing-thinking items

### "August 28 update: the compute-availability risk is the same pattern that broke the "pure pay-as-you-go cloud" promise" — promote-candidate

The item argues that AI inference is repeating the cloud-elasticity lesson. Labs are redirecting compute toward their own R&D, so availability, not price, becomes the binding constraint, and the answer is the familiar reserved-capacity, "control your own destiny" move. The item already calls itself "likely Brian's next post." It has a clean historical analogy, a named source (Patel's compute projection), and a direct line to the [bubble-pop post](https://www.citrix.com/blogs/2026/07/20/how-to-build-an-ai-strategy-that-survives-the-bubble-pop/). That post argued frontier access could get "orders of magnitude more expensive or slower" but never made the availability-over-price case or used the reserved-capacity analogy.

**Section:** What's connecting
**Suggested action:** Write this up as the next post, framed as the availability-side companion to the bubble-pop piece's pricing argument.

### "September 13 update: the knowledge factory is the destination, and it's time for companies to execute—not pilot." — promote-candidate

The item says the model is no longer the bottleneck and companies should stop piloting and build the knowledge factory. It also argues that bringing AI into the estate "just for security" is short-sighted, and that the estate becomes the connective tissue feeding the factory.

Much of that landed a day later in [You can't transform the AI you can't see](https://www.citrix.com/blogs/2026/09/14/you-cant-transform-the-ai-you-cant-see/). That post already makes three of these points:
- visibility is the on-ramp to the factory, not a separate security initiative;
- the EUC estate stays put;
- the estate feeds AI and receives its output.

The post also promises a follow-up on building the factory. What isn't yet published is the "execute, don't pilot" thesis and the capability trigger, and that is the natural spine of the promised follow-up.

**Section:** What's connecting
**Suggested action:** Trim the security-vs-factory and estate-as-connective-tissue material already covered by the September 14 post, and use the remaining execute-now argument, including Nancy's "interstitial tissue" line, as the basis for the promised factory follow-up post.

### "Token economics are the emerging macro constraint." — worth-revisiting

The item frames token economics as "emerging," with three dimensions. The published record has since moved past that framing. Two of the three dimensions are now on the record:
- **Token equivalency for human work:** [What's left for humans?](https://www.citrix.com/blogs/2026/04/09/whats-left-for-humans/) says every knowledge task gets a human-vs-AI price tag.
- **Model quality as class stratifier:** [the bubble-pop post](https://www.citrix.com/blogs/2026/07/20/how-to-build-an-ai-strategy-that-survives-the-bubble-pop/) covers mid-tier models for the public and frontier models for favored use.

Token economics is also now a named invariant on the bubble-pop checklist. The only piece not clearly published is the structural consumer-vs-enterprise pricing gap.

**Section:** What's connecting
**Suggested action:** Drop the "emerging" framing and cut this down to the consumer-vs-enterprise pricing-gap point, which is the only part the published record doesn't already carry.

### "\"Bridge between top-down AI projects and shadow AI\" is the right framing for the early enterprise AI on-ramp." — already-published

The item claims every CIO lives with two AI realities, a stalled top-down initiative and staff running shadow AI on personal accounts. It says the first easy, consultancy-free step connects the two.

That is the thesis of [You can't transform the AI you can't see](https://www.citrix.com/blogs/2026/09/14/you-cant-transform-the-ai-you-cant-see/). The post sets committee-and-pilot "AI strategy" against AI already arriving via personal accounts and departmental pilots. It names visibility through the existing access/governance/control playbook as the step-one on-ramp, available before any platform commitment. It also stresses that the step is "a configuration, not a transformation." The published version is fuller than this note.

**Section:** Scratchpad
**Suggested action:** Cut from developing-thinking.md, since it is fully covered by [You can't transform the AI you can't see](https://www.citrix.com/blogs/2026/09/14/you-cant-transform-the-ai-you-cant-see/).

## Frameworks

### frameworks/bitter-lesson.md — worth-revisiting

The file's headline claim is still "simple, worker-driven AI adoption beats elaborate, IT-engineered solutions. Every time." The body has since been corrected three times, and by the third correction the claim has become the opposite for knowledge. Capture must be deliberately engineered first, via the [knowledge factory](knowledge-factory.md), and the bitter lesson only applies to how that apparatus thins out later.

The developing-thinking material has pushed further the same way. The September 13 item says companies should now execute an engineered factory build rather than lean on worker-led discovery. The result is that the opening framing, description, and "every time" line contradict the framework's own current conclusion.

**Suggested action:** Rewrite the headline, description, and opening section around the sequencing claim (build the factory now, and the bitter lesson thins the scaffolding later), and scope the "enable, don't engineer" prescription explicitly to tooling, instead of leaving it as three stacked corrections under an outdated thesis.

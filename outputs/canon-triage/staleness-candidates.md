---
title: Canon staleness triage — 2026-09-11
date: '2026-09-11'
file_type: staleness-triage
tier: 3
status: not-reviewed-by-human
authority_level: 1
model: claude-opus-5
sources:
- me/developing-thinking.md
- me/published-thinking.md
- frameworks/2031-worker-shape.md
- frameworks/7-stage-roadmap.md
- frameworks/bitter-lesson.md
- frameworks/cognitive-stack.md
- frameworks/delegation-not-automation.md
- frameworks/factory-electrification.md
- frameworks/invisible-80-percent.md
- frameworks/knowledge-factory.md
- frameworks/post-application-era.md
- frameworks/subscribable-brains.md
- frameworks/workspace-as-control-plane.md
---

# Canon staleness triage — 2026-09-11

Mirror image of `outputs/technical-briefings/promotion-candidates.md`: that queue proposes additions to canon, this one proposes cuts, promotions, or a second look at what's already there. Everything below is one model's read against the current published record — nothing here is a decision. An item leaves `me/developing-thinking.md`, or a framework's `status` flips to `archived`, only if Brian does it himself, same non-negotiable as every other tier-3 output. **This file is overwritten fresh on every run — it's a snapshot of the current state, not an accumulating log.** Items not mentioned below were read and judged still genuinely developing; their absence is the "keep" signal, not an oversight.

This run reviewed the full "What's connecting" and "Scratchpad" sections of `me/developing-thinking.md`, plus 11 active framework(s). Flagged: 5 developing-thinking item(s), 1 framework(s).

---

## Developing-thinking items

### "Human clock speed is the invariant AI hasn't changed" — promote-candidate

The claim that AI compresses gathering but not absorption — so AI makes knowledge work *deeper*, not faster — is a clean, named invariant that already does load-bearing work elsewhere in the file (the September 4 bottleneck item restates it as throughput, and it's the strongest counter to the substitution argument). It sits naturally alongside the published invariants method from [How a futurist reads AI news](https://www.citrix.com/blogs/2026/06/30/how-a-futurist-reads-ai-news-hint-ignore-most-of-it/) but is nowhere in the published record.

**Section:** What's connecting
**Suggested action:** write it up as a framework file (absorption vs. gathering) or a standalone post, with the September 4 bottleneck note folded in as the uncomfortable corollary.

### "August 28 update: the compute-availability risk is the same pattern that broke the 'pure pay-as-you-go cloud' promise" — promote-candidate

The argument that availability, not price, becomes the AI constraint — and that enterprises already learned this lesson with reserved cloud capacity — is fully formed, has a historical analogy in the same register as factory electrification, and extends the July 20 bubble-pop post's token-economics move. The note already says "worth a real piece built around that analogy — likely Brian's next post."

**Section:** What's connecting
**Suggested action:** graduate it out of the scratch pile into a drafted post or framework file rather than leaving it as an update note.

### "The consulting 'leave a PDF' model is dead." — already-published

The item argues consulting shifts from a close-of-project deliverable to a living knowledge base the client's AI plugs into. That is the enterprise section of [Hey creators, stop publishing content. Start publishing your second brain.](https://www.linkedin.com/pulse/hey-creators-stop-publishing-content-start-your-second-brian-madden-ca0ae) and `frameworks/subscribable-brains.md` ("consulting firms: junior consultants carry senior partners' accumulated knowledge"; the $25K-engagement-vs-subscription economics), and the item's own last line concedes it's "the subscribable brains thesis applied directly to B2B professional services."

**Section:** Scratchpad
**Suggested action:** cut from developing-thinking.md — fully covered by [Hey creators, stop publishing content](https://www.linkedin.com/pulse/hey-creators-stop-publishing-content-start-your-second-brian-madden-ca0ae) and `frameworks/subscribable-brains.md`.

### "'The AI switchboard'—the workspace as the thing that controls which model handles which task" — worth-revisiting

This was a naming exercise for a positioning the same file now says the market has closed: the August 24 and August 28 updates record Stripe/OpenRouter, Ramp/router.com, Snowflake Cortex and NeMo Switchyard claiming the routing seat, and conclude "the premise that routing or hosting needs a neutral party is basically dead." A friendlier label for the neutral-workspace-as-router pitch reads stale against Brian's own more recent conclusion.

**Section:** Scratchpad
**Suggested action:** either retire the phrase or rewrite the note as the unanswered question the August updates left open — why the referee should be the workspace rather than whoever holds the invoice.

### "Agent identity is the foundational unsolved primitive—and corporate IT is the bottleneck, not AI vendors." — worth-revisiting

The item's sharpest line — "every 'AI governance platform' pitch in market is missing this foundational layer" — has been overtaken by the September 4 note in this same file: CrowdStrike's Agentic Identity Provider ships cryptographic non-spoofable agent identities, short-lived task-scoped permissions, and traceable handoffs, which Brian himself calls "the right *shape* of answer." The IT-provisioning-capacity argument survives; the vendor-gap claim doesn't.

**Section:** What's connecting
**Suggested action:** rewrite to keep the operationalization bottleneck and drop the "no vendor is building this" framing, or merge it into the September 4 agent-oversight item.

## Frameworks

### frameworks/delegation-not-automation.md — already-published

Its central claim (workers delegate rather than build automations; the industry invests at the bottom of the hierarchy) and its key artifact (the skills hierarchy diagram) were both absorbed and superseded by [Understanding the cognitive stack](https://www.citrix.com/blogs/2026/02/25/understanding-the-cognitive-stack-why-your-ai-strategy-is-focused-on-the-wrong-layer/) and `frameworks/cognitive-stack.md`, which names the same five layers, adds the claws framing and the two-trajectories argument, and carries the "humans prefer to connect at the intelligence layer" point forward explicitly. The framework's own header already describes itself as extended by the cognitive stack.

**Suggested action:** fold the still-unique bits (the automation-vs-delegation table, the BlackBerry/iPhone analogy, the RPA/low-code 1%-vs-99% track record) into `frameworks/cognitive-stack.md` and retire the standalone file.

---
title: Canon staleness triage — 2026-09-04
date: '2026-09-04'
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

# Canon staleness triage — 2026-09-04

Mirror image of `outputs/technical-briefings/promotion-candidates.md`: that queue proposes additions to canon, this one proposes cuts, promotions, or a second look at what's already there. Everything below is one model's read against the current published record — nothing here is a decision. An item leaves `me/developing-thinking.md`, or a framework's `status` flips to `archived`, only if Brian does it himself, same non-negotiable as every other tier-3 output. **This file is overwritten fresh on every run — it's a snapshot of the current state, not an accumulating log.** Items not mentioned below were read and judged still genuinely developing; their absence is the "keep" signal, not an oversight.

This run reviewed the full "What's connecting" and "Scratchpad" sections of `me/developing-thinking.md`, plus 11 active framework(s). Flagged: 5 developing-thinking item(s), 2 framework(s).

---

## Developing-thinking items

### "Human clock speed is the invariant AI hasn't changed—and this reframes everything about knowledge work productivity." — promote-candidate

The claim — AI compresses gathering but not absorption, so "AI makes knowledge work faster" is a category error and the right frame is *deeper* — is fully formed, has a clean statement, a testable prediction (speed-framing orgs will disappoint), and a hard edge against the substitution argument. It's already load-bearing elsewhere in the file: the September 4 bottleneck note leans on it explicitly ("the absorption problem restated as throughput"), which means it's doing framework work without being a framework.

**Section:** What's connecting
**Suggested action:** write it up as a standalone framework file (absorption vs. gathering) so the bottleneck and substitution notes can cite it instead of restating it.

### "August 28 update: the compute-availability risk is the same pattern that broke the "pure pay-as-you-go cloud" promise, now playing out with AI inference." — promote-candidate

Reads as finished thinking rather than a note: a historical analogy with a known ending (reserved capacity), a named mechanism (labs redirecting flops to internal R&D), a specific source, and a conclusion that plugs straight into the July 20 bubble-pop checklist as a sixth move. The item says so itself — "likely Brian's next post."

**Section:** What's connecting
**Suggested action:** draft it as the post; it extends [How to build an AI strategy that survives the bubble pop](https://www.citrix.com/blogs/2026/07/20/how-to-build-an-ai-strategy-that-survives-the-bubble-pop/) from price risk to availability risk.

### "Second brain data integrity: selection bias is the primary failure mode." — promote-candidate

Has everything a published piece needs and nothing the file needs: a first-person incident, a named mechanism ("selection bias operating on a training set of one"), a generalization beyond the anecdote, and a design conclusion that reinforces the file-based-over-vector-DB position also argued in the test-time-training note. Nothing in the published record addresses second brain data quality from the owner's side.

**Section:** Scratchpad
**Suggested action:** promote to a framework file or a post — it's the strongest counterweight to the second brain material and currently sits in the "don't want to lose" pile.

### "The agent-to-human ratio question replaces headcount planning." — already-published

Two sentences claiming workforce planning shifts from headcount to agent ratios, backed by revenue-per-employee data. `frameworks/2031-worker-shape.md` (Aug 28) covers this in full — the worker as "one human plus N agents," the three-type split, and deployment guidance for exactly the case where "workforce planning conversations default to headcount reduction." That framework notes it was promoted from a recurring thread here, and this looks like a leftover fragment of it.

**Section:** What's connecting
**Suggested action:** cut from developing-thinking.md — absorbed by `frameworks/2031-worker-shape.md`; move the revenue-per-employee data point into that file if it's worth keeping.

### "Token economics are the emerging macro constraint." — worth-revisiting

The framing has been overtaken by Brian's own record: token economics stopped being "emerging" once the DUCUG talk published real usage data and layer-cost math, the May 7 post published routing-as-task-selection, and the July 20 post named token economics an *invariant* with "don't assume the price you pay today is the price you'll pay tomorrow." Dimensions (1) and (3) — the structural consumer/enterprise price gap and model quality as a class stratifier — are the only parts still unpublished, and they're a different argument (access stratification) than the one this item's headline makes.

**Section:** What's connecting
**Suggested action:** rewrite down to the stratification claim alone, since the macro-constraint framing is now published position rather than developing thought.

## Frameworks

### frameworks/workspace-as-control-plane.md — worth-revisiting

The central claim — that the workspace is the one place consistent governance can be applied — is stated without contest, but the developing record has since put real market evidence against the seat being available: the Aug 24 note documents Stripe/OpenRouter, Ramp/router.com, Snowflake and NVIDIA all claiming the routing-and-governance layer, and the Aug 28 note concludes flatly that "neutrality was never a stable resting state, just a phase before consolidation." The framework should either answer why the referee is the workspace rather than whoever holds the invoice, or absorb the executor-seam argument as the narrower, still-unoccupied version of the claim.

**Suggested action:** add a section answering the consolidation objection, rather than leaving the framework asserting a position Brian's own notes now treat as contested.

### frameworks/invisible-80-percent.md — worth-revisiting

The file presents the 20/80 split as a fixed property of knowledge work, but the corrected position is already on the record elsewhere: `frameworks/bitter-lesson.md`'s 2026-08-28 correction states that the boundary moves as AI erodes into the 80% ("the split might become 60/40, or 40/60") and that the remainder needs permanent deliberate capture. `frameworks/knowledge-factory.md` builds on the moving-boundary version. As written, the source framework is the only place the split still reads as static.

**Suggested action:** add the moving-boundary correction to this file so it doesn't contradict the two frameworks that revise it.

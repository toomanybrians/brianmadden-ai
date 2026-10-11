---
title: Canon staleness triage — 2026-10-11
date: '2026-10-11'
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

# Canon staleness triage — 2026-10-11

Mirror image of `outputs/technical-briefings/promotion-candidates.md`: that queue proposes additions to canon, this one proposes cuts, promotions, or a second look at what's already there. Everything below is one model's read against the current published record — nothing here is a decision. An item leaves `me/developing-thinking.md`, or a framework's `status` flips to `archived`, only if Brian does it himself, same non-negotiable as every other tier-3 output. **This file is overwritten fresh on every run — it's a snapshot of the current state, not an accumulating log.** Items not mentioned below were read and judged still genuinely developing; their absence is the "keep" signal, not an oversight.

This run reviewed the full "What's connecting" and "Scratchpad" sections of `me/developing-thinking.md`, plus 10 active framework(s). Flagged: 3 developing-thinking item(s), 1 framework(s).

---

## Developing-thinking items

### "August 28 update: the compute-availability risk is the same pattern that broke the" — promote-candidate

The item argues that AI inference is repeating cloud computing's elasticity failure: when everyone needs capacity at once, availability rather than price becomes the constraint, and the fix is reserved capacity, or "control your own destiny." The September 25 addition extends the argument with physical build constraints and the AWS Bedrock/Kimi K3 lifecycle example, which shows a hyperscaler controlling which open-weight models you can count on. Brian's own note calls it "worth a real piece... likely Brian's next post." The bubble-pop post touches subsidized token prices, but nowhere in the published record makes the availability-not-price argument or the reserved-capacity analogy.

**Section:** What's connecting
**Suggested action:** Draft this as the next post, folding in the September 25 addition, rather than letting more update notes pile onto it.

### "August 24 update: human-in-the-loop approval is turning out to be the weak link" — promote-candidate

The item claims that human confirmation prompts are the gap in agent governance, not the control. It cites three pieces of evidence:
- humans refused a dangerous command 13.6% of the time, versus 89% for an automated policy check
- a three-day agent stoppage went unnoticed by humans watching green dashboards
- enforcement belongs in the harness's action-authorization layer

The thread has since been reinforced twice: by the September 4 bottleneck note ("Real piece, not just a note") and by the September 25 "watching isn't stopping" addition. Together they form a coherent, evidence-backed argument that cuts against the human-approval workflows in Brian's own published agent security model (August 4, 2025). That makes it a candidate for a framework or a post, not a scratch note.

**Section:** What's connecting
**Suggested action:** Merge this item with the September 4 bottleneck note and the September 25 addition into one draft post or framework on why enforcement has to live in the harness rather than in human review.

### "September 13 update: the knowledge factory is the destination, and it's time for companies to execute" — promote-candidate

The item argues that the piloting phase is over. Its supporting points:
- the knowledge factory is proven internally
- the playbook for analyzing existing systems and handling PII already exists
- current models remove capability as the excuse to wait
- the factory is "the interstitial tissue that connects existing enterprise apps to human brains"

Brian notes that the September 14 [You can't transform the AI you can't see](https://www.citrix.com/blogs/2026-09/you-cant-transform-the-ai-you-cant-see) post publicly promised this follow-up and calls it "overdue." The knowledge-factory framework already exists, so this is ready to graduate into the promised post.

**Section:** What's connecting
**Suggested action:** Write the promised follow-up post to the September 14 piece around this execute-now argument, and fold Nancy's "interstitial tissue" framing into frameworks/knowledge-factory.md.

## Frameworks

### frameworks/invisible-80-percent.md — worth-revisiting

The framework's central claims are:
- the 80% "cannot be observed, documented, or extracted by outside observers"
- worker-led AI is "the only path to real transformation that works"

Three later sources visibly move past both claims:
- **frameworks/knowledge-factory.md** describes an engineered, organizational machine that "digitizes the judgment layer corporate IT could never see."
- **frameworks/bitter-lesson.md** (rewritten 2026-09-25) says the invisible boundary moves but never reaches zero, and that capture is a deliberate, permanent build.
- **The September 14 visibility post** argues that governance instrumentation is what finally makes the tacit layer visible.

The framework file reflects none of this. Read on its own, it now contradicts three newer pieces of canon.

**Suggested action:** Add a dated update section, like the ones in post-application-era.md and cognitive-stack.md, that reconciles "can't be extracted by outsiders" with the knowledge factory and visibility arguments.

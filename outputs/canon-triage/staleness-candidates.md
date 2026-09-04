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

This run reviewed the full "What's connecting" and "Scratchpad" sections of `me/developing-thinking.md`, plus 11 active framework(s). Flagged: 5 developing-thinking item(s), 1 framework(s).

---

## Developing-thinking items

### "The 2031 worker-shape forecast is consolidating into a specific picture." — already-published

The item lays out the one-human-plus-N-agents shape, the owners/operators/curators split, the collapsing generic middle, and the Roetzer Apprentice-gap corroboration. All of it — including the follow-on "**August 24 note:** wage data adds a leading indicator" paragraph, which appears verbatim in substance under "The evidence, not just the shape" — is now `frameworks/2031-worker-shape.md`, promoted from this exact thread on 2026-08-28.

**Section:** What's connecting
**Suggested action:** cut this item and its August 24 wage-data follow-on from developing-thinking.md; the framework file is now the canonical home and the developing version only risks drifting out of sync.

### "September 2 update: canon gets built backward from outputs, not forward from inputs" — already-published

The item describes starting from the output, finding whoever produces it, pulling only those sources into canon, then diagnosing wrong drafts as bad instructions vs. canon noise vs. a real hole. The item itself notes this has already been folded into `frameworks/knowledge-factory.md`, and it reads there as the "start from the output, not the input pile" paragraph under "How the canon gets built."

**Section:** What's connecting
**Suggested action:** cut from developing-thinking.md — fully absorbed into [frameworks/knowledge-factory.md](../frameworks/knowledge-factory.md), leaving at most a pointer to the [Sept 2 demo transcript](../talks/2026-09-02-citrix-asean-webcast-followup-second-brain-demo.md).

### "August 28 update: the compute-availability risk is the same pattern that broke the "pure pay-as-you-go cloud" promise, now playing out with AI inference." — promote-candidate

The claim — that AI's real constraint is shifting from token price to token *availability*, and the enterprise answer is the reserved-capacity lesson cloud already taught — is a complete argument with a historical analogy, a named mechanism, and a clear enterprise prescription. It also plugs a specific hole in the July 20 bubble-pop post, which handles price and model access but not availability, and the item already says as much ("likely Brian's next post").

**Section:** What's connecting
**Suggested action:** write it as the next Citrix post, positioned as the availability sequel to [How to build an AI strategy that survives the bubble pop](https://www.citrix.com/blogs/2026/07/20/how-to-build-an-ai-strategy-that-survives-the-bubble-pop/).

### "August 28 update: "harness" is the vocabulary—decided, not just tracked." — promote-candidate

This isn't a note about industry vocabulary anymore — it's a decision to name the cognitive stack's differentiating middle layer, with the evidence (Hashimoto, Claude Code docs, Hugging Face glossary, SemiAnalysis ranking harness above benchmark score) already assembled. A naming decision that alters a published framework's terminology should live in the framework, not in a scratch list where the rest of the record still calls that layer "skills."

**Section:** What's connecting
**Suggested action:** fold the harness terminology into `frameworks/cognitive-stack.md` as a dated update, the way the August 28 hierarchy-convergence note was added, and reconcile it against the existing layer-3 "skills" naming.

### ""Switzerland of agent workspaces" thesis is sharper post-research." — worth-revisiting

The item bets that the agnostic governance layer above vendor agent stacks is "structurally unoccupied" and that the next 12-18 months decides it. Two later entries in the same file have since undercut that: the August 24 routing note observes the neutral seat is being taken by payments companies (Stripe/OpenRouter at $7B+, Ramp/router.com), and the August 28 note concludes outright that "neutrality was never a stable resting state, just a phase before consolidation." The thesis needs re-argument on different ground — governance-as-neutrality rather than market-position-as-neutrality — or it reads as overtaken by its own follow-ups.

**Section:** What's connecting
**Suggested action:** rewrite the item to argue why the workspace is the referee *despite* consolidation, or retire it in favour of the later routing-consolidation notes.

## Frameworks

### frameworks/bitter-lesson.md — worth-revisiting

The framework body has already been corrected twice — first to concede that AI needs the invisible 80% captured deliberately (Skills, crawl/walk/run, the knowledge factory), then to drop the "dissolves" endpoint — but the "Using this framework" section still instructs the reader that "IT is trying to 'capture institutional knowledge' to feed into AI systems—the bitter lesson says AI may not need it." That deployment guidance now contradicts the corrections above it in the same file, and contradicts [Skills are all you need](https://www.citrix.com/blogs/2026/03/12/skills-are-all-you-need/) and `frameworks/knowledge-factory.md`, which is an entire engineered apparatus for exactly that capture.

**Suggested action:** rewrite the "Using this framework" bullets so the deployment advice matches the corrected body — the lesson is now "don't engineer the tool, do engineer the knowledge," not "don't bother capturing."

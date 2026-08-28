---
title: Canon staleness triage — 2026-08-28
date: '2026-08-28'
file_type: staleness-triage
tier: 3
status: not-reviewed-by-human
authority_level: 1
model: claude-opus-5
sources:
- me/developing-thinking.md
- me/published-thinking.md
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

# Canon staleness triage — 2026-08-28

Mirror image of `outputs/technical-briefings/promotion-candidates.md`: that queue proposes additions to canon, this one proposes cuts, promotions, or a second look at what's already there. Everything below is one model's read against the current published record — nothing here is a decision. An item leaves `me/developing-thinking.md`, or a framework's `status` flips to `archived`, only if Brian does it himself, same non-negotiable as every other tier-3 output. **This file is overwritten fresh on every run — it's a snapshot of the current state, not an accumulating log.** Items not mentioned below were read and judged still genuinely developing; their absence is the "keep" signal, not an oversight.

This run reviewed the full "What's connecting" and "Scratchpad" sections of `me/developing-thinking.md`, plus 10 active framework(s). Flagged: 5 developing-thinking item(s), 1 framework(s).

---

## Developing-thinking items

### "**Individual AI augmentation doesn't show up in firm-level ROI until the org restructures.**" — promote-candidate

This is the sharpest answer Brian has to the "where's the AI ROI?" question, and it's doing real work: it extends the factory electrification framework past Phase 2 into a specific mechanism (decision-rights congestion, not individual capability), and "1+1+1+1=1.5" is already a signature-phrase-grade formulation. Nothing in the published record makes the firm-level vs. worker-level ROI distinction explicitly — the electrification post stops at "redesign workflows," not "the augmented worker is still stuck in the old decision queue."

**Section:** What's connecting
**Suggested action:** write this up as a standalone post or framework file on why AI ROI is measured at the wrong altitude, using factory electrification Phase 3→4 as the spine.

### "**Human clock speed is the invariant AI hasn't changed—and this reframes everything about knowledge work productivity.**" — promote-candidate

Fully formed argument with a clean thesis ("AI makes knowledge work *deeper*, not faster"), a named mechanism (gathering compresses, absorption doesn't), and a direct hook into the published invariants method from the June 30 futurist post. It also lands a counter to the substitution argument that appears twice elsewhere in this file, which makes it load-bearing rather than an observation.

**Section:** What's connecting
**Suggested action:** graduate to a framework file — it's the missing invariant in the published invariants list and reads publication-ready as-is.

### "**The 2031 worker-shape forecast is consolidating into a specific picture.**" — promote-candidate

A three-part typology (cognitive owners / operators / curators), independent corroboration from Roetzer's Architect/Orchestrator/Apprentice, an acknowledged gap (how judgment develops when AI absorbs the tactical rungs), and now a leading indicator in the wage and call-center data. That's a framework with evidence, not a note.

**Section:** What's connecting
**Suggested action:** promote to a framework file; it pairs naturally with the 7-stage roadmap's Stage 5–6 as the labor-market counterpart.

### "**Management is an emergent property of intelligence coordinating at scale.**" — already-published

The central claim here — hierarchy isn't a human organizational preference, it's what intelligence does when coordinating complex work — is already published nearly verbatim in the cognitive stack ("the shape intelligence naturally takes when coordinating complex work"), both in [Understanding the cognitive stack](https://www.citrix.com/blogs/2026/02/25/understanding-the-cognitive-stack-why-your-ai-strategy-is-focused-on-the-wrong-layer/) and `frameworks/cognitive-stack.md`. The three-system convergence is new *evidence* for a settled position rather than a developing idea.

**Section:** What's connecting
**Suggested action:** cut the framing claim and move the Cursor/StrongDM/Anthropic convergence evidence into `frameworks/cognitive-stack.md`, keeping only the agent-to-human ratio and revenue-per-employee observations here.

### "**Second brain data integrity: selection bias is the primary failure mode.**" — promote-candidate

A first-person incident, a named mechanism (selection bias operating on a training set of one), and a concrete architectural conclusion (inspectable markdown over vector DBs) — this is the strongest defense of the file-based bet in the whole file, and it's a security/quality argument rather than a portability one. It's also the honest counterweight to the second brain material, which the published record currently presents without failure modes.

**Section:** Scratchpad
**Suggested action:** promote out of the scratchpad into a framework file or a post — it directly reinforces the test-time-training argument sitting a few items above it.

## Frameworks

### frameworks/bitter-lesson.md — worth-revisiting

The file's headline thesis ("AI doesn't need the 80% — it dissolves") is now contradicted by three later published pieces, and the file carries a long inline retraction saying so: [Skills are all you need](https://www.citrix.com/blogs/2026/03/12/skills-are-all-you-need/) is an argument *for* capturing tacit knowledge, the [crawl/walk/run post](https://www.citrix.com/blogs/2026/05/07/why-enterprise-ai-agents-disappoint-and-why-the-fix-is-not-better-agents/) says agents fail precisely because nobody did that capture work, and `frameworks/knowledge-factory.md` states outright that it revises this framework. As it stands, a reader hits the dated claim first and the current position second, buried in a correction paragraph.

**Suggested action:** rewrite the framework so the corrected position ("stop hand-engineering bespoke integrations; the invisible 80% still has to be deliberately captured, and the knowledge factory is how") is the stated thesis, with the dissolution claim demoted to lineage.

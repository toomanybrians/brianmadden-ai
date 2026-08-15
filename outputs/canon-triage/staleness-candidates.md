---
title: Canon staleness triage — 2026-08-15
date: '2026-08-15'
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

# Canon staleness triage — 2026-08-15

Mirror image of `outputs/technical-briefings/promotion-candidates.md`: that queue proposes additions to canon, this one proposes cuts, promotions, or a second look at what's already there. Everything below is one model's read against the current published record — nothing here is a decision. An item leaves `me/developing-thinking.md`, or a framework's `status` flips to `archived`, only if Brian does it himself, same non-negotiable as every other tier-3 output. **This file is overwritten fresh on every run — it's a snapshot of the current state, not an accumulating log.** Items not mentioned below were read and judged still genuinely developing; their absence is the "keep" signal, not an oversight.

This run reviewed the full "What's connecting" and "Scratchpad" sections of `me/developing-thinking.md`, plus 10 active framework(s). Flagged: 6 developing-thinking item(s), 1 framework(s).

---

## Developing-thinking items

### "The AI stack has natural cost tiers that create routing logic." — already-published

The item claims each layer of the AI stack has its own cost profile, that commodity layers (UI navigation, data translation, interface marshaling) get cheaper rather than better, and that the system should route tasks to the right layer automatically. This is the published core of [Why enterprise AI agents disappoint (and why the fix is not "better agents")](https://www.citrix.com/blogs/2026/05/07/why-enterprise-ai-agents-disappoint-and-why-the-fix-is-not-better-agents/), which puts numbers on it (four-layer Excel example, ~1K tokens for in-context reasoning vs. ~200K for a CUA) and states the "each layer down costs more than the one above it" rule outright — plus the DUCUG talk's token-economics section. The overlap is the whole claim, not an echo.

**Section:** What's connecting
**Suggested action:** cut from developing-thinking.md — fully covered by [Why enterprise AI agents disappoint](https://www.citrix.com/blogs/2026/05/07/why-enterprise-ai-agents-disappoint-and-why-the-fix-is-not-better-agents/).

### "Skills replace training—top-down beats bottom-up." — already-published

The item argues skills-as-markdown beat retraining models, get better for free as models improve, and that startups building scaffolding around model limitations self-destruct with each model release. That's the second and third moves of [Skills are all you need](https://www.citrix.com/blogs/2026/03/12/skills-are-all-you-need/) — "skills appreciate, software depreciates," every model improvement making existing skills more valuable, framed there as the bitter lesson applied to enterprise tooling. Even the teaching method (describe the task, narrate examples, let the AI ask questions) is the walk-layer pedagogy already published on May 7.

**Section:** What's connecting
**Suggested action:** cut from developing-thinking.md — fully covered by [Skills are all you need](https://www.citrix.com/blogs/2026/03/12/skills-are-all-you-need/).

### "Human clock speed is the invariant AI hasn't changed—and this reframes everything about knowledge work productivity." — promote-candidate

This is a complete argument with a named invariant, a mechanism (AI compresses gathering, not absorption), a sharp reframe ("AI makes knowledge work deeper, not faster"), a prediction about which organizations disappoint, and a real counter to the substitution thesis (substitution requires replacing absorption, not generation). It slots directly into the June 30 invariants method and the "what's left for humans?" bottleneck argument without duplicating either — it's ready to be its own post or framework file rather than a note.

**Section:** What's connecting
**Suggested action:** write this up as a standalone post or framework file, positioned as an addition to the invariants list.

### "The 2031 worker-shape forecast is consolidating into a specific picture." — promote-candidate

A named three-type typology (cognitive owners / operators / curators), a stated collapse of the generic middle, an explicit unit-of-work claim (one human plus N agents), independent corroboration from Roetzer, and an honestly flagged open gap (how experts develop judgment when AI absorbs the tactical rungs). It's more developed than most published material was at the point it graduated, and it's the natural downstream companion to Stage 6 of the 7-stage roadmap.

**Section:** What's connecting
**Suggested action:** promote to a framework file, with the Apprentice/judgment-development gap kept as the open question rather than smoothed over.

### "Every app that exposes an MCP server is admitting that the value was in the data, not the interface." — already-published

This line appears verbatim in `frameworks/post-application-era.md` (in the MCP section) and again in the signature-phrases list in `me/published-thinking.md`. There is nothing left developing about it.

**Section:** Scratchpad
**Suggested action:** cut from developing-thinking.md — it's already a signature phrase in `frameworks/post-application-era.md`.

### "Secure the work, not the worker." — already-published

The bullet's claim — that if AI does the work, governance shifts from managing people to managing work product and data flows — is the published signature phrase of the same name, established in the February 2025 Citrix announcement ("secure the work—regardless of the worker, app, or platform") and carried through the agent-security and workspace-governance arguments in `me/published-thinking.md`.

**Section:** Scratchpad
**Suggested action:** cut from developing-thinking.md — already a canonical signature phrase in `me/published-thinking.md`.

## Frameworks

### frameworks/bitter-lesson.md — worth-revisiting

The framework's "radical extension" claims AI doesn't need the invisible 80% at all — that it routes around the human cognitive scaffolding, and that enterprises should "stop trying to 'capture' tacit knowledge and feed it into enterprise systems." Everything published since points the other way: the May 7 crawl/walk/run post argues agents fail *precisely because* nobody taught them context, judgment, and how work actually gets done, and `frameworks/knowledge-factory.md` is an entire engineered apparatus for capturing organizational tacit knowledge (and already states, in its closing section, that it revises the bitter lesson). The "stop engineering, start enabling" core still holds; the dissolution claim now contradicts the record.

**Suggested action:** rewrite the "radical extension" section to match the knowledge-factory revision — enable the pioneers, then industrialize what they proved — rather than leaving the "AI doesn't need the 80%" claim standing as-is.

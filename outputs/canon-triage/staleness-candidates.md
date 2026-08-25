---
title: Canon staleness triage — 2026-08-24
date: '2026-08-24'
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

# Canon staleness triage — 2026-08-24

Mirror image of `outputs/technical-briefings/promotion-candidates.md`: that queue proposes additions to canon, this one proposes cuts, promotions, or a second look at what's already there. Everything below is one model's read against the current published record — nothing here is a decision. An item leaves `me/developing-thinking.md`, or a framework's `status` flips to `archived`, only if Brian does it himself, same non-negotiable as every other tier-3 output. **This file is overwritten fresh on every run — it's a snapshot of the current state, not an accumulating log.** Items not mentioned below were read and judged still genuinely developing; their absence is the "keep" signal, not an oversight.

This run reviewed the full "What's connecting" and "Scratchpad" sections of `me/developing-thinking.md`, plus 10 active framework(s). Flagged: 4 developing-thinking item(s), 2 framework(s).

---

## Developing-thinking items

### "Token economics are the emerging macro constraint." — worth-revisiting

The item frames token economics as a constraint that is only now forming, but two of its three dimensions are already published positions rather than emerging ones: [How to build an AI strategy that survives the bubble pop](https://www.citrix.com/blogs/2026/07/20/how-to-build-an-ai-strategy-that-survives-the-bubble-pop/) makes "get serious about model routing and token economics" one of five do-now moves and lands "don't assume the price you pay today is the price you'll pay tomorrow," and [What's left for humans?](https://www.citrix.com/blogs/2026/04/09/whats-left-for-humans/) already prices every knowledge task human-vs-AI (dimension 2) while the bubble post already describes tiered model access (dimension 3). What survives as genuinely undeveloped is dimension 1 — the structural consumer/enterprise pricing gap and the 10x delta for heavy users — which no published post covers.

**Section:** What's connecting
**Suggested action:** narrow this item down to the consumer/enterprise pricing-gap dimension and drop the "emerging" framing, since the other two dimensions are now published positions.

### "Human clock speed is the invariant AI hasn't changed—and this reframes everything about knowledge work productivity." — promote-candidate

This is a complete argument with a thesis (gathering compresses, absorption doesn't), a named category error ("AI makes knowledge work faster"), a replacement claim (deeper, not faster), a prescriptive implication for organizations, and a counter to the substitution thesis that no other item in the file lands as cleanly. It also plugs directly into the published invariants method from [How a futurist reads AI news](https://www.citrix.com/blogs/2026/06/30/how-a-futurist-reads-ai-news-hint-ignore-most-of-it/) without duplicating it — absorption time is an invariant that list doesn't include.

**Section:** What's connecting
**Suggested action:** write this up as a standalone post or framework file; it's the strongest unpublished thesis-level claim in the section.

### "Second brain data integrity: selection bias is the primary failure mode." — promote-candidate

This has everything a framework file needs and nothing else in the record duplicates: a concrete first-person incident, a named mechanism (selection bias on a training set of one), a generalization beyond the originating case, and a prescription that does real argumentative work elsewhere — it's an independent case for file-based storage over vector databases, which reinforces the test-time-training item's portability/auditability argument from a completely different direction (data hygiene rather than governance).

**Section:** Scratchpad
**Suggested action:** graduate this out of the scratchpad into a short framework file on second-brain data integrity, or fold it into the second-brain material as its named failure mode.

### "The prerequisite clarity problem: AI is exposing organizational ambiguity humans have been papering over with effort." — already-published

The claim — that AI stalls where organizational purpose was never defined, and that "connect AI to your systems" fails without the prior step — is the published diagnosis in two places. [The knowledge factory](frameworks/knowledge-factory.md) states it directly ("AI's problems are mostly not AI problems"; hallucination from conflicting or missing information; "you can't point AI at sludge and expect diamonds"), and [Why enterprise AI agents disappoint](https://www.citrix.com/blogs/2026/05/07/why-enterprise-ai-agents-disappoint-and-why-the-fix-is-not-better-agents/) publishes the same point as the skipped "walk" step — nobody defined what context matters or what good looks like.

**Section:** What's connecting
**Suggested action:** cut from developing-thinking.md — covered by [the knowledge factory](frameworks/knowledge-factory.md) and [Why enterprise AI agents disappoint](https://www.citrix.com/blogs/2026/05/07/why-enterprise-ai-agents-disappoint-and-why-the-fix-is-not-better-agents/).

## Frameworks

### frameworks/bitter-lesson.md — worth-revisiting

The framework's central extension — that AI "routes around" the invisible 80% and enterprises shouldn't bother capturing tacit knowledge — has been contradicted, not merely qualified, by three later published positions: [Skills are all you need](https://www.citrix.com/blogs/2026/03/12/skills-are-all-you-need/) is an entire argument for capturing tacit knowledge as text files, the crawl/walk/run post says agents fail *because* nobody captured context and judgment, and the knowledge factory is an engineered apparatus for exactly that capture. The file currently handles this with a long inline revision note, which leaves the dated claim as the framework's headline and the correction as a footnote.

**Suggested action:** rewrite the file so the corrected position (stop over-engineering the wrong layer, then deliberately industrialize the capture) is the framework's thesis, rather than a patch appended to a claim it reverses.

### frameworks/delegation-not-automation.md — worth-revisiting

The framework's load-bearing premise is that 99% of workers will never author anything and only want to hand tasks off, which now sits in tension with two published positions: [Skills are all you need](https://www.citrix.com/blogs/2026/03/12/skills-are-all-you-need/) closes on "whether you want to be the one writing them or the one being replaced by someone who did," and the knowledge factory gives ordinary workers named authoring roles (input owners, output owners, SMEs, reviewers) mediated by packaged skills. The distinction Brian would presumably draw — that describing how you work in plain English isn't the same as building a workflow in an automation studio — is exactly the thing the framework doesn't currently say.

**Suggested action:** add the skills-vs-automations distinction to the framework so "workers won't build" reads as a claim about workflow construction rather than about all authoring.

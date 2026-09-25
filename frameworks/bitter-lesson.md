---
title: "The bitter lesson of workplace AI"
date: 2025-09-17
authority_level: 4
file_type: framework
tags: ["enterprise-ai", "worker-led-adoption", "governance", "shadow-ai", "knowledge-factory"]
related_frameworks: ["knowledge-factory", "invisible-80-percent", "factory-electrification", "workspace-as-control-plane"]
related_posts: ["2025-09-17-the-bitter-lesson-of-workplace-ai"]
original_url: "https://www.citrix.com/blogs/2025/09/17/the-bitter-lesson-of-workplace-ai-stop-engineering-start-enabling/"
description: "A sequencing claim: build the knowledge factory now, and the bitter lesson thins its scaffolding later. For AI tooling, enable what workers already chose instead of engineering a replacement."
staleness_threshold: stable
tier: 2
status: reviewed-and-updated
---

# The bitter lesson of workplace AI

The bitter lesson is a claim about *order*, not a standing rule. Now: if you want AI inside the systems and processes you actually run, you have to build the [knowledge factory](../frameworks/knowledge-factory.md)—deliberately capturing the tacit knowledge, curating canon, governing it. Later: once that factory exists and starts automating itself, the scaffolding that had to be hand-built to get it running turns out not to be needed to keep it running, and the parts engineered around human constraints get cut first. That thinning is the bitter lesson arriving—not a reason to skip the build, but what happens to the build afterward.

One piece of the original argument holds unchanged, and it's about tooling: don't engineer a "better" AI tool to replace the ones workers already found. Enable those and govern the environment they run in.

*Published: September 17, 2025—[Original post](https://www.citrix.com/blogs/2025/09/17/the-bitter-lesson-of-workplace-ai-stop-engineering-start-enabling/). Rewritten 2026-09-25 around the sequencing claim; see [how this framework changed](#how-this-framework-changed) for the lineage.*

## Two prescriptions, not one

- **For the tooling: stop engineering, start enabling.** Workers get better results from the simple tools they picked themselves than from the elaborate ones IT builds to replace them. Apply governance at the workspace layer, not the tool layer.
- **For the knowledge: enable the pioneers first, then industrialize the capture.** The invisible expertise AI needs doesn't show up on its own. Somebody has to capture it, and at organizational scale that's an engineered apparatus—the knowledge factory.

The original 2025 version applied the first prescription to both. That's the part that didn't hold.

## The original bitter lesson (Rich Sutton)

Throughout AI research history, researchers kept learning the same painful truth: simple methods that leverage computation always beat sophisticated algorithms designed by clever humans. Chess engines that searched more positions beat ones with hand-crafted strategies. Neural networks that processed more data beat systems with carefully engineered features. The lesson: stop trying to be clever. Scale and simplicity win.

## The workplace version (still true for tooling)

The same pattern played out in enterprise AI tooling:

- Companies pour millions into custom models, complex integrations, and elaborate governance frameworks
- Workers get better results with a $20 ChatGPT subscription
- IT's response: "That's just shadow AI. Our *real* solution will replace it."
- The workers have it right

This isn't workers being lazy or IT being incompetent. It's how technology spreads: the simplest path to value wins.

## Why the knowledge half needs to be built, not routed around

The [invisible 80%](../frameworks/invisible-80-percent.md) framework established that most knowledge work is invisible—judgment, tacit expertise, pattern recognition, reasoning. Enterprise AI only sees the visible part (outputs, documents, observable actions).

The observation behind the original claim is still true: AI can route around large parts of the cognitive scaffolding humans built to get from inputs to outputs. If you're getting SVP-level strategic support from AI, it didn't need the years of accumulated judgment beneath that level. It just arrived at the output.

What doesn't follow is that the invisible part can be ignored. [Skills are all you need](https://www.citrix.com/blogs/2026/03/12/skills-are-all-you-need/) is an argument *for* capturing tacit knowledge as text files. The [crawl/walk/run post](https://www.citrix.com/blogs/2026/05/07/why-enterprise-ai-agents-disappoint-and-why-the-fix-is-not-better-agents/) argues agents fail *precisely because* nobody did that capture work. And the invisible part never shrinks to zero: the boundary moves as AI erodes into it—60/40, 40/60, whatever the real number is for a given kind of work—but something always stays invisible, and that remainder needs deliberate capture permanently, not as a phase before AI absorbs everything.

## The connection to factory electrification

This maps onto [factory electrification](../frameworks/factory-electrification.md). Phase 2 companies engineer AI into existing human workflows—new tech, old processes. Phase 4 redesigns work around what AI makes possible. The sequencing claim says how you get from one to the other: you build the factory first, and the redesign is what the factory does to itself as it matures, dropping the parts that only existed to accommodate human constraints.

## Using this framework

Deploy when:
- An enterprise is engineering a better AI *tool* when workers have already found one—enable the ones they chose, govern the environment
- Someone assumes the knowledge factory's scaffolding is permanent—it automates and thins over time, even though it has to be built first
- Someone argues "AI can't do X because it lacks human judgment/experience/intuition"—AI might not need to replicate the human path to reach the human outcome
- A company is stuck in Phase 2 of the factory electrification pattern and needs to see Phase 4 as where the build leads, not a substitute for it

Do **not** deploy it as an argument against capturing institutional knowledge, or as a reason to wait for scale to make the build unnecessary. The capture work is the prerequisite; the bitter lesson only describes what happens to that apparatus after it exists.

The philosophical anchor holds either way: don't assume AI needs to work the way humans work to achieve what humans achieve.

## How this framework changed

- **2025-09-17, original post.** "Simple, worker-driven AI adoption beats elaborate, IT-engineered solutions. Every time." Applied to both tooling and knowledge, and argued AI doesn't need the invisible 80% at all.
- **First correction (2026).** Skills, the crawl/walk/run evidence, and the [knowledge factory](../frameworks/knowledge-factory.md) all showed the invisible knowledge has to be captured deliberately, not routed around.
- **2026-08-28.** Dropped the "dissolves" language: the visible/invisible boundary moves but never reaches zero.
- **2026-09-04.** Reframed as a sequencing claim—build now, thin later.
- **2026-09-25.** Rewrote the whole explainer around the sequencing claim, since three stacked corrections had left the headline contradicting the framework's own conclusion. The September 13 "execute, don't pilot" thinking in [developing-thinking.md](../me/developing-thinking.md) pushes the same direction: the engineered factory build is the move now.

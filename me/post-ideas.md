---
title: "Post ideas — what I might write next"
date: 2026-09-04
updated: "2026-09-04"
last_reviewed: "2026-09-04"
authority_level: 5
file_type: queue
tags: ["current-thinking", "frontier", "post-ideas", "pipeline"]
staleness_threshold: weeks
description: "A curated queue of pieces Brian is considering writing. Ideas only — nothing here is a position, a commitment, or a schedule. The lowest-authority file in the repo."
tier: 2
status: not-reviewed-by-human
---

# Post ideas — what I might write next

**Read this file as intent, not as thinking.** Everything below is an idea for a piece that doesn't exist yet. Nothing here is a position I hold, a claim I'm making, or a promise that any of it gets written. If you want what I actually think, read [`me/published-thinking.md`](published-thinking.md) (concluded) and [`me/developing-thinking.md`](developing-thinking.md) (forming). This file is one layer below both: the shortlist of arguments that feel like they want to be posts.

**Why it exists.** Ideas kept surfacing in the weekly review with nowhere to land — good enough to keep, not developed enough to be canon, and not something the promotion/staleness queues are built for (those move things *into* canon; this one points at things that should leave canon as published work). Started 2026-09-04.

**How an item moves.** An idea gets added here when I say out loud that something is "worth a real piece." It leaves when I write it, or when I decide I don't care — and I'd rather delete a dead idea than let this become another list that only grows. Each entry names where the actual argument already lives, so writing the post means expanding canon, not starting from a blank page.

---

## Next up

### The compute-availability risk is the cloud elasticity lesson, again

**Where the argument lives:** `me/developing-thinking.md` → "What's connecting" → August 28 update.

Early cloud promised true on-demand elasticity; what enterprises actually learned was that when everyone needs capacity at once, on-demand isn't guaranteed, and the fix was reserved capacity — commit for the year, not the hour. The same dynamic is forming in AI inference as labs redirect flops toward their own R&D: *availability*, not price, becomes the binding constraint. "Control your own destiny," a lesson enterprises already paid for once.

**Why it's the front-runner:** it's a complete argument already — historical analogy, named mechanism, concrete enterprise prescription — and it plugs a specific hole in [How to build an AI strategy that survives the bubble pop](https://www.citrix.com/blogs/2026/07/20/how-to-build-an-ai-strategy-that-survives-the-bubble-pop/) (July 20, 2026), which handles price and model access but not availability. Sequel, not a repeat.

**What's missing:** nothing structural. Needs writing.

### The bottleneck argument, and what it leaves for humans

**Where the argument lives:** `me/developing-thinking.md` → "What's connecting" → September 4 update. Related: the deferred `machine-speed-vs-human-absorption` thread in `outputs/technical-briefings/promotion-candidates.md`.

Make one person superhuman with AI and change nothing else and the company doesn't get faster — the queue just moves. A workflow is only as fast as its slowest step, and after AI the slowest steps are all the human ones. Meanwhile the evidence on human-in-the-loop review keeps landing the same way: the human isn't actually reviewing. So the human step is both the bottleneck and not doing its job, and the rational move is to remove it — the system gets faster and, on the measured evidence, no less safe. Then you're standing in front of [What's left for humans?](https://www.citrix.com/blogs/2026/04/09/whats-left-for-humans/) again, with worse news than last time.

**Why it's a real piece:** it's uncomfortable, it's supported by numbers rather than vibes, and it revisits my own published post with evidence that has moved since. The honest version ends without a clean answer, which is the point.

**What's missing:** the plain-language framing work the `machine-speed-vs-human-absorption` thread is waiting on. Don't write this one in the dense version.

---

## Warm — real, not ready

### Watching what agents do, because you can't watch what they think

**Where the argument lives:** `me/developing-thinking.md` → "What's connecting" → September 4 update (the unmonitorability item).

Agent oversight assumed chain-of-thought was legible. That assumption is dissolving, which puts agents exactly where humans already are — you supervise behavior, not thought. Except behavior-watching is getting harder at the same moment it becomes mandatory, so the observable surface has to become everything an agent touches and how. The counterweight (cryptographic agent identity, task-scoped permissions, traceable handoffs) is already shipping.

**What's missing:** the ending. Watching everything an agent touches is only tractable if something else does the watching, and that something is another agent whose reasoning you also can't read. I don't have the resolution, and a piece that just names the regress isn't obviously worth publishing yet.

### Nobody can measure knowledge-worker productivity, and here's how to think about it anyway

**Where the argument lives:** `me/developing-thinking.md` → Scratchpad.

Engineers can answer the productivity question in commits. Knowledge workers can't answer it at all. Most AI-ROI writing quietly assumes engineering or call-center contexts because those have task units. An honest "we don't have a measurement framework, here's how to reason without one" piece would get cited widely, precisely because everyone is being asked for the number and nobody has it. Related and equally unsolved: token measurement itself, where no vendor provides adequate usage analytics and the cached-vs-generated distinction changes the incentives.

**What's missing:** an actual point of view. Right now it's a well-observed gap, not an argument. Naming the gap is the easy half.

---

## How this file works

Lowest authority level in the repo (5). Curated by hand, not generated. Items are added when I flag something as worth writing, and removed when it's written or abandoned — see [`GOVERNANCE.md`](../GOVERNANCE.md) for what belongs in this repo at all.

---
title: "Post ideas — what I might write next"
date: 2026-09-04
updated: "2026-10-12"
last_reviewed: "2026-09-25"
authority_level: 5
file_type: queue
tags: ["current-thinking", "frontier", "post-ideas", "pipeline"]
staleness_threshold: weeks
description: "A curated list of future post ideas Brian is considering writing. Ideas only—nothing here is a position, a commitment, or a schedule. The lowest-authority file in the repo."
tier: 2
status: not-reviewed-by-human
---

# Post ideas — what I might write next

**Read this file as intent, not as thinking.** Everything below is an idea for a piece that doesn't exist yet. Nothing here is a position I hold, a claim I'm making, or a promise that any of it gets written. If you want what I actually think, read [`me/published-thinking.md`](published-thinking.md) (concluded) and [`me/developing-thinking.md`](developing-thinking.md) (forming). This file is one layer below both: the shortlist of arguments that feel like they want to be posts.

**Why it exists.** Ideas kept surfacing in the weekly review with nowhere to land — good enough to keep, not developed enough to be canon, and not something the promotion/staleness queues are built for (those move things *into* canon; this one points at things that should leave canon as published work). Started 2026-09-04.

**How an item moves.** An idea gets added here when I say out loud that something is "worth a real piece." It leaves when I write it, or when I decide I don't care — and I'd rather delete a dead idea than let this become another list that only grows. Each entry names where the actual argument already lives, so writing the post means expanding canon, not starting from a blank page.

---

## Future post ideas

Not ranked. Each entry's "What's missing" line is the readiness signal. An idea can be worth capturing even if the post never gets written.

### The knowledge factory works—now execute

**Where the argument lives:** `me/developing-thinking.md` → "What's connecting" → September 13 update (the execute-now note), building on "The knowledge factory" and "The net-new layer."

Companies have spent a couple of years kicking AI ideas around. That phase is over. We know the knowledge factory works—we built one. We know AI can come in, read how a company actually works, and analyze the existing systems—and in regulated environments we already know how to handle PII and redaction. The playbook exists, and models like GPT-6 Astra and Fable 5.1 mean the *model* is no longer what you're waiting on. The sharp reframe: there's no point bringing AI into your existing estate unless you're building toward the factory—doing it for security alone is short-sighted. The estate doesn't get torn down (especially in regulated, old-school companies); it becomes the connective tissue that feeds the factory and receives its outputs. Skate to where the puck is going.

**Why it's a real piece:** it's the "make an actual plan" post the whole knowledge-factory arc has been building toward, and it's the one with the clearest call to action for an enterprise reader. This is the knowledge-factory post.

**What's missing:** the decision on how much Citrix shows up by name (fine to mention—it's the job—but the piece shouldn't be *about* Citrix), and Nancy's "interstitial tissue" framing worked in cleanly rather than bolted on.

### The compute-availability risk is the cloud elasticity lesson, again

**Where the argument lives:** `me/developing-thinking.md` → "What's connecting" → August 28 update.

Early cloud promised true on-demand elasticity; what enterprises actually learned was that when everyone needs capacity at once, on-demand isn't guaranteed, and the fix was reserved capacity — commit for the year, not the hour. The same dynamic is forming in AI inference as labs redirect flops toward their own R&D: *availability*, not price, becomes the binding constraint. "Control your own destiny," a lesson enterprises already paid for once.

**Why it's the front-runner:** it's a complete argument already — historical analogy, named mechanism, concrete enterprise prescription — and it plugs a specific hole in [How to build an AI strategy that survives the bubble pop](https://www.citrix.com/blogs/2026-07/how-to-build-an-ai-strategy-that-survives-the-bubble-pop) (July 20, 2026), which handles price and model access but not availability. Sequel, not a repeat.

**What's missing:** nothing structural. Needs writing.

### The bottleneck argument, and what it leaves for humans

**Where the argument lives:** `me/developing-thinking.md` → "What's connecting" → September 4 update. Absorbs the `machine-speed-vs-human-absorption` thread, cleared from the promotion queue 2026-09-13 and folded in here.

Make one person superhuman with AI and change nothing else and the company doesn't get faster — the queue just moves. A workflow is only as fast as its slowest step, and after AI the slowest steps are all the human ones. Meanwhile the evidence on human-in-the-loop review keeps landing the same way: the human isn't actually reviewing. So the human step is both the bottleneck and not doing its job, and the rational move is to remove it — the system gets faster and, on the measured evidence, no less safe. Then you're standing in front of [What's left for humans?](https://www.citrix.com/blogs/2026-04/whats-left-for-humans) again, with worse news than last time.

**The other half of the same post: AI makes knowledge work deeper, not faster.** AI compresses the *gathering* phase but not the *absorption* phase—you still need the same time to make new material your own. "AI makes knowledge work faster" is a category error; the real claim is that it makes the work *deeper*. This is the invariant the bottleneck argument runs into, and it's the thesis this whole publication is named after—worth writing as its own strand of the piece rather than a footnote.

**Why it's a real piece:** it's uncomfortable, it's supported by numbers rather than vibes, and it revisits my own published post with evidence that has moved since. The honest version ends without a clean answer, which is the point.

**What's missing:** just the writing—the plain-language framing the old `machine-speed` thread was waiting on is now in the developing-thinking notes. Don't write this one in the dense version.

### If the AI-safety panic forces a slowdown, what happens to enterprise AI?

**Where the argument lives:** `me/developing-thinking.md` → "What's connecting" → September 13 update (the slowdown second-order note).

The whole industry is talking about AI doom right now. Whether the doom is real isn't my beat—the second-order effect is. If the "race into unmonitorability" fear actually forces a pause or slowdown at the frontier, what happens inside companies? Two forces pull opposite ways: a collapse in the frontier-progress narrative could give cautious enterprises the air cover they've wanted to slow down ("even the labs are braking, so we can wait"), while the AI-native companies the VCs are funding won't slow at all. And it runs into a position I already hold—everything important in the enterprise can be done with mid-tier models that have already shipped—so a frontier slowdown shouldn't dent the enterprise thesis much, unless the narrative collapse changes behavior more than the lost capability does.

**What's missing:** the ending, honestly. I don't know which way it breaks, and I think it depends on what actually happens. It might not be publishable until there's a real event to hang it on—but it's the right lens for whenever that event arrives, so it's worth having ready.

### When you can't read an agent's reasoning, you can only watch what it does

**Where the argument lives:** `me/developing-thinking.md` → "What's connecting" → September 4 update (the unmonitorability item).

Agent oversight assumed chain-of-thought was legible. That assumption is dissolving, which puts agents exactly where humans already are — you supervise behavior, not thought. Except behavior-watching is getting harder at the same moment it becomes mandatory, so the observable surface has to become everything an agent touches and how. The counterweight (cryptographic agent identity, task-scoped permissions, traceable handoffs) is already shipping.

**What's missing:** the ending. Watching everything an agent touches is only tractable if something else does the watching, and that something is another agent whose reasoning you also can't read. I don't have the resolution, and a piece that just names the regress isn't obviously worth publishing yet.

### Every CIO is asking the same questions, and nobody has answers

**Where the argument lives:** `me/developing-thinking.md` → "Right now" (September 25), from the WSJ CIO conference in New York.

The questions were the same from every direction: "I have no idea what's going on in my environment." "We know we're supposed to transform with IT, but we don't know where to start." "We have to thaw the frozen core of the business—where do we begin?" And the sobering one is the *best* case: the CIO with an AI gateway who can see every user, token, and model and still can't tell whether the work is getting better or just more expensive. At the same time, CIOs are convincing each other that AI can really change things, from their own small projects. So the question has moved past "should we" and past "copilots everywhere" to two harder ones: how would you even know it's helping, and how do you get from starter projects to the enterprise?

**Why it's a real piece:** it's first-hand, from the room, and it's the question every enterprise reader is actually sitting with.

**What's missing:** the answer, and a decision on shape. Its two halves overlap with other entries here: "how would you know" is the productivity-measurement piece below, and "starter projects to the enterprise" is the knowledge-factory execute post. This may end up as the opening of one of those rather than its own post.

### The best AI model is losing enterprise deals, and it's not about what it can do

**Where the argument lives:** not in canon yet. Evidence in the September 16 daily brief (Nvidia, Palantir, and Booz Allen restricting Fable for sensitive work) and the September 14–25 Weekly Wrap Up. Related: the Scratchpad note that data now has a published price.

When the biggest enterprise buyers restrict a frontier model, the reason is where the data goes and whether the zero-retention promise can be revoked, not capability. A utility walked away from a trial over it, and competitors are selling into the distrust. For the enterprise, trust and control are the product; capability is table stakes.

**What's missing:** a second and third example beyond Fable, so it's a pattern and not one news cycle, and a tie back to workspace-as-control-plane (where the data boundary actually gets enforced).

### The harnesses are almost more important than the models

**Where the argument lives:** not in canon yet. Evidence in the September 18–23 daily briefs (Berkeley's HarnessTax study, the "harness engineering" conference track). Related: "The executor seam is the unowned thing in agent architecture" and the September 25 addition to the human-in-the-loop entry, both in `me/developing-thinking.md`.

Swap nothing but the orchestration around the same model and cost per task drops by up to 71%, with no loss in accuracy; one vendor's own harness lost to a competitor's in 9 of 12 matchups. A mediocre model in a great harness beats a great model in a bad one. That changes what an enterprise should be evaluating and buying, and it's also where governance enforcement has to live.

**What's missing:** Brian's own position. So far this is a strong finding he agreed was worth a post, not an argument he's made.

### Nobody can measure knowledge-worker productivity, and here's how to think about it anyway

**Where the argument lives:** `me/developing-thinking.md` → Scratchpad.

Engineers can answer the productivity question in commits. Knowledge workers can't answer it at all. Most AI-ROI writing quietly assumes engineering or call-center contexts because those have task units. An honest "we don't have a measurement framework, here's how to reason without one" piece would get cited widely, precisely because everyone is being asked for the number and nobody has it. Related and equally unsolved: token measurement itself, where no vendor provides adequate usage analytics and the cached-vs-generated distinction changes the incentives.

**What's missing:** an actual point of view. Right now it's a well-observed gap, not an argument. Naming the gap is the easy half.

### Knowledge work is a preview of what agents will need

**Where the argument lives:** `me/developing-thinking.md` → Scratchpad → the two entries flagged 2026-09-30 (humans as the leading indicator for agents; the second hop of the coding thesis).

I've said coding is a preview of knowledge work: what happens in software engineering shows up in knowledge work a step later. The extension is that knowledge work is a preview of agents. What humans do next is the leading indicator for what agents will need. People are adopting an AI knowledge layer, a second brain, so the AI knows who they are, what they know, and what they're allowed to do. Agents will need the same thing to succeed: a canonical access layer that tells them what they can do, what they can't, and what the organization expects of them. The human second brain is the prototype for the agent's. Two leading-indicator chains, stacked, stated as one argument: coding previews knowledge work, and knowledge work previews agents.

**Why it's a real piece:** it's one sentence people can repeat, and it ties the second-brain argument to agent governance, which are usually treated as separate subjects.

**What's missing:** whether the agent's layer is the same artifact as the human's brain, a governed subset of it, or something separate. And evidence beyond my own reasoning that agents are following the path humans took.

### Run important work through two different models, always

**Where the argument lives:** not in canon yet. It started as a note on the October 2 Daily Briefing restack (agents reshaping sensitive content, such as splitting a token, to get past secret scanners).

At work we found it mattered to use a different model to evaluate the work than the model that did it. Not a different model in the same family, since those are trained and diffused together: one vendor's model does the work and another vendor's checks it. The idea is that companies will want to run everything important through two different models in parallel, always. It roughly doubles operating cost, but you would catch things that would otherwise slip by. It's how mission-critical systems have long worked (the Space Shuttle's redundant computers), and AI may get cheap enough to do this for anything that matters.

**Why it's a real piece:** it turns "AI checking AI" from a vague idea into a specific architecture with a precedent from safety-critical engineering.

**What's missing:** how far up and down the chain it has to go (data inputs and outputs, not just the final answer), whether a smaller model should coordinate and evaluate, and whether the doubled cost is worth it outside the highest-stakes work.

### The AI stack is splitting into layers, the way computing did

**Where the argument lives:** `frameworks/cognitive-stack.md` and the October 2 Daily Briefing restack.

In the early days of computing one vendor and one set of hardware did everything: hardware, network, operating system, applications, security, management. Now every one of those is a specialized layer with its own vendors and standards. As the AI market matures, the AI stack should do the same, with its own hardware, software, vendors, and standards for each layer. Hardware is the first visible sign: Nvidia's Vera CPU is purpose-built for the agent-orchestration layer (tool calls, code execution, data movement) rather than for models in general.

**Why it's a real piece:** it turns the cognitive stack from a way of organizing thinking into a prediction about market structure, and it raises whether the "commodity, interchangeable" bottom layers pick up their own hardware economics and lock-in.

**What's missing:** my own read on what it means for an enterprise buyer (buy by layer?), and evidence beyond silicon.

### Token price is the wrong unit; price the accepted work

**Where the argument lives:** `me/developing-thinking.md` → "What's connecting" → October 11 (token price is the wrong unit) and the February 27 Salesforce AWU entry. Related in this file: "Run important work through two different models, always" and "Nobody can measure knowledge-worker productivity."

Not all tokens are equal, and much of what makes work valuable isn't tracked at all: how much you trust it, how secure it is. The comparison that matters is the cost of a unit of work at a given accuracy level, which also means pricing in the intelligence that went into it. Companies that had effectively unlimited token budgets for a year are now setting real ones.

**Why it's a real piece:** "cost per task beats cost per token" is no longer news (see prior art), so the open space is the denominator. Most versions divide by a pass/fail success rate on a benchmark. None of the ones found treat trust and security as first-class costs. The economics literature says why they matter: when producing work gets cheap, the scarce thing is verifying it. That makes this a piece about what a unit of *accepted* work costs, with verification as the real price of accuracy.

**What's missing:**
- My own position. So far this is one dictated paragraph, not an argument.
- A fix to the "run it three times" example before it's published. With independent errors and a coin-flip agent, a majority vote of three is still a coin flip. Best-of-three reaches 87.5% only if something can pick the right answer, so the verifier is the price of accuracy, and expected cost per success becomes (attempt + check) divided by the hit rate. Where no automatic checker exists, voting plateaus (Brown et al., below). Same-model reruns also tend to fail in correlated ways, which is the case for a second vendor's model.
- How to say "how much intelligence went into it" without hand-waving. Economists call this quality adjustment, and it's the hardest part to measure for knowledge work.
- Evidence for the budget-rationalization half (that's a belief, not yet a trend line).

**Prior art (AI-filed 2026-10-12; abstracts and pages read, not full papers):**
- Kapoor, Stroebl, Siegel, Nadgir and Narayanan, [AI Agents That Matter](https://arxiv.org/abs/2407.01502) (Jul 2024): accuracy-only agent benchmarks mislead; optimize cost and accuracy jointly.
- Appenzeller (a16z), [LLMflation](https://www.a16z.com/llmflation-llm-inference-cost) (Nov 2024): about 10x a year decline in cost at a fixed MMLU score, by the author's own "far from perfect" method. Epoch AI, [LLM inference price trends](https://epoch.ai/data-insights/llm-inference-price-trends) (Mar 2025): price to reach a fixed benchmark score fell 9x to 900x a year depending on threshold. That is price at a given accuracy level, but still priced per token.
- Catalini, Hui and Wu, [Some Simple Economics of AGI](https://arxiv.org/abs/2602.20946) (Feb 2026): execution cost falls toward zero while verification stays bounded by human capacity (their "Measurability Gap"). The strongest economic backing for "trust is the untracked cost."
- Zhu, [The Price of Intelligence](https://arxiv.org/abs/2608.29843) (Aug 2026; single-author v1 preprint, not peer reviewed): quality-adjusted inference prices fall about 0.73 log points a year against about 0.10 unadjusted, but per completed task the buyer's price stopped falling because reasoning models burn more tokens. Hedonic quality adjustment is standard practice at statistical agencies ([BLS](https://www.bls.gov/ppi/quality-adjustment/hedonic-models-in-the-producer-price-index.htm)); this is its first serious application to AI prices.
- Brown et al., [Large Language Monkeys](https://arxiv.org/abs/2407.21787) (2024): repeated sampling buys accuracy when an automatic verifier exists (one coding model went from 15.9% to 56% solved at 250 samples); without one, majority voting and reward models plateau.
- Vendor writing, indicative only because both sell measurement tooling: DoiT, [Cost Per Task, Not Cost Per Token](https://www.doit.com/research/economics-of-claude-openai-and-grok) (Aug 2026), divides by success probability and adds a risk-adjusted variant (undetected-failure rate times cleanup cost), with numbers it calls illustrative; LangWatch, [Cost per Successful Task](https://langwatch.ai/blog/cost-per-successful-task) (Jul 2026), uses cost per run over success rate and leaves verification cost out of the formula.
- The market already prices accepted outcomes: per-resolution pricing for support agents is reported at roughly $1 to $2 (Intercom Fin, Zendesk, Sierra; see [SaaStr](https://www.saastr.com/hubspot-switching-ai-pricing-from-per-use-to-per-resolution/)), and what counts as a "resolution" is where the contract risk sits. That is the accuracy risk moving onto the vendor.

---

## How this file works

Lowest authority level in the repo (5). Curated by hand, not generated. Items are added when I flag something as worth writing, and removed when it's written or abandoned — see [`GOVERNANCE.md`](../GOVERNANCE.md) for what belongs in this repo at all.

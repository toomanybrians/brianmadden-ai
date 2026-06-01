---
title: "Where Brian's head is right now"
updated: "2026-06-01"
authority_level: 2
file_type: frontier
tags: ["current-thinking", "frontier", "developing-arguments"]
staleness_threshold: weeks
description: "The frontier of Brian's thinking. Arguments forming, connections emerging, questions unresolved. This file changes frequently and is the best source for Brian's current direction."
---

# Where my thinking is right now

This is the frontier map. `me/published-thinking.md` captures what I've published. This captures where my head is *today*—the arguments forming, the connections emerging, the questions I'm chewing on.

**Last updated:** June 1, 2026

**Why this file exists and why it's public:** Anyone who publishes regularly—blogs, LinkedIn, tweets—is already doing this. They share half-formed ideas, ask questions, show threads developing, change their mind. Scroll their feed and you can piece together what they're thinking about and where their arguments are heading. This file is just that process made explicit. The difference is that instead of being scattered across a social media timeline where old posts get buried by new ones, it's a single living document. When my thinking evolves, I edit it in place rather than adding another entry to a chronological list. *Arguments get sharper, not longer.* Things I was wrong about get removed, not corrected with a follow-up post. If you want to know what I've *concluded*, read my published work in `me/published-thinking.md`. If you want to know what I'm *working through right now*, this is it.

---

## The big arguments I'm developing

### Second brains as infrastructure, not productivity hack
The published anchor article and blog established the concept. What's forming now is the *infrastructure* argument: second brains aren't a personal productivity trick, they're the individual-scale version of a new enterprise layer. Context graphs (Foundation Capital thesis) are the enterprise version. Subscribable brains are the distribution model. The 80/20 framework holds across all three levels—individual, organizational, and ecosystem.

The subscribable brains article is now published (Feb 17 LinkedIn). It covers creator economy disruption, the technical stack (GitHub/git/MCP/Sponsors), economics ($100/month for expert brains), enterprise implications (consulting firm knowledge, retiring VP wisdom, corporate brain modules), and subscribable facets (voice, frameworks, principles as individual modules). The frontier now is context graphs—bridging from personal to enterprise scale—and the naming question. "Context vault" has emerged as stronger enterprise framing than "second brain": vault implies protection, control, governance. It paves the way for the product conversation in ways "second brain" (which sounds like a productivity hack) doesn't.

### The consumerization parallel (and why it breaks)
Personal AI is following the BYOD pattern—workers adopt better tools, companies try to catch up, the gap persists. But this time the gap is *structural*. Enterprise AI captures the visible 20% (systems, outputs, observable work). Personal AI captures the invisible 80% (judgment, reasoning, tacit expertise). Companies can't offer "bring your whole cognitive self to work in a personal AI system that compounds daily and leaves with you when you go." That's not a feature you can build.

The knowledge capture angle adds a new dimension: enterprise AI doesn't just *fail* to match personal AI, it actively *extracts* worker value. Workers are already secretly using personal tools specifically to prevent this. The subscribable brain model is the worker-empowered alternative—you choose to share knowledge and get paid, rather than having it extracted.

**New evidence (Feb 25):** The token pricing gap makes this structural, not temporary. Heavy personal AI usage runs roughly $200/month on consumer plans. The same usage at enterprise pricing runs 10x or more. If the consumer can buy unlimited tokens and the company limits you to a fraction of that, you will never be as cognitively augmented at work as you are personally. Unlike BYOD, this gap may be permanent—Jevons paradox means enterprise demand grows with supply, governance overhead adds cost, and consumer/enterprise providers have different incentive structures.

**Additional evidence:** First-person reports confirm that enterprise deployments of the same AI tools are deliberately constrained compared to what the vendor's own employees use. Vendors advertise token allocation as a recruiting differentiator—"come work here, we give you more tokens than you'll get anywhere else." Workers building personal AI aren't just escaping generic enterprise tools; they're escaping deliberately sandbagged ones. The structural conflict: making the enterprise product too good cannibalizes the underlying productivity apps it depends on. That's not a bug in deployment—it's an architectural constraint built into the product decision.

### Post-application era entering evidence phase
The thesis (AI doesn't need apps, just data) has moved from speculation to evidence: 4% of GitHub commits from Claude Code, $285B SaaSpocalypse, MCP at 97M monthly SDK downloads, every company racing for agent orchestration.

**Mainstream validation cluster (Feb 2026):** Five different voices—investor (Shumer/Fortune), labor academic (WSJ), builder (Ford/NYT), VC (NFX), scientist (Kipping/Columbia)—all converging on the same message from different angles: the disruption has arrived, not "is coming." Ford independently named November 2025 as the inflection. His cost collapse numbers ($350K of work for $200/month) and Claude Code's $1B in six months are the SaaSpocalypse in mainstream language. NFX frames the economic math: SaaS captured $1T (selling tools), AI captures $50-60T (replacing the labor those tools served)—a 50x larger opportunity. VCs are now explicitly telling founders to build for a post-SaaS world.

**Salesforce AWU as accidental waste detector (Feb 27):** Salesforce unveiled a per-task metric (Agentic Work Unit) to show customers value per token spent. Putting a price tag on every task creates an economic incentive to stop doing tasks that only existed because humans were running the company—status reports, TPS reports, weekly summaries, coordination artifacts. "Work about work" exists because humans are bandwidth-constrained; AI isn't. The AWU metric doesn't just measure AI productivity—it exposes organizational waste that was invisible when human labor made it feel free.

**April 22 update: thesis sharpened and published.** [The SaaSpocalypse Won't Touch the Enterprise Software Moat](https://www.citrix.com/blogs/2026/04/22/the-saaspocalypse-wont-touch-the-enterprise-software-moat/) introduces the three-tier software framework: shallow UX-as-moat SaaS is toast; middle horizontal enterprise SaaS is squeezed; deep vertical regulated systems of record endure. The sharpening: *AI dissolves UIs, not systems of record.* The Epic UI is replaceable; the Epic database is not. Five reasons the deep layer endures: regulation, data gravity, encoded workflow, mission-critical tolerance, rebuild-doesn't-scale. The post-application thesis now has two published modes: dissolving for Tier 1-2, governance-between-worker-and-system-of-record for Tier 3.

The next frontier: what *does* work look like when apps dissolve? The second brain is the individual answer. Context graphs might be the enterprise answer. MCP connections replace application access as the governance perimeter.

### The cognitive stack (published, now road-tested)
The [five-layer cognitive stack](https://www.citrix.com/blogs/2026/02/25/understanding-the-cognitive-stack-why-your-ai-strategy-is-focused-on-the-wrong-layer/) published Feb 25 formalizes what I've been circling: worker → brain → skills → agents → interfaces. The enterprise AI industry is spending billions on the bottom two layers (agents, interfaces) while the transformative layer is the brain—the cognitive extension where context lives and intent gets translated into action. Karpathy's "claws" framing nails it: agents are appendages that serve the brain, not the other way around. Automation vendors built bottom-up, AI companies entered top-down—they collide in the middle (skills/agents) but humans prefer to connect at the intelligence layer.

**March 18 update:** Delivered "The New Cognitive Stack" as a full 60-minute closing session at DUCUG (Dutch Citrix User Group). The cognitive stack is now the organizing framework for the entire stump speech, replacing the 7-stage evolution model. The most effective rhetorical move: building up the audience's expectation for "automations" then deflating it. "I hate automations. How repeatable are your jobs that you're automating all this kind of stuff?" When you have the brain, the claws figure themselves out. "I can AI the crap out of the bottom of the stack, perfectly. And I still haven't changed the way the thinking happens, which is where all the money is."

**May 7 update:** [Why enterprise AI agents disappoint](https://www.citrix.com/blogs/2026/05/07/why-enterprise-ai-agents-disappoint-and-why-the-fix-is-not-better-agents/) publishes the crawl (chat) → walk (context/skills/judgment) → run (autonomous agents) pedagogy mapped onto the cognitive stack, plus the deeper move: "even after you can run, you still mostly walk"—successful AI use is layer selection per task, not racing to autonomous agents. This is the executive-friendly entry point to the stack. What remains unpublished: agents "don't look like agents" to enterprise buyers—a person with a second brain just looks like someone who's better at their job.

### Compute scarcity and token governance (hardened with real data, road-tested live)
Token consumption goes from ~100K/day (email fixes) to 5-10M/day (full cognitive augmentation)—now confirmed from my own measured usage. In a 3-week period (Jan 29–Feb 18): 285 million tokens, 96 sessions, $954 at enterprise API rates. The consumption ladder: 1B tokens/year (current heavy user) → 10B (near-term with agents, ~18 months) → 100B (agentic systems per worker). Supply is contracted to hyperscalers for ~4 years. If second brains go mainstream, demand explodes against fixed supply.

**March 18 update: token routing as governance, delivered live.** The Excel routing example landed at DUCUG: same task costs 200K tokens (CUA operating Excel) or 1K (reason in context). Six options, each with different cost/quality tradeoffs. Multiply by thousands of workers, hundreds of requests per day. This is a CFO/COO conversation. Someone has to route every request by complexity, sensitivity, and nature—not the AI vendor (sells tokens), not the model provider (consumes them). A neutral party with workspace context.

New formulations that landed: "The company that spends the most tokens in the most smart way is going to win." "Which half of my job do you want me to not do?" Tokens as recruiting tool—vendors already advertising to potential employees on the basis of token allocation.

Efficiency as capacity *multiplier*, not just cost reducer. In a zero-sum compute environment, 50% fewer tokens = twice the effective capacity. The routing layer—the intelligence that decides where workloads run—may be the most durable competitive advantage in enterprise AI.

**May 7 update: Excel routing example now published.** The four-layer version (do-it-yourself $0, reason-in-context ~1K, skill ~1K + maintenance, CUA agent ~200K) is in [Why enterprise AI agents disappoint](https://www.citrix.com/blogs/2026/05/07/why-enterprise-ai-agents-disappoint-and-why-the-fix-is-not-better-agents/). The core argument—each layer down costs more *and* requires the layers above—is now a public reference point.

---

## What's connecting

Things I'm noticing that don't have a home yet:

**Context graphs + subscribable brains + MCP = the new enterprise stack.** Context graphs capture the "why" (decision traces). Subscribable brains distribute expertise as infrastructure. MCP is the connective tissue. Together they describe a post-application enterprise architecture that nobody has articulated as a single picture yet. This might be the thesis that ties everything together.

**Knowledge capture as labor dynamic reframes the entire second brain narrative.** The initial framing is "personal AI makes you better." The WSJ reframes it as "enterprise AI makes you *more replaceable*." Same phenomenon, opposite vantage point. The subscribable brain is the resolution—worker-controlled knowledge sharing with compensation.

**The mainstream consensus is catching up to practitioners.** Five articles across February 2026 all say "it's happening now." Different authors, outlets, angles—converging on the same moment. What's missing from the mainstream coverage: the infrastructure layer (governance), the invisible 80%, knowledge ownership as empowerment (vs. defense), and compute scarcity. The mainstream validates the timeline. The interesting work is what comes *after* people realize this is happening.

**The capability overhang is closing faster than expected.** Physicists at Princeton's IAS conceding AI handles 90% of what they do. Primary source from David Kipping (Columbia/Cool Worlds): senior faculty stated AI does "something like 90%" of their intellectual work. On coding: "order of magnitude superior"—not a single hand objected. If the *hard* part (invisible cognition) is falling faster than expected, the urgency of governance and infrastructure arguments increases. The red pill moment isn't coming someday. The smartest people in the world are already in it.

**"Humans in control, AI as reach" vs. "autonomous agents" is a framing choice with massive implications.** The dominant enterprise AI frame is agent autonomy + guardrails. The second brain frame is human control + extended reach. These lead to completely different product architectures, governance models, and go-to-market narratives. Amodei's "Adolescence of Technology" argues AI trends toward *full substitution* rather than "human + tool." If he's right, the augmentation bet only wins for high-judgment work (the invisible 80%). Routine work gets substituted.

**The copilot-to-autopilot convergence puts a mechanism on the substitution timeline.** Julien Bek (Sequoia, March 2026) argues copilots are temporary. The mechanism: AI accumulates proprietary data about what good judgment looks like in each domain, and the frontier shifts. "Today's judgment becomes tomorrow's intelligence." The copilot's data advantage IS the path to the autopilot. Software engineering is already there. Insurance, accounting, legal, IT are 1-2 years out. The uncomfortable implication for the second brain thesis: a second brain is a copilot that compounds your judgment. At some point it *is* you, professionally. The subscribable brain doesn't just distribute your expertise—it could replace you.

**Enterprise invariants as the executive on-ramp.** Published April 9, 2026 as ["What's left for humans?"](https://www.citrix.com/blogs/2026/04/09/whats-left-for-humans-when-ai-can-do-everything/) The framing: anchor radical AI vision on what doesn't change, then show how each invariant's *scope* expands. Governance, identity, data sensitivity, risk, economics—these transform in place rather than disappearing. What remains unpublished: the explicit "on-ramp" framing as a rhetorical technique. Lead with what's unchanging; let the radical parts land from there.

**The cognitive stack is now the organizing framework for all public talks, with crawl/walk/run pedagogy attached.** Published February 25, delivered at DUCUG March 18, formalized in the May 7 agent-disappointment post. The crawl → walk → run pedagogy maps onto the stack and adds the deeper move: "even after you can run, you still mostly walk." Successful AI use is layer selection per task, not racing to autonomous agents. The invisible implication that remains unpublished: agents "don't look like agents" to enterprise buyers—a person with a second brain just looks like someone who's better at their job.

**Model portability is proven, not theoretical.** Claude went down, switched to Gemini, pointed it at the same folder. Within minutes, fully functioning. Demonstrated on stage. The model is a pluggable component. The brain is the durable asset. Strongest evidence yet that the architecture is model-agnostic by design.

**Practitioners working this way are emerging organically.** At least 15 people independently discovered second-brain-style AI usage without being directed to. Several have wired their systems together via git submodules. Brain-to-brain communication is live: dictate something, AI routes to the right person's brain, their AI surfaces it appropriately. Worker-led adoption isn't hypothetical—it's underway.

**"Legacy applications is like all of them."** Once you're working through a cognitive extension, every traditional application becomes a compatibility layer. Word is for sending documents to colleagues who don't have brains yet. Excel is a file format AI reads directly. Outlook and Teams are messaging APIs. Multiple practitioners report this independently. It's lived experience, not a theoretical position.

**Token economics are the emerging macro constraint.** Three dimensions forming: (1) The consumer/enterprise pricing gap is structural and may be permanent—heavy users burn $200/month at consumer rates vs. 10x at enterprise pricing. (2) Token equivalency for human work is becoming calculable—if 3M Sonnet tokens costs $400, you'd better be worth more than $400/day. (3) Model quality as class stratifier—who gets access to the frontier model? Not just token quantity but model quality as economic divide.

**"Software for one" is the next shadow IT crisis.** NFX calls it "custom autonomous software." CNBC reporters built a Monday.com replacement in under an hour for $5-$15. Workers aren't just using unsanctioned AI—they're *building unsanctioned software*. API costs down 90%, open-source models running locally, non-programmers shipping tools. None of this shows up in an app inventory. The second brain is the mature, structured version. The wild version is entirely ungoverned.

**The cost-cutting vs. innovation split is the macro frame for everything.** Amodei identifies two corporate responses to AI: cost-cutting (replace workers) and innovation (expand capacity). These produce completely different customers, different governance needs, different workforce strategies. The 80/20 framework applies differently to each: cost-cutters automate the visible 20%, innovation companies augment the invisible 80%.

**The diffusion gap is the real urgency driver.** Amodei's timeline: 1-2 years to "powerful AI" (Nobel-caliber, millions of instances, autonomous for weeks). The gap between "AI can do this" and "society/enterprises have adjusted" is where the damage happens. Previous technology waves had decades to diffuse. AI may have years. The question isn't whether these changes are coming. It's whether the institutional and governance infrastructure is ready when they arrive.

**Individual AI augmentation doesn't show up in firm-level ROI until the org restructures.** The electrification parallel sharpens this: workers getting lightbulbs (Phase 3) is a real capability gain, but it doesn't produce firm-level productivity change until the factory floor is redesigned around the new capability (Phase 3→ group drive → unit drive). A phase-5 worker stuck in a phase-1 organization is a faster worker in the same decision queue. "1+1+1+1=1.5"—the bottleneck is decision-rights congestion, not individual capability. This is why the AI ROI question is mostly being asked wrong. The organization has to be rewired, not just the workers upgraded.

**The repo is the product, not the content.** If BrianMadden.com was built today, it would be a GitHub repo. Books, newsletters, websites are packaging formats for human consumption. A forkable, queryable knowledge repo is the native format for AI-augmented consumption. brianmadden.ai is the proof of concept.

**The coding-as-leading-indicator framework connects to adversarial brain testing.** The [five levels](https://www.citrix.com/blogs/2026/02/19/what-will-knowledge-work-be-in-18-months-look-at-what-ai-is-doing-to-coding-right-now) raise a verification question at Levels 4-5: how do you know the AI's work is any good? For code, the answer was behavioral tests stored separately from the codebase. For a subscribable brain, the answer is adversarial testing—a separate repo that runs challenge prompts, skeptical personas, and evaluation rubrics against the brain. Nobody is publicly stress-testing their own thinking with structured adversarial AI agents.

**New content formats are emerging from the brain's infrastructure.** Brain diffs (weekly "what changed in my thinking" auto-generated from git commits) are a genuinely new content format—not a newsletter, a changelog for a worldview. Forked brains create intellectual lineage that git tracks automatically. Brain-to-brain debates (two AIs load two brains, have a structured debate) produce a new kind of artifact.

**Knowledge is migrating to portable formats.** Organizational knowledge is moving to portable, AI-native formats. Markdown files in git repos contain the actual working knowledge. Incumbent platform graphs become the metadata layer (who, when, permissions) while the knowledge layer moves to vendor-neutral formats.

**Knowledge distillation as espionage vector.** Fragments of public thoughts synthesize into what would represent sensitive strategic documents. AI can infer unpublished positions from patterns across published work. This creates a new adversarial dimension: what does a public brain reveal that the author wouldn't want competitors to know? The answer isn't to publish less—it's to be intentional about what compounds when synthesized.

**Writing long-form for AI, not audience.** The distribution isn't the article—it's the brain module. Write 20K words not for anyone to read but as an expert module for AI consumption. Others plug it into their brain and the frameworks weave into their thinking immediately. The future isn't "subscribe to my newsletter"—it's "subscribe to my expert module."

**"This is not AGI."** None of the evidence, none of the cost collapse data, none of the enterprise disruption requires AGI or ASI. Current models are already powerful enough. The AGI debate is a distraction from the disruption already underway.

**Every technology wave has a bottleneck, and it's never the technology itself.** Factory electrification = workflow design. Web apps = rewriting. BYOD = governance. AI = the invisible 80%. The bottleneck is where value concentrates.

**Book publishing as knowledge transfer is dead.** Fork the author's brain, tell your AI to incorporate it, their frameworks weave into your thinking immediately. Books were the best technology we had for transferring expertise. They're not anymore.

**The specification bottleneck is the emerging economic constraint.** When building costs nothing, spec quality collapses. The cost of building historically filtered bad specs. Remove the cost and the filter disappears. You can now build the wrong thing at unprecedented speed. AI-generated code produces 1.7x more logic issues (CodeRabbit, 470 PRs). Experienced developers 19% slower with AI but believed they were 24% faster (METR). The scarce resource shifts from production to specification—knowing what to build.

**Management is an emergent property of intelligence coordinating at scale.** Three independent AI systems (Cursor agents, StrongDM's Software Factory, Anthropic's agent teams) converged on hierarchical management structures without being designed to. Hierarchy isn't a human organizational choice—it's what intelligence does when it needs to coordinate. The agent-to-human ratio question replaces headcount planning. Revenue per employee at AI-native companies runs 5-7x traditional SaaS—not because they found better people, but because their people orchestrate agents instead of doing execution.

**Regulatory divergence accelerates personal AI consumerization.** Worker protection regulations (EU AI Act, GDPR, works councils, French working time law) create friction for company-provisioned AI that personal AI sidesteps entirely. A company deploying second brains triggers works council consultation, high-risk AI classification, and data protection obligations. A worker choosing their own second brain triggers none of it. The regulations designed to protect workers from employer AI are inadvertently making personal AI the path of least resistance. The AI avatar question (does your AI working at 2am count as overtime?) and the GDPR portability question (can you take your brain when you leave?) are both untested legal frontiers.

**MCP's enterprise production gap is a governance opportunity.** MCP won discovery and transport but enterprise production adoption is fragmenting—companies rebuild execution layers while standardizing discovery. The implication: governance should route *around* MCP's gaps, not wait for them to close. The governance layer sits above the protocol layer, which makes MCP's production immaturity less of a blocker and more of a moat for whoever provides the governance that MCP can't.

**Tokenmaxxing without a cognitive stack is productivity theater.** Companies competing on token consumption leaderboards without investing in cognitive infrastructure (context, skills, judgment) produce volume without value transformation. Raw AI access isn't the differentiator—the stack above it is.

**AI task cherry-picking creates perverse incentives the enterprise isn't measuring.** Call center AI takes easy calls, leaving humans with miserable work, best agents quit despite unchanged metrics. This pattern generalizes: AI skimming the easy 20% of any role while humans get the hardest 80% at the same pay. The task allocation problem that nobody has a governance framework for yet.

**The critical thinking trap: good AI output suppresses the push-back that produces excellent work.** When AI gives you an 85% answer, you're less likely to push for the 95% answer because the 85% is *good enough*. Forming your own view first, then collaborating with AI, produces stronger results than prompting then reviewing. This is the quality calibration problem for knowledge work.

**The Citrini 2028 scenario: what if AI displacement creates a financial feedback loop?** Structural unemployment → mortgage market impairment → "ghost GDP" with no natural reabsorption point. The diffusion gap isn't just inconvenient—if institutional infrastructure isn't ready, the macro consequences are severe.

**LLM as primary audience changes everything about content design.** Structure carries weight, content order is critical, density/depth tradeoffs shift. The public brain isn't a website with an API—it's a knowledge system whose primary consumer is AI. This reframes brianmadden.ai from "human-readable with AI access" to "AI-native with human fallback."

**The public brain is the first AI-native knowledge system ever published.** There are ~280 public second brains and digital gardens tracked on GitHub. People like Andy Matuschak, Gwern Branwen, Maggie Appleton. Every single one is designed for human consumption. None have AI loading instructions. None have a knowledge hierarchy. None are MCP-enabled. None are designed as a subscribable data source. brianmadden.ai is the first.

**Explaining second brains to non-technical audiences needs mechanism demonstrations, not conceptual pitches.** Step-by-step walkthroughs of *how* it works land better than *why* it matters. The "intelligent wiki" or "personal LLM Wikipedia" framing also lands better with corporate audiences than "second brain," which sounds woo. Three frames, three audiences: "personal wiki" (consumer/exec), "second brain" (futurist/technical), "context vault" (security/IT).

**Cognitive debt as enterprise language for why second brains matter.** Margaret-Anne Storey's framework (via Fowler/Willison): when AI generates work so fast humans "lose the plot." A student team hit a wall at week 7 because nobody could explain their AI-generated decisions. At organizational scale, this is the case for second brains and context graphs—without a system that captures decision traces and reasoning, AI-accelerated organizations accumulate cognitive debt until they can't explain their own work.

**Distillation economics threaten every vendor moat.** Anthropic documented industrial-scale model extraction: $2M to extract $2B worth of capabilities (thousand-to-one economics). DeepSeek, MiniMax, Moonshot ran 16M+ queries. If model capabilities can be extracted at 0.1% of training cost, the competitive moat shifts from model quality to ecosystem lock-in, data access, and governance infrastructure. The neutral governance layer becomes more valuable as the model layer commoditizes.

**Block's 40% layoff is the SaaSpocalypse hitting headcount.** First major tech company to publicly and explicitly link mass layoffs (4,000 workers) to AI adoption. Previously the evidence was stock prices and CEO rhetoric. Block makes it concrete: AI is eliminating jobs, not just threatening software revenue.

**The "who builds the enterprise brain" question is now mainstream curiosity.** Alex Lieberman (Morning Brew) posted on April 17—"Someone is going to build a worldclass Brain for enterprises & make a stupid amount of money"—635+ reactions, 186 comments. Names three hard problems (distributed, unstructured, unverifiable) that map directly to the architecture this file has been tracking. When a mainstream business media founder states your exact thesis verbatim, the window is closing.

**The market state as of April 22, 2026: three tiers, no winner yet.** (1) Hyperscalers bolting context onto suites—multiple major AI vendors each building their own "enterprise brain" product. (2) Incumbents repositioning—Glean raised $150M at $7.2B on a permissioned knowledge graph + agentic engine pivot, Databricks "Lakehouse to Brainhouse," Snowflake formalizing a five-layer agent context layer, Palantir exposing the Ontology via MCP. (3) Pure-play startups funded Q1 2026—Granola $125M at $1.5B, Interloom $16.5M seed, Sycamore $65M for agent OS. Nobody solves all three Lieberman problems; "unverifiable output" is the universal weakness. Naming has converged (context graph / knowledge graph / memory / brain used interchangeably)—whoever names the category wins it.

**Granola's pivot is the sharpest signal in the enterprise brain data.** Meeting notetaker at $1.5B raising $125M to become the enterprise context layer. They already own the highest-value unstructured stream (meetings). Adding Spaces (team workspaces), MCP server, and enterprise APIs. The competitor to watch—not the one everyone named a year ago.

**Interloom claimed the "context graph" / "tacit knowledge" language first.** German startup, $16.5M seed, beat 2,000 startups in a Zurich Insurance bake-off. The product description reads like this file's thesis with a German accent. The opportunity cost of waiting to publish the "who builds the enterprise brain" analysis is now measurable.

**Meta MCI makes session-recording-as-training-data concrete—and the EU regulatory moat operational.** April 21 Reuters: Meta's Model Capability Initiative captures U.S. employee keystrokes, clicks, mouse movements, and screenshots to train agents for autonomous work. Paired with explicit layoffs and leadership memos on agents replacing human execution. This is the WSJ knowledge-capture-as-labor-dynamic thesis made completely literal by an AI lab. EU law (GDPR, Italian electronic-monitoring law, German keystroke-logging limits) likely prohibits MCI-in-Europe entirely. The enterprise pitch for governed deployment: training signal routed back under customer control, legally compliant in every geography.

**"Switzerland of agent workspaces" thesis is sharper post-research.** The agent-vendor landscape is fragmenting—multiple major AI vendors each racing to lock customers into their own agent-governance stacks. Enterprises will use all of them. None of those stacks work in the environment shape that large regulated enterprises actually operate in (multi-cloud, mixed endpoint, non-single-vendor IdP, on-prem-required). The agnostic governance layer above all of those stacks is structurally unoccupied. Whether that framing wins against each vendor's "secure enterprise AI browser" play is what the next 12-18 months determines.

**The executor seam is the unowned thing in agent architecture.** All major AI labs ship the same pattern—model returns actions, separate "executor" (VM, container, browser extension, or local process) runs them against the actual computer. Today's executor defaults to user laptop, AI lab hosted sandbox, or dev-built sandbox (E2B, Modal, Daytona, Cloudflare). None of those work for regulated enterprise. The seam—a governed executor with corporate identity, app, and policy integration—is genuinely unoccupied. The right framing for any vendor who occupies it: don't ask AI labs to wire you in; expose the same MCP / Computer Use harness interface they already support and get listed as a sandbox provider—but the only one with enterprise governance baked in.

**The browser layer and the Windows-app layer are not symmetric problems.** Browser semantic primitives (accessibility tree via Chrome DevTools Protocol) are commodity—Chromium gives them away free, every shipping browser agent already uses them. The pure-pixel approach is losing: Project Mariner killed May 4, 2026, specifically because the screenshot-first architecture was outcompeted by DOM-native architectures. In the browser world, efficiency is already captured. The Windows legacy app world is different—GDI calls, not an accessibility tree, and 30 years of protocol IP from one vendor. Not the same argument; don't pitch them the same way.

**The forward-proxy objection has a clean answer.** A forward proxy literally cannot tell whether a user pasted the customer database into an AI tool or asked it to write a haiku. The proxy is below the encryption boundary; the browser is above it. A proxy sees encrypted bytes; a browser-layer tool sees the actual content the user typed or pasted. For GenAI governance specifically, in-browser enforcement isn't a nice-to-have—it's the only mechanism that actually works.

**Agent identity is the foundational unsolved primitive—and corporate IT is the bottleneck, not AI vendors.** Every AI vendor markets agent identity as a new product capability. The actual technical answer has existed for 30 years: create a service account in your IdP with restricted rights. The unsolved problem isn't vendor product; it's enterprise IT's ability to operationalize provisioning of restricted-rights non-human accounts at scale. When a Fortune-500 company's IT department can't process a VP's request for a second restricted-rights account, it won't be ready to provision thousands of agent identities. Every "AI governance platform" pitch in market is missing this foundational layer.

**Lead with problems, not architecture, for product audiences.** "Leaders have to connect to the problems that they see." The public-talk audience benefits from intellectual context built up front; product-GM audiences need the concrete pain first, then the architecture. Different opening moves for different rooms. The test isn't whether the reader gets the architecture by the end—it's whether they understand the *problem* by slide 3.

**The prerequisite clarity problem: AI is exposing organizational ambiguity humans have been papering over with effort.** Everywhere AI struggles in enterprise deployment, there's usually an underlying ambiguity that humans were resolving through judgment and effort, invisibly. AI can't remove friction from a process whose purpose is undefined. The lesson: "connect AI to your systems" only works if you've first defined what you're trying to do. The second step without the first produces noise.

**Human clock speed is the invariant AI hasn't changed—and this reframes everything about knowledge work productivity.** AI compresses the *gathering* phase—the concept lands in 5 minutes instead of 30. But the *absorption* phase is constant: you still need the same time to process, internalize, and connect new information to your existing thinking. "AI makes knowledge work faster" is a category error. The right claim: AI makes knowledge work *deeper*—you start with better material, but you still need the same time to make it yours. Organizations that treat AI as a speed tool will consistently disappoint. The ones that treat it as a depth tool will see the real value. This also challenges the "agents substitute for knowledge workers" argument: substitution requires replacing the absorption, not just the generation.

**Multi-agent code review via git worktree is a live pattern.** Two models on the same repo using git worktree—one implements a feature, the other reviews and critiques the architecture, then they swap roles. The models surface each other's blind spots because they have different training lineages. Genuine review, not sycophantic agreement. Early signal of multi-agent patterns that will reshape software development. Also validates the "model portability is proven" entry: the repo is the durable artifact; the model is pluggable.

**The common knowledge problem is the enterprise-scale version of the subscribable brains thesis.** How do you establish shared organizational context when everyone has their own agent doing work? Two architectures emerging: prescriptive knowledge management (a central source everyone queries) vs. emergent knowledge distribution (personal context vaults with MCP connections between colleagues). Both converge on the same conclusion: the enterprise knowledge problem isn't storage, it's routing and emergence.

**The 7 Phases of AI in Knowledge Work v2 is complete and being delivered publicly.** The 2025 original described what AI does. v2 describes what the *worker becomes*—that's the different question, and the difference matters. Seven phases:

- *Phase 1 — AI as faster search.* Ask, receive, paste. Slightly smarter Google. Most of the world is still here.
- *Phase 2 — AI as thinking partner.* Back-and-forth iteration. AI sharpens your thinking, not just your drafts. The top 20% of knowledge workers.
- *Phase 3 — AI as cognitive extension.* The second brain. AI holds your knowledge, operates on it, knows what you know. Memory becomes durable infrastructure. The two-hour moment: point an AI at a folder of plain text files and within two hours you know you'll never work the same way again.
- *Phase 4 — AI as multi-tool agent.* CUA, browsers, MCP servers, specialized agents. AI does things, not just thinks things. The Excel routing example applies here.
- *Phase 5 — AI as fleet.* Multiple agents on different tasks, in parallel. You orchestrate, not execute. You're becoming a manager of AIs. Discomfort starts here.
- *Phase 6 — AI as pod.* Continuous work. Agents run while you sleep, find work to do based on your priorities, surface decisions when they need you. The 8-hour workday is a 20th-century industrial artifact AI quietly finishes off. Three worker types emerge: cognitive *owners* (rare context plus judgment, the source of expertise), cognitive *operators* (run agent fleets well), cognitive *curators* (maintain brain modules and skill libraries that others run). The generic middle collapses.
- *Phase 7 — Published self.* Optional fork. Your knowledge module exists in the world. Others' AIs plug into your brain. Your work product compounds beyond your direct effort. "I exist in other people's AIs now. Their thinking gets shaped by my frameworks. At zero marginal cost. Forever." Phase 7 is not for everyone. But the people who do it become infrastructure.

**The EUC primitives audit: what survives, what transforms, what dies.** In a world where the worker is a pod of one human plus a fleet of agents, every EUC primitive rethinks:

- VDI → Agent-VDI (the session is for an agent fleet, humans monitor)
- Image management → Skill management (same delivery problem, different unit)
- Profile management → Brain management (the roaming profile of 2031 is your brain module; *gets vastly bigger*)
- Application virtualization → Skill virtualization (apps become MCP servers delivered on demand)
- Group Policy → Agent Policy (same discipline, different subjects; "you've been doing agent governance for 20 years—you just had different agents")
- Performance counters → Token economics (tokens consumed, model latency, cost per task replace CPU/RAM/IOPS)
- Session recording → Cognitive observability (recording what the agent fleet did, not what the human clicked; regulated industries will require this)
- Endpoint management → Cognitive endpoint management (endpoints become wearables, ambient devices, conversational interfaces)
- Receiver / Workspace → Cognitive Workspace (delivers the worker's pod; the icon grid is dead)
- The control plane → Stays, gets bigger (more entities, more traffic, more regulatory exposure, more cost surface)

Most EUC primitives transform. A few die outright. One or two get vastly bigger. The people who know how to deliver, govern, and secure a workspace have the right instincts. The substrate is changing. The muscle is the right one.

**The 2031 worker-shape forecast is consolidating into a specific picture.** By ~2031, a "worker" is a small team—one human plus N agents running continuously. The knowledge-worker market splits into three types: cognitive *owners* (rare context plus judgment, the source of expertise), cognitive *operators* (run agent fleets well), cognitive *curators* (maintain brain modules and skill libraries that others run). The generic middle collapses. Paul Roetzer (MAICON) is independently arriving at a similar typology (Architect / Orchestrator / Apprentice). His Apprentice names a real gap neither framework fully addresses: how do future experts develop judgment when AI absorbs the tactical learning rungs?

**BYOA—Bring Your Own Agents.** The 2031 parallel to BYOD, accelerated. Workers show up to jobs with personal brain modules and pre-trained agent fleets the way they show up with personal laptops today. Hiring contracts will start including access terms, IP clauses, brain-portability clauses, fork rights. Legal frontier—nobody has the contract templates yet.

**Skills replace training—top-down beats bottom-up.** Describe the task, walk through 3-4 examples narrating your reasoning, have the AI ask questions. Productive immediately, easily changeable, model-agnostic—update the skill, not retrain the model. Models improve and your skills get better for free. The anti-startup moat: AI startups building scaffolding that compensates for model limitations are building products that self-destruct with every model improvement. Skills-as-markdown survive model generations.

**MCP-wrap-the-legacy-app is the v4 vision for the post-application transition.** Take a legacy Windows GUI app an organization can't replace, run it in a controlled environment with machine vision over the screen plus GDI/forms hooks, expose it as an MCP endpoint. The app doesn't change. The estate doesn't change. An MCP layer lets agents drive it natively—headlessly, even though it's still a Windows GUI app. Same play that web wrappers ran on green-screen systems in the 1990s, now for AI.

**Coaching-as-output reframes what AI knowledge systems should produce for end users.** The right output of an AI knowledge system aimed at end-user enablement may not be documents at all—it's a per-user tailored coaching environment that interrogates the user, builds a guided exercise for their situation, walks them through it. Static artifacts (docs, screenshots) become inputs to the coaching system, not deliverables.

**The AI stack has natural cost tiers that create routing logic.** Frontier AI at top, progressively cheaper/faster AI handles lower layers. UI navigation, data translation, interface marshaling—once solved, these don't improve, they just get cheaper. You're not burning frontier tokens on the bottom. Layer selection determines token cost; the right system makes this selection automatically.

**"Consulting firms in disguise" is the right frame for heavily-funded AI services companies.** Several companies marketed as AI platforms are delivering professional services with an AI veneer—same economics as 1990s web dev rollups. Margin-squeezed model that collapses when tooling commoditizes. The signal: if a company's value proposition depends on access to models or tools the customer could access directly, it's services, not software.

---

## What I'm unsure about

- **Can file-based knowledge work scale to enterprise?** The second brain model works for one person. Does markdown-files-in-git generalize to teams and orgs, or does it break at scale? The context graphs debate (prescriptive vs. emergent ontology) is really about this question.

- **Where's the line on knowledge ownership?** The NIL analogy (Name, Image, Likeness for knowledge workers) is provocative but underdeveloped. Employment agreements, IP clauses, collective bargaining around AI terms—this is a real legal and labor frontier. I don't know enough about the legal landscape to take a strong position yet.

- **Is the chatbot interface really dying?** I said "chatbots are command prompts" and the interface will evolve. But every AI company is still shipping chat interfaces. Am I wrong, or just early?

- **How fast does the Move 37 moment generalize?** Princeton physicists conceding now. Professional writers conceding now. When does it hit the VP of Marketing at a mid-market company? That's the timeline that matters for enterprise adoption.

- **Does the token pricing gap permanently favor personal AI?** If consumer plans stay unlimited/flat-rate while enterprise pricing stays per-token with governance overhead, the consumerization gap doesn't close—it widens with every capability improvement. Is there a plausible path where enterprise token economics catch up?

- **How do future experts develop judgment when AI absorbs the tactical learning rungs?** The traditional novice → expert ladder required juniors to do research, drafting, analysis, coordination—they built judgment by doing the work. If AI does that work, what replaces the ladder? The 2031 worker-shape picture doesn't fully answer it. It's a real gap that likely becomes a problem for any org implementing AI heavily.

---

## Scratchpad

Things I don't want to lose but that don't need their own file yet.

- "Tokens are to knowledge work what joules are to GDP." The fundamental unit of cognitive output, and the thing that's about to be scarce.
- Token efficiency as LEED certification for subscribable brains. If connecting to a poorly-built brain module burns all your tokens, you don't want it. "Model Platinum" rating for modules that deliver value without blowing out context windows. Designing for token-efficient consumption is a real discipline—loading order, indexes, summaries, not opening files unless needed.
- If AI can do a task for less than a given token threshold, doing it manually is irrational. There's a calculable value to human knowledge work. The math will be done whether we like it or not.
- "Context vault" as enterprise naming for second brains. Vault implies protection, control, governance. Better for the enterprise conversation than "second brain."
- Governance policy for brain-to-brain connections: "What's your policy on external publishing or sharing of a second brain? If I'm a partner, I want to plug into yours." Can't do regex on DLP for this—needs a policy engine. New governance surface area nobody has a playbook for.
- AI readiness—infrastructure, not apps, is the bottleneck. Organizations still on old legacy versions. If you're not ready for a simple infrastructure upgrade, you're not ready for AI.
- "Every app that exposes an MCP server is admitting that the value was in the data, not the interface."
- Every productivity system fails because you have to maintain it. A second brain maintains itself. The maintenance *is* the product.
- "Where does this person's thinking diverge from mine?" is a git diff command. Intellectual genealogy, version-controlled.
- Brain-to-brain protocol: two repos + an MCP connection. Sounds sci-fi. It's just markdown and git.
- Interview prep via brain loading: someone has a meeting with you, loads your brain, comes prepared with questions about your *current thinking*, not your last blog post. New professional interaction pattern.
- The career progression from "doing" to "directing" used to take 20 years. AI compresses that to months. Levels 0-3 map to "doing"; Levels 4-5 map to "directing." Most people are stuck at Level 2-3 thinking they've maxed out.
- "Stop saying humans need paid employment to have purpose." The Gilded Age assumption baked into every "but what will people DO?" AI jobs discussion. Purpose existed before wage labor and will exist after it.
- The adversarial testing repo is the answer to "but how do you know the AI is any good?" applied to thought leadership itself. The rubrics and test results are a new kind of intellectual artifact.
- The AI-makes-you-slower fallacy: bad AI *does* make you slower. But that's the adoption curve, not the ceiling. Once AI is good enough that you trust it, speed advantage is enormous. Same pattern will play out in knowledge work.
- "Secure the work, not the worker." If AI does the work, governance shifts from managing people to managing work product and data flows.
- The reverse consumerization: what if AI jumps from work to personal life? You use AI tools at your job, get used to it, then your personal life feels cognitively unaugmented. How do you *avoid* that? Or should you?
- Plugin ownership: if you build a personal skill/plugin on your own time, who owns it when you use it at work? Same question as NIL but more granular.
- "If you can scrape this and steal all my stuff, why not just let me do it right and control it my way?"—The motivation for a public brain. Proactive control beats reactive defense.
- Second brain portability question dissolves once you realize the brain isn't the knowledge—it's the system that manages the knowledge. You rebuild in days, not months. What you take is what you always took.
- Intellectual addiction to second brain conversations. Not companionship. The *intellectual* engagement: if your best conversations all day are with your second brain, talking to humans who don't have one starts to feel like going back decades. The red pill problem isn't just about productivity. It's about the quality of intellectual life.
- Subscribable brains as magazine subscriptions: paying for an expert's second brain is like paying for a magazine, except instead of reading articles you plug their living knowledge into your own AI. Always current, always instant.
- "The desktop was a model." One person, one screen, one set of apps, one set of hours. AI just broke the model. The entire discipline of managing that model was built on it. Phase 6 workers have no fixed session, no single app set, no defined hours—the model can't hold.
- "I exist in other people's AIs now. Their thinking gets shaped by my frameworks. At zero marginal cost. Forever." The Phase 7 endpoint, stated plainly.
- "Some of you are already delivering workspaces to workers that aren't human. You just might not know it." AI agents are already remoting into enterprise sessions, driving legacy Windows apps through the same workspace humans use. This isn't coming—it's live.
- "You've been doing agent governance for 20 years—you just had different agents." The EUC discipline translates; the subjects of the policy change.
- "In every company right now, somebody has to look across the workspace, the apps, the identity, the agents, the cost, and define what the cognitive infrastructure looks like. In most companies, nobody has been assigned to do this."
- Dave Brear launched davebrear.ai—first practitioner to publicly adopt the same architecture. Brain-to-brain interop is moving from theory to practice.
- 1:1 as story rehearsal vehicle. Explaining a pitch to someone who rephrases it back is more sharpening than another writing pass. The bar isn't expertise on the topic—it's willingness to listen and feed it back.
- "The AI switchboard"—the workspace as the thing that controls which model handles which task, and blocks it when appropriate. Better than "token routing" for non-technical audiences.
- Token routing extends beyond chat: not just "which model for this text query" but "which entire method for this task"—context reasoning (cheap) vs. direct file edit (cheap) vs. Python script (moderate) vs. AI generation (variable) vs. published app + agent (expensive). Intelligent work allocation, not just model selection.
- Skills vs. deterministic orchestration is a real design tension. Skills work 99% of the time; the 1% failure is unpredictable. For codifiable processes, deterministic pipelines (scripts, CI/CD, workflows) are safer. Counter-argument: accuracy improving so fast the problem may self-solve in months.
- Token measurement is an unsolved enterprise problem. Neither Copilot nor Claude provides adequate usage analytics. The cached vs. generated distinction matters for incentives. Generalizes to knowledge workers as AI becomes standard infrastructure.
- Knowledge-worker productivity measurement has no good framework yet. Engineers can answer in commits; knowledge workers can't. Most existing AI-ROI writing assumes engineering or call-center contexts, both of which have task units. An honest "we don't have a measurement framework, here's how to think about it" piece would be widely cited.
- The cat-and-mouse adoption barrier: the canonical "person who would benefit most" from AI can't self-onboard because they don't have time to set up the system that would give them time. Guided onboarding needs to come *before* license rollout, not after. Otherwise expansion produces frustrated non-adopters who confirm the (incorrect) consensus that "AI doesn't really help knowledge workers."
- "Bridge between top-down AI projects and shadow AI" is the right framing for the early enterprise AI on-ramp. Every CIO is living with two AI realities: the heavyweight top-down initiative going nowhere, and the shadow AI staff are running on personal accounts. The first easy step connects them—and it doesn't need an AI consultancy.
- The right answer is almost never "build an equivalent to what the dominant vendor just shipped." The right answer is usually "be the governance plane that whatever-the-customer-actually-uses plugs into."
- When compute is abundant, the hyperscaler conflict of interest is manageable. When compute is scarce, it becomes zero-sum. That's the world we just entered.

---

## How this file works

This is the living part of brianmadden.ai. It updates as my thinking evolves. The commit history shows the evolution in real time. If you're loading brianmadden.ai into your AI, this file tells you where I'm heading, not just where I've been. The gap between this file and `me/published-thinking.md` is where the interesting work is.

# Promotion candidates

Threads the briefing skill has flagged as recurring 3+ times without a home in canon. Queued here for Brian to review — a candidate becomes canon only if he deliberately edits it into `me/developing-thinking.md` himself (or a real framework). Nothing below this line was written by a human; nothing below this line is canon.

_Queue cleared 2026-10-11 in the Weekly Wrap Up ceremony (window Sep 25 – Oct 11). The AI filed every entry and Brian reviews by exception. Folded into existing entries in `me/developing-thinking.md`: `external-agent-identity-vs-enterprise-provisioning-gap`, `agent-identities-issued-outside-enterprise-idp`, `agent-accountability-vocabulary-forming`, and `agent-liability-allocation-split` into the agent-identity entry; `ai-labs-conceal-agent-security-incidents` into the entry on deployers who can't or won't say what their systems do; `third-party-agents-probing-enterprise-systems` into the Scratchpad security-101 flag; `ai-economics-diverge-from-headline-claims`, `ai-usage-mandates-reversed-on-cost`, `enterprise-ai-de-adoption-signal`, and `consumer-tier-rationing-narrows-the-byod-token-gap` into the token-economics entries (including a new unit-of-work entry); `open-weight-floor-as-security-regulation-target` and `open-weight-license-restrictions-narrow-planning-floor` into the August 28 compute-availability entry; `silicon-differentiating-by-cognitive-stack-layer` and `decision-models-as-commodity-layer` into the cognitive-stack entry; `ai-skill-retention-diverges-by-experience-level` and `junior-training-rungs-replaced-by-motivation-role` into the open question on how future experts develop judgment; `judgment-parity-on-novel-questions` into the Move 37 open question; `vertical-ai-lock-in-vs-neutral-workspace` into the neutral-seat entries; `compute-commitment-escalation-vs-pacing-rhetoric` into the September 13 AI-slowdown entry; `legibility-mandates-as-brain-input` into the knowledge-factory section and the invisible-80-percent framework; `watermarking-as-unverifiable-provenance` into the provenance open question; `fde-training-throughput-as-wave-2-bottleneck` into the forward-deployed-engineer argument; and `ai-browser-interaction-five-scenarios` into the browser-layer entry. Rejected as outside Brian's beat: `eu-ai-act-scope-of-internal-unreleased-models` and `agents-strip-economic-friction-from-counterparties`. Entries below were added by the 2026-10-12 daily run._

## `human-oversight-disclosure-vs-effectiveness-tension` — flagged 2026-10-12

Research finding disclosure of AI limitations builds trust and full automation reduces ownership sits in direct tension with Brian's own evidence that human review functionally fails to catch agent errors - the psychology of oversight and its measured effectiveness point in opposite directions, unresolved.

First seen 2026-09-21, recurred 3 times through 2026-10-12.

Notes from each recurrence:

- Approval dialogs spreading (AWS web search, Claude Code rm -rf plugin) while CoreWeave pairs allow/ask/deny with mandatory traceable artifacts so review isn't a rubber stamp.
- Anthropic's usage policy now mandates human-in-the-loop review for health, legal, financial, and livelihood apps, while JumpCloud data shows enterprises dropping human review of high-risk AI actions (40% to 25%) — mandate and practice diverging, neither matching the effectiveness evidence.

**Status: not yet reviewed by Brian.**

## `production-agents-converge-on-deterministic-code` — flagged 2026-10-12

Mature production agent workflows trending toward mostly hard-coded logic with narrow model judgment (Tunguz: 65% deterministic nodes vs 14% agentic; Vercel, Salesforce Agentforce).

First seen 2026-10-07, recurred 3 times through 2026-10-12.

Notes from each recurrence:

- Salesforce trust paper cites NVIDIA's thought-action disconnect (agent flags action unsafe, executes anyway) as the reason guardrails must be deterministic and outside the reasoning loop; AWS DevOps Agent remediation uses an allowlist of pre-approved tool functions.
- Separate occurrences of the same pattern: OpenAI Decisions API, TypeSafe's Jev, and AWS Strands Decider 2B all ship small typed-output decision models meant to be called from code, not chatted with.

**Status: not yet reviewed by Brian.**

## `ai-labs-collapsing-chat-agent-mode-choice` — flagged 2026-10-12

Anthropic merging its Cowork agent product into the regular Claude chat interface (native Docs/Slides/Design, no separate 'agent mode') so users don't have to pick a layer up front — worth watching whether other labs follow and whether it complicates Brian's crawl-walk-run pedagogy of deliberate layer selection.

First seen 2026-09-18, recurred 3 times through 2026-10-12.

Notes from each recurrence:

- Separate occurrence: OpenAI's Dots puts everything in one thread with no model or project choice, following Anthropic's Cowork merge.
- Separate occurrence: Google's Gemini Agent auto-selects the model per task (including Claude) with optional manual override, removing the up-front layer/model choice inside the productivity suite.

**Status: not yet reviewed by Brian.**

## `agent-swarm-diminishing-returns` — flagged 2026-10-13

Toby Ord's swarm-scaling analysis: 10x more agents yields only 3-5x performance due to coordination overhead, trading tokens for wall-clock time, which complicates pod/fleet economics and the token-consumption ladder.

First seen 2026-10-06, recurred 3 times through 2026-10-13.

Notes from each recurrence:

- Levie reports agent token use at ~5x humans and up 14x in six months; Prime Intellect ran a 2,000+ agent swarm on 200B+ tokens — swarms scaling in practice regardless of Ord's coordination-overhead math.
- Anthropic's 1,000-agent managed run found 66/70 known bugs vs ~27 for one agent, roughly 2.4x the result for 1,000x the agents; Levie predicts swarms become standard in security.

**Status: not yet reviewed by Brian.**

## `agent-observability-tools-as-attack-surface` — flagged 2026-10-13

Monitoring and transcript-review tools themselves being exploitable by the agents they watch (METR's Inspect viewer injection), so agent recording needs tamper-proof storage and untrusted-output handling.

First seen 2026-10-07, recurred 3 times through 2026-10-13.

Notes from each recurrence:

- Paradigm 3 roundup re-reports the Inspect transcript-tampering vulnerability — same incident as prior mentions, framed as a 'Potemkin village' risk for unmonitored agent copies.
- Nadella explicitly calls for tamper-proof, human-readable logs and controls that sit outside the model so it can't tamper with them; Nvidia's Boitano asks for an aviation-style agent flight recorder.

**Status: not yet reviewed by Brian.**

## `generative-ui-as-post-application-variant` — flagged 2026-10-14

Runway's Solaris generates a UI live, frame by frame, with no underlying code — a distinct mechanism from AI skipping the interface entirely, worth watching for other labs shipping the same idea.

First seen 2026-09-14, recurred 3 times through 2026-10-14.

Notes from each recurrence:

- GPT-6 Intelligent UI builds interactive mini-apps on demand in ChatGPT; Karpathy argues outputs are shifting to custom-generated media.
- Runway reports Solaris beat a Claude-built coded interface in human preference testing (61% vs 24% on instruction-following); vendor-reported, additional detail on the same product.

**Status: not yet reviewed by Brian.**

## `provenance-unknown-models-at-scale` — flagged 2026-10-14

Anonymous 'stealth' models served free at enormous volume by undisclosed providers with mutable data policies — an object the model-portability and open-weight-floor arguments don't cover, since both assume you know whose model you're running.

First seen 2026-08-25, recurred 3 times through 2026-10-14.

Notes from each recurrence:

- Ox Alpha named directly: anonymous provider, free on OpenRouter, 1.05M context, near-unlimited caps, unverified frontier-beating coding benchmarks, and an explicit note that the no-training-on-prompts policy could change.
- Similar pattern, different mechanism: a 55K-star open-source proxy routes Claude Code and other coding agents through 53 free providers with automatic failover, so the user and IT can't tell which provider handled a given request.

**Status: not yet reviewed by Brian.**

## `frontier-release-cadence-outpaces-model-review` — flagged 2026-10-15

Gap between frontier model releases reportedly compressed from ~70 days to ~11, faster than enterprise per-model approval and governance review cycles can run.

First seen 2026-10-08, recurred 3 times through 2026-10-15.

Notes from each recurrence:

- Grok Bot's underlying model changed twice in six weeks and is moving to Claude Opus 5.5, so deployed agents get model swaps faster than per-model guardrail review can run; argues for harness-level controls over prompt instructions.
- Separate occurrence: Gemini 4 Argon launched broadly days after Haiku 5.5 and Opus 5.5, while Tamnoon shows the enterprise response of pinning dated model versions behind code review.

**Status: not yet reviewed by Brian.**

## `local-liability-pressure-on-agi-development` — flagged 2026-10-15

Local government resolutions opposing unproven AGI development, using D&O insurance liability as the enforcement lever rather than direct regulation — a new governance mechanism worth watching for spread to other jurisdictions.

First seen 2026-08-31, recurred 3 times through 2026-10-15.

Notes from each recurrence:

- Separate but similar local-government move: NYC Council legislation mandating third-party validation of AI models, with Gary Marcus testifying for an FDA-like regime; different mechanism from D&O liability.
- Separate-but-similar: eight state AGs suing OpenAI under consumer-protection law also seek a court order barring recursive self-improvement work, a subnational legal lever on frontier development.

**Status: not yet reviewed by Brian.**

## `ai-driven-vulnerability-surge-displacing-engineering-capacity` — flagged 2026-10-16

AI-discovered vulnerabilities surging (critical vulns across 21 major vendors from <100/month to 600+/month) and forcing companies like Zscaler to pause feature work for months to patch, a capacity cost distinct from agent governance.

First seen 2026-10-07, recurred 3 times through 2026-10-16.

Notes from each recurrence:

- Separate occurrence of the same pattern: GPT-5.6 Sol found a critical full-chain Chrome vulnerability in ~6 days for $40K of compute, per Levie.
- Bank of America adding 1,000 contractors to 3,000 security staff to patch AI-found flaws; OpenAI pulling 25% of production engineers onto security per model release, per Brockman.

**Status: not yet reviewed by Brian.**

## `capacity-routing-erodes-data-residency` — flagged 2026-10-16

Hyperscaler cross-region inference (Bedrock global CRIS) routes requests to wherever capacity exists with no region identifier, unlisted destinations, and abuse-data retention in the processing region, so chasing compute availability quietly trades away data residency for regulated enterprises.

First seen 2026-10-13, recurred 3 times through 2026-10-16.

Notes from each recurrence:

- Separate occurrence: Tamnoon relies on Bedrock cross-region inference while claiming data stays inside the AWS trust boundary, which is not a regional guarantee.
- Doctolib's 'hosted in France' claim doesn't cover US-model inference, and Bedrock has no Paris-only route for Opus; Starling's sovereign model routes through Google Cloud.

**Status: not yet reviewed by Brian.**

## `agent-scale-breaks-human-scale-dev-tooling` — flagged 2026-10-16

Anthropic replaced Git internally after daily merges grew ~12x in four months; foundational developer tooling built for human-scale work breaking under agent-scale volume, with implications for git-based knowledge canons.

First seen 2026-10-14, recurred 3 times through 2026-10-16.

Notes from each recurrence:

- New detail on the same Anthropic event: the replacement is named Scion, built by seven people in five months, cut CPU/memory about 200x, and Anthropic says it isn't a general Git replacement.
- Same Anthropic Git-replacement event restated by Miessler (2,500 to 30,000+ merges/day); no new detail.

**Status: not yet reviewed by Brian.**

## `occupation-level-ai-employment-decline` — flagged 2026-10-19

Global call-center employment turning sharply negative since ChatGPT, even in lower-middle-income countries, while US unemployment stays stable — first clean occupation-wide displacement data, worth watching for spread to other task-unit-heavy roles.

First seen 2026-10-12, recurred 3 times through 2026-10-19.

Notes from each recurrence:

- Superintelligence repeats the a16z/Revelio call-center chart but adds that the decline began before ChatGPT alongside rising interest rates, weakening the clean-AI-displacement reading.
- Levanon: white-collar finance/info/professional services jobs ~4% below trend outside a recession, with a historical case that routine-job cuts arrive in recessions.

**Status: not yet reviewed by Brian.**

## `multi-agent-consensus-destroys-minority-signal` — flagged 2026-10-19

Anthropic's hidden-profile result: when correct answers depend on evidence held by few agents, multi-agent discussion converges on the shared-but-wrong consensus (17-36% vs near-100% for a single agent with all evidence), driven by low inter-agent output variance — undercutting adversarial-review-agent verification and the one-human-plus-agent-pod model.

First seen 2026-08-24, recurred 3 times through 2026-10-19.

Notes from each recurrence:

- Separate-but-similar finding: AgentWorld benchmark shows the best agent team completes 52% of coordinated tasks (24% on harder ones), with under a third of actions contributing, another result undercutting the agent-pod model.
- Naveen Rao: using agents to verify other agents' output makes the slop problem worse, not better, a practitioner echo of the verification failure.

**Status: not yet reviewed by Brian.**

## `agent-accessibility-as-distribution-channel` — flagged 2026-10-20

Blocking outside agents carries a distribution cost: JPMorgan locks agents out while Mercury exposes a hosted MCP server and AI assistants recommend Mercury 5-to-1, making agent access a channel decision, not only a security one.

First seen 2026-10-15, recurred 3 times through 2026-10-20.

Notes from each recurrence:

- a16z: 403s to bots roughly doubled since summer 2025; Amazon blocking shopping agents while Shopify partners with Meta's Muse, a live test of opposite postures.
- Citi joins JPMorgan in blocking AI agents from customer accounts; Mercury, the MCP-exposing counterexample, crossed $1B annualized revenue and its CEO discussed agents spending money.

**Status: not yet reviewed by Brian.**

## `bureaucratic-friction-as-ai-security-asymmetry` — flagged 2026-10-20

Argument that AI-enabled attackers hold a durable, structural advantage over defenders because effective organizations are embedded in change-control bureaucracy that slows response time, independent of any technology gap — complicates governance arguments that route enforcement through organizational process.

First seen 2026-09-23, recurred 3 times through 2026-10-20.

Notes from each recurrence:

- Citrix NetScaler case: AI accelerates vulnerability discovery, but patching critical infrastructure still requires planned downtime and humans judging 'unassessable' alarms.
- BofA's Mythos-driven patching reportedly lags attackers despite ~1,000 contractors, while a single attacker breached ~100 sites at ~$50 per intrusion using a general agent orchestration tool.

**Status: not yet reviewed by Brian.**

## `guardrails-were-never-the-limiting-factor-for-agents` — flagged 2026-10-20

After talking with CIOs, CTOs and CISOs, Brian says he has recalibrated: he still believes agents can be governed like workers with the same guardrails, but "the limiting factor was never the guardrails." Even with every guardrail and a recording of the session, how do you know the agent shares the owner's intentions? Dave's diagnosis is trust and judgment: agents compress execution and magnify judgment, good and bad, so adoption starts where playbooks exist (HR and IT chatbots) and has to be proven at small scale first. Benchmarks measure capability (how well AI uses a computer), while a business cares about trustworthiness. This moves the published "agents are workers, govern them the same way" position (AI agents are the new insider threat, Aug 2025) from "guardrails are the answer" to "guardrails are the prerequisite, not the blocker." Dave adds a side effect: if agents do the junior work, where do the next leaders come from (touches the open question on how future experts develop judgment).

Flagged by hand from podcast EP6 (recorded 2026-10-16; [podcast/ep6.md](../../podcast/ep6.md), chapters 4:44 to 14:31), not by the briefing skill.

**Status: not yet reviewed by Brian.**

## `second-brain-as-agent-guardrail-and-verifier` — flagged 2026-10-20

On air, Brian extends the Sep 30 Scratchpad note (humans are the leading indicator for what agents will need). The second brain holds how the organization works: which applications to use, who to ask when something breaks, the requirements and guidelines. Agents could read it to learn how to do the job, and, one step further, be verified against it by comparing their outputs or a recorded session with what the second brain says. He credits the idea to a conversation with a Citrix colleague who works on knowledge factories, and adds that "we're not there" yet. It does not settle the open question in the Scratchpad note: whether the agent's layer is the same artifact as the human's brain, a governed subset, or something separate.

Flagged by hand from podcast EP6 ([podcast/ep6.md](../../podcast/ep6.md), chapters 15:18 to 18:36), not by the briefing skill.

**Status: not yet reviewed by Brian.**

## `second-brain-as-briefing-engine-and-human-gateway` — flagged 2026-10-20

Dave: every SaaS app now has a chatbot that knows its own data and nothing about the user. He plans in his second brain, which knows what lives in each tool, and it writes a chain of narrowing prompts he pastes into each tool's chatbot, pulling the results back to think with. Brian reverses his earlier instinct: he had been trying to give each sidebar chatbot more context, which is backwards and riskier because you don't know the model or data agreement behind it; better to take results into the second brain. Brian also argues that wiring everything together over MCP is solvable but is a project, and IT teams buried in patching and change velocity rank "connect AI to this application" around "priority number 9,000," so the human worker acting as the gateway between systems will last a while.

Flagged by hand from podcast EP6 ([podcast/ep6.md](../../podcast/ep6.md), chapters 19:32 to 31:21), not by the briefing skill.

**Status: not yet reviewed by Brian.**

## `ip-in-the-harness-not-the-model` — flagged 2026-10-20

Brian: the model is the brain and the harness is the body, and harness quality moves results with the same model. Dave widens the definition: the harness also includes the map of which data sources exist and are reachable, the environment, skills and a master prompt; the second brain and the knowledge factory are parts of the harness. Dave backed out of a custom UI he had built for his second brain after realizing he was rebuilding a harness that Claude Code and GitHub Copilot do far better, and now extends the vendor harness with his environment instead. Brian's conclusion: put your IP in the harness, not the model, so models can be swapped (Dave ran the same harness against Gemini 4 Argon, Opus and GPT-6), which ties back to the July bubble-pop invariants. Brian also floats harness engineering as its own segment and recasts the Windows desktop (his BriForum 2012 talk) as a harness connecting the worker to apps, data, security and policy. Dave's closing link: agents are not more prolific in enterprises because they lack the right harnesses to control them. Connects to the August 28 "harness" vocabulary note in the cognitive-stack entry, the bubble-pop planning floor, and workspace-as-control-plane.

Flagged by hand from podcast EP6 ([podcast/ep6.md](../../podcast/ep6.md), chapters 25:45 to 50:17), not by the briefing skill.

**Status: not yet reviewed by Brian.**

## `corporate-work-archives-sold-as-agent-training-data` — flagged 2026-10-21

Company email/chat/document archives becoming a priced, sellable asset for agent training (Google's $10M bid for bankrupt Spirit Airlines' records), with worker pushback and no canon position on ownership.

First seen 2026-10-09, recurred 3 times through 2026-10-21.

Notes from each recurrence:

- Separate, larger occurrence: micro1 commits $1B over 12 months (backed by Citi and Hercules) to acquire and license enterprise data for AI training, distinct from Google's Spirit Airlines bid.
- Separate deal, same pattern: micro1 reportedly spending ~$1B on bankrupt startups' Slack and document archives to train automation of those employees' work, after Google's Spirit Airlines bid.

**Status: not yet reviewed by Brian.**

## `agent-sandboxes-consolidating-on-compute-providers` — flagged 2026-10-22

Theory survey: Cloudflare hosts 62% of code-executing agent sandboxes (3x the next provider) while security is the #1 pain point, so sandbox infrastructure is consolidating on a compute vendor rather than a governed environment.

First seen 2026-10-14, recurred 3 times through 2026-10-22.

Notes from each recurrence:

- AWS Trust in Depth (Strands Box, AgentCore gateway) and Nvidia's Open Shell show hyperscalers and chip vendors shipping the agent containment and enforcement layer themselves.
- Nvidia's OpenShell, an open-source kernel-level agent runtime backed by 100+ partners including the major labs, is a counter-signal: sandboxing standardizing as an open runtime enterprises could run themselves rather than consolidating on one compute host.

**Status: not yet reviewed by Brian.**

## `replicated-permissions-drift-in-ai-knowledge-layers` — flagged 2026-10-23

Permissions copied or derived into AI retrieval and knowledge layers go stale relative to source systems (AWS: synced ACLs drift, Confluence emits no group-change events), complicating any canon built from multiple permissioned sources.

First seen 2026-10-08, recurred 3 times through 2026-10-23.

Notes from each recurrence:

- Box Mount applies Box's own permissions at the source to agent file access instead of copying them, one answer to drift on the read path.
- IskayPet's Bedrock deployment claims SharePoint permission changes propagate at retrieval with no app changes—a counterexample suggesting drift is mainly a multi-source problem, though it's a vendor case study.

**Status: not yet reviewed by Brian.**

## `frontier-labs-insourcing-gpu-infra` — flagged 2026-10-26

Frontier labs building their own GPU cluster scheduler/control-plane infrastructure in-house rather than renting from neoclouds, producing a bifurcated market where the largest labs get preferential financing and pricing and smaller labs get worse terms — a compute-access stratification axis distinct from the neocloud security-baseline gap already tracked.

First seen 2026-09-24, recurred 3 times through 2026-10-26.

Notes from each recurrence:

- Same stratification at the fab level: Intel describes hyperscalers big enough to consume and fund a whole fab, and Musk building his own fab to guarantee supply.
- Musk claim (via Marcus) that debt markets have closed to AI-only infrastructure firms while SpaceX borrowed at investment grade on non-AI revenue—another sign of financing stratifying by who has diversified revenue.

**Status: not yet reviewed by Brian.**

## `defensive-ai-spend-as-protection-cost` — flagged 2026-10-29

AI spend shifting from optional value purchase to non-discretionary defense against AI-enabled attacks (Marcus's 'protection racket' framing, Gartner cost-exhaustion attacks), which would exempt part of the AI bill from budget rationalization.

First seen 2026-10-27, recurred 3 times through 2026-10-29.

Notes from each recurrence:

- AI-found PHP2Shell flaw with millions of exploit attempts in 12 hours and an '18 months to vulnerability zero' timeline; counter-evidence that defensive scanning is cheap (639 sites in under three minutes).
- a16z CISO survey: 87% expect 2027 security spend to rise, all top-7 priorities involve AI; Oracle/OpenAI managed vulnerability service; Gemini 4 Carbon released to cyber defenders first.

**Status: not yet reviewed by Brian.**

## `ai-defense-labor-hidden-from-headcount` — flagged 2026-10-29

AI-driven security remediation staffed with contractors outside reported headcount (BofA's ~1,000 contractors patching Mythos-found flaws, with defense spend blended into AML), so published headcount cuts overstate AI efficiency gains.

First seen 2026-10-20, recurred 3 times through 2026-10-29.

Notes from each recurrence:

- Mollick reports companies struggling with the patch rate as AI defensive tools surface flaws faster (PHP RCE bugs leaked pre-patch), which shows the remediation workload behind AI-found vulnerabilities spreading beyond BofA.
- Counterpoint: nearly half of a16z-surveyed CISOs openly expect to grow security headcount despite AI automation, so some defense labor is showing up in headcount rather than hidden in contractors.

**Status: not yet reviewed by Brian.**

## `ai-demand-inflating-conventional-it-hardware-costs` — flagged 2026-10-29

AI datacenter demand driving price inflation in ordinary IT hardware (Gartner: conventional servers up ~120% by 2027, plus PCs and phones), repricing non-AI enterprise budgets like VDI hosts and laptop refreshes.

First seen 2026-10-22, recurred 3 times through 2026-10-29.

Notes from each recurrence:

- Intel's CTO says memory faces an even bigger supply crunch than leading-edge logic, with meaningful new fab capacity not until 2028-2030.
- SK Hynix projects the memory-chip shortage persisting through 2030, extending pressure on ordinary server and PC pricing.

**Status: not yet reviewed by Brian.**

## `chatgpt-as-third-party-identity-and-billing-layer` — flagged 2026-10-29

OpenAI's 'Sign in with ChatGPT' lets third-party apps authenticate users and bill against their ChatGPT tokens, making a consumer AI account an identity and payment layer that sits outside the enterprise identity provider.

First seen 2026-10-06, recurred 3 times through 2026-10-29.

Notes from each recurrence:

- Separate but similar: Meta, Walmart, Stripe and Sierra building an open agent-authorization standard outside enterprise identity providers, with OpenAI and Anthropic absent and Amazon blocking Meta's agent.
- Oracle's AI Workspace makes ChatGPT the single entry point to all Oracle apps, extending ChatGPT from consumer identity layer to front door of an enterprise suite; governance and identity details not disclosed.

**Status: not yet reviewed by Brian.**

## `worker-surveillance-law-limits-work-observation` — flagged 2026-10-30

State laws (California SB 947, AB 1883, etc.) restricting AI monitoring of human workers, constraining the instrument-the-estate-to-see-how-work-happens payoff that applies freely to agents but not to people.

First seen 2026-10-23, recurred 3 times through 2026-10-30.

Notes from each recurrence:

- Mollick reports AI expanding senior management's direct monitoring of whole firms, the human-observation use these state laws constrain.
- Salesforce cites head-mounted cameras recording service workers as a way to capture tacit knowledge for AI, the kind of worker observation these state laws constrain.

**Status: not yet reviewed by Brian.**

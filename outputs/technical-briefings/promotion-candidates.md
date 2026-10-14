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

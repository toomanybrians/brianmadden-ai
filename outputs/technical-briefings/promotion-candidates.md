# Promotion candidates

Threads the briefing skill has flagged as recurring 3+ times without a home in canon. Queued here for Brian to review — a candidate becomes canon only if he deliberately edits it into `me/developing-thinking.md` himself (or a real framework). Nothing below this line was written by a human; nothing below this line is canon.

## `machine-speed-vs-human-absorption` — flagged 2026-08-17

Infrastructure vendors explicitly marketing 'work at machine speed' as the new operating tempo, in direct tension with the position that human absorption speed is the unchanged invariant — the open question is whether these workflows still have a human absorbing anything.

First seen 2026-08-13, recurred 3 times through 2026-08-17.

Notes from each recurrence:

- GPT-5.6 Sol Ultrafast (750 tokens/sec on Cerebras, framed as no intelligence tradeoff) sharpens the tension: if the value proposition is purely tempo, the open question is who or what is absorbing the output on the other end.
- Anthropic made auto mode the default in Claude Code partly because humans only refused a dangerous swapped command 13.6% of the time; Brockman's cyber post pitches AI triaging nearly all initial alerts. Both remove the human absorption step on the grounds that it wasn't functioning.

**Status: intentionally left open 2026-08-24** — this is likely the evidence base for the staleness queue's "Human clock speed is the invariant AI hasn't changed" promote-candidate (`me/developing-thinking.md`, "What's connecting"), better resolved together with that item than decided in isolation. Brian's other five 2026-08-17-and-earlier stragglers were cleared this same session (folded as brief notes into "The cognitive stack," "The 2031 worker-shape forecast," and "What I'm unsure about," or dropped with no canon addition) — see the 2026-08-24 Weekly Update session log in `BUILD.md`.

## `git-host-as-agent-control-point` — flagged 2026-08-25

Code/knowledge repository hosting turning into the agent runtime and a vendor-owned governance surface — Cursor's Origin defaulted on for paid plans under an owner that also controls the editor and the model, against canon's treatment of git as neutral, boring infrastructure.

First seen 2026-08-19, recurred 3 times through 2026-08-25.

Notes from each recurrence:

- Cursor launched Origin—native repos, PRs, and agents—defaulted on for paid plans, consolidating editor, repo, and model under one owner; coincided with a 6h42m GitHub outage.
- Hugging Face testing a sale at $13B+ extends the pattern from code repos to the model registry: the 'neutral' open-model hub gets an owner with its own interests, and neutrality becomes a business decision rather than a property.

**Status: not yet reviewed by Brian.**

## `harness-as-the-named-value-layer` — flagged 2026-08-25

The industry converging on 'harness' (system prompt, tool catalog, execution loop, sandbox, authorization) as the differentiating and defensible layer above a commoditized model — validating the middle of the cognitive stack while naming only the plumbing, not the context/judgment layer.

First seen 2026-08-21, recurred 3 times through 2026-08-25.

Notes from each recurrence:

- SemiAnalysis explicitly ranks harness quality above benchmark score for real-world outcomes (Claude Code beating higher-scoring GPT-5.2), and DeepSeek open-sourced a fully pluggable harness framework at 160k+ stars — the harness is now both the value layer and part of the open-weight planning floor.
- AlphaSignal states it outright — 'model plus harness is becoming one unit, evaluating a model alone is losing meaning fast' — plus Pi's 26-35% context / 88% cost reduction from a disk-based tool-output pattern, CLI agents 5-28x cheaper than MCP across seven scaffolds, and Anthropic finding interpretability tools no better than reading raw transcripts. Three independent findings that the simple scaffolding wins; still nobody naming the context/judgment layer above the harness.

**Status: not yet reviewed by Brian.**

## `youth-ai-sentiment-inversion` — flagged 2026-08-26

Under-30s now as or more concerned than older cohorts about AI (Pew, 55%) and drifting toward trades — inverting the demographic engine that drove every prior consumerization wave the worker-led adoption thesis is modeled on.

First seen 2026-08-21, recurred 3 times through 2026-08-26.

Notes from each recurrence:

- Exponential View: 22-25 year olds in AI-exposed occupations now 19% below employment trend, up from 15% a year ago — gives the sentiment inversion an economic basis and widens the tactical-learning-rungs gap Brian lists as unresolved.
- Pew at 55% of under-30s more concerned than excited (up from 31% in 2021), now paired with labor data: 22-25 year-olds in AI-exposed occupations 19% below employment trend, up from 15% a year ago.

**Status: not yet reviewed by Brian.**

## `ai-dissolving-hardware-software-moats` — flagged 2026-08-27

AI-assisted chip design and agent-written GPU kernels eroding the compiler/driver ecosystem moat that protects hardware incumbents (OpenAI's Jalapeño ASIC at 16 months to tapeout beating Blackwell on perf/watt; Hawkeye kernels exceeding expert-authored ones by up to 18.9x) — encoded expertise as a category of moat the three-tier software framework doesn't cover and which appears more vulnerable than regulation, data gravity, or encoded workflow.

First seen 2026-08-25, recurred 3 times through 2026-08-27.

Notes from each recurrence:

- Same evidence as when the thread opened (OpenAI's 16-month ASIC tapeout, Hawkeye kernels at up to 18.9x), plus a new adjacent data point: Nvidia shipping a CPU purpose-built for agent orchestration rather than inference.
- OpenAI published its own Jalapeño benchmark numbers (1.5-1.9x perf/watt over Nvidia GB200/GB300) and Nvidia's ~$6B Poolside license deal both extend this thread with concrete data points.

**Status: not yet reviewed by Brian.**

## `inference-allocation-as-supply-risk` — flagged 2026-08-27

Labs projected to shift compute away from external inference toward internal R&D as frontier-capability compounding outvalues token revenue (Patel: Anthropic+OpenAI toward most usable global flops by end-2028, ~$50M revenue per megawatt against $10-15M compute cost) — reframing lab dependency from a price risk into an availability/supply-guarantee risk that token economics arguments don't address.

First seen 2026-08-25, recurred 3 times through 2026-08-27.

Notes from each recurrence:

- Patel puts numbers on it: OpenAI+Anthropic at 40-50% of incremental compute in 2026, $50-100M revenue per MW vs $10-15M cost, and a shrinking share of compute allocated to external inference in favor of internal R&D. OpenAI's reinstated five-hour Plus cap is the same story visible at the subscription tier.
- Brian's own open question about labs deprioritizing paid inference for internal R&D reappears, with the Jalapeño chip investment and Nvidia/Poolside deal read as circumstantial evidence for an infrastructure-over-revenue bet.

**Status: not yet reviewed by Brian.**

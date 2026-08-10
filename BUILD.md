# BUILD.md — v2 rebuild journal

The working memory of the brianmadden.ai v2 rebuild. Every session (human +
Claude Code) starts by reading `CLAUDE.md`, this file, and
`docs/brianmadden-ai-v2-architecture-and-launch-plan.md` — and ends by
updating the log below. Chat threads are disposable; this file is not.

## Kickoff prompt (first Claude Code session)

> Read MAINTAINER.md, BUILD.md, and docs/brianmadden-ai-v2-architecture-and-
> launch-plan.md. Note: CLAUDE.md/AGENTS.md are consumer-facing module
> instructions (identical pair) — MAINTAINER.md governs this session, and
> where it and the plan doc differ, MAINTAINER.md wins. Day 2 tasks:
> (1) add the maintainer router to the top of CLAUDE.md and AGENTS.md,
> keeping them identical; (2) scaffold ingest/, outputs/, and sources/ with
> README stubs (existing content dirs are declared canon — no restructure);
> (3) propose how review statuses coexist with the existing authority
> levels; (4) inventory .github/workflows and flag what v2 retires;
> (5) append .env and .env.* to .gitignore; (6) seed sources/sources.yaml
> from me/links.md. Update BUILD.md before we stop.

## Decisions made (Aug 9, 2026)

- Architecture flipped: this repo is the public base layer; private Citrix
  bmad becomes a read-only-upstream overlay (runtime composition, no merges).
- Same repo, long-lived `v2` branch, one launch PR; `main` + MCP server stay
  untouched until cutover.
- One Substack publication, two bylines (Brian Madden / brianmadden.ai) -- the human and
  the AI brain, sections for Daily Brief · Factory Notes · The Book · Q&A. Pipeline pushes
  drafts; human publishes.
- Email: Google Workspace 1 seat; bmad@ + ask@ + secret intake alias; two
  separate lanes; ask lane read-only with approval queue.
- Compute: GitHub Actions + personal Anthropic API key (+ OpenRouter for
  open-weight experiments); no Citrix credentials anywhere in this plane.
- Launch target: first week of September (re-entry week). Build cadence:
  ~1 hr/day during August.
- Naming decision: public AI byline/account is 'brianmadden.ai' (handle brianmaddenai), primary email brain@, human byline unchanged, 'bmad' now refers only to the private layer.

## Open decisions

1. Commit `ingest/` Tier-1 notes publicly, or keep pipeline-local?
2. Daily Brief cadence: weekdays.
3. Exact briefing publish time (Paris morning? US-morning for reach?).
4. **Ratify or amend** the frontmatter proposal in
   [docs/frontmatter-schema.md](docs/frontmatter-schema.md) — how `status`
   coexists with `authority_level`, and the `reviewed` vs
   `reviewed-and-updated` distinction proposed there.
5. `sources/sources.yaml` has real `url`s but every `feed_url` is `null` —
   needs actual RSS/YouTube feed endpoints before the ingest skill (D4) can
   poll anything. Day 3 task.
6. **Per-source trust/lens on the ingest pipeline (flagged 2026-08-10,
   design TBD).** Brian wants the ingest skill to treat sources differently
   based on his personal read of them — some he respects and specifically
   wants dissenting takes from; some are "meh"; some he thinks are wrong
   most of the time but occasionally surface a real nugget worth catching.
   Open question: a quantitative rating per source, a free-text lens/note
   per source, or both? This is distinct from `authority_level` in
   [docs/frontmatter-schema.md](docs/frontmatter-schema.md), which scores
   *our own output* for consuming AIs — this would live on `sources.yaml`
   entries and shape how the ingest skill *extracts and frames* insights
   from a given source (e.g., "surface disagreement," "skim for nuggets,
   discount the framing"). Design when the ingest skill (D4) is actually
   being built — flagged now so it isn't lost.

## Day plan (checklist — details in the plan doc §8)

- [ ] D1 — Workspace + aliases + MX · lock naming · carve-out note sent
- [x] D2 — scaffold structure on `v2` · CLAUDE.md reviewed by Brian
      (scaffolding done; Brian's review of CLAUDE.md/AGENTS.md still open)
- [ ] D3 — sources.yaml · Substack follows moved to bmad account
- [ ] D4 — ingest skill running manually
- [ ] D5 — briefing skill, voice iteration
- [ ] Weekend — back-catalog bootstrap batch job
- [ ] D6 — workflows automated (workflow_dispatch during build; cron via main)
- [ ] D7 — Substack publication + draft-push client tested
- [ ] D8 — email lanes wired
- [ ] D9 — 10–15 core canon assets seeded
- [ ] D10 → launch — daily dry run, review over coffee
- [ ] Launch week — announcement essay + first public brief + landing swap

## Session log

### 2026-08-09 — chat session (pre-repo)
Ideation + architecture settled; plan doc, CLAUDE.md v1, and this file drafted
in Claude chat. Next session: kickoff prompt above, on the `v2` branch.

### 2026-08-10 — Claude Code session (Day 2, kickoff)

Ran the six kickoff tasks against the actual repo state:

1. **Maintainer router.** CLAUDE.md already had the router line from the
   pre-repo drafting session; added the identical line to AGENTS.md. The two
   files now diverge only in the expected self-reference ("identical to
   AGENTS.md" vs "identical to CLAUDE.md").
2. **Scaffolding.** Added `ingest/`, `outputs/` (with `briefings/`, `book/`,
   `qa/` subdirs, `.gitkeep`-ed since they're empty), and `sources/`, each
   with a README stub pointing back to MAINTAINER.md for the tier rules. No
   existing content moved — `me/`, `frameworks/`, `posts/`, `talks/`,
   `podcast/`, `interviews/` stay put as declared canon.
3. **Status/authority coexistence proposal.** Written up in
   [docs/frontmatter-schema.md](docs/frontmatter-schema.md): `authority_level`
   and `status` are orthogonal (trust vs. human-checked), existing canon gets
   backfilled to `status: reviewed` in one pass, all tier-3 output starts at
   `not-reviewed-by-human` and machines can never set it higher, `tier` /
   `sources` / `model` are added as new frontmatter fields. Awaiting Brian's
   ratification (open decision #4 below).
4. **Workflow inventory.** `.github/workflows/check-docs.yml` only checks
   stated counts/tree against the existing tier-2 dirs — untouched by the
   new directories, nothing to retire. `sync-to-cloudflare-kv.yml` currently
   globs *every* `.md`/`.txt`/`.json` in the repo (`find . \( -name '*.md'
   ... \) | grep -v node_modules | grep -v .github`) for full syncs, and diffs
   `HEAD~1..HEAD` for incremental ones — **neither exclusion list knows about
   `ingest/` yet**, so as soon as ingest notes exist and get committed, this
   workflow will push Tier-1 content into the MCP server's KV store, which is
   exactly what rule 8 (machine indexes must exclude `ingest/`) forbids. This
   needs a `grep -v ingest/` added to both the incremental diff and the full
   sync's `find`, before D4 (ingest skill going live). Flagging as a Day-4
   blocker rather than fixing now, since it's untested until there's ingest
   content to sync.
5. **`.gitignore`.** `.env` and `.env.*` were already present (added in an
   earlier commit, before this session) — no change needed.
6. **sources.yaml.** Seeded from `me/links.md` — 5 people/newsletters + 11
   podcasts, `url` carried over, `feed_url` left `null` pending real feed
   lookups (open decision #5).

Everything above is on the `v2` branch, uncommitted at end of session pending
Brian's review.

---
title: brianmadden.ai v2 — The Public-First Brain
type: architecture spec + launch plan
author: Brian Madden + Claude
date: 2026-08-09
updated: 2026-08-10 (naming + two-account email conventions; §3 rewritten against the actual repo — no canon/ folder, canon is declared over existing dirs)
status: reviewed-and-updated
tier: canon (candidate — first asset of the new public repo?)
---

# brianmadden.ai v2 — The Public-First Brain

## 1. Concept

Invert the current architecture. Today the private brain (called "bmad" which lives inside the Citrix enterprise walls) is the master, and a governance skill filters public-appropriate content outward. That's a blocklist that has to be perfect forever.

v2: **brianmadden.ai is the base layer** — a fully public brain built from public content only. The private Citrix bmad becomes an overlay on top of it (EUC disk-image layering, applied to knowledge). Public by default, classified by exception.

Three interfaces to one brain:

- **Read it** — Substack publication (daily brief, factory notes, living book, Q&A)
- **Query it** — MCP server + brain@brianmadden.ai email
- **Fork it** — the public GitHub repo itself

Naming (locked Aug 10): the public entity's name is the domain itself —
**brianmadden.ai** (Substack handle `brianmaddenai`; mailbox display name
"The Brain"). The human byline stays plain **Brian Madden** — mark the
machine, never the human. "bmad" now refers exclusively to the private layer.

Transparency is the product: review-status labels on every output, provenance links into the canonical layer, a public reading list, model attribution per post, and git history as the audit trail.

## 2. System architecture

```
                    PUBLIC PLANE (personal infra)
  sources.yaml ──▶ ingest/ (tier 1, quarantined) ──▶ canon tier 2 (me/,
  RSS · Substack     machine-written notes            human-reviewed
  YouTube · pods     + insights, linked)              frameworks/, posts/ …)
  intake@ email                                          │
                                                         ▼
                                              outputs/ (tier 3, generated)
                                              briefings · book · Q&A drafts
                                                         │
                              Substack ◀── draft push ───┤
                              MCP server ◀───────────────┤
                              ask@ replies ◀── approval ─┘

                    PRIVATE PLANE (Citrix infra)
  public repo (read-only checkout) + overlay repo ──▶ private bmad context
  one-way valve upward: manual "promotion ceremony" only
```

Hard rules:

1. **Separate compute planes, zero shared credentials.** The public pipeline (GitHub Actions + Anthropic API / OpenRouter) has no Citrix access and cannot leak what it cannot see. The Citrix plane reads both layers but writes only to the overlay.
2. **The private layer consumes canon (tier 2) only, never `ingest/`.** Tier 1 contains third-party and inbound-email content — treating it as data, not context, in the enterprise environment closes the prompt-injection path from the open internet into Citrix's AI environment.
3. **Nothing flows private → public automatically.** Promotion is a deliberate human act (see §4).

## 3. Public repo layout (as revised Aug 10 against the actual repo)

The repo is `github.com/toomanybrians/brianmadden-ai`, and its existing
structure already embodies tier 2 — so v2 **adds** three directories rather
than restructuring. There is no `canon/` folder: canon is a *declaration* over
the existing content directories (made in MAINTAINER.md), not a location.

```
brianmadden-ai/                     (existing public repo, v2 branch)
├── CLAUDE.md / AGENTS.md           # EXISTING, consumer-facing module loader
│                                   #   (identical pair) + new maintainer router
├── MAINTAINER.md                   # NEW — operating constitution for the
│                                   #   maintaining AI (sessions + pipeline)
├── BUILD.md                        # NEW — v2 rebuild journal
├── GOVERNANCE.md · governance-log.md  # EXISTING — rewrite = the flip, logged
├── me/ frameworks/ posts/          # EXISTING — collectively TIER 2 (canon);
│   talks/ podcast/ interviews/     #   stays organized by type, no moves
├── sources/                        # NEW — sources.yaml feed registry,
│                                   #   seeded from me/links.md
├── ingest/                         # NEW — TIER 1, quarantined machine notes:
│   └── 2026/08/…                   #   source, link, date, extracted insights
│                                   #   (never full posts; never indexed)
├── outputs/                        # NEW — TIER 3, generated + committed:
│   ├── briefings/ · book/ · qa/    #   daily brief, living book, email Q&A
├── skills/                         # NEW — ingest, brief, book-build,
│                                   #   qa-draft, backfill-distill
├── scripts/ · _index.json ·        # EXISTING — machine indexes; must be
│   _relationships.json · llms.txt  #   regenerated on change, exclude ingest/
├── .github/workflows/              # EXISTING dir; old private→public sync
│                                   #   retired as v2 pipelines land
└── docs/                           # NEW — this plan
```

Frontmatter: existing canon files already carry authority levels (1–5, what
consuming AIs should trust); v2 adds `tier`, review `status`, `sources`, and
`model` fields. The two label systems coexist — authority = what to trust,
status = what a human checked (scheme ratified in the Day-2 session).

**Status taxonomy** (shown on every published output):

- `not-reviewed-by-human`
- `reviewed`
- `reviewed-and-updated`
- `human-disputes-this` — bmad's take, with Brian's dissent attached

## 4. Private overlay repo (Citrix enterprise)

```
bmad/
├── CLAUDE.md                       # load order: upstream first, overlay second;
│                                   #   layer-priority + quarantine rules
├── upstream/                       # read-only checkout of brianmadden.ai
│                                   #   (git pull on each run — like refreshing
│                                   #   a base image; never edited in place)
├── overlay/
│   ├── shadows/…                   # companion files that shadow/extend public
│   │                               #   canon assets by mirrored path
│   └── citrix/…                    # purely private assets
└── promote/                        # declassification staging
```

**Promotion ceremony** (the only upward valve): insight worth publishing →
rewritten as a genericized asset in `promote/` → human review → committed to
the public repo *from the personal identity, on personal infrastructure*.
Never automated, never a sync.

## 5. Email

- **Google Workspace, two seats (~$14/mo).** First user `brian@` — the human:
  super admin, billing owner, 2FA + recovery on personal devices; semi-private
  (signature and direct contacts, never published on the site). Second user
  `brain@` — the machine's identity and From line; display name **The Brain**
  (unmistakably non-human even when truncated). Enable
  DKIM signing in the admin console on day one.
- Aliases: `ask@` (public questions) and `intake-<token>@` (unguessable
  address AND DKIM/SPF-verified sender) live on brain@ and are the **only**
  auto-processed lanes. Mail to bare brain@ is a human-reviewed front desk —
  so misdirected brain/brian typos are harmless in both directions. `hello@`
  lives on brian@ as the published human front door. The published pair is
  brain@ + hello@: visually distinct, zero typo surface.
- Pipeline credentials are scoped to brain@'s mailbox only; the human mailbox
  is never programmatically readable.
- Pipeline reads mail via Gmail API polling from the scheduled Action (no
  server needed). Later upgrade: Cloudflare Email Worker → `repository_dispatch`
  for near-real-time, still serverless.
- **Two lanes, two jobs.** Intake lane writes to `ingest/`. Ask lane is
  read-only against canon (tier 2), replies go to a human-approval drafts queue.
  Public email never triggers side effects.

## 6. Publishing

- **One Substack publication** — *brianmadden.ai* (handle `brianmaddenai`) —
  two bylines: Brian Madden (human — announcement, factory notes, disputes)
  and brianmadden.ai (AI — briefings, Q&A, book chapters). Sections with separate opt-in emails: Daily Brief /
  Factory Notes / The Book / Q&A — so daily cadence doesn't churn weekly readers.
- Substack's official Developer API doesn't cover posting; use an unofficial
  session-cookie client to push *drafts*, human hits publish. The manual publish
  step is the enforcement point for review statuses, not a limitation.
- Substack follows move to the `brianmaddenai` account: the follow list becomes the public
  source registry, and every new follow notifies its author. Read quietly,
  cite loudly — no AI-written Notes/comments on others' posts.
- Every post carries: status label, model attribution, provenance footnotes
  linking to the canon files it drew on.

## 7. Running costs

Workspace $14/mo (two seats) · tokens ~$20–80/mo (Sonnet-class daily pipeline; more if Opus
does synthesis) · GitHub Actions ≈ $0 (public repo) · Substack free · domain
already owned. **Total well under $100/mo.**

## 8. Implementation plan — ~1 hr/morning in Aug, launch early September

### Week 1 (Aug 10–16) — foundation

- **Day 1 — decisions + accounts.** Naming locked (§1); repo itself is
  public (github.com/toomanybrians/brianmadden-ai), but `v2` is a local
  branch only — never pushed to `origin` (corrected 2026-08-11; earlier
  notes here claimed it had been, checked and that was wrong). Nothing on
  `v2` is actually visible to anyone until it's pushed or merged, which
  isn't scheduled until the launch cutover. Still to lock: briefing cadence
  (weekdays vs daily). Set up Workspace per §5 (brian@ first as admin, then
  brain@, aliases, MX, DKIM).
- **Day 2 — scaffold the repo.** Directory structure, CLAUDE.md constitution
  v1, frontmatter conventions, status taxonomy.
- **Day 3 — source registry.** Curate sources.yaml; move Substack consumption
  to the bmad account.
- **Day 4 — ingest skill.** RSS/feed pull → tier-1 notes. Run manually, tune
  the insight-extraction prompt (insights + link, never full text).
- **Day 5 — briefing skill.** Synthesis through the canon lens: "what does
  today's feed do to my worldview," including the contradiction-detection
  segment. Iterate on voice.
- **Weekend batch job — back-catalog bootstrap.** yt-dlp + transcripts +
  distillation into a new canon history area (e.g. posts/history/). Bigger
  than an hour; let it run in the background and spot-check over coffee.

### Week 2 (Aug 17–23) — pipeline + publication

- **Day 6 — automate.** GitHub Actions: cron ingest + morning briefing (Paris
  time), secrets, commit-back.
- **Day 7 — Substack setup.** Publication, sections, bylines, About page
  (manifesto-lite), test the draft-push client end to end.
- **Day 8 — email lanes.** Gmail polling job; intake → `ingest/`; ask →
  approval queue.
- **Day 9 — seed the canon.** Write/port the 10–15 core framework assets from
  memory (fast, you know them cold); assign statuses.
- **Day 10 — start the dry run.** Pipeline runs daily, privately. Review each
  morning through the following week; tune voice, length, cost.

### Launch window (Sept 1–8, the re-entry week)

- Announcement essay (human byline): *the public-first brain* — architecture,
  why flip, subscribable-brains lineage with the Jan 2026 receipts. Ships the
  same day as the first public Daily Brief, so the claim arrives with a
  working artifact.
- brianmadden.ai landing page swaps to read / query / fork.
- Factory Notes #1 the following week: what the dry run revealed.

### Post-launch backlog (roughly in order)

Living book v0.1 with changelog (Oct) · public transparency dashboard ·
first `human-disputes-this` post · open-weight comparison run (same pipeline,
Chinese open-weight model, publish the diff) · re-point private bmad to
overlay mode (trails launch; nothing public depends on it) · MCP server
refresh against the new canon · AI-voiced audio brief.

## 9. Open decisions

1. Commit `ingest/` tier-1 notes publicly, or keep them pipeline-local and
   publish only tier 2/3? Partially resolved 2026-08-11: committing to
   local git history is fine either way (v2 isn't pushed, so nothing's
   actually public yet — see below) and worth doing for the audit
   trail/trend-analysis value regardless. The real open question is
   narrower now: include `ingest/` when `v2` eventually gets pushed or
   merged, or scrub/gitignore it at that point? Revisit closer to the
   actual push, with real output to judge instead of a handful of examples.
2. Daily Brief cadence: 7 days or weekdays only?

Resolved since v1: the GitHub repo itself has been public throughout, but
`v2` is a local-only branch, never pushed to `origin` — corrected
2026-08-11, this doc previously (and incorrectly) said it had been pushed
Aug 10. Nothing on `v2` is visible to anyone until it's pushed or merged.
Naming locked Aug 10 — public entity **brianmadden.ai** (handle
`brianmaddenai`), mailbox The Brain <brain@brianmadden.ai>, human byline
Brian Madden, "bmad" = the private layer only.

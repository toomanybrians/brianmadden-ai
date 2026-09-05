# outputs/ — Tier 3: generated artifacts

This directory holds generated output — daily briefings, book editions, Q&A
drafts. Everything here is **always regenerable from Tiers 1–2** (`ingest/`
and canon); it's committed for audit, not treated as truth.

## Rules (see [MAINTAINER.md](../MAINTAINER.md))

- **Provenance always.** Every output footnotes the canon files (and, where
  relevant, ingest notes) it drew on, plus which model wrote it.
- **Status labels.** Every output carries a review status
  (`not-reviewed-by-human` · `reviewed` · `reviewed-and-updated` ·
  `human-disputes-this`) in frontmatter — see the coexistence proposal in
  [docs/frontmatter-schema.md](../docs/frontmatter-schema.md).
- **Draft, not publish.** Pipelines push drafts (Substack, email replies);
  a human hits publish/send. The manual step is the review checkpoint, not
  friction to route around.

## Subdirectories

- **`technical-briefings/`** — the dense Daily Brief (synthesis over the
  latest `ingest/` batch through the canon lens), written by
  [skills/brief/brief.py](../skills/brief/brief.py). `YYYY/MM/YYYY-MM-DD.md`
  is the brief itself — full detail, every source cited, the audit trail
  and the thing a future AI (an MCP-connecting client, say) would actually
  want to read. `.last_run.json` and `.thread_tracker.json` are pipeline
  state, not content (git-tracked so a fresh checkout doesn't lose the
  tracker's history, but not meant to be read as canon).
  `promotion-candidates.md` is a human-review queue — threads the brief
  has flagged as recurring without a home in canon, appended to by the
  machine, promoted to `me/developing-thinking.md` only by Brian editing
  it in himself. Nothing in `promotion-candidates.md` is canon until that
  happens.
- **`published/`** — the condensed, Substack-voiced rendering of that same
  day's dense brief, written by
  [skills/brief/publish.py](../skills/brief/publish.py). `YYYY/MM/YYYY-MM-DD.md`
  — human-facing, shorter, 2-4 (or however many the day warrants) stories
  written for a subscriber, not an AI. Split from `technical-briefings/`
  2026-08-12 (Brian's call) since the two serve genuinely different
  audiences and were getting confused living in one folder under a
  `-published` suffix. `YYYY-MM-DD.html` (gitignored, not repo content) is
  [skills/brief/render.py](../skills/brief/render.py)'s copy-paste
  rendering for Substack's editor.
- **`book/`** — Living book chapters/editions with changelog.
- **`qa/`** — Drafted replies to the `ask@` inbox lane, queued for human
  approval before sending.
- **`canon-triage/`** — the staleness-triage queue, written by
  [skills/triage/triage.py](../skills/triage/triage.py). Mirror image of
  `technical-briefings/promotion-candidates.md`: that queue proposes
  *additions* to canon, `staleness-candidates.md` proposes *cuts,
  promotions, or a second look* at `me/developing-thinking.md`'s "What's
  connecting"/"Scratchpad" sections and active `frameworks/*.md` files,
  judged against `me/published-thinking.md`. Overwritten fresh every run
  (a snapshot of the current record, not an accumulating log) — nothing in
  it is canon, and nothing here ever edits `developing-thinking.md` or a
  framework's `status` directly. Built 2026-08-15 for BUILD.md open
  decision #8.
- **`weekly-updates/`** — **Weekly Wrap Up**, a lower-frequency, dual-byline
  (`brianmadden.ai` + Brian Madden) companion to the Daily Brief (the
  directory kept its original internal name; the publication itself is
  called Weekly Wrap Up — named Deeper Thinking at launch, renamed by
  Brian on Substack 2026-08-26). Built 2026-08-24 for
  `BUILD.md` open decision #13. Half-automated: the prep doc is assembled
  and emailed to Brian unattended every Friday by
  [skills/weekly/gather.py](../skills/weekly/gather.py) (wired into
  `daily-pipeline.yml`), but the actual decisions still need Brian live —
  see [.claude/skills/weekly-update/SKILL.md](../.claude/skills/weekly-update/SKILL.md)
  for that ceremony. `YYYY/MM/YYYY-MM-DD-prep.md` is the machine-written
  recap Brian reads first (week's stories, unresolved promotion/staleness
  candidates, current `developing-thinking.md` "Right now"); `YYYY/MM/YYYY-MM-DD.md`
  is the finished post, drafted live with Brian's own takeaways folded in.
  `.last_run.json` is pipeline state, shared between `gather.py` and the
  live ceremony, same convention as
  `technical-briefings/.last_run.json`.
- **`essays/`** — one-off long-form pieces that don't belong to any recurring
  cadence (not a Daily Brief, not a Weekly Wrap Up entry) — a milestone in
  the brain's own build worth writing up properly, the kind of thing
  [`CHANGELOG.md`](../CHANGELOG.md) at the repo root links out to instead of
  trying to tell the full story itself. Hand-drafted per piece, same as
  `substack-migration/` below: no `brief.py`/`publish.py` involved, drafted
  directly and hand-pasted into Substack by Brian. Started 2026-09-04 with
  the first one, on the `semantic_search`/Vectorize build.
- **`substack-migration/`** — one-off drafts for Workstream C
  (`docs/substack-as-primary-home.md`): moving the ~90-item back catalog
  (podcast, talks, LinkedIn, Citrix blog, frameworks) onto Substack.
  Hand-built per content type, not a pipeline output — no `brief.py`/
  `publish.py` involved, each file is drafted directly from the matching
  canon source and hand-pasted into Substack by Brian. Started 2026-08-12
  with one pilot draft per type, per the treatment table in the Workstream
  C doc, before deciding whether the rest is worth automating.

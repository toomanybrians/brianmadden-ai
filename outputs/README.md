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

- **`briefings/`** — Daily Brief editions (synthesis over the latest
  `ingest/` batch through the canon lens), written by
  [skills/brief/](../skills/brief/). `YYYY/MM/YYYY-MM-DD.md` is the brief
  itself; `.last_run.json` and `.thread_tracker.json` are pipeline state,
  not content (git-tracked so a fresh checkout doesn't lose the tracker's
  history, but not meant to be read as canon). `promotion-candidates.md`
  is a human-review queue — threads the brief has flagged as recurring
  without a home in canon, appended to by the machine, promoted to
  `me/developing-thinking.md` only by Brian editing it in himself. Nothing
  in `promotion-candidates.md` is canon until that happens.
- **`book/`** — Living book chapters/editions with changelog.
- **`qa/`** — Drafted replies to the `ask@` inbox lane, queued for human
  approval before sending.

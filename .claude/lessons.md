# Lessons

Persistent log of mistakes and corrections for maintainer sessions on this
repo. `/maintain` reads it at session start. When Brian corrects something
that could recur, add an entry here immediately, in the same session.

Voice and style corrections do **not** go here: `me/voice.md` is the single
source of truth for those (MAINTAINER.md rule 7). Edits to it are Brian's.

Entry format: **Date**, what happened, the rule, scope. If a lesson becomes a
permanent rule in MAINTAINER.md or a skill, note that and delete it here.
Public repo: no internal names, strategy, or private-system details.

## Active lessons

### The domain is brianmadden.ai, not brainmadden.ai
- **Date:** 2026-02-26 (carried over from the pre-v2 private brain)
- **What happened:** "second brain" primes a natural typo. It appeared in 9
  files, and later in an Analytics Engine dataset name that broke queries.
- **Rule:** brian + madden. Grep for `brainmadden` after writing anything
  that names the domain, a dataset, or a URL.
- **Scope:** All files and commands.

### Talks and podcasts have more than one place to update
- **Date:** 2026-04-03 (carried over)
- **What happened:** A podcast was added to `_content-index.json` (homepage)
  but the speaking page, which lives in the separate `brianmadden-ai-server`
  repo and has its own video grid, wasn't updated.
- **Rule:** When a talk or podcast with a video is added, update both
  `_content-index.json` here and `pages/bmad/speaking.md` in
  `~/git/brianmadden-ai-server`. The canonical `_content-index.json` is the
  one in this repo; the server repo's copy is only a fallback.
- **Scope:** Every new talk, podcast, or speech.

### Filing without syncing is incomplete
- **Date:** 2026-02-22 (carried over)
- **What happened:** Seven speech transcripts were filed but never made it
  into the public brain's talks index.
- **Rule:** A new talk is not done until the file has frontmatter, and
  `talks/index.md`, `_index.json`, and `COLLECTIONS.md` are updated. Run
  `python3 scripts/check_doc_accuracy.py` and `python3 scripts/audit.py
  --dry-run` before calling it done.
- **Scope:** Every new talk, post, or framework.

### Names in voice transcripts are phonetic; first names are ambiguous
- **Date:** 2026-03-27 / 2026-04-09 (carried over)
- **What happened:** Transcription turned "Sridhar" into "Speeder", and a
  first-name-only reference was attributed to the wrong person.
- **Rule:** Treat every name in a transcript as a phonetic guess. Check it
  against known people and the episode or talk context. If it doesn't match
  or could be two people, give the best guess and ask Brian. Never copy the
  raw transcribed spelling into a published file.
- **Scope:** Podcast, talk and interview processing.

### Don't schedule an autonomous job that reports "nothing changed"
- **Date:** 2026-10-04
- **What happened:** The old private brain's autonomous weekly review ran 17
  straight weeks on an unchanged repo, committing a fresh review each time.
  The output got longer while the content stayed static.
- **Rule:** Any scheduled job that commits must skip the commit when its
  inputs haven't changed (see `monthly-audit.yml`). Review ceremonies that
  need Brian's judgment (`/weekly-update`, `/connect-the-dots`) stay
  interactive.
- **Scope:** Every new scheduled workflow or cron task.

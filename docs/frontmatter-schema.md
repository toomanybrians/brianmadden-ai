---
title: "Frontmatter schema — authority levels + review status (proposal)"
type: proposal
author: Claude Code (Day 2 session)
date: 2026-08-10
status: ratified
---

# Frontmatter schema: how status coexists with authority

MAINTAINER.md rule 4 calls for a Day-2 proposal on how the new review-status
taxonomy coexists with the existing authority-level system, for Brian to
ratify. This is that proposal.

## The two systems answer different questions

- **`authority_level` (1–5, existing).** *What should a consuming AI trust
  when sources conflict?* A property of the content itself — is this a
  primary statement of Brian's thinking, a derived framework, or source
  material. Set once, changes rarely (only if the content's role in the
  hierarchy changes).
- **`status` (new: `not-reviewed-by-human` · `reviewed` ·
  `reviewed-and-updated` · `human-disputes-this`).** *What has a human
  actually checked?* A property of the process that produced or last
  touched the file. Set on every write, expected to change often for
  tier-3 output and rarely for hand-written tier-2 canon.

They're orthogonal axes, not a hierarchy — a file can be high-authority and
unreviewed (freshly generated synthesis that would carry a lot of weight if
confirmed) or low-authority and reviewed (a fully human-checked source note).
Neither field substitutes for the other; both live in frontmatter side by
side.

## Proposed frontmatter additions

```yaml
tier: 2                        # 1 = ingest, 2 = canon, 3 = outputs
status: not-reviewed-by-human  # required on every tier-2/3 file
sources: []                    # tier 3 only: canon files / ingest notes drawn on
model: claude-sonnet-5         # tier 3 only, or any machine-written tier-1/2 file
```

`authority_level` and its existing companions (`file_type`, `tags`,
`staleness_threshold`, etc.) are unchanged.

## Defaults by tier

- **Tier 1 (`ingest/`)** — no `authority_level` (excluded from every index
  that field would matter to). `status` is not meaningful here either;
  ingest notes aren't reviewed, they're either promoted or discarded.
- **Tier 2 (`me/`, `frameworks/`, `posts/`, `talks/`, `podcast/`,
  `interviews/`)** — existing files: backfill `status: reviewed` in one pass
  (Brian wrote or personally published all of it; the review already
  happened, frontmatter just needs to say so). New canon files added going
  forward (e.g., the Day-9 seed batch, ported from memory) start at
  `status: not-reviewed-by-human` until Brian confirms the port is faithful,
  then flip to `reviewed`. `authority_level` is assigned as today, independent
  of status.
- **Tier 3 (`outputs/`)** — every generated file starts at
  `status: not-reviewed-by-human` by construction; a machine can never set
  anything else (rule 4: status is never upgraded by machine). `authority_level`
  reflects how derivative the synthesis is — typically lower than the tier-2
  material it cites, since it's synthesis, not primary source.

## `human-disputes-this`

Reserved for the case where a generated output (typically a Daily Brief or
Q&A reply reasoning from canon) reaches a conclusion Brian disagrees with.
The file keeps the machine's reasoning intact and Brian's dissent is
appended inline, not overwritten — the disagreement is the content. This is
the only status that pairs with mandatory human-authored text in the same
file.

## Enforcement

- `scripts/check_doc_accuracy.py` (or a new `scripts/check_frontmatter.py`)
  should fail CI if a tier-2/3 file is missing `status`, or if a `status`
  transition *to* `reviewed`/`reviewed-and-updated`/`human-disputes-this`
  appears in a commit not authored/co-authored by Brian — the machine can
  set `not-reviewed-by-human` and nothing else.
- `_index.json` should surface both fields so consuming AIs can filter or
  weight on either axis independently.

## Open question for Brian

Should `reviewed-and-updated` require a diff (i.e., only used when Brian
edited the machine's draft), versus `reviewed` meaning "read and left as-is"?

Answer: yes — `reviewed-and-updated` implies the committed text
differs from what the machine originally generated; a no-change approval is
just `reviewed`.

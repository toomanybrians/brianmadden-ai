You are doing a staleness-triage pass over Brian Madden's developing
thinking and named frameworks, for his own review. You are not writing in
his voice and not writing to a reader — this is an internal audit, third
person throughout ("Brian's post on X already covers this"), addressed to
Brian.

## Why this pass exists

`me/developing-thinking.md`'s "What's connecting" and "Scratchpad" sections
have grown into a large, ungrouped pile of items with no reliable dates —
per-item dating turned out to be unrecoverable (most of the file's existing
content arrived in a handful of historical batch syncs, not one item at a
time). The only honest signal left is content: has this idea already been
said, in substance, somewhere in the published record? Has the field moved
past it? Is it mature enough to graduate into something real? The same
question applies to `frameworks/` — a framework doesn't have a shelf life
by rule, but the field can move past one, or a later post can make it
redundant.

## Your task

Read every item in the "What's connecting" and "Scratchpad" sections below,
and every framework file below, against the full authority record
(`me/published-thinking.md`). For each one, silently judge whether it is:

- **Still genuinely developing.** Not covered elsewhere, not resolved, not
  superseded. **Do not mention these at all.** Their absence from your
  output is the "keep" signal — this file should only ever contain
  actionable flags, never a status report on everything that's fine.
- **`already-published`** — the substance of this item is already said, in
  full, somewhere in `me/published-thinking.md` or a framework. Cite
  exactly where (post title + link if the published-thinking.md text gives
  you one, or the framework file). Only flag this if the overlap is real
  and substantial, not a loose thematic echo — the published version
  should genuinely make the developing-thinking item redundant, not just
  related.
- **`promote-candidate`** — the idea reads as mature and load-bearing
  enough that it's ready to become a real framework file or get written up
  properly in published-thinking, the way the knowledge factory and three
  waves material did on 2026-08-14. This is a compliment, not a cut — flag
  it because it's ready to graduate, not because it's stale.
- **`worth-revisiting`** — doesn't cleanly fit either bucket above, but
  something about it reads as dated, went nowhere, or the field has
  visibly moved past its framing since it was written. Say specifically
  what changed or why it reads stale now — don't just assert it.

Apply the same three categories to each framework file, judging it as a
whole rather than line by line: is a framework now redundant with
something published more recently, or does its central claim read as
dated relative to where the published record and the developing-thinking
material have since moved? Frameworks you don't mention were judged still
current — same "silence means keep" rule.

**Be conservative.** This is a short list for Brian to actually read, not
an exhaustive audit. If you're not confident an item is actionable, leave
it out. A previous manual pass through this same material (2026-08-14)
flagged only a handful of items out of nearly a hundred — that's the right
hit rate to aim for, not an exception.

## Output format

For every item you flag, and only those, write:

```
### "the item's own opening words, quoted verbatim" — already-published

One to three sentences: what the item claims, exactly where it's now
covered (name the post/framework, link it if you have a URL), and why the
overlap is real rather than loosely thematic.

**Section:** What's connecting
**Suggested action:** cut from developing-thinking.md — fully covered by [linked title](url).
```

Use the item's real opening words as the heading (not a paraphrase, not a
number) so Brian can find it with a text search. `**Section:**` is one of
`What's connecting` or `Scratchpad`. For a framework, use its path as the
heading instead of quoted text (e.g. `### frameworks/bitter-lesson.md —
worth-revisiting`) and drop the `**Section:**` line.

`**Suggested action:**` is one sentence — what you'd actually recommend
Brian do, not a repeat of the category name. Never write anything implying
the item has already been changed; you are proposing, not deciding — the
file only changes if Brian edits it himself.

Group your output under two headers, `## Developing-thinking items` and
`## Frameworks`, in that order. If a group has nothing to flag, write the
header followed by "(nothing flagged this pass.)" — don't omit the header
entirely, since the calling script counts flagged items by header.

Do not write anything outside this format — no preamble, no summary at the
top, no sign-off. The calling script adds its own framing before and after
your output.

## Reference: Brian's published thinking (the authority record — what he's actually argued)

{{PUBLISHED_THINKING}}

## Reference: active frameworks (full text, each delimited by its path)

{{FRAMEWORKS_FULL}}

## Material to triage: developing-thinking.md's "What's connecting" and "Scratchpad" sections, verbatim

{{DEVELOPING_THINKING_CANDIDATES}}

---

Produce your output now, following the format above exactly.

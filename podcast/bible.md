# Citrix AI Hotsheet — production reference

Maintainer/production reference, not consumer module content. Deliberately
**not** listed in `_index.json`, `COLLECTIONS.md`, or `llms.txt` — same
reasoning as `MAINTAINER.md`/`BUILD.md` living at repo root: this is how
the show gets made, not part of Brian's public thinking those surfaces are
curated to expose. If it turns out useful for a consuming AI to see too,
that's a separate decision — add it to the curated surfaces deliberately,
don't let it happen by default.

## The default, as of 2026-09-02

Podcast production happens **natively in `brianmadden-ai`**, not staged in
Brian's private/work second brain first. Every Hotsheet episode is public
content the moment it's recorded — there's no private-first step to
justify, unlike content that starts as internal Citrix material and gets
promoted later. Episodes 1–5 were drafted privately and mirrored into this
repo after the fact (ep5 mirrored 2026-09-02, the session that wrote this
file); starting with episode 6, drafting happens here from the first
transcript onward. See `MAINTAINER.md`'s Working conventions.

## Two canonical links, two audiences — not one either/or

- **Substack (`brianmadden.ai/p/...`) is the canonical link for humans.**
  Full formatting, no character limit, comments, already the polished
  site people land on from a podcast player. This is what goes in
  Riverside's description, YouTube's description, and everywhere else a
  listener might click.
- **This repo (`podcast/epN.md`) is the canonical source for AI/machine
  consumption.** Per `CLAUDE.md`: *"This repo is built for AI consumption
  via MCP. The primary audience is other AI systems, not humans browsing
  files."* Never send a human listener here as "the show notes page" —
  raw markdown on GitHub is a worse experience than the Substack post,
  and it fights the repo's own stated purpose.

Don't relitigate this per episode. Both links get filled in; neither
replaces the other.

## Riverside's real constraints (confirmed 2026-09-02, see BUILD.md)

- **The hosting/publish form has exactly one text field: Description.**
  No transcript field, no separate long-form show-notes field. (Source:
  Riverside's own "Hosting: Upload and publish new episode" help article.)
- **The "Transcript" tab on the public episode page is Riverside's own
  raw AI transcription of the recording** — generated automatically,
  separate from the publish form, and rough (confirmed live on the ep5
  page: mangled words, run-on sentences, no real punctuation). There is
  no bulk-upload/replace path for it. The only lever Riverside exposes is
  manual, word-by-word correction inside their own editor ("Correct the
  transcript and caption text," "Correct Everywhere") — not a fit for
  swapping in an already-cleaned transcript. **Don't try to make
  Riverside's transcript authoritative. It never will be.** The
  Substack post and this repo's `podcast/epN.md` carry the real one.
- Riverside added rich-text support to the Description field at some
  point after this was first written — Brian's live call (2026-09-02):
  "pretty garbagey." Not worth building against yet; the plain-text,
  character-budget-constrained approach below is still the practical
  one until that changes.
- **The Description field's practical limit is ~4,000 characters of
  stored HTML**, and Riverside auto-links every URL it detects into
  `<a href="URL" target="_blank" rel="noopener noreferrer nofollow">URL</a>`
  — **66 fixed characters plus the URL twice**, so a link costs ~110
  characters minimum however short the URL is (calibrated 2026-09-01:
  typing `bm.ai` moved the live counter to 91). Two consequences, both
  the opposite of what you'd expect:
  - Hyperlinking words doesn't help — the fixed markup dominates, and
    Riverside's editor has no link tool; pasted `<a>` tags get stripped.
  - A handful of links can burn a third of the whole budget on markup
    nobody sees.
  So: **prose plus one link out** (to the Substack canonical page),
  nothing else. Superseded approaches, confirmed not to work: bare
  `Label: URL` lines (~5,600 on the counter for a full link list),
  markdown `[words](url)` pasted as text (renders as literal brackets),
  pasting rendered HTML from a preview or browser (anchors get stripped
  on paste). No script exists in this repo yet to compute this count
  automatically — if you want one, verify whatever formula it implements
  against Riverside's live counter before trusting it; the 66+2×len(url)
  figure above is a reconstruction from one calibration point, not
  something this repo has tested in bulk.

## The publishing-prep doc

Working draft for an in-progress episode → `outputs/podcast/epNN-publishing.md`
(tier 3: regenerable, committed for audit — same pattern as
`outputs/weekly-updates/`). Sections, in the order they get filled in:

1. **Title** — candidates, then Brian's final call marked explicitly.
2. **SHORT** (~250 chars) — for previews, social, RSS summary.
3. **SUBSTACK** — the show notes: YouTube link (plain text, own line —
   not a hyperlink, so Substack's own paste-detection can auto-embed it
   as a player), description, every link mentioned, the complete
   transcript. No chapters, no platform-links block beyond YouTube —
   Brian's explicit call (2026-09-02). This is the canonical page (see
   above) and goes live **before** Riverside or YouTube, since both
   point at it. Render it from the finished `podcast/epN.md` with
   `python3 scripts/render_substack_html.py podcast/epN.md` (or `--all`
   for every episode) — see Tools below.
4. **RIVERSIDE** — prose + one link out, character-budget-constrained per
   the rules above.
5. **LONG** — the YouTube description: full narrative, chapter list with
   timestamps, links mentioned, a "Find us online" block, show boilerplate.
6. **Links checklist** — every URL mentioned, checked off as verified.
7. **Publish checklist** — the episode-level steps (below).

## Tools

- **`scripts/render_substack_html.py`** (added 2026-09-02) — renders a
  finished `podcast/epN.md` into Substack-paste-ready HTML:
  `outputs/podcast/epN-substack.html`. Pulls exactly four things (YouTube
  URL as plain text, Description, Links mentioned, Transcript — nothing
  else), splits the transcript into speaker turns so names land on their
  own bold line instead of folding into the paragraph (plain markdown
  conversion alone doesn't do this — a `**Name**` line immediately
  followed by text with no blank line is one soft-wrapped paragraph
  under CommonMark), and autolinks any bare URLs in the links list.
  Usage: `python3 scripts/render_substack_html.py podcast/epN.md` for
  one episode, or `--all` for every `podcast/ep*.md`. Output is meant to
  be opened in a real browser, selected all, copied, and pasted into
  Substack's editor — Substack's rich-text paste carries over the
  headings/bold/links/lists, and a bare YouTube URL on its own line is
  what triggers Substack's auto-embed into a video player.
- No script exists yet for the Riverside description's character-budget
  count — see the caveat above. Not urgent per Brian's 2026-09-02 call
  on Riverside's rich-text field.

## Publish checklist (episode level)

1. Record (Riverside).
2. Draft `outputs/podcast/epNN-publishing.md` directly in this repo —
   title options, all description variants, chapters, links checklist.
3. Publish the Substack show notes first (canonical link) — captures the
   URL every other platform's description points at.
4. Upload to YouTube; paste the LONG description and chapters; capture
   the URL.
5. Publish on Riverside; paste the RIVERSIDE description (budget-checked
   against the live counter, not just the reconstructed formula); capture
   the episode URL.
6. Verify Apple Podcasts / Spotify / Amazon Music picked it up via RSS.
7. Assemble `podcast/epNN.md` — the canon file — from the publishing doc
   and the final (cleaned) transcript. Format below.
8. Update every index/stats surface (checklist below).
9. LinkedIn post, if planned for this episode.

## The final episode file (`podcast/epNN.md`)

Mirror the existing episodes' format exactly — frontmatter (`title`,
`date`, `show`, `hosts`, `format`, `authority_level`, `file_type`, `tags`,
`staleness_threshold`, `tier`, `status`), then:

```
# EP N: Title

*Citrix AI Hotsheet · Brian Madden & Dave Brear · Month Day, Year*

## Listen
## Description
## Topics covered
## Chapters
## Links mentioned
---
## Transcript
```

`## Listen` includes the Substack canonical link alongside the platform
links. `## Description` reuses the LONG description's narrative
paragraphs, dropping the generic welcome preamble. `## Chapters` keeps
the "timestamps are estimates from the transcript — verify against
Riverside" disclaimer even after publish, matching existing episodes.

## Index/stats checklist (every time a new episode lands)

- `podcast/index.md` — new episode bullet; add any new recurring theme
  to the show's own frontmatter `tags`.
- `_index.json` — new file entry inserted after the previous episode's
  (keep the `podcast/` block contiguous), `total_files` +1, `total_words`
  bumped by the new entry's `word_count`, `generated` date bumped. Edit
  the JSON with targeted text edits, not a full rewrite/regeneration —
  `json.dump` reformats every inline array in the file and produces
  unrelated diff noise (hit this exact problem 2026-09-02; reverted and
  redid it as surgical edits).
- `_content-index.json` — new entry inserted at its correct
  chronological position (the feed is reverse-chronological).
- `COLLECTIONS.md` — add to whichever thematic sections the episode's
  actual *content* justifies. Check the content, don't just pattern-match
  the previous episode's placements.
- `llms.txt` — bump the episode count in the `podcast/index.md` bullet;
  nudge the summary header line's file/word counts (these were already
  approximate before any of this — treat them as directionally honest,
  not exactly reconciled, unless you're prepared to audit the whole
  corpus).
- If the episode is a deep dive on an existing framework (ep5 was, for
  `frameworks/knowledge-factory.md`), cross-reference it from that
  framework's own text and add it to `_relationships.json`'s
  `referenced_by_podcast` array (introduced 2026-09-02 — mirrors the
  existing `referenced_by_talks` shape; no other framework has this yet).
- Run `python3 scripts/check_doc_accuracy.py` — it won't catch
  podcast-specific drift (no count-checks exist for `podcast/` yet), but
  it does catch phantom framework references and general cross-file
  parity. Do a final `git diff` review before committing regardless.

## History

- Episodes 1–4 were processed on Brian's private/work second brain,
  mirrored into this repo after the fact, with no working doc or bible
  living here.
- Episode 5 (recorded 2026-09-01) was the last one processed that way —
  transcript and publishing doc drafted privately, then a Claude Code
  maintainer session built `podcast/ep5.md` and updated every index
  surface from the pasted material (2026-09-02).
- This file was written the same day, to make episode 6 onward default
  to happening here from the start.
- Also 2026-09-02: Brian asked where the actual Substack content for
  episodes 1-5 lived, since he needed it as pasteable HTML and didn't
  have it in hand. `scripts/render_substack_html.py` was built in
  response and run with `--all`, producing
  `outputs/podcast/ep{1,2,3,4,5}-substack.html`.

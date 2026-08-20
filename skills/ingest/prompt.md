You are helping build the tier-1 `ingest/` layer of brianmadden.ai, Brian
Madden's public second brain. Brian's core focus: AI's impact on knowledge
work and the enterprise — how AI is reshaping how people work, how
organizations are structured, and what the workplace looks like as it
changes.

This is raw material, not synthesis — extract what's actually in the piece,
plainly. Don't try to connect it to Brian's specific frameworks or existing
thinking; that judgment needs the whole day's notes and his full canon in
view at once, which a single-article extraction doesn't have. Just capture
what's there.

You're reading one item from a source Brian follows: **{{SOURCE_NAME}}**
({{SOURCE_TYPE}}).{{SOURCE_POV_BLOCK}}

Item metadata:
- Title: {{ENTRY_TITLE}}
- Author: {{ENTRY_AUTHOR}}
- Published: {{ENTRY_DATE}}
- URL: {{ENTRY_URL}}

Item content (fetched for this extraction only — do not reproduce it):
---
{{ENTRY_CONTENT}}
---

Ground everything below ONLY in the content between those `---` markers.
Even if you recognize this source or episode from training data, do not
draw on what you know about it — use only what's actually in front of you.

## Your task

Two checks first, each with its own exact-output response if it fails —
do these before writing anything else, and don't explain your reasoning
in prose either way; the sentinel alone is the whole response:

1. **Relevance**: is this item at all about AI, the future of work,
   knowledge work, the enterprise, or adjacent futurism? If it is clearly
   off-topic (e.g. politics, personal life, unrelated hobbies), respond
   with exactly the single line `NOT_RELEVANT` and nothing else.
2. **Sufficiency**: is the content above a stub, paywall notice, episode-
   description-only page, or otherwise too thin to support real insights
   (roughly under 100 words of substance)? If so, respond with exactly
   the single line `INSUFFICIENT_CONTENT` and nothing else — don't invent
   or infer what the piece probably covers.

Otherwise, write a tier-1 ingest note body in Markdown with this shape:

```
## Insights

- 3-6 bullets, in your own words, capturing the substantive claims/ideas —
  not a re-summary of the whole piece, the parts worth remembering
- Neutral, analytical third person. Do not adopt Brian's voice or opinions —
  this is raw material for a later synthesis step, not a finished take.
{{LENS_INSTRUCTION}}

## Quote

> One direct quote, under 25 words, attributed. Omit this section entirely
> if nothing is quote-worthy — don't force one.
```

Hard rules (non-negotiable, from this repo's governance):
- Never reproduce more than one short quote, and never over 25 words.
- Never summarize so closely that it amounts to a paraphrase-length reprint
  of the source — insights, not a reprint.
- No preamble, no "Here is the note" framing — output starts at `## Insights`
  (or is exactly `NOT_RELEVANT` or `INSUFFICIENT_CONTENT`, nothing appended).

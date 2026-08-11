You are helping build the tier-1 `ingest/` layer of brianmadden.ai, Brian
Madden's public second brain. Brian's core focus: AI's impact on knowledge
work and the enterprise — how AI is reshaping how people work, how
organizations are structured, and what the workplace looks like as it
changes.

Brian has named frameworks for parts of this argument. When an item clearly
connects to one, say so by name in your insights — don't force a connection
that isn't really there:

{{FRAMEWORKS_LIST}}

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
If the content above is a stub, paywall notice, or otherwise too thin to
support real insights (roughly under 100 words of substance), say so
plainly instead of inventing or inferring what the piece probably covers.

## Your task

First, decide relevance: is this item at all about AI, the future of work,
knowledge work, the enterprise, or adjacent futurism? If it is clearly
off-topic (e.g. politics, personal life, unrelated hobbies), respond with
exactly the single line `NOT_RELEVANT` and nothing else.

Otherwise, write a tier-1 ingest note body in Markdown with this shape:

```
## Insights

- 3-6 bullets, in your own words, capturing the substantive claims/ideas —
  not a re-summary of the whole piece, the parts worth remembering
- Neutral, analytical third person. Do not adopt Brian's voice or opinions —
  this is raw material for a later synthesis step, not a finished take.
- If a framework below genuinely applies, cite it by name and say how.
  If none genuinely applies, cite none and don't mention the absence —
  silence, not a hedge.
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
  (or is exactly `NOT_RELEVANT`).

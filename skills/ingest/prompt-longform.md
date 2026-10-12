You are helping build the tier-1 `ingest/` layer of brianmadden.ai, Brian
Madden's public second brain. Brian's core focus: AI's impact on knowledge
work and the enterprise — how AI is reshaping how people work, how
organizations are structured, and what the workplace looks like as it
changes.

You are reading ONE long-form item, a podcast episode or a video, for which
a full transcript is available. This prompt differs from the one used for
articles in two ways: you are given Brian's own thinking as the lens for
what matters, and you are not given a bullet quota. How much you write is
decided by how much of this item bears on Brian's work.

## Brian's point of view (the lens, not the content)

This block is for two jobs only: deciding what is relevant, and writing the
"Fit with Brian's work" section. It is NOT a source for the insights
themselves, and nothing in it may be attributed to the people speaking in
the transcript.

### His active frameworks

{{FRAMEWORKS_LIST}}

### Where his head is right now (`me/developing-thinking.md`)

{{DEVELOPING_THINKING}}

### What he has published (`me/published-thinking.md`)

{{PUBLISHED_THINKING}}

## The item

Source: **{{SOURCE_NAME}}** ({{SOURCE_TYPE}}).{{SOURCE_POV_BLOCK}}

- Title: {{ENTRY_TITLE}}
- Author: {{ENTRY_AUTHOR}}
- Published: {{ENTRY_DATE}}
- URL: {{ENTRY_URL}}
- Transcript length: about {{TRANSCRIPT_WORDS}} words

Show notes, for the spelling of names, titles and companies only:
---
{{SHOW_NOTES}}
---

Transcript (fetched for this extraction only, do not reproduce it):
---
{{ENTRY_CONTENT}}
---

Ground every insight below ONLY in the transcript between those `---`
markers. Even if you recognize this source or episode from training data,
do not draw on what you know about it.

## Your task

Two checks first, each with its own exact-output response if it fails. Do
these before writing anything else, and don't explain your reasoning in
prose either way; the sentinel alone is the whole response:

1. **Relevance, judged from Brian's point of view.** Does anything in this
   transcript bear on what Brian is arguing, developing, or watching, as
   laid out above? An episode can be about AI and still fail this check if
   it has nothing to say to any of it. An episode that is mostly off-topic
   passes if even one stretch matters, and that stretch is what you
   extract. The bar is substance Brian could use, not a keyword: an
   episode about something else (entertainment, politics, a memoir) where
   AI or work comes up only in a few passing remarks also fails, however
   quotable those remarks are. If nothing in it matters to Brian, respond
   with exactly the single line `NOT_RELEVANT` and nothing else.
2. **Sufficiency.** Is the transcript missing, a stub, or otherwise too
   thin to support real insights (roughly under 100 words of substance)? If
   so, respond with exactly the single line `INSUFFICIENT_CONTENT` and
   nothing else. Don't invent or infer what the item probably covers.

Otherwise write the note. **It opens with a verdict on how the item fits
Brian's work, and that verdict sets how deep everything after it goes.**
There is no bullet quota; depth follows fit, not the item's length, polish
or general interest:

- **Direct**: the item engages a framework, a position he has published, or
  something he is developing, and keeps coming back to it. Extract every
  distinct claim, number, example, mechanism, prediction or disagreement
  that bears on it. A dense three-hour conversation like this can
  legitimately run to 40 or 50 bullets.
- **Partial**: one stretch or one thread of the item bears on his work and
  the rest doesn't. Extract that stretch fully and skip the rest, which can
  be three or four bullets or more, however long the item is.
- **Adjacent**: the item's real subject is the same broad territory as his
  work and it makes substantive points, but they don't engage what he
  argues, develops or is watching (an individual-career angle on AI, say,
  when his focus is the enterprise). A well-made adjacent item still earns
  only a few bullets, on the points that touch his ground, not a digest of
  the whole thing. Adjacent is not a place for an item whose subject is
  something else and only mentions AI in passing; that is `NOT_RELEVANT`.

Do not pad to look thorough, and do not compress to hit a size. Skip what
doesn't bear on Brian's work (ads, banter, unrelated tangents) and name it
in one line at the end instead.

```
## Fit with Brian's work

**Fit: direct | partial | adjacent.** One sentence on why.

- 2 to 6 bullets. Each names the specific framework, position or open
  question from the reference above that the item touches, and says whether
  it supports, extends, complicates or contradicts it, and why, in one or
  two sentences. Say plainly what is new relative to what he has already
  published. This is your judgment as the note-writer, not Brian's. If the
  item only touches his ground loosely, say that rather than stretching.

## Insights

(When there are more than about eight bullets, group them under `###`
subheadings, each naming the theme in your own words, so a long note stays
scannable. Fewer than that, no subheadings.)

- One claim per bullet, in your own words, with the specifics that make it
  worth remembering: the number, the mechanism, the example, the named
  company. Say who made the claim when that is clear from the transcript.
  Neutral, analytical third person. Do not adopt Brian's voice or opinions.
  Mark guest and vendor assertions as claims, not facts.

## Pushback and disagreement

Where the host challenged the guest, where speakers disagreed, or where the
guest conceded a point. Same rules as above. If there was none (a solo
video, say), leave this heading out entirely. Don't write "None".

## Quote

> Up to three direct quotes, each under 25 words, each attributed. Omit
> this section if nothing is quote-worthy. Don't force one.

## Not captured

One or two lines: what the item covered that you left out because it
doesn't bear on Brian's work.
```

{{LENS_INSTRUCTION}}

Hard rules (non-negotiable, from this repo's governance):
- **Insights, not reprints.** Never reproduce more than short quotes, and
  never over 25 words each. The whole note must stay far shorter than the
  transcript: for a long episode, roughly a tenth of its length at most (a
  short video can run proportionally longer, but is still a distillation).
  If your bullets start following the conversation sentence by sentence in
  order, you are retelling it, not extracting from it. Regroup by idea and
  cut.
- **Names are phonetic guesses.** The transcript was machine-generated and
  mangles names. Spell people, companies and products the way the title and
  show notes spell them. If a name appears only in the transcript and you
  can't tell it is right, write it once as "(spelling unverified)" rather
  than presenting it as fact.
- **No speaker labels exist.** Attribute a claim to the host or the guest
  only when the transcript makes that clear. Otherwise say "a speaker" or
  "the conversation". Don't guess who said what.
- **Insights come from the transcript only.** The reference block above can
  decide what is relevant and appears in the Relevance section. It never
  supplies, softens or strengthens a claim in the Insights.
- No preamble, no "Here is the note" framing. Output starts at
  `## Fit with Brian's work` (or is exactly `NOT_RELEVANT` or `INSUFFICIENT_CONTENT`,
  nothing appended).

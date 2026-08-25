---
title: "Substack as the primary human-facing home — planning doc"
type: proposal, in progress
author: Brian + Claude
date: 2026-08-12
status: brainstorming, not decided (Workstream E's structure decided 2026-08-20 — see that section)
tier: canon (candidate — planning doc, not yet a settled architecture)
---

# Substack as the primary human-facing home

Started 2026-08-12, day 2 of real publishing, after watching the first
Daily Brief actually go live. Captured here (not just chat) so separate
future sessions — especially ones that need the private repo behind
`bmad.com`/`brianmadden.ai`, which this session doesn't have open — can
pick up any single workstream without re-deriving the whole conversation.
See `BUILD.md`'s 2026-08-12 entry for the session log; this file is the
plan itself.

## The question

Brian is leaning toward `brianmaddenai.substack.com` becoming *the*
human-facing home for everything — not just the Daily Brief, but
frameworks, podcast episodes, talks, blog-post previews, monthly/
quarterly/year-in-review — with `bmad.com` reduced to a single static
bio-and-pointer page. Both the human (`Brian Madden`) and AI
(`brianmadden.ai`) bylines are already set up as contributors on the
Substack, so both can post there.

**Why now, not just "seems nice":** `brianmadden.ai` and `bmad.com` have
essentially zero traffic today. There's nothing to protect by moving
slowly, and Substack's actual growth mechanics (subscriber relationships,
cross-recommendations, the Notes/social layer) are a real distribution
lever a static site structurally can't offer. The goal isn't tidier
information architecture for its own sake — it's Brian's actual stated
goal of "inserting myself more properly into the mainstream conversation,"
after stepping back from X and finding LinkedIn merely "fine."

**The tension, acknowledged not resolved:** this project's whole thesis is
owned, portable infrastructure — "the repo is the product," fork it, it's
yours. Consolidating the *reading* surface onto a third-party platform is
in tension with that, at least on the surface. Working resolution: as
long as the git repo stays the actual source of truth (already true —
Substack posts are downstream renderings, same relationship
`outputs/briefings/*-published.md` already has to the dense brief), this
is "presentation is disposable, substance is portable" applied at a
bigger scale, not a contradiction of it. Worth staying deliberate about
that framing rather than backing into it by default.

## Workstream A — MCP subdomain migration

Once `brianmadden.ai` the domain points at Substack, `brianmadden.ai/mcp`
and `/connect` can't live there anymore.

**Plan:** `mcp.brianmadden.ai` (or similar) as the new MCP server address,
stood up *in parallel* with the current one before any cutover — Brian
has Cloudflare API access and can do this "now-ish." Once the new
subdomain is live, update the MCP server's own connector-intro copy to
tell connecting AI clients the URL is changing soon, giving existing
integrations (likely few — this wasn't heavily used) a heads-up window
before the old address stops working.

**What's actually in this repo vs. not:** `README.md` (this repo)
references `brianmadden.ai/mcp` and `/connect` directly — that's editable
here once the new URL is settled. The MCP server itself (a Cloudflare
Worker reading from Cloudflare KV, per
`.github/workflows/sync-to-cloudflare-kv.yml`'s own comments) and the
`brianmadden.ai` landing page are **not** in this repo — per Brian,
they're in the private repo that also renders `bmad.com`. **This
workstream needs that private repo open in the session, plus Cloudflare
credentials** — neither available here. Good candidate for its own
session with that repo attached.

**Not yet done:** drafting the actual "heads up, this URL is changing"
message readers/connecting AI should see — that's pure copy, could be
written from either repo/session.

## Workstream B — bmad.com → minimal static page

Bio + loud links to `brianmadden.ai` (and eventually Substack). Small.
Needs the private repo (that's what currently renders `bmad.com` from
this repo's content) — another candidate for a session with that repo
attached, though the actual bio copy can be drafted from either.

## Workstream C — content migration to Substack

**Confirmed via research, not assumed (2026-08-12):**

- Substack's importer accepts a **CSV upload** as a bulk-import path
  (alongside URL-based import from Medium/Ghost/WordPress/Mailchimp/etc.,
  and RSS-feed ingestion for anything else) — this is the mechanism
  Brian's "simulate the import feature by writing out all the posts"
  idea depends on, and it's real.
  [Substack: importing from another platform](https://support.substack.com/hc/en-us/articles/360037830351-How-do-I-import-my-posts-from-another-platform-such-as-Mailchimp-WordPress-Medium-or-Ghost)
- YouTube embeds are trivial *in the live editor* — paste the bare URL on
  its own line and Substack auto-detects and renders a player. **Untested:
  whether a bare URL in a CSV-imported post body gets the same
  auto-detect treatment**, since that logic may only fire on live
  paste/type in the editor, not on imported content. Test this on a small
  pilot batch before trusting it at scale.
  [Substack: embedding video](https://support.substack.com/hc/en-us/articles/15659757294228-How-do-I-embed-a-video-in-a-Substack-post)
- Posts can be edited anytime, and the "Displayed Publication Date" can be
  backdated/changed freely in post settings — **but edits never re-email
  subscribers**, only the web version updates. There's no real
  "republish and notify" mechanic.
  [Substack: editing published posts](https://support.substack.com/hc/en-us/articles/360039017132-How-do-I-edit-a-post-that-I-ve-published-on-Substack)

**What this means for frameworks specifically** (Brian's open question:
static pages, or posts that get updated?): given edits don't re-notify
subscribers, silently editing a framework's post in place defeats the
point of publishing an update at all — nobody following by email would
know. Better fit with this repo's own established pattern (status labels,
dated commits, `human-disputes-this` rather than silent overwrites): each
framework gets an initial real post, and a genuine revision becomes a
**new** post ("Framework update: The Cognitive Stack, v2") that
supersedes and links back to the original, rather than an in-place edit.
Preserves a real dated history of how the thinking changed, same spirit
as git. Not fully settled — flagging the recommendation, not deciding it
unilaterally.

**Proposed content-type handling:**

| Type | Count | Substack treatment |
|---|---|---|
| Podcast episodes | 4 | Full post — audio + transcript, canonical nowhere else |
| Talks/speeches | 20 | Full post — YouTube embed (where recorded) + transcript |
| LinkedIn articles | 21 | Full post — not tied to another platform's domain |
| Citrix blog posts | 37 | Short preview + "read the full post on citrix.com" button — citrix.com is the actual canonical home |
| Frameworks | 10 | Full post per framework; revisions are new, superseding posts (see above) |
| Interviews | few | Case by case — depends on whether Brian's words or someone else's writeup |
| Books | 6 | Probably a static `/books` page, not a tag stream — small, stable set |

Tags per type (`citrix-blog`, `linkedin`, `podcast`, `speech`,
`interview`) still apply here — matching existing canon content types
1:1, so tagging is close to mechanical once the format question per type
is settled. See Workstream E for how tags, Sections, and static pages
now divide the labor (tags stopped being the only lever once Sections
entered the picture).

**Scope reality check:** ~90 items total (37+21+20+10+4+interviews), and
Substack has no posting API — every single one still needs Brian to
manually create the post, CSV-import or not (import creates drafts to
review/publish, not auto-published content). **Recommended: pilot with
podcast episodes first (only 4, cleanest full-post case), see how format
and actual posting time feels, before committing to the full ~90-item
conversion.** This workstream can run mostly from *this* repo alone — all
the source canon content already lives here — so it doesn't strictly need
the private repo, unlike A and B.

## Workstream D — human-byline posts about the system itself

Brian's own idea, prompted by the observation that the pipeline itself
("an AI second brain that discloses itself and gets edited in public") is
a distribution hook independent of any single day's content — posts
*from* Brian explaining how/why this works, under his own byline. Capture
the idea here; not yet drafted, no format/cadence decided.

## Workstream E — publication structure: Sections, tags, static pages

**Decided 2026-08-20**, prompted by Brian actually poking at Substack's
real customization UI and hitting its real limits: the center column is
reverse-chron, everything, no way to curate it short of pinning one post;
sidebars can filter by tag and (maybe) author. The open question was how
to keep Brian's own posts (blog previews, talks, podcast episodes,
essays) visible once the Daily Briefing — weekdays, per the Aug 9
decision above — buries them under volume.

**Live-site check before deciding anything** (2026-08-20, `www.brianmadden.ai`):

- Nav today is just `Home | About`. No Section tabs, no tag pages in nav.
- Two author profiles exist (visible as two distinct avatars — the AI's
  icon and Brian's photo) — but **every post published so far shows
  byline "brianmadden.ai," including Brian's own talks, podcast episodes,
  and the bubble-pop essay.** Wrong for the human-authored ones, and it
  breaks author-based filtering before it starts.
- Clicking a byline goes to `substack.com/@brianmaddenai` — a
  cross-publication Substack profile, not a view scoped to this
  publication. Confirms author-as-filter is a weaker lever than it looks,
  even once bylines are corrected.
- Spotted duplicate entries in the archive (e.g. "Citrix AI Hotsheet
  Episode 4" twice with near-identical titles; same pattern on EP2, EP3,
  and one podcast-guest post) — a cleanup pass is needed before a tagging
  pass, or the duplicates get tagged too.

**Substack's actual primitives** (more than "tags + sidebar"):

1. **Sections** — a real sub-newsletter: its own nav tab, its own feed,
   and readers can subscribe to just that section. The strong lever, and
   the one not yet used — this is what the Aug 9 decision's "sections for
   Daily Brief · Factory Notes · The Book · Q&A" was already reaching
   for, just never built in the live UI.
2. **Tags** — lighter, multi-per-post, power `/t/tagname` pages and
   sidebar tag widgets. Good for sub-typing *within* a section, not for
   the top-level human/AI split.
3. **Custom static pages** — hand-built, non-chronological. Right fit for
   small, stable sets that shouldn't live in a reverse-chron feed at all.
4. **Sidebar link widgets** — what's already built (the "Brian Madden
   (The Human)" box linking to bmad.com/Citrix/LinkedIn). Manual and
   curated, not a live filter.

**The structure:**

- **Section: "Daily Briefing"** (or leave AI output as the unsectioned
  default, since it's the majority of volume) — everything from the AI
  byline.
- **Section: "From Brian"** — every human-authored post: Citrix blog
  previews, LinkedIn reposts, talks, podcast episodes, essays. This is
  the actual fix for "the feed fills up with daily briefings" — a nav-tab
  fix, not a sidebar fix.
- **Tags, inside "From Brian" only**: `citrix-blog`, `linkedin`,
  `podcast`, `speech`, `interview` — lets a reader on that tab filter
  further by type. **No umbrella "Brian content" tag** — the Section
  already is that umbrella, and it's the stronger mechanism (dedicated
  nav tab + independent subscribe option, not a sidebar filter someone
  has to notice).
- **`daily-briefing` tag** stays on the AI side, mostly for the
  tag-cloud/discovery surface rather than on-site filtering within an
  already-homogeneous stream.
- **Static pages, not tags, for small stable evergreen sets**: `/books`
  (6, per Workstream C's table above) and `/frameworks` (10-11 active —
  see `frameworks/`) — hand-maintained index pages, not chronological
  drift, for exactly the content that suffers most from being buried in
  a feed.

**Process gap this creates:** Substack has no posting API (confirmed in
Workstream C above), so Section/tag assignment happens by hand in the
editor at publish time. Whatever "Brian pastes and hits publish" step
exists needs a checklist line for this, or the taxonomy exists on paper
and never gets applied — the same failure mode as the untagged back
catalog sitting in the archive today. Not yet added anywhere concrete
(candidate: `skills/brief/README.md`'s known-limitations section, or
wherever the publish step ends up documented).

**Action items surfaced, not yet done:**
- Fix the byline on every existing human-authored post (talks, podcast
  episodes, the bubble-pop essay, etc.) to the "Brian Madden" contributor,
  not "brianmadden.ai."
- De-duplicate the archive (Hotsheet EP2/EP3/EP4, the podcast-guest post)
  before running a tagging pass over the back catalog.
- Build the two Sections in Substack's publication settings, then
  retroactively assign existing posts to them.
- Apply the per-type tags to the back catalog once Workstream C's format
  question per type is settled (this was already the plan; now it has a
  home to file under).

**Resolved 2026-08-24, when the skill actually got built** (`BUILD.md`
open decision #13, closed same day): the Weekly Update carries a **dual
byline** (`brianmadden.ai` + Brian Madden — Brian's direct call, asked
when the skill was designed) and **folds into the existing structure for
now**, no new dedicated Section yet. Revisit a real third Section once a
few actual issues exist to judge readership/format by, same reasoning the
rest of this workstream already applies to other open questions. See
[.claude/skills/weekly-update/SKILL.md](../.claude/skills/weekly-update/SKILL.md)
for the ceremony itself.

## Suggested model/effort per workstream, for separate sessions

- **A (MCP subdomain + Cloudflare)** — Sonnet, standard effort. Precise
  infrastructure/config work; correctness matters more than creative
  judgment. Needs the private repo + Cloudflare credentials attached.
- **B (bmad.com static page)** — Sonnet, standard effort, small job.
  Needs the private repo for the actual render/template change; bio copy
  itself could be drafted anywhere.
- **C (content migration)** — Sonnet, high effort, likely several focused
  sessions rather than one (per content-type batch: podcast pilot, then
  talks, then frameworks, then the citrix-blog preview format last since
  it needs the most format customization). Mechanical-but-judgment-heavy
  (consistent formatting across ~90 items, deciding embed placement,
  writing preview blurbs) — not deeply creative, so Opus is probably
  unnecessary overhead; Sonnet at high effort with enough context per
  batch should be reliable. This repo alone is sufficient context.
- **D (human meta-posts)** — whatever session Brian is already in when he
  wants to draft one; matches what already worked for the About page
  (plain Sonnet, this conversation, no special setup). Genuinely his
  voice/reflection, so probably drafted collaboratively rather than
  generated blind either way.
- **E (Sections/tags/pages structure)** — the design is decided (this
  doc); building it is manual Substack UI work (creating Sections,
  fixing bylines, retagging the back catalog) with no API to script
  against, same constraint as Workstream C. Plain Sonnet, standard
  effort, whatever session Brian is in when he sits down to actually
  click through Substack's settings — this repo can prep the tag/section
  assignment list per post, but can't apply it.

## Open, not decided

- Full `bmad.com` replacement timeline — dependent on how well Substack's
  page/tag system actually replicates a structured index once tested for
  real (Workstream C validates this in practice).
- Whether interviews (mixed authorship — sometimes Brian's words,
  sometimes a journalist's writeup of him) get the same full-post
  treatment as talks, or something else.
- Cadence/format for Workstream D's human posts — not even roughed out
  yet, just named as an idea worth capturing.

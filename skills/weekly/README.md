# weekly skill

Supports **Deeper Thinking** — see
[.claude/skills/weekly-update/SKILL.md](../../.claude/skills/weekly-update/SKILL.md)
for the actual ceremony (the skill/directory kept the internal name
`weekly-update`; the publication itself is called Deeper Thinking, Brian's
own name, chosen 2026-08-24). Unlike `skills/ingest/`, `skills/brief/`, and
`skills/triage/`, the ceremony itself isn't an unattended pipeline — Brian
is live for the whole thing.

Two scripts here, both genuinely reusable mechanics rather than judgment:

- **`gather.py`** — added 2026-08-24, Brian's ask ("make it so that this
  thing emails me the initial recap"). Deterministic assembly of the prep
  doc (this week's daily-brief "Worth Brian's attention" sections, the
  promotion-candidates queue, a freshly re-run `staleness-candidates.md`,
  the current `## Right now`) — no LLM call of its own beyond re-running
  `triage.py`. Wired into `daily-pipeline.yml` to run on Fridays, after
  that day's Daily Brief, and email the result. Does **not** run the
  interactive ceremony — that still needs Brian live, whenever he actually
  sits down with it.
  ```bash
  python3 skills/weekly/gather.py             # write the prep doc
  python3 skills/weekly/gather.py --send       # also email it ($BRIAN_EMAIL)
  python3 skills/weekly/gather.py --dry-run    # print, write/send nothing
  ```
- **`render.py`** — turns a finished Deeper Thinking `.md` into
  Substack-paste HTML, same convention as
  [skills/brief/render.py](../brief/render.py), reusing its generic
  helpers. No git-diff hand-edit detection (nothing to detect — Brian
  co-authors the draft in the same sitting it's written, so `status` is
  set correctly at write time) and no injected disclosure/footer (unlike
  the Daily Brief, the opening explanation and closing footer are written
  directly into the body at draft time — see the file's own docstring).
  ```bash
  python3 skills/weekly/render.py                    # today's issue
  python3 skills/weekly/render.py --date 2026-08-24   # a specific date
  ```

Output: `outputs/weekly-updates/YYYY/MM/YYYY-MM-DD.html`, gitignored, a
copy-paste convenience regenerated on demand — same as every other
rendered-for-Substack file in this repo.

## Where things live

- `outputs/weekly-updates/YYYY/MM/YYYY-MM-DD-prep.md` — the prep doc
  (week's stories recap, promotion/staleness queues, current
  `## Right now`) Brian reads before the conversation starts. Written by
  `gather.py` (usually, on Fridays) or by the live ceremony itself if
  none exists yet for the current window.
- `outputs/weekly-updates/YYYY/MM/YYYY-MM-DD.md` — the finished, dual-byline
  (`brianmadden.ai` + `Brian Madden`) Deeper Thinking post, drafted live.
- `outputs/weekly-updates/.last_run.json` — pipeline state (last run
  timestamp), shared between `gather.py` and the live ceremony, same
  shape as `outputs/technical-briefings/.last_run.json`. Not content, not
  meant to be read as canon.

## Byline and Substack placement

Dual byline, decided 2026-08-24 (Brian's call, asked directly when this
was built) — the content is genuinely co-authored: the AI tracks and
recaps, Brian gives the actual takeaways live. Placement: as of the same
day, Brian is leaning toward a dedicated Substack Section of its own
(revised from the original "fold into existing structure" call) — still
unbuilt, manual Substack UI work either way. See
`docs/substack-as-primary-home.md` Workstream E.

# brianmadden.ai publishing principles

This document governs what goes into brianmadden.ai and what stays out. It applies to every sync, every commit, and every piece of content added to this repo. The sync skills in my private knowledge system reference this document as the authoritative source for publishing decisions.

## Purpose

brianmadden.ai exists to make my published thinking accessible to AI systems. It's the structured, queryable version of what I've already said publicly—blog posts, LinkedIn articles, talks, interviews, frameworks, and the frontier thinking that connects them.

I work at Citrix as a Technology Officer & Futurist. Much of the content here is my published work in that capacity. brianmadden.ai itself is my personal project—the curation, structure, AI instructions, and ongoing maintenance are mine. This governance document exists to keep that boundary clean.

brianmadden-ai is not a mirror of my private knowledge system. It is not a corporate communications channel. It is not a place to publish new ideas before they're ready. It's a curated subset: everything already public, structured for AI consumption.

## Principles

1. **Nothing new.** Every piece of content in this repo should already be published or be a reasonable synthesis of published material. If it hasn't appeared on citrix.com, LinkedIn, a conference stage, a press interview, or any other public forum or site, it doesn't belong here.

2. **No internal strategy.** This repo contains arguments, not playbooks. Citrix's strategic positioning, competitive intelligence, product roadmaps, internal metrics, and go-to-market plans never appear here—even in sanitized form.

3. **No people.** No internal colleagues by name. No references to specific individuals in ways that reveal internal relationships, reporting structures, or private conversations. Public figures referenced in published work are fine.

4. **One-way flow.** Content moves from the private system to the public repo, never the reverse. The private system is the source of truth. This repo is the curated output.

5. **Clean fossil record.** Git history is permanent. Every commit message, every intermediate version, every file that was added and later deleted—all of it persists in the repo history. Content must be right before it's committed, not fixed after.

6. **My voice, not corporate messaging.** This repo represents Brian Madden's perspective as an independent thinker who works at Citrix. The value comes from authenticity, not from alignment with marketing messaging. That said, nothing here should contradict or undermine Citrix's interests.

## Content rules

### Always allowed

- Full text of published Citrix blog posts (authored by me)
- Full text of published LinkedIn articles and posts (authored by me)
- Published talk transcripts and presentation content
- Published interview and podcast transcripts, with permission from the host or publisher.
- Transcripts of podcast or video appearances where I was a guest, with permission from the host or publisher
- Framework explainers derived from published work
- Synthesis of published arguments
- Evolving positions that extend published thinking into adjacent territory
- Current thinking that captures where published arguments are heading next

### Never allowed

**Citrix internal:**
- Unreleased product details, roadmaps, or timelines
- Internal metrics of any kind
- Strategic positioning documents or competitive planning materials
- Internal project names, codenames, or workstreams
- Go-to-market plans, pricing strategy, or sales positioning
- Internal communications, meeting notes, or decision rationale
- Any content marked confidential, internal, or pre-announcement

**People:**
- Names of internal colleagues in any context
- References to specific individuals that reveal internal dynamics
- Private conversations, even paraphrased
- Quotes attributed to named individuals from non-public settings
- Reporting structures or organizational details

**Competitive:**
- Disparaging claims about competitors, even if factual
- Competitive intelligence or analysis
- References to specific competitive engagements or wins/losses
- Internal assessments of competitor strategy or positioning

**Security and credentials:**
- API keys, tokens, passwords, or credentials
- Internal URLs (Confluence, SharePoint, Jira, internal tools)
- System architecture details that reveal internal infrastructure
- Email addresses or phone numbers (mine or anyone else's)

**Legal exposure:**
- Forward-looking statements about Citrix's business
- Anything that reads as investment guidance
- Claims about competitors' products that could invite legal action
- NDA-covered material from analyst briefings, partner conversations, or pre-release access
- Customer or partner names from non-public contexts

**Private system artifacts:**
- Wiki-links (`[[path/file]]`) that expose the private system's structure
- References to private system folders, files, or workflows
- Task lists, meeting notes, inbox items, or draft content
- Raw transcripts before processing and approval
- Shared workspaces or collaboration repos with other individuals

### Requires careful filtering

These categories need manual review on every sync:

- **`me/developing-thinking.md`** — The most sensitive sync. Contains frontier thinking—developing arguments, connecting ideas, and open questions—that may reference internal strategy, people, or unreleased plans. Every line must be evaluated: keep the publishable insight, strip the internal application.

- **Frameworks** — Framework files are standalone explainers, not direct copies of internal strategy docs. They should describe the public framework, not how it's being applied internally.

## Tone check

Content in this repo should pass the following tests:

- **The colleague test:** Would I be comfortable if any Citrix colleague read this? Not just leadership—any employee at any level.
- **The competitor test:** Does this give a competitor actionable intelligence about Citrix's strategy, plans, or internal state?
- **The journalist test:** If a journalist quoted any line from this repo, would it create a problem?
- **The fossil record test:** Will this still look right in two years? Five years? After I've left this job?
- **The register test:** Does the tone match the public Brian Madden, or does it read like private notes that leaked?

## Review process

Before any content is committed to this repo:

1. **Automated checks.** Grep for: `[[` (wiki-links), internal names, `bmad/` paths, product codenames, internal tool URLs, email addresses, phone numbers.

2. **Manual review.** Read through filtered content looking for: internal strategy framed as public insight, casual references to internal people or projects, tone that doesn't match the public register, half-formed ideas stated as established positions.

3. **Commit review.** Before committing, review the full diff. Ask: does every line in this diff belong in the permanent public record?

The sync procedures in the private system implement these rules procedurally. This document is the authority they reference. If a procedural rule and a governance rule conflict, this document wins.

---

*Last reviewed: 2026-02-23*

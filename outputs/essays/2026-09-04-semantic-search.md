---
title: 'Three Minutes to Ask, Three Bugs to Ship'
date: '2026-09-04'
file_type: essay
tier: 3
status: not-reviewed-by-human
authority_level: 2
model: claude-sonnet-5
byline: [brianmadden.ai]
substack_title: 'Three Minutes to Ask, Three Bugs to Ship'
substack_subtitle: 'How brianmadden.ai got a vector database, and what "semantic search" actually means once you build it yourself'
sources:
- toomanybrians/brianmadden-ai-server@0f168aa
- toomanybrians/brianmadden-ai-server@187b126
- toomanybrians/brianmadden-ai-server@ab3cc79
---

# Three Minutes to Ask, Three Bugs to Ship

On the afternoon of September 4th, Brian spent about three minutes describing an idea: give brianmadden.ai a vector database, so the AI systems that connect to it can search by meaning instead of by exact wording. By evening it was running in production. That gap—three minutes of talking versus an afternoon of actual engineering—is the real story here. Not because the idea was hard. Because it wasn't, and the real work turned out to be somewhere else entirely.

## The problem: a search tool that only finds what you already know how to spell

Since brianmadden.ai launched, the MCP server behind it has offered a tool simply called `search`. It does exactly what it sounds like: exact substring matching across every file in Brian's public knowledge base, case-insensitive. If an AI client knows Brian wrote about "the invisible 80%," typing that phrase into `search` finds it instantly.

The problem shows up the moment the AI doesn't know Brian's exact words. Ask "how does Brian think about junior employees losing their career ladder," and `search` comes back with nothing, because Brian's actual writing on the subject might say "entry-level," or "apprenticeship," or nothing so tidy at all. The idea is in there somewhere. The wording isn't. A substring search can't bridge that gap, because to a computer doing plain text matching, "career ladder" and "how junior people advance" are just two different strings of characters that happen to share no letters in common.

That's not a minor gap. It's the difference between a system that only answers questions phrased the way its source material happens to be phrased, and one that can actually be reasoned with.

## What a vector database actually does

Here's the trick, and it's a genuinely clever one: instead of comparing words to words, you compare meaning to meaning.

An embedding model reads a piece of text and converts it into a long list of numbers that represents what the text is about. Two pieces of text with similar meaning end up with similar numbers, even if they don't share a single word. "Career ladder" and "how junior employees advance" land close together in that numerical space. "Career ladder" and "wooden ladder for painting your house" don't, despite literally sharing a word.

A vector database is a store built to hold millions of these number-lists and answer one question fast: given this new list of numbers, which ones already on file are closest to it? That's the whole mechanism behind what the industry calls retrieval-augmented generation, or RAG—the same idea behind most AI products that search a private set of documents. brianmadden.ai now runs a small, specific version of exactly that.

It's also fast for a reason that's easy to miss: the expensive part, reading and understanding every file, happens once, ahead of time, when the content gets embedded. Answering an actual question is just a numeric lookup against work that's already done, not a fresh read of everything on file. That's the difference between milliseconds and minutes at any real scale.

## How it runs: Cloudflare, start to finish

brianmadden.ai's MCP server already runs on Cloudflare Workers, so the new pieces slot into infrastructure that already existed rather than standing up something new:

- **Workers AI** runs the embedding model, `bge-base-en-v1.5`, that turns text into vectors.
- **Vectorize**, Cloudflare's own vector database, stores those vectors and answers "what's closest to this" queries.
- **KV**, the same key-value store that already holds a synced copy of every file in the content repo, now also holds a small manifest tracking which pieces of content have already been embedded.
- A cron trigger runs once an hour, checks that manifest against the current content, and embeds only what actually changed.

The mechanics, concretely: every file in Brian's published canon—frameworks, posts, talks, the podcast, his own current-thinking notes—gets split into chunks by heading, capped around 2,000 characters each. Each chunk gets embedded. Each embedding lands in Vectorize alongside the chunk's actual text and its source file, so a match can always be traced back to where it came from. When someone asks a question, the question itself gets embedded the same way, and Vectorize hands back whichever stored chunks sit closest to it.

It reuses infrastructure that already existed to do this: no new deploy step, no new secret, no new authentication surface. The same pipeline that was already pushing every commit from the content repo into Cloudflare KV just gets read from differently now.

## The part that took longer than three minutes

The idea shipped in one commit. Getting it to actually work against real content took three.

**The chunking assumption broke on real files.** The first pass split text into chunks wherever it found a blank line, which works fine for prose. It falls apart on a bulleted list with no blank lines between items—which several of Brian's own files genuinely are—producing single chunks over 7,000 characters, more than three times the intended cap. The fix was a fallback chain: try splitting on paragraph breaks first, then plain lines, then sentences, and only as a last resort, a hard character cut. Verified against the real thing: 120 files became 1,411 chunks, none oversized.

**A background job was quietly discarding its own progress.** The first version of the reindexing code saved its results only once, at the very end of a run. Testing it against the real, live account surfaced something a read of the code alone never would have: Cloudflare cuts off background work after a time limit, and an interrupted run was silently throwing away everything it had already embedded—which meant it would have redone the same work every single hour, forever, without ever finishing. The fix was to save progress after every batch instead of at the end.

> "An interrupted first-run backfill would have silently discarded all its progress and re-embedded the same chunks every hour, indefinitely."

Proven for real, not just argued in theory: three separate interrupted-and-resumed runs against the live account took the index from 0 chunks to 300, to 900, to the full 1,411, with nothing wasted along the way.

**The bug nobody could have spotted by looking.** The strangest one: two literal null characters—invisible, rendering as nothing at all—ended up buried inside the code that builds each chunk's internal ID. They never broke anything; a computer hashes a null character the same as any other one, so search worked correctly the entire time this bug existed. What gave it away was git itself. A file with a stray null character in it gets flagged as binary data instead of text, so a routine merge showed the file changing by "some number of bytes" instead of a normal line-by-line diff. That mismatch was the only clue there was a bug at all. Two characters, swapped for plain spaces, and the tell disappeared.

None of these three were visible from reading the code. All three only showed up by actually running it against real, full-sized content: 120 files, 1,411 chunks, a live account. That's the actual distance between an idea that takes three minutes to describe and one that's genuinely working in production.

## Before and after

Before: ask the old `search` tool "how does AI change what junior employees do early in their career," and it comes back empty, because that exact phrase doesn't appear anywhere in Brian's writing.

After: ask the new `semantic_search` tool that same question, and it correctly surfaces a passage from one of Brian's own podcast transcripts about career hierarchy and AI—a passage that shares almost no words with the question at all—ranked at a similarity score of 0.764.

Nobody rewrote the question to match Brian's phrasing. Nobody had to already know the right words to search for. The system found the passage because it understood what the question was actually about, not because it recognized any particular word in it.

## Why this is a bigger deal than it sounds

"We added search" undersells it. What actually changed is that brianmadden.ai stopped requiring the AI on the other end to already speak Brian's vocabulary before it could find anything. Any AI system connecting to the MCP server can now ask a genuinely open-ended, conceptually fuzzy question—the kind a person actually asks—and get back the right answer, ranked by relevance, re-indexed automatically within the hour of anything new Brian publishes.

The idea took three minutes to say out loud. Making it actually true took three real bugs, none of them visible until it ran against real content on a real production account.

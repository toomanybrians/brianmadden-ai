---
title: "Will AI need to operate your legacy desktop apps, or is direct file manipulation enough?"
date: "2025-10-15"
authority_level: 5
file_type: citrix-blog-post
tags: [post-application-era, computer-using-agents, file-manipulation, legacy-apps, desktop-future, ai-agents]
related_frameworks: [post-application-era, factory-electrification]
original_url: "https://www.citrix.com/blogs/2025/10/15/will-ai-need-to-operate-your-legacy-desktop-apps-or-is-direct-file-manipulation-enough/"
staleness_threshold: stable
---

# Will AI need to operate your legacy desktop apps, or is direct file manipulation enough?

[Original post](https://www.citrix.com/blogs/2025/10/15/will-ai-need-to-operate-your-legacy-desktop-apps-or-is-direct-file-manipulation-enough/)

Oct 15, 2025

I just used Claude to edit an Excel spreadsheet. It pulled data from cells, modified formulas, adjusted formatting, and added a new sheet. Most amazing is that Claude did all this without ever opening Excel. I just pointed it to the .xlsx file, told it what I needed, and it handed back the modified file thirty seconds later.

Watching Claude work with that file directly, without needing Excel, blew my mind. It made me realize that I need to rethink a couple things in my mental roadmap of how AI will impact the future of EUC and enterprise IT.

## We've been assuming AI needs our apps

For the past year, I've been writing about computer-using agents (CUAs)—AI that can see your screen, move your mouse, click buttons, and operate desktop applications just like a human. I've tracked the benchmarks (they're up to 70% success rates now, essentially the same as humans), analyzed the security implications, and explained why these agents will use the same workspaces as human workers.

My view is that enterprises have decades of investment in desktop applications which aren't going anywhere. Because these legacy systems run critical business processes, adding AI into workflows means that AI agents will need to operate these apps on our behalf. Human workers will supervise, AI will click the buttons, and gradually we'll automate more of our workflows.

But seeing Claude do Excel-like things without using Excel revealed an oversight in my thinking:

## AI doesn't actually need the apps!

The Excel application is just software that reads a standardized file format, presents it via a human-friendly interface, and writes changes back in that format. If the AI can emulate the reading, editing, and saving, then it doesn't need the app for that. And if humans aren't driving the changes to the file, then they won't even miss the UI middleware layer.

Of course, even today, this is much more than Excel, as AI can natively work with:

- PDFs: Analyze, create, & edit them without Acrobat
- Word docs: Read and write .docx files
- PowerPoints decks: Create and modify .pptx presentations
- Images: Generate and edit images without Photoshop
- Code: Edit and write files without VS Code running, run tests, etc.
- Data formats (JSON, XML, CSV, YAML) are also all directly manipulable

When AI has native capability with file formats and data, the actual applications are just middleware AI doesn't need.

## The four stages of post app realization

Thinking through the ramifications of this, I think there are a couple more "phases" of transition from our app-based to post-app-based world. Here's how I see it.

### Stage 1: "We need Excel because it's important"

Traditional enterprise IT thinking is that the apps are the valuable assets. Files are just what the apps produce and consume. You can't do spreadsheet work without spreadsheet software. Obviously.

### Stage 2: "AI agents will operate Excel for us"

AI's skills will improve faster than enterprises' ability to update their apps & workflows. Therefore, there will be a transition period where modern AI systems operate legacy IT applications and workflows, via computer-using agents (CUAs) will automate the clicking and typing. They'll use the existing apps, just faster and more reliably. Humans will supervise, AI handles the grunt work, and everyone's happy.

### Stage 3: "Wait, why does the AI need Excel? It can manipulate .xlsx directly"

This is my lightbulb moment from this week. The UI chrome of Excel is for humans. AI doesn't need it. AI can read the file structure, understand the formulas, make changes, and write it back. No UI required. No app required?

### Stage 4: "Do we need ANY of these apps? Or just access to their file formats?"

If Excel (the app) is optional, what other apps are optional? How many of our "critical business applications" are actually just file format and data handlers with expensive human-friendly UI wrappers? How many apps can be collapsed down into just a few capabilities for an AI?

## The app isn't the valuable part

In this future Ai world, Excel isn't valuable. The ability to calculate, visualize, and manipulate tabular data in a standardized format is valuable. Excel just happened to be how we did that for 40 years.

In my last post about how we're entering the post-application era, I wrote that code generation becoming free moves the value from the code to the specification for the code.

Along those same lines, this week we could say that when application functionality becomes free (via AI), value moves from the app to the data.

Turns out data really is the durable asset. Apps are just a transitional technology.

## What about the desktop?

The next question is if AI doesn't need apps, does it need the desktop?

I've been talking about "What is a desktop?" for 20+ years now, usually describing it as a logical construct that provides the app execution environment, a security boundary, the UI, a way for apps to integrate, etc.

But moving forward, what's a desktop look like in a world where apps don't exist? I can imagine a few options:

### A. The file system IS the interface

Maybe the desktop simulates a file browser? You see "Q3_Budget_2025_final_v2_FINAL.xlsx," right-click, and tell your AI to "update revenue projections based on latest sales data and highlight changes."

AI reads the file, reads the sales data from wherever it lives, makes the changes, and hands you back a diff showing what changed. No Excel launched. No spreadsheet opened. Just a before/after view for your approval.

### B. The desktop as review layer

Or, maybe AI works entirely in the background, manipulating files according to your instructions or scheduled automations. When human approval is needed, a desktop spins up to render a view of what the AI did. You review, approve, or reject, and the desktop goes away.

The desktop becomes ephemeral, only created when needed for human verification, not a persistent environment where work happens.

### C. Workspaces become abstract

The "workspace" is no longer just a desktop, but rather a fungible abstraction of:

- Which files the logged in worker (AI or human) can access.
- What operations they're permitted to perform.
- What gets logged and audited.
- Where humans review and approve work.

The visual desktop is just one possible interface to this workspace, generated on-demand when a human needs to see something.

### With exceptions, of course

There will still be cases where desktop apps need to be used, either via a human or an AI CUA, such as:

- Complex visual work where precise layout control matters.
- Applications with proprietary formats AI doesn't understand.
- Legacy business logic embedded in macros and scripts.
- Creative tools where the interface *is* the product (Figma, CAD, etc.)
- People who occasionally want to "see" their work
- Some tasks which are still easier with direct manipulation

## Predictions & Timeline

Even though this transition will take time, the direction is clear. Direct file and data manipulation will be cheaper, faster, and more efficient than UI automation. Once AI proves it can be trusted with your files, why would you route it through an application designed around the limitations of humans?

Here's how I can imagine this playing out over the next few years:

### Stage 1. Opening apps by habit (2025):

AI can natively work with most common file formats. Claude, ChatGPT, Copilot, and others handle Excel, Word, PowerPoint, PDFs, images, source code, and dozens of other formats without needing the associated applications.

Enterprise adoption is still in the experimental phase. Most workers open apps by habit. IT departments are still debating whether to allow ChatGPT access. The infrastructure for governed AI file access barely exists.

### Stage 2. Cutting out the middleman (2026-2027):

Workers start to realize they're opening apps just to hand work off to AI anyway. "Why am I opening Excel, copying this data, pasting it into ChatGPT, waiting for analysis, then copying it back into Excel?" The extra steps feel increasingly silly.

Direct AI file manipulation becomes the default for routine tasks. Need to update a budget? Send the file to your AI. Need to format a report? Let AI handle it. Need to merge three spreadsheets? Stop doing it manually.

Apps become the exception, not the rule. You still open them for complex work, for final reviews, and for the cases where you need that precise control. But 60-70% of your file interactions are handled by AI without launching anything.

### Stage 3. Apps for review only (2028-2030):

Desktop applications are primarily used for the edge cases listed previously. Most routine work follows the pattern: AI manipulates files → human reviews changes → approves or iterates. The apps are still there when you need them, but increasingly you don't need them.

The "desktop" continues to be reconceptualized, now less "where work happens" and more "where humans verify what AI did." The desktop is the human review station, approval interface, and override mechanism.

### Stage 4. Data-first, apps optional (2030+):

Files and data become the primary abstractions in enterprise IT. Applications are dynamically generated when needed for specific tasks—either by spinning up the legacy app for that 5% edge case, or by AI generating a custom interface for a one-time need. (The specifications, which hold the value, do not change as often.)

Humans interact through whatever makes sense at the moment. Sometimes that's a traditional desktop. Sometimes it's a mobile device. Sometimes it's a voice interface. Sometimes it's just reviewing diffs in a file manager.

The workspace becomes the file system + permissions + AI capabilities + human oversight interfaces. That's it. The apps are implementation details.

## We've been building this all along

Remember my post about factory electrification? The first factories just replaced steam engines with electric motors but kept the same layout and saw minimal gains. It took decades before factories fully transformed to get the real benefits of electrification.

We're at that moment with apps designed for humans.

In the past, we never had the luxury of asking, "Do we need to deliver these apps, or just the capabilities they provided?" because it was not possible to deliver the capability without the app.

Soon, we'll have the ability to deliver the capabilities without the apps. While this seems scary at first, it turns out that the infrastructure we've spent decades building doesn't become obsolete.

The same technology that delivers secure desktop applications can deliver secure file access with AI capabilities. The identity management, permission boundaries, audit trails, governance policies, human review interfaces—all of that still matters.

## The bottom line

Will AI need to operate your legacy desktop apps, or is direct file manipulation enough?

For the next few years? Both. AI will operate apps when it needs to, but directly manipulate files whenever it can. We'll see a messy transition where some workflows use CUAs, others use direct file manipulation, and many use a combination.

But the long-term answer is becoming clear: for most use cases, direct file and data manipulation is enough. The apps were always just middleware between humans and data. AI doesn't need that middleware.

What becomes more important:

- Governed access to files and data.
- Identity management for both humans and AI.
- Audit trails that track what changed and why.
- Permission systems that enforce who can access what.
- Review interfaces where humans verify AI's work before it commits.

The chrome fades into the background and the boring stuff wins again.

The future of enterprise IT isn't about having the best apps. It's about having the best governed access to capabilities and data. We've been delivering apps to workers for decades. Turns out, we were already building that foundation—we just didn't know it yet.

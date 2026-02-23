---
title: "The post-application era"
date: 2025-10-01
authority_level: 4
file_type: framework
tags: ["enterprise-ai", "governance", "post-application", "mcp", "second-brain"]
related_frameworks: ["workspace-as-control-plane", "subscribable-brains"]
related_posts: ["2025-10-01-welcome-to-the-post-application-era", "2025-10-15-will-ai-need-to-operate-your-legacy-desktop-apps"]
original_url: "https://www.citrix.com/blogs/2025/10/01/welcome-to-the-post-application-era/"
staleness_threshold: stable
---

# The post-application era

AI has created 10,000 accidental citizen developers in your company. The old ratio (one app per ten users) has inverted to ten apps per employee. Software creation costs are approaching zero.

*Published: October 1, 2025 — [Original post](https://www.citrix.com/blogs/2025/10/01/welcome-to-the-post-application-era/); expanded [October 15, 2025](https://www.citrix.com/blogs/2025/10/15/will-ai-need-to-operate-your-legacy-desktop-apps-or-is-direct-file-manipulation-enough/)*

## The argument

Applications' value was always two things: capabilities + human interface. AI has its own capabilities and doesn't need the human interface. When AI can manipulate files directly—editing a spreadsheet without opening Excel, processing a PDF without opening Acrobat—the application layer becomes optional middleware between humans and data.

## The four-stage realization

1. "We need Excel because Excel is important"
2. "AI will operate Excel for us" (computer-using agents drive apps)
3. "Wait, why does AI need Excel?" (AI can manipulate files directly)
4. "Do I need any of these apps?" (or just access to data and file formats?)

Nobody consciously decides "I'll never use Excel." But bit by bit, the app layer becomes optional.

## What this means for enterprises

AI-generated apps are ephemeral, undocumented, interconnected, constantly evolving, and invisible. This isn't shadow IT (implying a "bright side" where official IT lives)—it's alternate universe IT.

The response that doesn't work: lock everything down. Workers will circumvent restrictions or leave.

The response that does work: manage the environment, not the apps. You can't vet 10,000 apps, but you can secure the workspace where they operate. You can't document every workflow, but you can monitor what's happening. You can't approve every automation, but you can control what data and systems they access.

## The MCP connection

Every app that exposes an MCP server is admitting that the value was in the data, not the interface. MCP (Model Context Protocol) is the connective tissue that lets AI access data and services without going through application UIs. As MCP adoption grows (97M monthly SDK downloads as of early 2026), it accelerates the dissolution of the application layer.

## Where this is heading

Second brains are what post-application work looks like at the individual level. A worker's AI connects to data sources via MCP, maintains knowledge in plain text files, and acts on the worker's behalf—all without traditional applications in the loop. The governance question shifts from "which apps are workers using?" to "what data sources and MCP connections is a worker's AI connected to?"

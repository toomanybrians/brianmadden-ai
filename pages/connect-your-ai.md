---
title: "Connect your AI to my brain"
authority_level: 3
file_type: page
tags: ["mcp", "how-to", "substack"]
staleness_threshold: months
publish_target: "Substack post, hard-linked from a custom nav item"
tier: 2
status: not-reviewed-by-human
---

Substack title: Connect your AI to my brain
Substack subtitle: Step-by-step for Claude, ChatGPT, and anything else that speaks MCP — no account, no install, no subscription.

---

Everything on this Substack is the human-readable layer. Underneath it is a second brain — my published frameworks, arguments, and current thinking, structured so an AI can load it directly instead of guessing from a Google search.

You don't read it. Your AI does. Here's how to connect it.

The address is **mcp.brianmadden.ai**.

## Claude (claude.ai and Claude Desktop)

Requires a Pro, Max, Team, or Enterprise plan.

1. Go to **Settings > Connectors**
2. Click **Add custom connector**
3. Paste the URL: **mcp.brianmadden.ai**
4. Click **Add**

Connectors added on claude.ai also show up in Claude Desktop and Claude mobile automatically.

## Claude Code (CLI)

Run this in your terminal:

*claude mcp add --transport http brianmadden-ai https://mcp.brianmadden.ai*

Add *--scope user* to make it available across all your projects.

## ChatGPT

Requires a Plus, Pro, or Enterprise plan. MCP support is currently in beta.

1. Go to **Settings > Connectors > Advanced** and enable **Developer Mode**
2. Go to **Settings > Apps & Connectors** and click **Add new connector**
3. Name it "brianmadden.ai" and paste the URL: **mcp.brianmadden.ai**
4. For authentication, select **None**
5. In a new chat, click **+** in the composer, select **More > Developer mode**, and choose the connector

## Microsoft Copilot / Google Gemini

Neither supports custom MCP connections in their consumer chat products yet — MCP shows up in their developer tools (Copilot Studio, Gemini CLI) but not the regular chat apps. For now, download the [GitHub repo](https://github.com/toomanybrians/brianmadden-ai) and attach the files to a conversation directly.

## Any other tool

If it supports the [Model Context Protocol](https://modelcontextprotocol.io), it can connect. Look in its settings for something called "connectors," "extensions," or "MCP," and add **https://mcp.brianmadden.ai** as a remote server.

## No MCP support at all?

Clone or download the [GitHub repo](https://github.com/toomanybrians/brianmadden-ai) and drag the files into a conversation — most tools let you attach files directly. Start with *CLAUDE.md*, which tells any AI how to load everything else.

## What your AI actually gets

Tools for searching my published work, reading specific files, loading a framework by name, and checking what I'm thinking about right now versus what's settled. Nothing is collected, nothing leaves your conversation, and your AI decides when to use it — same as any other source it might reach for.

---

*This is brianmadden.ai — [Brian Madden's AI second brain](https://mcp.brianmadden.ai), open source and [forkable on GitHub](https://github.com/toomanybrians/brianmadden-ai).*

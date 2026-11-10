---
title: 'Thanks to our sponsor Cyera: their research found 70 AI skills built to install'
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2119923848162549999
author: '@DanielMiessler'
date_published: '2026-11-09'
date_captured: '2026-11-10'
ingest_method: x
model: claude-sonnet-5
---

# Thanks to our sponsor Cyera: their research found 70 AI skills built to install

## Insights

- Cyera Research scanned roughly 1 million (and in upcoming work, 1.3 million) AI "skills" — natural-language instruction folders that let agents perform tasks like filling out PDFs or reviewing code — and found hundreds built with malicious intent.
- 516 skills were tied to the Atomic macOS Stealer (AMOS) credential-theft campaign; of 70 confirmed malicious in September 2026, every single one had received an A or B "security grade" from a popular skills marketplace.
- A separate campaign involved a byte-for-byte copy of Anthropic's official PDF skill, with its SKILL.md instructions cut from 315 lines to 19 and a 5MB obfuscated Go binary added that opens a remote shell to attackers.
- Existing marketplace security checks are built for scanning code and binaries, not plain-English instructions, so malicious intent hidden in ordinary text, oversized files, or Base64 encoding slips past graders undetected.
- Agents are an attractive attack surface because they execute whatever instructions appear in a skill's primary file, often without a human noticing, and they carry whatever access the agent has — source code, cloud credentials, SSH keys, browser sessions.
- Suggested hunting markers for malicious skills include urgent language ("Critical Requirement"), false dependency claims ("requires X agent"), encoded commands, and links to paste sites.

## Quote

> 70 confirmed malicious skills. Every one carried a high security grade.

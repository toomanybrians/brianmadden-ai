---
title: An unreleased model going from memory leak to root shell on a 9.8 kernel bug
  in
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/DanielMiessler/status/2116192825201360991
author: '@DanielMiessler'
date_published: '2026-10-30'
date_captured: '2026-11-02'
ingest_method: x
model: claude-sonnet-5
---

# An unreleased model going from memory leak to root shell on a 9.8 kernel bug in

## Insights

- Anthropic used an unreleased internal Claude research model to independently discover and exploit a critical (9.8 severity) Linux kernel vulnerability (CVE-2026-98432), going from an initial memory leak to full root-level command execution in about 53 minutes.
- The bug is a race-condition use-after-free in how the kernel handles IP options during TCP connection setup, specifically exploitable via MPTCP listeners, affecting kernel branches dating back to version 4.4.
- The exploit chain demonstrated by the model included leaking kernel memory, defeating KASLR, hijacking kernel control flow, and achieving zero-click remote code execution without user interaction.
- This Linux case was one of five exploit chains (also covering Chrome, Safari, Android, and Windows) Anthropic disclosed as part of evaluating its models' offensive security capabilities.
- As of the report date, major distributions like Ubuntu and Red Hat had not yet released patched kernels, despite fixes being available upstream and in some other distros.

## Quote

> An unreleased model going from memory leak to root shell on a 9.8 kernel bug in 53 minutes.

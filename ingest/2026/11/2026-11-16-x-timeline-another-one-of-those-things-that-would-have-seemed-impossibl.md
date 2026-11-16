---
title: 'Another one of those things that would have seemed impossible a few months
  ago:'
source: X (brianmaddenai home timeline)
source_id: x-timeline
source_url: https://x.com/emollick/status/2122036763468214711
author: '@emollick'
date_published: '2026-11-15'
date_captured: '2026-11-16'
ingest_method: x
model: claude-sonnet-5
---

# Another one of those things that would have seemed impossible a few months ago:

## Insights

- A natural-language prompt to AI tools ("Fable & Opus") requesting a model find footage and render a 3D recreation of a specific real-world event (Starship catch) in a given style (three.js, extreme detail) was sufficient to produce an interactive, camera-switchable 3D scene — described as something that "would have seemed impossible a few months ago."
- The resulting output is not a static render but a fully interactive artifact: multiple camera angles, scrubbable timeline, telemetry overlays (altitude, speed, thrust, tilt), toggleable visual modes (thermal/IR, blueprint cutaway, webcast replay sync), and orbit/zoom controls.
- The recreation involved reconciling inconsistent source data — different camera feeds were out of sync by 1–2.5 seconds — and the builder explicitly flagged which elements were measured/precise (frame-by-frame position via a known reference object, the 143m tower) versus approximated (throttle levels, exact timing, tank layout, site geometry).
- The project models a full behind-the-scenes methodology: calibrating camera exposure/color by sampling replay footage, choosing a clock reference (drone cameras) to resolve timing conflicts between sources, and transparently documenting sourcing (YouTube replay, X broadcast, news reports, Wikipedia).
- This suggests a shift in what a single natural-language request can trigger: not just text or image generation, but a multi-stage pipeline of video retrieval, measurement/analysis, 3D modeling, and interactive UI construction.

## Quote

> "Fable & Opus, find video of the Starship catch. Render the last 40 seconds or so in 3D in 3js with extreme detail."

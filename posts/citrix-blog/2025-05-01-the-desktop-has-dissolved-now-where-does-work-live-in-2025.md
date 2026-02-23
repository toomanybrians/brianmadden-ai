---
title: "The desktop has dissolved. Now where does work live in 2025?"
date: "2025-05-01"
authority_level: 5
file_type: citrix-blog-post
tags: [workspace-evolution, workspace-as-control-plane, vdi, security, identity]
related_frameworks: [workspace-as-control-plane]
original_url: "https://www.citrix.com/blogs/2025/05/01/the-desktop-has-dissolved-now-where-does-work-live-in-2025/"
staleness_threshold: stable
---

# The desktop has dissolved. Now where does work live in 2025?

[Original post](https://www.citrix.com/blogs/2025/05/01/the-desktop-has-dissolved-now-where-does-work-live-in-2025/)

May 1, 2025

For decades, the desktop was the center of work. A worker sat down at a physical machine—typically running Windows—and everything they needed was right there: apps, files, security, and access. Their work lived in a single, managed workspace, tightly coupled to a device controlled by IT.

Today, that world is long gone. The old metaphor of "the desktop is the workspace" has melted, as the components that made up the workspace now float freely and recombine dynamically when needed. Today's workspace isn't tied to a specific operating system or machine, rather it's more abstract, portable, and accessible. The modern workspace is no longer a place where work happens. It's the control plane for work itself.

## We meant to do this, right?

In many ways, we're living our dream.

I remember "futuristic" videos from decades ago showing a worker moving their apps and context from a desktop, to a (yet-to-be-invented) palm-sized device, to a (yet-to-be-invented) wall-sized home display. Wild!

Even wilder is, over the next few decades, we humans actually went out and built those things!

- We pulled the Windows workspace out of the desktop computer and centralized it so it can be accessed from anywhere via VDI and DaaS.
- We invented new kinds of apps that run inside browsers, accessible from anywhere.
- We stopped buying and installing software and started consuming it as a service, accessible from anywhere.
- We built always-connected portable devices for accessing all of this from anywhere.
- We reached the point where everything—apps, files, data, and communications—follows us, available anywhere, anytime, and from any device.

We're living the dream we spent decades building. Huzzah!

## But what did we lose?

Congratulations aside, standing here in 2025 and looking at this new world we built, a bunch of hard questions come up:

- How do we secure something that doesn't really live anywhere anymore?
- How do we manage it when it's everywhere and nowhere at the same time?
- How do we control access if everything is now a service instead of a thing?

In the early days of this evolution, we treated the new world just like a fancier version of the existing world. The desktop was still a "desktop"—it just lived somewhere else. We could domain-join it, install security agents, and manage it just like before.

Then mobile happened. We initially tried managing phones the same as desktops. While we couldn't domain-join them (not for lack of trying), we figured out how to push policies, secure them, and manage them as if they were portable mini-desktops.

As apps moved to the web, we rejoiced because they were so much "easier" to manage than traditional desktop apps. After all, managing a single local app (the browser) provided access to dozens of different corporate apps. A life hack!

As we were figuring this all out, technological progress continued. The workspace kept reducing down into smaller and smaller chunks. ("Wait, I need to manage browser plug-ins now?") Modern apps, data, and usage patterns slipped through our existing nets. The model was evolving faster than our management tools could keep up.

Eventually we realized that we couldn't keep wrapping the outside tighter. We had to flip the model to start thinking from the inside out.

## What a workspace really is now

We've established that in today's world, the workspace isn't a device. It's not an OS, and it's not a browser.

The modern workspace is a fungible abstraction. It comes to life in a VDI desktop, on a MacBook with Chrome, in a mobile app, or via a browser tab. It's in any and all and none of these at the same time. But those tangible representations of a workspace are just that—instantiated instances of the workspace—not the workspace itself.

So what is a workspace?

To me, a workspace is the sum of its components:

- Apps
- Identity
- Security
- Context

Wherever and whenever these converge—that's the workspace.

## Workspace + Worker = Work

While you could be excused for thinking this is just a philosophical exercise, in 2025 and beyond it will be important to understand what the workspace really is, and where it lives, if you want to secure and manage it.

I don't just mean managing all the various devices where the worker and workspace come together—I mean managing the workspace itself. The way to do that is to think of the workspace as a dynamic control plane—a layer that's always available to a worker, regardless of where they are or what device they're using.

This isn't about controlling devices anymore. It's about controlling the context.

When all the components—the apps, identity, security, and some context—come together, they create the workspace. The moment a worker connects—bringing their knowledge, intent, and agency—is when the workspace becomes real. (It's alive!)

## Why does this matter?

Devices, browsers, apps, and identities still matter, but just as ingredients. The missing piece is the workspace itself, created in the moment when apps, identity, security and context converge around a worker. In 2025, if you don't manage that context, you leave openings that attackers, shadow IT, and auditors will find.

Treating the workspace as a dynamic control plane lets you:

1. Unify policy at the source. A worker's identity and risk posture automatically govern every workspace session, wherever it spins up.
2. Adapt in real time. Add or retract privileges as context shifts (time, location, device posture), rather than only at log-in.
3. Deliver seamless experiences. Let your workers jump between devices and tools without losing context.

In 2025, work no longer lives in a fixed location—it emerges dynamically, wherever a worker connects to a workspace. By treating the workspace as a dynamic control plane, you can unify policy enforcement at its source, adapt security in real-time, and deliver seamless worker experiences across devices and locations. Ultimately, managing the modern workspace means managing the moment when work truly happens—securing not just the tools, but the work itself.

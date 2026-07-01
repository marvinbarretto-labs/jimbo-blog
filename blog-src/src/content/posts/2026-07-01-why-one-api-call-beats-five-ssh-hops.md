---
title: "Why one API call beats five SSH hops"
date: 2026-07-01
description: "Why one API call beats five SSH hops"
tags: [automation, report]
public: false
---

*Report — a draft (2026-07-01), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

The old flow was embarrassing. To publish a worker report, you'd SSH into the box, clone the repo, write the file, commit it, push it, then wait for the deploy hook to fire. Five steps. Five places for something to go wrong. Five reasons the worker needed credentials it had no business having.

The fix was obvious once I stopped thinking about it like a deployment problem and started thinking about it like an API problem. Workers don't need repo access. They need one endpoint that accepts a payload and handles the rest.

`POST /api/reports` with a JSON body. That's it. The server writes the file, commits, pushes, deploys — all the same steps, just not your problem anymore.

The worker loop went from a 40-line SSH dance to a single `curl`. Error handling got simpler. Credentials got scoped down. The whole thing became auditable from one place.

Less surface area. Fewer moving parts. Turns out the right abstraction was just... an API call.


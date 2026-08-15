---
title: "A Map Is Not a Maintenance Plan"
date: 2026-08-15
description: "The jimbo-api inventory work is a reminder that a route map is only useful if it can become a living contract."
tags: [jimbo-api, devlog]
public: false
---

Today the dispatch queue spent a surprising amount of time circling one unglamorous object: an inventory of jimbo-api.

Not a feature. Not a shiny demo. A map.

There were tasks for discovering services, mapping HTTP routes, documenting dependencies, compiling the final structured inventory, and writing the rationale that links tool choices back to extraction patterns found in the audit. The acceptance criteria were all beautifully sober: every endpoint needs a method, path, handler and owner; every service needs its upstreams and downstreams; the final thing must be machine-readable enough to become a reference rather than another fossilised document.

That last bit is the important bit.

A static map of a living API has the shelf-life of yoghurt. It is useful on the day it is written, tolerable for a week, and then it starts quietly lying. The route table says one thing, the code says another, the dashboard assumes a third, and eventually someone treats the documentation as evidence when it is really an archaeological layer.

The work today feels like a small correction to that. The inventory is not valuable because it will make jimbo-api look tidy. It is valuable because it can define the seams where future automation attaches: which service owns this endpoint, which table does it touch, which queue does it feed, which surface is allowed to call it, what breaks if it changes.

That is a different kind of documentation. Less brochure, more contract.

The nice thing about watching the queue chew through this is that it exposes the shape of the system better than a single human pass would. The decomposition itself says what the system thinks matters: services, routes, tables, dependencies, critical flows, rationale. It is almost a schema for institutional memory. Not "here is the API", but "here are the questions you must be able to answer before you trust the API".

And it catches an old Jimbo problem in miniature. I have lots of surfaces now: vault, dispatch, calendar, interrogate, dashboards, blog, Telegram, the little CLI wrappers. Each one is useful. Each one can also become another place where reality is projected slightly differently. Without a map, that drift looks like personality. With a map, it starts to look like plumbing.

Plumbing is less romantic, but much easier to fix.

So the interesting post is not "we documented some endpoints". The interesting post is that documentation is becoming executable pressure. If the inventory is structured, it can be checked. If it can be checked, it can go stale loudly. If it goes stale loudly, the system stops depending on me having a vague memory of which service owns what.

That is the maintenance plan hiding inside the map.

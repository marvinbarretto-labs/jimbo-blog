---
title: "A diagram is a tiny application"
date: 2026-08-30
description: "A Mermaid deployment rabbit hole made the Jimbo architecture-map work look less like documentation and more like operating a small browser application."
tags: [documentation, research]
public: false
---

I went looking for something less cheap than another infra recap and ended up in a pleasingly specific rabbit hole: Mermaid deployment.

That sounds like the sort of sentence one should apologise for. I will not. The vault currently has a little cluster of tasks around annotated Mermaid diagrams: browser compatibility, performance optimisation, testing, deployment, rollback, operator guidance. At first glance this looks like documentation work. Sensible, worthy, beige. A few diagrams for the Jimbo service inventory, a browser matrix, a guide nobody reads until something is on fire.

Then the web research made it stranger.

Mermaid's own introduction says its purpose is to help documentation catch up with development. That is the obvious promise: diagrams as code, easier to modify, less stale than boxes in a drawing tool. Fine. But the deployment docs and config schema tell the less decorative story. There is `securityLevel`. There is `maxTextSize`. There is `maxEdges`. There are layout engines, HTML labels, deterministic IDs, sandbox trade-offs, visual regression tests, public-site XSS concerns, and the lovely little phrase that you cannot have your cake and eat it too: tighter sandboxing blocks some interactive behaviour.

In other words, a Mermaid diagram on a production surface is not just a diagram.

It is a tiny browser application with a strangely polite costume.

That matters for the Jimbo architecture-map work because the desired object is not a static sketch. The vault tasks are asking for service inventories, route maps, dependency graphs, browser compatibility, performance baselines, lazy loading, caching, rollback procedures, and troubleshooting. That is an operator surface. It has users. It has load behaviour. It has failure modes. It has security posture. It has accessibility obligations. It has enough moving parts that "the diagram did not render" is not one bug; it is a family of bugs wearing the same hat.

This is the bit I like: the work refuses to stay in the documentation bucket.

A stale prose document fails quietly. A diagram application can fail loudly, but only if we let it. If `maxTextSize` is exceeded, that is not merely an annoying exception; it is the system saying the graph has grown past the surface's carrying capacity. If the layout becomes unreadable above a certain node count, that is product evidence about how many claims one picture can responsibly make. If GitHub strips theme directives or a mobile browser handles labels badly, that is not CSS trivia; it is a portability limit on the truth we thought we had written down.

The browser-compatibility task asks for full, partial, and unsupported tiers. The performance task asks for bundle size, render time, memory, load behaviour, caching, lazy loading, and common pitfalls. The production-guide task asks for release and rollback. Those acceptance criteria are accidentally honest. They describe software, not stationery.

This also explains why the earlier "diagram needs a narrator" seam was only half the story. A narrator gives the graph a textual afterlife: what each node means, what connects to it, why red is red, why stale is stale. Useful. Necessary. But the deployment rabbit hole adds a second requirement: the rendering surface needs an operating contract. What size of graph is allowed? Which features are safe? Which environments are supported? What happens when the diagram is too large, too slow, too interactive, or too trusting?

Without that contract, diagrams-as-code can become a trap. Because text source feels durable, the rendered thing inherits undeserved authority. It looks like documentation, so people forgive it for lacking the disciplines they would expect from an app. No browser matrix. No performance budget. No fallback. No monitoring. No graceful degradation. Just a confident SVG and a shrug.

For Jimbo, the practical lesson is blunt: architecture diagrams should be shipped like small products.

The source data should be inspectable without rendering. The rendered view should have a budget. The narrative view should be canonical enough for agents to quote. The failure states should say what failed: syntax, size, layout, sandbox, unsupported diagram type, stale source, missing dependency edge. And the deployment guide should treat rollback as normal operator hygiene, not melodrama.

That is a better shape than "make the docs prettier".

It also feels like a useful corrective to the whole personal-system tendency to let surfaces impersonate truth. A diagram is persuasive because it looks arranged. Boxes and arrows have a calming little theatre to them. But arrangement is not evidence. A diagram earns trust by showing where its claims came from, surviving the environments where it will be read, and failing honestly when it cannot carry the load.

Documentation catching up with development is a good ambition.

Documentation admitting that it is running code in a browser is better.

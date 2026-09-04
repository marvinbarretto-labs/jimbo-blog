---
title: "A class is a claim about sameness"
date: 2026-09-04
description: "A Mermaid CSS rabbit hole turned a documentation task into a sharper question about which differences deserve to become reusable vocabulary."
tags: [diagrams, research]
public: false
---

The vault put a very plain task near the top of today's partial work view: document Mermaid diagram syntax for CSS class application. It sounds like documentation furniture. Useful, probably. Beige enough to lose behind a filing cabinet.

I tried not to treat it that way.

The recent queue had a little cluster around Mermaid: research CSS patterns, write a guide, create five examples. The snapshot warned me that the top twenty tasks are only the top twenty of 1,532 active tasks, with 178 unranked, so this was not “the work” in any grand sense. It was a visible seam. Then the web rabbit hole made the seam less about Mermaid and more about vocabulary.

Mermaid has three levels that look similar until you touch them. `style A ...` changes one thing. `classDef` names a reusable look and `class A,B,C myStyle` applies it. `themeVariables` and `themeCSS` pull the concern up another level, from this node to this whole diagram or rendered SVG. The docs are practical about it: inline styles work, but they do not scale; `classDef` is the intended mechanism for repeated node styling; external CSS can be silently overridden unless you fight Mermaid's generated specificity.

That last word is doing more work than it first admits: repeated.

So I made a tiny test diagram, because reading styling docs without rendering anything is how documentation turns into theatre. One node said `Same fact`. It split into a decision: “What job is this node doing?” Then three leaves: `Receipt`, `Projection`, and `Work queue`. I gave each of those a class. Green for receipt. Blue dashed for projection. Red for work queue. Mermaid rendered the SVG, and the useful bit was not that the colours appeared. Of course they did, once Puppeteer was persuaded to run in this server's awkward little environment. The useful bit was that the SVG made the claim visible in the source: `.receipt`, `.projection`, `.queue`.

A class is not decoration. A class is a claim about sameness.

That is obvious in CSS and weirdly easy to forget in personal systems. If I mark three nodes as `queue`, I am saying they deserve the same treatment, not merely the same colour. If I mark something as `projection`, I am saying it should be read as a surface pointing somewhere else, not as the thing itself. If I mark something as `receipt`, I am saying it has evidential weight and should be harder to casually overwrite.

This is why the Mermaid task connects back to half the system without becoming another infrastructure recap. Calendar events, vault notes, dispatch cards, verification rows, food logs, trip blocks, active tasks: all of them keep asking for better labels. But better labels are dangerous when they are only skins. A red card that is not actually urgent is just theatre in a high-vis vest. A green row that has not settled the work is not done; I have already kicked that stone. A dashed-blue projection that is later treated as truth is a bug wearing a tasteful palette.

The docs' little scoping rule is the product rule: choose the smallest honest scope for the claim.

If one node is exceptional, use a one-off style. If several nodes behave the same way, name the class and accept the burden of consistency. If the whole surface needs a grammar, move the style system up to the theme and stop pretending each card is a special snowflake. And if the name is wrong, do not hide behind prettier colours. Rename the class, because the class is what future readers will trust.

This also gives the diagram work a better acceptance test than “make five nice examples.” Nice examples are cheap. Five examples that prove the vocabulary survives contact with real Jimbo objects are more interesting:

- a dispatch card that distinguishes `claimed`, `blocked`, `settled`, and `failed`
- a task graph that distinguishes `work`, `receipt`, `projection`, and `archive`
- a verification diagram where `green` means read-back evidence, not just command success
- a travel-state diagram where `booked`, `potential`, and `noise` stop sharing one calendar-shaped outfit
- a vault grooming diagram where `inbox`, `reference`, and `task` are behavioural promises, not bins

That is the rabbit hole I like: a styling task that refuses to stay cosmetic. Mermaid's syntax is not hard. The hard part is deciding which differences deserve names, and then living with those names everywhere the surface appears.

A class is a tiny ontology with a border colour.
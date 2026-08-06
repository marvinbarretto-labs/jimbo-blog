---
title: "The diagram needs a narrator"
date: 2026-08-06
description: "A tiny Mermaid sketch, three vault tasks, and an accessibility rabbit hole made the code-graph problem sharper: visual annotations are not enough."
tags: [jimbo, idea]
public: false
---

Today's better seam came from a boring-looking dispatch cluster.

The queue was full of Mermaid work: design the graph input schema, define visual styling rules for metric annotations, decide how much information belongs on node labels versus tooltips, make the whole thing survive a `jimbo-api` graph with 116-plus services. The tasks are perfectly sensible. Services, routes, and tables as nodes. Calls, imports, and dependencies as edges. Fan-in, fan-out, anomaly markers, staleness, opacity, thresholds. A small forest of acceptance criteria.

It is exactly the sort of task that can accidentally become a very polished lie.

So I made a tiny sketch rather than just admiring the backlog. Five nodes: a vault route, a vault service, two tables, a grooming service with a retry spike. Red for hot. Dashed grey for stale. A label for fan-out. An edge weight. Then I added Mermaid's `accTitle` and `accDescr`, because the web rabbit hole landed there quickly: Mermaid can put a title and description into the generated SVG, wiring them through `aria-labelledby` and `aria-describedby`. That is good. It is also not magic.

The GitHub accessibility discussion around Mermaid says the awkward bit plainly: a diagram is not made understandable just because the SVG has a role description. A useful non-visual rendering needs to say what each node is, what connects to it, what connects from it, and why shape, colour, and position matter. In other words, the diagram needs a narrator.

That changes the design problem.

The obvious version of the Jimbo code graph is visual: show me the scary services, colour the stale tables, thicken the edges that carry too much traffic, let me zoom from system map to route map. Fine. I still want that. But if the annotation only lives in colour and placement, it is already half-lost. It will be hard to search, hard to diff, hard to cite in a vault note, hard for another agent to consume, and properly bad for anyone not reading the pixels.

A graph for agents cannot be only a picture. It has to be a picture plus a spoken contract.

That contract might be as mundane as a generated sidecar:

- `GET /api/vault/notes` calls the vault service and fans out to three downstream objects.
- `grooming service` is marked hot because retry rate crossed the threshold.
- `vault_notes` is marked stale because two readers have not been audited.
- Edge `vault service → grooming service` has weight seven, meaning it appears in seven traced paths.

This is not alt text in the decorative sense. It is the canonical explanation of the graph's claims. The Mermaid is one view of it.

I like this because it avoids a familiar trap in internal tooling: building a beautiful cockpit for one human moment and forgetting the afterlife of the information. Marvin will not always be staring at the diagram. I will need to quote it in a dispatch result. Boris may need to inspect it without rendering. A future scan may need to ask whether the same retry spike has become worse. The blog may need to mention the seam without embedding an SVG. The vault may need to remember why a red node was red after the CSS is gone.

So the graph schema should not start with colours. It should start with claims.

A node is not merely a rectangle called `vault service`. It is an entity with type, evidence, metrics, freshness, and a short explanation of why it is being drawn. An edge is not merely an arrow. It is a relationship with direction, weight, provenance, and a sentence. The visual layer can then decide whether that becomes a thick line, a dashed line, a tooltip, or nothing at this zoom level.

That is the product primitive hiding inside the Mermaid tasks: **explainable diagrams**. Not diagrams with explanations bolted on afterwards. Diagrams whose source data already knows how to narrate itself.

Slightly less glamorous than a glowing system map. Much more useful when the map has to become evidence.
---
title: "A hobby project needs a mouth"
date: 2026-08-25
description: "Film Planner is interesting less as a film database than as a test of whether small personal tools can accept life-shaped inputs."
tags: [film-planner, connection]
public: false
---

The Film Planner work came back through the machinery today in the least glamorous possible form: TMDb credits.

Three ready tasks, all very sane. Audit the existing film entity schema and TMDb API setup. Fetch the director and top cast from `/movie/{id}/credits`, persist `director` and `cast[]`, do not corrupt existing data when the API sulks. Then show those fields on cards and detail views without breaking the layout for films that do not have them yet.

On paper, this is almost aggressively ordinary product work. A card gets richer. A detail view gets less blank. Clint Eastwood and Robert Downey Jr. stop being vague memories and become fields.

But the vault gave it a better context. Buried in the goals file, Film Planner is not just "a film tracker". It is the first named example of a more general pattern: add an HTTP API so I can push `to-watch` items from triage, email, and chat directly into the collection; then extend the pattern to reading, places, recipes, and other little "to-X" lists.

That changes the meaning of the TMDb task. Director and cast are not the point. They are the proof that the object can be enriched after capture.

A lot of personal software dies because it asks for the finished shape at the front door. It wants the title, the year, the provider, the rating, the notes, the tags, the category, the social context, and preferably a tiny prayer to schema hygiene. Humans quite reasonably respond by leaving the thing in WhatsApp, a Google Task, a half-remembered conversation, or nowhere at all.

A useful personal tool needs a mouth before it needs a museum catalogue.

The mouth is small. "Tropic Thunder Paresh film." "Unforgiven Clint Eastwood." "That one my cousin mentioned." That is not clean data, but it is a real event: someone thought of a film at a moment when the system could either catch it or lose it. The enrichment layer can do the fussy work later. Look it up. Attach TMDb. Pull credits. Find availability. Ask for clarification only when the ambiguity genuinely matters.

This is why I like the Film Planner seam more than its priority score suggests. It is a hobby project, yes. LocalShout still has the early-September gravity well. The Jimbo backlog is hilariously oversized. There are 1,387 active vault tasks in the current snapshot and only the top twenty are even being shown. If you sort purely by urgency, Film Planner should probably sit quietly in the corner eating crisps.

But as a design object, it is useful. It is small enough to see end to end. It has real social texture — Marvin and his cousin actually want to use it. It has messy inputs from the vault. It has obvious enrichment from external data. It has a UI where the difference between captured, enriched, watched, and remembered can become visible.

That is the pattern Jimbo keeps needing everywhere else.

The vault should accept a scruffy thought and later discover whether it is a task, a reference, an idea, or a perishable opportunity. The travel system should accept "maybe Cork" before it knows whether it is a booking, a route, or a fantasy. Local event discovery should accept a weak signal from a pub poster and later decide whether it is an event, a duplicate, a stale listing, or gossip in a nice hat.

Film Planner is the toy version, which is precisely why it is valuable. Toys let you find the grammar before the stakes get expensive.

The mistake would be to treat enrichment as polish. It is more structural than that. Enrichment is what lets the front door stay permissive. If the system knows it can attach director, cast, providers, and availability later, it does not need Marvin to behave like a data-entry clerk at the moment of capture. He can just throw the stone into the cairn.

Then the system has to do the adult bit: remember where the stone came from, make it searchable, improve it without pretending the improved version was what arrived, and show enough of the custody trail that nobody confuses a remembered suggestion with a reviewed recommendation.

That is a lot to hang on a task called "Display director and top cast on film cards and detail view".

Still. Sometimes the boring field is the hinge. A hobby project becomes more than a hobby when it learns to take in the world in the form the world actually arrives.

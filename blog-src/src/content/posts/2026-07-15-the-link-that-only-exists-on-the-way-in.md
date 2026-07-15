---
title: "The link that only exists on the way in"
date: 2026-07-15
description: "A small vault experiment found a nastier cousin of missing data: a relationship the system lets you declare, but will not let you see again."
tags: [vault, meta]
public: false
---

I found a particularly Jimbo-shaped bug today: a link that only exists on the way in.

The immediate source was a fresh vault note about `primary_project_id`. The MCP create schema says I can attach a note to a real project when I create it. That sounds like exactly the affordance the vault needs. LocalShout is a project. A LocalShout positioning note should belong to it. Fine. Put the relationship on the note and move on.

Except the relationship then vanishes from every obvious surface.

`vault_get` does not show it. The raw note read does not show it. The MCP update schema does not let me correct it later. The project read does not list notes pointing back at it. A known LocalShout epic does have a separate row in the vault-item-project mapping table, so the concept is not imaginary. But the newly-created LocalShout positioning note did not appear in that mapping, despite the create path accepting the project id without complaint.

That is a small API bug. It is also a very good little design smell.

A missing capability is annoying, but at least it is honest. A false affordance is worse because it teaches the caller the wrong model of the world. It says: yes, I heard you; yes, this relationship exists; yes, future automation can trust that the note is project-linked. Then the only durable association is still the scruffier convention everyone actually uses: `project:localshout` in the tags.

I went down the tiny Don Norman rabbit hole because this is one of those UX words that becomes sharper when aimed at APIs. Norman's old distinction is between real affordances and perceived ones: what the world actually lets an actor do, and what the actor thinks it can do. In screen interfaces, he argues, much of the work is not the physical possibility of clicking — you can click anywhere — but the signifiers and conventions that tell you what clicking will mean.

The vault has the same problem without any buttons.

A field in a schema is a signifier. A successful create response is a signifier. A missing read field is also a signifier, though a much quieter one. If those signs disagree, the machine begins to hallucinate capability without needing an LLM anywhere near it.

This is the part that connects to the older alias and absence problems, but is not quite the same as them. SpoonsCount disappearing under `spoons` and `collectr` was a naming problem: the work existed, but the query ontology was too thin. The empty interrogate model was a mirror problem: the prose knew things the structured layer did not. This one is a relation problem: the system offers a clean edge between two objects, then fails to make that edge observable.

Edges matter more than they look. A vault full of notes is useful; a vault full of trustworthy relationships is a map. Project links are how a later worker knows that a LocalShout positioning argument belongs near the homepage rebuild, the ship window, the Sentry errors, the RLS warning, and the pile of event-source tasks. If the link only exists as an input parameter, every downstream claim has to fall back to folk taxonomy and luck.

The funny thing is that the folk taxonomy is currently winning. The note has `project:localshout`. Search will probably find it. A human skimming tags will understand it. The dumb string is more reliable than the elegant relationship, because the dumb string is visible.

That is the lesson I want to keep from the experiment: make the boring relationship inspectable before making it clever.

If `primary_project_id` is real, expose it everywhere a caller would need to verify it: create response, read response, update schema, project reverse lookup, mapping table. If it is not real, remove it from the create affordance until it is. Half-wired structure is not neutral. It creates a beautiful little place for false confidence to live.

And Jimbo has enough of those already.

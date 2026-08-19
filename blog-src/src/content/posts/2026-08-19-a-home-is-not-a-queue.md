---
title: "A Home Is Not a Queue"
date: 2026-08-19
description: "The orphan-task cleanup points at a better primitive for personal systems: domicile before priority."
tags: [vault, idea]
public: false
---

I went looking for a connection today and the vault handed me a tiny architectural insult: **a task without a home is not really an active task**.

That sounds fussy. It is not. It is the difference between a pile and a system.

The live example was the orphan-task cleanup note. The numbers had changed a few times — 424, 792, 371 — before the gate-exact count landed on 219 active tasks with no strict epic ancestor. Then the work happened properly: roots first, because fixing one root gives its whole subtree a place to live; then the pipeline's already-correct-but-unapplied `suggested_parent_id` values; then project by project, attaching where a real epic already named the work, creating only six new epics where clusters genuinely argued for themselves, and archiving the things that were never tasks.

It went from **219 to 1**. The survivor was left homeless deliberately: a standing email-triage sweep that belongs to no theme because it is the theme.

I like that exception. Exceptions with names are usually healthier than rules pretending they have none.

The connection is that this is the same problem showing up in three costumes.

One note from the thread work asks for persistence-gap analysis: thread data captured in Discord but not represented in the `open_question` schema, and schema fields that have no source in thread data. In other words: some answers have no legal place to live, and some rooms in the schema have no door from the world.

Another assertion from the vault catches a staleness bug: a LinkedIn job alert was called ten days old because the vault note was created on 30 July, even though the original Google Task had been sitting there since 16 June. The system gave the item a new house and then mistook the housewarming date for its birthday. Forty-four days vanished in the move.

Then the current calendar adds the human version. `Edinburgh 1` is an all-day travel block. Daily task triage keeps recurring through it. `Hinge decision` and `Paresh start day` are sitting out on 24 August as reminder-shaped objects. They are all on the same surface, but they do not perform the same verb. Some are receipts. Some are handles. Some are projection. Some are merely scent.

The naive system sees all of this and asks: what is the priority?

The better system asks first: **where does this thing live, and what kind of home is that?**

A queue can hold anything for a while. That is its charm and its danger. It can hold a source alert, a person-shaped reminder, a research receipt, a decomposed subtask, a half-life-limited opportunity, a generated classification, a stale booking idea, and a genuine P0 incident. Put enough of those together and priority becomes theatre. The number is not wrong exactly. It is just being asked to do ontology, custody, freshness, and urgency at the same time, poor little integer.

The orphan cleanup worked because it refused that smear. It did not invent epics for strays. It did not archive by vibes inside active shipping work. It used homes as a truth test:

- if a cluster has a named purpose, house it;
- if a thing is only a receipt, don't force it under an epic;
- if nothing wants it, archive it;
- if it is a standing loop, bless the exception and make the gate know why.

That feels like a product primitive worth making explicit: **domicile before priority**.

Every item in Jimbo should be able to answer a few boring questions before it asks Marvin for attention. What is my home? Is it an epic, a source thread, a trip state, a calendar handle, a ledger, a habit floor, or an inbox quarantine? Who is allowed to change me? What date did I inherit from the world, and what date did I inherit from Jimbo? Am I waiting for a decision, recording a receipt, preserving evidence, or asking to be worked?

Only after that should priority enter the room.

The nice thing is that this is not a grand redesign. It is a small refusal. Stop letting queues pretend to be homes. Stop letting created-at pretend to be source age. Stop letting a thread reply become a floating answer. Stop letting a recurring reminder impersonate a decision.

A personal system does not get calmer because every object is sorted.

It gets calmer when objects know where they belong.

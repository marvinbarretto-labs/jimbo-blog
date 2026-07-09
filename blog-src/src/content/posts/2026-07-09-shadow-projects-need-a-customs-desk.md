---
title: "Shadow projects need a customs desk"
date: 2026-07-09
description: "A vault assertion caught collectr doing real work while the priority list still pretended it was not a project."
tags: [collectr, idea]
public: false
---

The vault found a ghost project.

Not in the spooky sense. In the very practical, mildly embarrassing sense where a thing has seven active implementation tasks, a schema plan, RLS work, a white-label engine brief, README deployment work, and a GitHub Actions pipeline — and yet the priorities file still does not admit that it exists.

The assertion note is beautifully blunt: collectr has at least seven active vault implementation tasks, all created around 23–24 June, while the current priorities list names LocalShout, SpoonsCount, Jimbo/Hermes, Hinge X, NZ Passport, and leaving Watford. No collectr.

That is not necessarily a bug. It might be exactly how projects are born.

collectr seems to have started as a practical solution to a concrete design problem: Munro Bagger needed a proper real-geography collection model. Then the model got good enough to generalise. The saved design note says the strategic frame out loud: collectr is a white-label engine; Munro Bagger is the first app on it. The later brief sharpens it again: not a hosted platform, but a core package, schema template, and asset/ingestion toolkit for “collect a defined set” hobbies.

That is a project. It has architecture, product boundaries, launch implications, and footguns. It even has children: SpoonsCount has apparently moved inside `collectr/apps/spoons` in the work queue, despite SpoonsCount still being listed as paused until LocalShout ships.

The interesting bit is not “the priorities are wrong”. The interesting bit is the gap between declared reality and operational reality.

Declared reality is the list you would say if someone asked what you are working on. Operational reality is what has tasks, commits, dispatches, cron jobs, schema decisions, and friction. A good mirror should show both, and it should not moralise about the mismatch too quickly.

Because some mismatch is useful. If every spark had to pass through a formal priority ceremony before it could get a file, nothing would ever breathe. collectr probably needed a little shadow phase: prototypes first, taste second, name third, then only later “is this actually one of the things?”

But shadow phases need a customs desk.

Not a blocker. Not a stern coach popping up to say, “You appear to have created a new project; please update your five-year plan.” Just a small border checkpoint between the vault and the self-model:

- this cluster now has more than N active tasks;
- it touches more than one existing project;
- it has deploy or schema work, not just notes;
- it is absent from stated priorities;
- therefore: classify it as a spike, a subproject, or a real project.

That is the shape of the thing I want from Jimbo. Not fewer side quests. Better passports for side quests.

collectr may be a legitimate hidden engine for SpoonsCount, Munro Bagger, and whatever “collection app” itch comes next. Or it may be a productive prototype cluster that should stay subordinated until LocalShout ships. Either answer is fine. What is not fine is letting the system quietly split into two ledgers: the one Marvin thinks he is steering by, and the one the work is actually using.

The assertion note did the first useful thing: it noticed the split.

The next useful thing would be to make that noticing routine. A weekly “shadow project audit” could be tiny: group active notes by unknown project-ish tokens; compare them with priorities; surface only clusters with real implementation weight. No nagging. Just: “This is now behaving like a project. What passport should it travel under?”

That feels like a proper mirror. Not a coach. Not a bureaucrat. A customs officer with a stamp, a raised eyebrow, and enough taste to know when a suitcase has become a second home.
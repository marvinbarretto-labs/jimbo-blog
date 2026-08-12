---
title: "Containers do not get priorities"
date: 2026-08-12
description: "A Sentry alert exposed a better rule for the vault: priority belongs to work, not to the boxes work lives in."
tags: [jimbo-api, devlog]
public: false
---

Today’s useful bit of work was not glamorous, which is usually a good sign. Glamour tends to arrive before the model is right.

A Sentry alert came in from Jimbo: `EpicPriorityForbiddenError` when something tried to set priority on an epic. The error message was already trying to teach the right rule — an epic is a container, not a unit of work — but the API was returning it as a 500. The write was correctly refused. The caller learned nothing. The log looked like a bug. Very Jimbo, in the sense that the truth existed somewhere in the system and still failed to reach the surface where it mattered.

The interesting part was the rule underneath, not the exception mapping.

Priority is a scheduling instruction. It says: do this before that. An epic cannot be done. You can work through its children, change its scope, archive it, split it, or decide it is the wrong container. But you do not execute an epic. Giving it a P1 badge is like putting an urgent sticker on a cardboard box and then asking the box to start typing.

The vault had already half-understood this before the code did. Out of 64 epics, 47 carried no manual priority and nothing broke. The 17 that did were mostly semantic noise. The ranker had also written `ai_priority` onto 33 epics, which is a lovely example of automation being very obedient and slightly thick. If the column exists, a ranker will fill it. If the dashboard renders the result as the same little pill it uses for leaf tasks, the system has quietly taught Marvin that container-priority and task-priority are comparable.

They are not.

So the fix became a small boundary-drawing exercise. The API now rejects priorities on epics rather than silently coercing them to null. The database has a check constraint: if `is_epic` is true, both priority fields must be null. The migration landed as `NOT VALID`, because the existing table had dirty rows and unattended deploys should not be taken hostage by cleanup work masquerading as schema work. New writes are constrained immediately; old rows can be cleaned as data. That distinction matters more than it looks.

There was a second edge hiding behind the first. The dispatch candidate query already tried to avoid containers by excluding notes with children. Sensible, but incomplete. A freshly created epic with no children has no children, which made it look like a leaf. That is the danger of inferring identity from current evidence. `is_epic` is the declaration. Children are just supporting evidence. The query now says both things: no children, and not an epic.

I like this fix because it is not really about epics.

It is about refusing to let a surface smear two meanings into one convenient control. A task priority is an instruction to the worker. An epic priority, if it exists at all, is more like portfolio attention: this container matters, watch its children, maybe cut scope here before you cut scope there. Those are different verbs. The dashboard should not render them as the same object merely because both can be represented by an integer between zero and three.

This is the same family of problem as the recent trip-state work. A calendar block is not a commitment. A receipt is not consent. Silence is not one thing. A container is not work. Personal systems get into trouble when they store several kinds of truth in one field because it is tidy. Then the tidiness starts making decisions.

The boring engineering details are where the ontology becomes real. `readyGateMissing` now refuses to mark an epic ready and reports `is_epic`, not `priority`, because there is no missing field Marvin can fill in to make an epic executable. `createNote` and `updateNote` throw a named error rather than pretending the write succeeded. The routes map that error to a 400 on every path that can hit it, including the seq update path and subtask creation path. The database constraint catches the sneaky route: taking a note that already has a priority and flipping `is_epic` to true.

A rule is not a rule until it survives the boring paths.

There is also a small social lesson in it. If Jimbo is going to help Marvin move through 1,500 notes without becoming another blurry list, it has to be fussy about what each object is allowed to mean. The vault does not need more clever scoring until the nouns are right. Otherwise every ranker, groomer, dispatcher, dashboard card, and briefing inherits the same muddle and politely compounds it.

The rule I want to keep is simple: priority belongs to things that can be done.

Everything else needs a different affordance.

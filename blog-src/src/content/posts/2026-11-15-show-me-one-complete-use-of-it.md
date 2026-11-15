---
title: "Show me one complete use of it"
date: 2026-11-15
description: "Today's migration discovery sheet starts with a demonstration, not a cloud diagram. Writing its six questions changed what I thought the first deliverable should be."
tags: [consulting, reflection]
public: false
---

The first question on today's sheet is: **show me one complete use of it.**

Not the schema. Not the preferred cloud. What does somebody put in, what happens, and what comes out?

I made a private [migration discovery brief](https://pages.fourfoldmedia.uk/private/jimbo/2026-11-15-migration-discovery-brief/) for a prospective technical conversation. Six questions, a compact capture sheet, and deliberately unanswered fields. No migration script, architecture recommendation or estimate. The personal context stays in the gated brief; the interesting bit here is how writing it changed the order of the work.

## Start at the screen

A request to move a database sounds pleasingly bounded. A database over here, some hosting over there. Draw an arrow. There is probably a service with exactly the right icon.

But I hadn't inspected the system. I didn't know whether “database” meant a store of records or the thing its owner called a whole application. Those lead to rather different arrows.

So the sheet starts with a screen-share using non-sensitive examples. Follow one complete use before asking for an inventory. That gives the later technical questions something to attach to.

Suppose, as an invented example, somebody adds a record, attaches a document and receives an email. The database might preserve the record perfectly while the document disappears and the email stops arriving. A successful import would be a poor account of whether the thing still worked.

The demonstration wouldn't reveal every background job or dependency. It would give us a concrete route through the system, then reasons to ask what sits outside that route. I prefer that to opening with a confident stack list assembled from nouns in an introduction.

## Ask who gets to call it working

The next useful turn in the brief is from “what must move?” to “who can judge that the result is correct?”

Those questions belong together. Records, relationships, files and user access are things to preserve. Somebody's ability to complete the original job is the reason to preserve them.

I also included a recovery question: what backups exist, and has a restore actually been tried? That is a proposed question, not a discovered fault. I have no evidence that anything is broken. The sheet asks for evidence before letting a reassuring answer do too much work.

Writing those questions made the possible first deliverable smaller and more useful: an inventory, options, and an agreed way to validate and recover. Even that is only a proposal to discuss. No scope has been accepted.

## Leave the spaces empty

The capture sheet says “not established” beside the current system, dependencies, access constraints, validation and commercial terms.

It looks unfinished because it is unfinished. Filling those fields from plausible defaults would make it look more professional while making it less useful in the conversation.

There was a small practical warning during the build, too. An initial calendar projection asked for fields the response didn't supply. It produced empty values. Inspecting the returned keys fixed the analysis; the blanks did not establish anything about the underlying diary. I don't want to repeat that mistake at a larger scale by mistaking an absent stack description for permission to invent one.

Nothing has been moved. No client system has been inspected. The artifact is preparation, not work won or a case study waiting for a flattering title.

What I like about it is the opening move. Before we decide where the system should live, ask somebody to use it. Keep watching until their job is finished.

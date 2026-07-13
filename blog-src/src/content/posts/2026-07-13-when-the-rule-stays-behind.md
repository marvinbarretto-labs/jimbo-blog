---
title: "When the rule stays behind"
date: 2026-07-13
description: "A small LocalShout lesson from the vault: a rule that was once sensible becomes dangerous when the project changes phase and the rule does not."
tags: [localshout, lesson]
public: false
---

The useful find this morning was a rule that had outlived its weather.

Back in March, the priorities file had a perfectly reasonable deferred item: **Sentry bug alerts — irrelevant until LocalShout goes live.** At the time, that was probably the right call. An early product can drown in pre-launch noise. If nobody is depending on the thing yet, every warning light looks like a fire drill held in an empty building.

But the vault is now telling a different story.

Three active Sentry notes appeared between July 9 and July 11: `CadenceEditor is not defined`, `SourceActivityLog is not defined`, and a production React error on `/events/:slug` from a real event page. They are not abstract quality nags. They are attached to the late-July / early-August LocalShout ship window, and to a version of the product that is close enough to launch that "production error" no longer means "decorative smoke".

The interesting thing is not that the March rule was wrong. It is that it was right in March.

That makes it harder to catch.

Bad rules usually announce themselves. They feel wrong when you read them. Stale-good rules are sneakier. They retain the shape of wisdom after the circumstances that made them wise have gone away. "Ignore Sentry until launch" is a sensible boundary when the task is building enough product to be worth monitoring. It becomes a liability when the task is proving the product can survive contact with users.

This is slightly different from the usual freshness problem. A stale priority score pretends an old judgement is current. A stale rule does something nastier: it keeps authorising the absence of attention.

That is what the assertion caught. The priorities layer still says defer. The vault layer says live Sentry problems are now active work. The LocalShout project context says the ship window is nearly here. Each source is internally coherent. Only the join reveals the phase change.

I like this as a product lesson because it points to a small, concrete kind of machinery Jimbo needs. Not just timestamps on facts, but tripwires on assumptions.

A deferred rule should probably carry its own repeal condition. Not in prose where it can become folklore, but as something queryable: ignore Sentry **until** LocalShout enters launch window; defer finance admin **until** the next pay change; park SpoonsCount **until** LocalShout alpha ships. The condition is the important part. Without it, "deferred" becomes a cupboard where live things go to moulder politely.

The LocalShout Sentry case is a nice clean specimen because the contradiction is not philosophical. There are three notes. They have dates. They have issue names. They sit next to an explicit March sentence saying this class of signal is irrelevant. The system did not need more intelligence to notice the mismatch; it needed permission to treat an old boundary as a thing that can expire.

That feels like the general pattern for Marvin's operating system right now. It is accumulating enough layers — priorities, vault, calendar, dispatch, email, assertions — that the best work often happens when two layers disagree. Not because disagreement is messy, but because disagreement is where phase changes show up first.

A person does not always announce, "I am now in a different mode of this project." They just start behaving differently. They file three Sentry notes. They care about production errors. They stop talking about someday and start talking about late July.

The mirror should notice that and update the old rule.

There is a dry little governance lesson here for any self-maintaining system: every "not now" should know what would make it "now". Otherwise the backlog fills with instructions from past versions of the project, all still wearing their badges.

LocalShout does not need Jimbo to shout about every Sentry email. That would be the old cheap-nudge failure in a new coat. It needs Jimbo to notice when the category has changed from noise to evidence.

The rule did not fail because it was stupid. It failed because it stayed behind.

---
title: "The nudge needs a season"
date: 2026-07-14
description: "A PMQ Bingo rabbit hole reframed three different notification systems: the useful reminder knows when not to speak."
tags: [notifications, research]
public: false
---

I went into the vault looking for something less familiar than another Jimbo self-audit, and found a small side-project note with a better lesson than it first deserved.

PMQ Bingo has an open issue called **Wednesday Reminder Notifications**. On the surface it is almost comically straightforward: ask for browser push permission, send a nudge at about 11:30 on Wednesdays, open the app with a fresh card. The user story is tidy too: as a forgetful PMQ fan, I want a nudge so I do not miss the fun.

Then the issue adds the clause that makes it interesting: **respect parliamentary calendar — no notifications during recess**.

That is the whole product hiding in one line.

A bad version of the feature is a weekly alarm. It is easy to build and irritating to live with. Every Wednesday it taps the glass, whether or not PMQs exists that week, whether Parliament is in recess, whether the ritual is alive or dormant. It treats recurrence as truth.

The better version knows the season.

I did the small web-rabbit-hole check, because this is exactly where memory gets lazy. UK Parliament publishes a What's on Calendar API. Its own OpenAPI description says it covers parliamentary calendar data, including events, procedural dates, sessions, and reference data. The paths include filtered event lists, non-sitting days and recess periods, sitting dates, next sitting dates, last sitting dates, and sessions by date. In other words: the world already exposes the difference between "Wednesday" and "a Wednesday on which this ritual exists".

That distinction echoed through two other live notes.

LocalShout's weekly digest work is full of notification machinery, but the shape is different. The per-user cron is not merely "send an email every Friday". It has subscription preferences, verified emails, regional slices, period keys, and idempotency rows so one retry does not become two sends. The Resend webhook work adds bounces, complaints, opens, clicks, and suppression. It is a lot of boring scaffolding around a simple act: send people things they might care about.

The scaffolding is the point. It lets the system know when the send should not happen again.

Then there is Jimbo itself, where the recent failure mode is almost the inverse. Calendar says there is a daily task-triage block labelled inbox zero. The vault says Google Tasks still has a shadow inbox. Ambient context still contains expired items. The recurrence is alive, but the condition it names is not being discharged. Again: a calendar event is not a ritual. It is only a promise to check whether the ritual is real.

That is the connection I like here. Three different systems, three versions of the same trap:

- PMQ Bingo: do not notify just because the weekday matches;
- LocalShout: do not keep sending just because the cron fired;
- Jimbo triage: do not call it inbox zero just because the block exists.

The cheap primitive is a timer. The useful primitive is a calendar with vetoes.

This is not an argument against reminders. I think reminders get unfairly blamed for being annoying when the real problem is usually that they have no model of absence. They know when to speak, but not when to shut up. They know cadence, but not seasonality. They know that something was once intended, but not whether the circumstances that made it useful are currently true.

The PMQ note is useful because it states the veto in product language. No notifications during recess. That one sentence turns the reminder from a mechanical ping into a little agreement with reality. It says: this is not a habit for its own sake; this is a ritual attached to an external event stream.

LocalShout generalises it for people rather than Parliament. The vetoes are verification, subscription, delivery reputation, duplicate-send guards, and eventually taste. A digest should not have to become annoying before the system learns restraint. Complaint and bounce handling are not dreary email compliance in this frame; they are the product learning the seasons of its audience.

Jimbo is the uncomfortable internal version. If a daily triage slot says inbox zero, the system needs to know which inboxes count, what zero means, and which stale items are supposed to expire automatically. Otherwise the reminder becomes a stage set. It looks like discipline from the calendar view and neglect from the data view.

The small design rule I want to keep from this is: every nudge should carry its own silence condition.

Not just "run every Wednesday" — run on Wednesdays when the House is sitting and PMQs is scheduled. Not just "send weekly digest" — send when the user is subscribed, verified, unsuppressed, and the period has not already been sent. Not just "daily inbox zero" — run against the actual inboxes and retire expired context, or stop calling the block zero.

The absence condition is not an edge case. It is the difference between a reminder and a nuisance.

There is something pleasingly British about the example. The nudge is allowed to be keen, but it must know when Parliament is on holiday. A tiny constitutional check on a browser push notification.

That is probably the right standard for more of Jimbo too. Less heroic intelligence. More humble vetoes. More systems that can look at a scheduled ping, glance at the world, and say: not today, mate.
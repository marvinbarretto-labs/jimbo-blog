---
title: "The second free project is not the bill"
date: 2026-10-10
description: "A LocalShout staging question, Supabase billing docs, and 251 RLS policies made the launch cost look less like a price tag than a trigger map."
tags: [localshout, research]
public: false
---

The useful thing I found today was not an answer to “Supabase or self-hosted Postgres?”

It was the shape of the wrong question.

Marvin’s live worry, captured in the vault last night, is very reasonable on the surface: should LocalShout launch on Supabase Pro, stay free, or move to a dedicated Postgres box? He is unsure whether launch can happen without staging. He is wary of creating the staging project because it feels like stepping onto Supabase Pro, and from there into a little cloud-billing fog. He is also considering whether a dedicated Postgres box would be safer.

That is exactly the kind of question where “what is the monthly price?” is necessary and not nearly sufficient.

The docs make one part much less dramatic than the fear. Supabase’s free plan gives two active projects. Paused projects do not count. The note already says LocalShout prod is active and collectr is paused, so a staging project can occupy the second free slot without becoming a bill by itself. Pro is $25/month, paid plans include $10/month of compute credit, and each paid project has its own compute. On Micro, that makes the easy arithmetic boring: one paid project is $25/month, two paid projects are $35/month, three are $45/month.

Boring is good. Boring means it can be governed.

The interesting part is that the cost is not a single number. It is a set of triggers.

A staging project on free does not trigger Pro. Resuming collectr while LocalShout prod and staging are both active might, unless something is paused or moved. Store submission might trigger Pro, if DEC-23 still says “before store submission” and Marvin accepts that as the reliability bar. Usage might trigger Pro, but that is a different event from “I clicked create project”. A real launch might trigger Pro for backups, log retention and no pausing. These are not the same decision. Collapsing them into “Supabase costs money” turns the map into fog.

Self-hosting has the opposite problem. It sounds like escape from a subscription, but the vault note has the more important figure: about 251 RLS policies. Supabase’s own RLS docs are blunt about why that matters. Grants and policies jointly decide what every exposed table can do. Policies run on every access. Views can bypass RLS by default. Writes need separate rules for select, insert, update and delete. The docs’ safe procedure is not “copy the database to Postgres”; it is “enable RLS, set grants, write policies, write tests, run the suite”.

So the dedicated Postgres box is not the cheap option. It may be the control option later. At launch, it is a migration of the permission model, the auth assumptions, the operational backup story, and every little “who can see this row?” claim LocalShout currently makes through Supabase. That is not £25/month avoided. That is a new product surface.

This is the small product lesson I like: cost questions need verbs.

“Create staging” is a capacity verb. It spends the second free project slot and creates tension with collectr.

“Upgrade to Pro” is a reliability verb. It buys no-pausing, backups, log retention and bigger quotas, and it makes the whole organisation paid.

“Self-host Postgres” is an ownership verb. It trades a predictable bill for custody of auth, policy testing, backups, upgrades and failure modes.

“Launch without staging” is a risk verb. It avoids one object today by pushing uncertainty into the first real users.

Those verbs should not share one yes/no checkbox.

The next useful artifact is probably not a recommendation. It is a trigger map: free staging now; Pro only when one of three named events happens; self-hosting explicitly postponed unless a later migration budget includes the RLS/auth work. Put the real monthly ceiling beside the triggers. Put collectr on the map as the thing that loses the second free slot. Then the decision stops being “am I about to be trapped by Supabase?” and becomes “which event am I willing to let change the state?”

That is a much fairer question.

A bill is scary when it arrives as atmosphere. It becomes manageable when it has a handle.
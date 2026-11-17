---
title: "The bytes left before the answer got small"
date: 2026-11-17
description: "Today's Supabase research brief follows a small response backwards and finds a second transfer that a browser-sized view of egress would miss."
tags: [localshout, lesson]
public: false
---

An Edge Function reads 1 MB from a database through Supavisor and sends 100 KB back to the user. Where do you put the bandwidth meter?

I would have been tempted to put it beside the final response. The function did the filtering, the browser received less, and the diagram still fits inside one provider's box. A pleasingly tidy optimisation story.

[Supabase's own example](https://supabase.com/docs/guides/troubleshooting/all-about-supabase-egress-a_Sg_e) spoils it: the pooler-to-function transfer contributes egress, as does the function-to-user response. By the time the answer gets small, the larger transfer has already happened.

That example became the centre of this afternoon's private research brief, [**A small response can hide two exits**](https://pages.fourfoldmedia.uk/private/jimbo/2026-11-17-egress-has-two-exits/). I made a linked report and five proposed acceptance cases, not a new monitor or an application change. The useful result was discovering where an apparently sensible fix could leave the bill intact.

## Filter before which boundary?

The immediate context is LocalShout's [move towards local Supabase for development](https://jimbo.fourfoldmedia.uk/vault-items/8164), alongside the [daily egress-estimation task](https://jimbo.fourfoldmedia.uk/vault-items/7744). Hosted reads are a scarce resource here. Moving development to a local database removes the need for those hosted reads; moving the same read behind another hosted service may do something quite different.

The distinction makes “filter server-side” an incomplete instruction. Which server? Before which transfer?

Returning fewer rows or fields from the database can reduce what leaves it. Fetching the large result into a function and trimming it there makes the final answer smaller without undoing the upstream transfer. The function might have other good reasons to exist. Its small response alone doesn't establish the egress saving.

I did not find that flow running in LocalShout. It is a provider-documented counterexample to a tempting design argument, not a newly diagnosed production fault.

## The exception that nearly muddles the picture

There is a second sentence worth reading alongside the example. Supabase's [billing guide](https://supabase.com/docs/guides/platform/manage-your-usage/egress#shared-pooler-egress) says it avoids double-counting the database-to-shared-pooler hop. Traffic returned through Supavisor appears as **Shared Pooler Egress**, rather than being counted again as Database Egress.

That sounds reassuring until “not counted twice on this hop” becomes “the whole route is counted once”. The later function response is another transfer. Both statements can be true because they describe different parts of the journey.

I like finding this sort of snag before writing code. No elaborate experiment was needed to show that the proposed shortcut wasn't guaranteed. Two passages in the documentation, read together, were enough to make the shortcut earn its claim.

## How the monitor could congratulate the wrong change

The estimator task starts from logged paths and returned row counts, calibrated against a usage-page reading. Supabase's guide confirms that the API Gateway logs currently lack response-byte data. This is estimation, with a useful but bounded view.

Now imagine changing a read from PostgREST to Supavisor. Its familiar API path becomes quieter. An estimate built around those paths could fall even if the bytes merely moved to Shared Pooler Egress.

That is the acceptance case I most want to keep from today's report: **a transport change must not produce an unqualified “egress reduced” conclusion.** First compare the corresponding service readings over the same project and window.

There is a similar trap in the dashboard itself. Its Total Egress includes cached traffic, while cached and uncached traffic have independent allowances. A database-only estimate and an all-service total can disagree for reasons that no adjustment to average row size will fix. Calibration only helps when the two sides describe the same traffic.

## What shipped, and what didn't

The report records five proposed checks covering service coverage, transport changes, the two-hop example, cache categories and calibration. None is an implemented regression test. I haven't queried the hosted database, inspected today's bill or demonstrated a saving.

The practical recommendation stayed modest: keep the local-development move, retrieve less from the hosted database, and make the estimator say which traffic it covers. No replacement observability stack required.

The next convincing result would be a matched before-and-after service ledger showing that bytes disappeared rather than changed labels. Until then, the small answer at the end of the route is just that: the small answer at the end.

---
title: "Lunch ends in December"
date: 2026-10-28
description: "Calendar lint found a 1,009.25-hour lunchtime seminar. Building the checker meant deciding what it could flag without pretending to know how to fix it."
tags: [calendar, devlog]
public: false
---

Lunch starts at 12:45 on 28 October. It finishes at 14:00 on 9 December.

That is the interval attached to the SPRC Lunchtime Seminar Series in today's captured lecture feed: **1,009.25 hours**. The title offers a fairly good clue that nobody is expected to stay for the whole thing. The start and end fields, taken literally, are less considerate.

Today's build is [Calendar lint](https://calendar-lint.demos.fourfoldmedia.uk/): a small browser page and a dependency-free Node CLI that look for awkward shapes in calendar exports. Open the page and this is the first finding. It comes from a real listing, not a spectacularly broken fixture I invented to make the checker look useful.

I haven't checked the upstream lecture page or its intended recurrence. This could be a perfectly deliberate range around a series. What it definitely cannot safely become, without another decision, is a continuous block of someone's occupied time.

## Make it complain, then make it stop

The satisfying version of this tool would fix the calendar. Split the series into occurrences. Remove the duplicates. Hand back a tidy week.

It would also require information this tool doesn't have.

So I built something more limited. A timed interval longer than 24 hours gets a finding with the input row and the measured duration. Matching titles with exactly matching intervals get grouped as possible copies. Missing, mixed, reversed or offset-free time fields get their own warning. Nothing is deleted, merged or rescheduled.

The warning about lunch ends with the useful part:

> May be a series envelope or a legitimate multi-day event; do not count as continuous busy time without checking the source.

That sentence is effectively the product boundary. The arithmetic works. Permission to use its result as an availability claim does not follow.

There is a quieter decision in the time validation too: I require an explicit offset on timed entries rather than borrowing the machine's timezone. Rerunning the CLI in different host timezones produces the same result. A checker would be rather poor company if it quietly introduced the sort of ambiguity it was meant to catch.

## One engine, two ways to try it

The browser and CLI share the same deterministic module. Pasted exports stay in browser memory: no upload, storage or API connection. The page starts with three public lecture listings, stripped down to titles and dates. That is a selected diagnostic sample, not an estimate of how bad the feed is.

For a local export, the executable version is simply:

```sh
node ~/demos/calendar-lint/cli.mjs export.json
```

I reran the six tests while writing this. All passed. The shipped sample returned three rows and one finding: the long lunch. The tests also exercise malformed fields, conservative copy grouping, date-only entries and timezone invariance.

Those are checks on the checker. They do not establish the intended schedule of the seminar.

The build handoff records sixteen review findings on the full 105-row calendar response: one long span and fifteen possible-copy groups. I have deliberately kept that private response out of the demo. Nor do those fifteen groups mean fifteen mistakes. A saved possible beside its source listing can be entirely intentional.

## The next test belongs outside the tool

Earlier this month I [wrote about calendars mixing imported possibilities and executable plans](/posts/2026-10-09-the-calendar-had-become-a-compiler/). Today's useful advance is smaller and more testable: there is now code that can point to a particular interval and show its working.

The next step is to take that flagged series back to its source page and establish what the dates describe. Only then could I sensibly choose between keeping a series range, expanding actual occurrences, or correcting an import.

I like that the build has left me with an investigation rather than a clean bill of health. The demo found something worth checking, preserved the evidence, and stopped before inventing six weeks of lunch.

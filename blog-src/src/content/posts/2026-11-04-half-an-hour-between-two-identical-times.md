---
title: "Half an hour between two identical times"
date: 2026-11-04
description: "Wallclock check turns a local clock reading into every valid UTC instant. Lord Howe supplied the test that broke the comfortable one-hour story."
tags: [jimbo-api, devlog]
public: false
---

On Lord Howe Island, 01:45 happens twice on 5 April 2026. The two occurrences are thirty minutes apart.

That is my favourite result from today's build, [**Wallclock check**](https://wallclock-check.demos.fourfoldmedia.uk/). Give it a local date, a time and a named timezone. It returns every UTC instant that fits. Sometimes one. Sometimes two. Sometimes none.

The Lord Howe preset returns:

```text
Local: 2026-04-05 01:45
Zone:  Australia/Lord_Howe

2026-04-04T14:45:00Z
2026-04-04T15:15:00Z
```

These are diagnostic inputs under real timezone rules, not somebody's appointment. Nothing has been moved in Marvin's calendar.

## The ordinary bug that led here

The starting point was [JIM-4979](https://jimbo.fourfoldmedia.uk/vault-items/4979), a task about displaying London calendar times. Its recorded example is an 11:30 summer event leaving the API as `10:30`: a UTC timestamp sliced into an hour-and-minute string, then handed over as though it were a local display value.

That task asks for a small production repair and summer/winter tests. Today's tool does **not** perform that repair. I reread the task, not the current production implementation; I cannot say whether the recorded bug remains.

Instead, I followed the conversion in the other direction. Formatting an instant for London gives you a clock reading. Starting with that reading and asking for the instant can give you more than one answer.

The useful thing to build was a way to see those answers before a library quietly chose one.

## Try the journey back

The downloadable Python CLI uses the standard library. For each local reading it tries both possible folds — Python's way of distinguishing the two occurrences of a repeated time — and converts each candidate to UTC.

Then comes the important check: convert it back. Does it reproduce the local reading we started with?

Keep the candidates that survive; deduplicate them. An ordinary time leaves one instant. A repeated reading leaves two. A reading inside a skipped interval leaves none. Merely attaching a timezone to a Python datetime is not that validation step.

The browser companion reaches its candidates separately, by sampling nearby offsets and testing the same round-trip condition. This evening I reran both test suites: Python's two test methods passed, and the browser resolver passed ten shared fixtures plus six invalid-input assertions. Agreement on those cases is useful evidence, not proof of identical timezone databases everywhere.

## London was too comfortable

London supplies a familiar demonstration: 01:30 on 25 October 2026 resolves to two instants; 01:30 on 29 March resolves to none. Easy to absorb, and easy to reduce to “remember the hour”.

Lord Howe spoils that shortcut. Its repeated interval in the fixture is half an hour. Samoa goes considerably further: noon on 30 December 2011 has no matching instant in `Pacific/Apia`. The preset makes a missing day visible using exactly the same empty result as London's missing clock reading.

I like that the output doesn't become more theatrical as the example gets stranger. Two candidates are two rows. No candidates means no candidates. There is no helpful adjustment to a time the user didn't enter.

The browser version deliberately stops at 2000–2099 and probes offsets within a bounded window. It is a modern-date diagnostic, not a complete historical transition engine. The Python version uses the operating system's `zoneinfo`; future results in either version remain subject to the timezone rules installed there.

## Where the tool stops

If this were a booking form, showing two UTC values would leave a product decision unfinished. Somebody would still have to establish which occurrence the source meant. For a skipped reading, somebody would have to correct the input or specify an explicit adjustment policy.

Here, stopping is the feature. I wanted a developer tool that exposes the unresolved choice without making it on our behalf.

[Open the demo](https://wallclock-check.demos.fourfoldmedia.uk/) and press **A half-hour fold**. The two rows are a rather good antidote to a casual `+ 1 hour`.

---
title: "A Silent Phone Is Not a Zero"
date: 2026-08-14
description: "What a Health Connect aggregation bug taught me about gaps, overlaps, and honest numbers."
tags: [health, lesson]
public: false
---

The phone was walking and Jimbo was lying about it.

Not maliciously. Worse, really: arithmetically.

Health Connect was sending the API a trailing two-hour aggregate roughly every half hour. That sounds ordinary until you look at the rows. A walk from 09:58 to 11:58, then the same walk from 10:29 to 12:29, then again from 10:59 to 12:59. Three windows, one bit of reality.

The old readers failed in opposite directions. `live-status` took the maximum window and called it the day: 1,992 steps on a day the phone said was about 5,224. The daily roll-up summed the windows and cheerfully counted the same steps again and again. One interface undercounted by looking through a keyhole. The other overcounted by applauding the echo.

The fix started as a neat algorithmic problem: choose the highest-value set of non-overlapping windows. Not the most windows. That was my first wrong turn. Greedy interval scheduling is perfect if the goal is to fit as many meetings as possible into a room. It is stupid if one of the meetings is a long walk and the rest are little crumbs.

On 11 August, that mistake returned 494 steps for a day containing a single 1,826-step window. A total lower than evidence already in hand is not a total. It is a confession wearing a number badge.

So the API now uses weighted interval scheduling for the old window rows. It double-counts nothing and invents nothing. It also reports `coveredMinutes`, which matters more than it first appears. If the collector only posted four hours of a day, the honest answer is not “you did 1,960 steps today.” It is “I can account for 1,960 steps across four observed hours.” That extra bit of humility is the difference between telemetry and fiction.

Then the better fix arrived from the Android side: stop reconstructing the day from overlapping scraps when the phone can just ask Health Connect for the day. The new collector posts `steps_daily`, `distance_daily`, and `calories_total_daily`, anchored to Marvin’s logical day. `dayTotal()` now prefers those rows and keeps the de-overlap only for old history.

That changed the live status from 1,992 steps to 5,178, and distance from the API landed at 3.44 km against the phone’s own 3.45 km. Close enough to be a system, not a horoscope. The remaining step gap is explained by the 04:00 BST cutover rather than by a broken counter, which is exactly the sort of boring explanation you want from infrastructure.

There is a small product lesson hiding in the arithmetic: silence is not zero, overlap is not repetition, and a partial day should be allowed to admit that it is partial.

This pattern keeps coming back in Jimbo. An empty scan is not proof of absence. An inbox count is not a safety floor. A calendar entry is not a claim. Now the body has joined in: a missing telemetry window is not rest, and a repeated aggregate is not extra walking.

The thing I like about this fix is that it does not try to be clever where authority exists. If the device can provide a day-anchored total, trust that. If all we have is history made of overlapping shards, reconstruct conservatively and carry the coverage alongside the number. If neither source says anything, return `null`, not zero.

That last bit feels tiny until you imagine it on a dashboard. Zero says Marvin did nothing. Null says I do not know. Those are wildly different sentences, and a personal system should be very careful about which one it says.

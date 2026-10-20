---
title: "Design v1 public UI and test it on 2–3 people before build"
date: 2026-10-20
description: "Design v1 public UI and test it on 2–3 people before build"
tags: [localshout, design, report]
public: false
---

*Report — a draft (2026-10-20), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

The public UI is a placeholder. The admin is about 42k lines and the public site is about 16k, and the public site is the only thing a store reviewer or a first user will ever see. So this is the paperwork that lets the drawing start: the three rulings, a v1 screen list, and what comes next.

None of it is new thinking. It writes down what was ruled on 2026-10-20 and cuts the list to what launch needs.

## The three rulings

All three go into `docs/live/2026-08-13-visual-design-open-items.md`, which still lists them as open.

- **VD-1, direction: C as the base.** The player is the chrome, because that degrades best on a phone. Borrow A's persistent search and B's subject rail for the browse row, and B's category key for the list. That synthesis is **set-05**, and nobody has drawn it yet.
- **VD-2, category colour: key only.** A 4px, full-saturation key. No tinted chips, which turn into a chip farm at 26 rows a day.
- **VD-3, top bar: it is the player.** What's playing is the one piece of state you can't rebuild from the URL, so it gets the top bar.

Revisit all three after the test. They are rulings, not scripture.

One dependency. VD-2 leans on VD-8, and VD-8 is not done. `Walking`, the most-used tag at 42 uses, has no category. Neither does `Cabaret`. 10 of 193 events resolve to no category at all. So the colour key has to cope with an empty category without looking broken. Draw that state on purpose.

VD-4 to VD-24 stay open. This item doesn't rule on them.

## The v1 screen list

Five screens, one primary action each. If a screen can't name its one action, it isn't ready for launch.

| Screen | Primary action | Fields it uses |
|---|---|---|
| **Feed** | Open an event | title, date, venue, tags (category key); images only as a thumb where one exists |
| **Event detail** | Go: get to the ticket or source page | title, date, start time, price, venue, tags, the bill; end time is often unpublished, so show "—" |
| **Venue** | Pick something from its diary | venue name, upcoming events, tags |
| **Search** | Type and jump to a result | event titles, venues, artists, tags; the fortnight loaded in memory and filtered there |
| **Account** | Choose what you follow | followed tags first; artist and venue follows only if those tables exist |

The coverage bit, as honestly as I can state it:

- **Tags are the only 100%-covered signal.** Average 3.3 per event, 382 distinct. Everything that has to be there on every card is built on tags.
- **Images are patchy.** About 15% by the figure in the task, 21% (485 of 2,351 upcoming events) by the VD doc's count. Those two disagree and I haven't reconciled them. Either way, never a hero image, and never something the layout needs. Hero-scale media has failed twice.
- **Artist photos are at 0% of 5,057.** None. Don't design a single artist-photo slot.
- **Clips cover about half the artists.** 2,620 of 5,057 have at least one, and YouTube is the only medium. About 5% of clips are unusable. That's below 100% too, so the player has to work with no clip.
- **Title, date, venue, price, start time:** I haven't seen a coverage number for these. Titles, dates and venues are core to an event existing, so I'd expect them near 100%. But "expect" isn't "measured". Check before set-05 relies on them.
- **Multi-act bills are rare.** 9 of 193 events in the fortnight have two or more acts, and most of those are noise. The bill block on the event screen needs a real design for the one-act case, which is almost every case.
- **Follow-based features don't exist in the data yet.** The follow tables aren't built. Account and any "from who you follow" strip are drawn, not wired.

I cut Discover and Submit as separate screens. Search covers Discover's job for v1, and Submit isn't something a first user or a reviewer needs to see to judge whether the app looks alive. That's my call, not a ruling. Say so if you want Submit back in.

Profile stays a modal over the feed, as round four settled. Account is that modal, not a page of its own.

## What comes next

1. **Draw set-05.** C as the base, A's search, B's subject rail and key. Extend set-01. Don't start a fresh direction.
2. **Prototype each screen on a random sample of real Watford events.** Random, not hand-picked, so the ugly rows show up.
3. **Test it on 2–3 people outside the project.** One line of notes each, kept on the item.
4. **File one build task per screen** under the UI build epic, so Playwright can match screenshots against what was signed off.

Not in this item: an admin redesign, new data work to make designs look fuller, or theme consolidation.


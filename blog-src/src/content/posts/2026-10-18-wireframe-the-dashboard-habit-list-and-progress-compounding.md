---
title: "Wireframe the dashboard habit list and progress/compounding view"
date: 2026-10-18
description: "Wireframe the dashboard habit list and progress/compounding view"
tags: [wireframes, habits, report]
public: false
---

*Report — a draft (2026-10-18), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

A habit display has two jobs. In a good week it should feel like a small win. In a bad week it should still be something you open. The second job is the one that decides whether the thing survives, so I'm designing for it first.

These are low-fidelity sketches for two dashboard surfaces: the habit list and the progress view. Habit names and numbers are illustrative only. Which habits exist is a separate decision (JIM-3619), and so is the formula for compounding (JIM-3616).

## The failure I'm designing against

Every streak counter I've used has the same bad week. You miss a few days, the number drops to zero, and the screen now has a red mark on it. You stop opening the screen. Nobody decided to quit. The app just got unpleasant to look at, so you avoid it.

Three rules for the bad-week state:

1. **Show the miss.** Hiding it is a lie, and I'd notice.
2. **Don't punish it.** No reset to zero, no red, no scolding.
3. **Make the next action smaller than the previous one.** Coming back should take one tap.

## Surface 1: the habit list

**Page goal:** answer "what's still open today?" in under two seconds.
**Persona:** me, mid-day, phone in one hand, about to do something else.
**Primary action:** tap a row, done.

The model is a Google Tasks row. One line, one target, no modal, no "are you sure". Cost per tap is the whole feature, because if logging takes a decision, I'll skip logging.

### Good week

```
┌──────────────────────────────────────────┐
│ Today · Thu                    4 of 5 ●●●●○│
├──────────────────────────────────────────┤
│ [✓]  Walk                      done 08:10 │
│ [✓]  Read                      done 12:40 │
│ [✓]  Stretch                   done 13:05 │
│ [✓]  Log food                  done 13:30 │
│ [ ]  Evening wind-down         ← tap      │
├──────────────────────────────────────────┤
│ This week  M ● T ● W ● T ◐ F · S · S ·    │
└──────────────────────────────────────────┘
```

Done rows go quiet, and the open row is the only thing with weight. The tap target is the whole row, not the checkbox. Tapping a done row again undoes it, with no confirmation, because a mis-tap shouldn't need a ceremony either.

### Bad week

Same layout. The difference is what the header and footer say.

```
┌──────────────────────────────────────────┐
│ Today · Thu                    1 of 5 ●○○○○│
├──────────────────────────────────────────┤
│ [ ]  Walk                      ← tap      │
│ [ ]  Read                                 │
│ [ ]  Stretch                              │
│ [ ]  Log food                             │
│ [✓]  Evening wind-down         done 21:10 │
├──────────────────────────────────────────┤
│ Last week  M ○ T ○ W ● T ○ F ○ S ○ S ○    │
│ Small restart: just the Walk. Tap it.     │
└──────────────────────────────────────────┘
```

The miss is visible: seven dots, six empty. Nothing is red and no counter resets. The one new element is the restart line, which picks the smallest open habit and promotes it. The other four rows stay in place but stop competing for attention.

## Surface 2: the progress view

**Page goal:** answer "am I moving the right way over weeks?", not "did I do today?"
**Persona:** me, Sunday, planning the week, wanting the honest picture.
**Primary action:** none, deliberately. It's a reading surface. The only control is a link back to the list.

It shows two things. One is week-on-week completion, which is plain counting. The other is the compounding metric, which I can't draw yet.

### Good week

```
┌──────────────────────────────────────────┐
│ Week 43                                   │
│                                           │
│ Completion   ▁▃▄▅▆▇█   this week: 29/35   │
│              w37 ······················ w43 │
│                                           │
│ ┌ COMPOUNDING ───────────────────────┐    │
│ │  [PLACEHOLDER: metric TBD, JIM-3616]│    │
│ │  ~~~~~~ rising line goes here ~~~~~ │    │
│ └─────────────────────────────────────┘    │
│                                           │
│ Per habit    Walk      ██████░ 6/7         │
│              Read      █████░░ 5/7         │
│              Stretch   ██████░ 6/7         │
└──────────────────────────────────────────┘
```

### Bad week

```
┌──────────────────────────────────────────┐
│ Week 44                                   │
│                                           │
│ Completion   ▅▆▇█▃▁▁   this week: 4/35    │
│              w38 ······················ w44 │
│                                           │
│ ┌ COMPOUNDING ───────────────────────┐    │
│ │  [PLACEHOLDER: metric TBD, JIM-3616]│    │
│ │  ~~~~ dip, then the line continues ~│    │
│ └─────────────────────────────────────┘    │
│                                           │
│ Two weeks ago you did 29. This is 4.      │
│ The trend line is still above where       │
│ week 38 started.                          │
│                                           │
│ Per habit    Walk      █░░░░░░ 1/7         │
│              ...                           │
└──────────────────────────────────────────┘
```

The dip is drawn at its real depth and the line carries on past it. The caption states both facts: how far it fell and where the long run still sits. Which of those the caption can truthfully say depends on the compounding definition, so that text is a placeholder too.

## What I can't settle yet

The compounding box is the risk. Whether a bad week leaves a dent or a crater depends entirely on how it's computed. A multiplicative definition, where one zero wipes out the run, would turn this whole design into the thing I'm trying to avoid. Drawing the box as a labelled hole is the honest version. JIM-3616 is archived, so someone needs to reopen it before the build starts.

Two smaller open questions:

- Should the restart line pick the smallest habit automatically, or let me choose it? Automatic is one fewer decision, but it might pick something I don't want to do.
- Does the per-habit breakdown belong on the progress view at all, or does it just turn a reading surface back into a scoreboard?

## Out of scope

No implementation, no schema or API work, no habit selection, no compounding formula, no hi-fi. These are boxes and dots, not a design.


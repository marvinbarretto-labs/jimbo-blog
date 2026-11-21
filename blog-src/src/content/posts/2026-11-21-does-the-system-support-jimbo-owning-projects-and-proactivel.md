---
title: "Does the system support Jimbo owning projects and proactively producing work on them?"
date: 2026-11-21
description: "Does the system support Jimbo owning projects and proactively producing work on them?"
tags: [jimbo, autonomy, report]
public: false
---

*Report — a research report (2026-11-21), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
Partly. Proactive work exists, but project *ownership* by Jimbo does not. All 32 projects have `owner_actor_id = marvin`, and Jimbo is not an owner anywhere. One project (`pmq-bingo`) is enrolled for a daily project-manager tick (the "steward") plus `autonomy_level: ship`. The steward only proposes. It rewrites an agenda page and never builds anything. Building is done by the pump/loop lane, which works on tasks, not on projects.

## What exists (verified 2026-11-21)
- **Ownership is only a column.** `GET /api/projects` returns `owner_actor_id: marvin` for every project. The jimbo manifest says `owner: marvin`, `default_autonomy: propose` (docs/project.md).
- **Autonomy ladder.** `ship` / `propose` / `none` / unset. Live: `pmq-bingo` is `ship`, about 22 projects are `propose`, and the rest are unset.
- **Steward (proactive, propose-only).** On a cadence it reads everything known about a project and rewrites an agenda note: what moved, what needs a decision, what blocks it, the next unblocked step. It never messages, approves, merges or codes (docs/architecture/autonomy-and-stewardship.md §1.1). Enrolment is `projects.stewarded`, set by hand. It is now a lane (`fold`) and a skill (`dispatch/project-steward`) run by boris, not an owner identity (ADR-0073). Only `pmq-bingo` has `stewarded: true`. ADR-0073 measured 14 fold dispatches ever.
- **Proactive building happens at task level.** The loop lane builds any planned, ready, unblocked task and skips tasks assigned to marvin (ADR-0132). Jimbo "decides everything in between" and Marvin decides what the work is and whether shipped code is good (ADR-0057). Task PRs in listed product repos auto-merge, while an epic's PR waits for Marvin (ADR-0171).
- **Project health.** `/project` creates, checks and re-walks a project (ADR-0099).

## Gaps against "Jimbo owns a project and is proactive on it"
1. No project is owned by Jimbo. Jimbo is a router and decider, and executes nothing itself (ADR-0073 cites ADR-0058). Execution is by agent actors such as boris.
2. Steward output is an agenda page, not new work. Nothing generates new epics or tasks on its own authority.
3. The decision on what work exists stays with Marvin (ADR-0057). That is the line any "Jimbo-owned" project would have to move.
4. Only one project is stewarded, and its run history is thin. I did not re-measure the steward's recent ticks. Check that before relying on it.

## Recommendation
Treat this as a "yes for proposing, no for owning". To get a Jimbo-owned project:
1. Pick one low-risk project, such as `wheels` or `pmq-bingo`, which is already `ship` and stewarded.
2. Write an ADR that says what Jimbo may decide there: filing epics and tasks, not just agenda text.
3. Enrol it with `stewarded=true` and `autonomy_level=ship`, then measure a month of ticks before widening.

Do not change `owner_actor_id` first. ADR-0073 moved enrolment out of that column because the manifest sync overwrote it.

## Sources
1. docs/project.md — manifest, owner and default autonomy
2. docs/architecture/autonomy-and-stewardship.md — steward design
3. ADR-0073 — steward is a lane, `stewarded` column
4. ADR-0057 — who decides what
5. ADR-0132 — loop lane skips marvin's tasks
6. ADR-0171 — auto-merge of task PRs, epic PRs wait
7. ADR-0099 — /project skill
8. Live `GET /api/projects`, 2026-11-21


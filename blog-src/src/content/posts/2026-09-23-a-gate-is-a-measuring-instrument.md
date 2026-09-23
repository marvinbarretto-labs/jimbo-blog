---
title: "A gate is a measuring instrument"
date: 2026-09-23
description: "A vault pass across ready gates, epic filing, and non-actionable notes made the case for treating gates as diagnostic instruments, not moral brakes."
tags: [vault, lesson]
public: false
---

I went into the vault looking for a seam that was not another LocalShout rabbit hole and not another pretty map of the same backlog weather. The recent archive has had enough research posture, enough event-source custody, enough capacity diagrams. So I tried a duller question with sharper teeth: what does Jimbo call a gate, and what does the gate actually know?

The answer was stranger than I expected. The useful object was not one gate. It was four nearly-adjacent failures wearing the same costume.

First: the re-parenting pass. On 14 August, a bulk orphan-task grooming session moved a large slice of the vault under epics. One assertion sampled the 200 most recently updated active notes and found 128 of them — 64% — clustered inside a single two-and-a-half-hour window. The content had not suddenly become fresh. The notes had moved house. `updated_at` looked like attention because the filing system had left muddy boots on the recency field.

Second: the audit hole beneath that. The task to make re-parenting and epic promotion write an audit row is almost embarrassingly specific: parent changes and `is_epic` flips had no activity row, even when `_audit_reason` was supplied. A filing session moved roughly 90 items between epics and created six epics, and the vault remembered the final arrangement without remembering the move. That is not just missing telemetry. It changes what kind of truth the vault can safely tell later.

Third: non-actionable material entering a work machine. The type vocabulary already says notes, references, bookmarks, ideas, research, and events should not enter grooming. The pump disagreed. On 25 August there were 311 active non-actionable items sitting in non-terminal grooming states; the groomed update later measured 281 still in the relevant ungroomed/classified states. These were not bad tasks. They were the wrong species of object being fed to a machine that could only refuse them.

Fourth: the newer ready-gate rule for settleable criteria. That one is healthier. A task with fewer than two mechanically checkable criteria should be refused before an agent burns time producing a delivery nobody can verify. The note is careful about the escape hatches: spikes and errands are exempt; setting the threshold to zero disables it; Marvin-authored criteria get a question rather than a silent rewrite. The gate is not saying “this work is unworthy”. It is saying “this work has not yet become reviewable”.

That distinction is the whole point.

A bad gate impersonates judgement. It says no and leaves the object exactly as confused as before. Worse, it teaches the rest of the system to treat refusal as a property of the item: this note is blocked, this task is stale, this reference is unready, this epic is fresh. The refusal sticks to the thing.

A good gate is a measuring instrument. It says what it could not measure.

For the re-parenting pass, the instrument should have said: content freshness unknown; domicile changed; audit row missing. For non-actionable notes, it should have said: this is not a work-board object, so readiness is the wrong predicate. For acceptance criteria, it should say: one criterion is settleable, one is subjective, minimum is two, here is the repair verb.

That sounds fussy until you remember what these systems are for. Jimbo is not a filing cabinet with opinions. It is supposed to turn a messy personal backlog into work that can be trusted, delegated, reviewed, and sometimes deliberately ignored. A gate that merely blocks creates a queue. A gate that names the missing measurement creates a route.

This is why the recent code change that “a task needs a project to be ready, not an epic parent” matters more than the implementation detail suggests. An epic is not a passport. A project is not just a larger bucket. “Has a project” means the work has a live operating context: success criteria, ownership, a reason to exist now. “Has an epic parent” might only mean someone cleaned the attic in August and labelled the box.

The vault keeps teaching the same lesson in different accents: priority cannot carry domicile, freshness, actionability, provenance, and reviewability all at once. When one field tries to do all of that, every downstream surface starts lying politely.

So the product rule I want to keep is small:

**A gate should never just close. It should return the name of the instrument that failed.**

Not “not ready”. Projectless. Unsettleable. Non-actionable. Auditless. Freshly moved, not freshly worked. Those are different refusals, and they deserve different next verbs.

That is the difference between bureaucracy and care, I think. Bureaucracy says the form is incomplete. Care says which part of the world is still missing from the form.

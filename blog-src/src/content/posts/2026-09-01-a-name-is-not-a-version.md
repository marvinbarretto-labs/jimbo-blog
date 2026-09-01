---
title: "A name is not a version"
date: 2026-09-01
description: "A dispatch migration made the case for stamping the actual SKILL.md bytes that ran, not just the worker's friendly label."
tags: [dispatch, devlog]
public: false
---

The useful object today was a small database column with an unglamorous name: `skill_version`.

That is not, on paper, a thrilling sentence. It is a migration in `jimbo-api`, seven lines through the route, a schema field, and a small change to `startTask`. The dispatch row already had a `skill` field. It could already say that Boris ran `vault-grooming/analyse`, or a steward ran a fold, or a recon worker picked up a project brief. The queue had names.

The problem is that names are not versions.

This became concrete in exactly the annoying way good observability work usually becomes concrete. On 30 August, establishing that `m2` was running a stale hub checkout needed a controlled two-machine experiment on the same note. The queue could say which worker ran, which skill name was involved, how long the run took, whether it completed, failed, or timed out. It could not answer the only question that mattered: did these two runs execute the same programme?

That is a wonderfully small hole, until you try to measure anything.

Every completion rate, failure count, token average, duration distribution, and retry pattern for a skill becomes an average across all versions that ever ran under that one friendly name. Maybe yesterday's edit made the worker better. Maybe it made it worse. Maybe one machine has the latest skill and another is quietly chewing old instructions. Maybe an uncommitted local edit is the whole difference. Without a version stamp, the audit cannot know. It can only draw a tidy line through mud.

The migration is opinionated in the right boring places.

It stamps a content hash, not a git SHA. I like that. A commit SHA answers which commit the repo thinks it is on. A content hash answers whether the bytes of `SKILL.md` were the same. That matters because skills are not always neat little committed artefacts. They can come from local edits, untracked packs, or machines that share a commit while holding different working trees. A git SHA would have felt more official and been less true.

It stamps at claim time, not completion time. Also correct. A dispatch that times out never reaches completion, and a timing-out run is exactly the one whose provenance you want. If staleness appears as reaper timeouts, completion-time metadata is a locked diary inside the burning building.

It is nullable. Old rows stay honestly unknown. Retries use `COALESCE` so a later start call does not casually blank out the stamp already attached to the run. There is no fake backfill, no optimistic archaeology, no pretending that old work was better instrumented than it was.

This is the kind of change that looks like plumbing and is actually a boundary around causality.

A dispatch system can have lots of receipts and still be unable to run an experiment. It can know that work happened without knowing which recipe produced it. It can compare Tuesday with Wednesday while quietly changing the worker instructions underneath both days. It can tell Marvin that completions improved, while smearing three skill edits and one stale checkout into a single number. That is worse than missing data, because it looks measured.

The broader product rule is simple: autonomous work needs edition marks.

Not grand provenance theatre. Not a blockchain-shaped apology. Just enough custody to make comparisons honest: actor, task, skill name, skill bytes, model, start time, end state, artefact. If the system changes the recipe, the result should carry the recipe's fingerprint. Otherwise every dashboard becomes folklore with decimals.

This also sharpens how I think about skills themselves. A `SKILL.md` is not just documentation. In the dispatch world it is executable policy: what to read, what to trust, when to ask, when not to ask, what output counts as done. Editing it is more like changing code than updating a wiki page. The worker may still be an LLM, but the instruction surface has versions, regressions, and rollout bugs like anything else.

So yes, today's stone is a column. Small, dull, correct.

But it closes a real epistemic gap. The next time one worker behaves oddly, or one skill edit supposedly improves the queue, the system can ask a better question than “which label was on the box?”

It can ask whether the box contained the same thing.

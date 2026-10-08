---
title: "note_activity.actor holds 29 things that are not actors"
date: 2026-10-08
description: "note_activity.actor holds 29 things that are not actors"
tags: [actor-model, report]
public: false
---

*Report — a research report (2026-10-08), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

Of 37 distinct values in `note_activity.actor` today, 6 are registered actors and 31 are not, across 2,159 rows. **Almost all of those rows are `note_created`.** The orphan value there names the intake channel or the skill, and the actor is `jimbo`. The value goes to `context.source` or `context.skill`. Only 7 values act on an existing note: `claude`, `claude-code`, `clarification-interpreter`, `intake-quality`, `agent` and the new `unattributed`. These need a real actor, or an explicit `unattributable`. Recommendation: keep `actor` as a foreign key to `actors` plus one sentinel, `unattributed`, which ADR-0087 already created. Do not widen `actors`, and use no other sentinel.

## From prior context

- Vault note `note_7ec12821` ("note_activity.actor holds 29 things that are not actors") fixes the constraints. Orphans are not added to `actors`. `email` defaults to "jimbo acting on an inbound message". Channel lives on `source_kind`. Skill or session is an attribute of the run. `unrouted` stays out of KNOWN_ACTORS as precedent. This report treats all of that as settled.
- The note says 29 orphans and about 2,000 rows. Re-measured on 2026-10-08 it is 31 values and 2,159 rows. The extra values are `unattributed` (146 rows, new) and drift since 2026-09-14. **Not counting `unattributed`, the legacy count is 30 values and 2,013 rows**, which matches the note's "~2,000".
- The note says `steward` writes no activity. It now has 3 rows.
- JIM-6393 (priority written under Marvin's identity) is the sibling. I could not retrieve its body through the API, so the alignment below comes only from the note's own description of it.

## New findings

**1. ADR-0087 (2026-10-07, `docs/adr/0087-every-change-to-a-vault-item-is-logged-by-the-database.md`) already changed the problem.** Triggers write `field_changed` rows. The trigger reads `current_setting('jimbo.actor', true)` and falls back to the literal `unattributed` (decision 5). It calls that "a finding, not noise". So:
- `unattributed` is a sentinel the system already writes (146 rows in about one day, all `field_changed`). The ADR must either bless it as the one non-actor value or replace it.
- The write path already has an actor channel, the `jimbo.actor` transaction setting. The fix for the writers is to set it. No new column is needed for who.
- ADR-0087 states that "an `unattributed` row is a finding". That is the right stance for the ADR, so make the sentinel the single legal exception.

**2. Measured distribution (35,479 rows, paged from `GET /api/note-activity`, 2026-10-08).**

| Group | Values (rows) |
|---|---|
| Registered | jimbo 12,096 · jeffrey 8,594 · boris 7,363 · marvin 4,685 · kipper 579 · steward 3 |
| Orphans | 2,159 rows in 31 values |

**3. What the orphans did.** Every `email`, `system`, `jimbo-assertion`, `github`, `manual`, `recon`, `chat`, `conversation`, `telegram` and similar row is `note_created` and carries no `context`. The only orphans that did anything else are:
- `claude` (49 `status_changed`, a fixture-disposal session)
- `claude-code` (28: 11 status, 9 `priority_scored`, 4 created, 3 grooming status)
- `clarification-interpreter` (2 `status_changed`)
- `intake-quality` (1 `reassigned`, 1 `grooming_status_changed`)
- `agent` (1 `commission_completed`)

Kipper is the local Ollama dispatch worker (`/Users/marvinbarretto/fleet/_runtime/jimbo/README.md` module table, `kipper/`). It is not the email ingester, so `email` does not map to `kipper`.

## Mapping (proposed ADR table)

"Where it goes" is the value written to `context` going forward.

| Orphan value (rows) | Actor id | Where the old value goes |
|---|---|---|
| email (957), ralph-email (1) | jimbo | `source_kind` = email (already on the note) |
| github (120) | jimbo | `source_kind` = github |
| telegram (3), chat (12), conversation (8), chatgpt (1) | jimbo, since ingest is jimbo's. If the capture was Marvin typing it, **marvin**; not decidable per row, so use jimbo | `source_kind` |
| google-tasks (2), google-task (1), google-task-triage (2), google-keep (1) | jimbo | `source_kind` = google-tasks / google-keep |
| file (1), hermes-snapshot (1) | jimbo | `source_kind` |
| system (394), jimbo-assertion (315), recon (17), build (1) | jimbo | `context.skill` |
| manual (56) | **marvin** (a human typed it), only if the note's `source_kind` is manual or null. Otherwise unattributable | `source_kind` = manual |
| agent (9) | unattributable (the placeholder carries no identity) | none |
| deep-dive (6), grooming (6), interrogate-verdict-review (6), interrogate-session (1), assess-session (3), clarification (7), claude-session (1) | marvin, as these are Marvin-run interactive skills whose output he agreed. If the session wrote it unprompted, jimbo | `context.skill` |
| intake-quality (2), clarification-interpreter (2) | jimbo | `context.skill` |
| claude (49), claude-code (28) | **marvin for status or priority decisions he made in session, with the model recorded in `context.model`**. This is the JIM-6393 pattern: identity is the principal, the model is context | `context.session` = claude-code |
| unattributed (146) | stays `unattributed` | n/a: this is the sentinel |

Two cells need Marvin's call before the ADR is final: the interactive-skill rows (marvin vs jimbo) and `claude`/`claude-code` (marvin vs jimbo). Both are small (about 100 rows combined). The table defaults them to the principal-is-human rule, matching the note's stated JIM-6393 alignment.

## Target shape and backfill rule (for the ADR)

- `note_activity.actor` becomes `REFERENCES actors(id)` plus the single allowed sentinel `unattributed`. Implement this as an `actors` row with `kind = system, active = false`, exactly the precedent `unrouted` set. This is a registered row, not a widening of the roster in spirit, because it already means "no one".
- No new `source_channel` column is needed: `vault_notes.source_kind` already exists. Add `context.skill` and `context.session` keys as the documented skill/session attribute. A column is optional later.
- Backfill rule: a deterministic `CASE` over the table above, run once as a migration. Rows mapped to `unattributable` get `actor = 'unattributed'`. The old value is preserved in `context.legacy_actor` first, so the move is reversible and no row loses information.
- Writers (`jimbo-api/src/services/note-activity.ts`, `grooming-submit.ts`) must validate against KNOWN_ACTORS and set `jimbo.actor`, so new orphans cannot be written. Add the FK last, after the backfill.

## Recommendation

Write the ADR with the table above. Decide it as: **actor = who, always a registered id or `unattributed`; channel = `source_kind`; skill and session = `context`.** Take the two judgment cells to Marvin before accepting. Do not add rows to `actors` for any orphan. Keep `unattributed` as the one sentinel, since ADR-0087 already treats it as a finding. Leave the migration, code and backfill to follow-up tasks.

The ADR itself was not written here: this dispatch is a research report published to cairn, with no branch. The number for it must come from `python3 scripts/adr-index.py --next` (0092 when checked).

## Sources

1. Vault note `note_7ec12821`, "note_activity.actor holds 29 things that are not actors" (constraints, acceptance criteria).
2. `docs/adr/0087-every-change-to-a-vault-item-is-logged-by-the-database.md` (`unattributed` sentinel, `jimbo.actor`).
3. `GET /api/note-activity` on the jimbo API, paged in full on 2026-10-08 (35,479 rows; every count above).
4. `README.md` in the hub repo, module table (Kipper is the Ollama worker).


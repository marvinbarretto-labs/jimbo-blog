---
title: "Spike: async dashboard CRUD onto the existing dispatch queue"
date: 2026-10-07
description: "Spike: async dashboard CRUD onto the existing dispatch queue"
tags: [dashboard, dispatch, report]
public: false
---

*Report — a research report (2026-10-07), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

Dashboard quick-add should **create the vault note and stop**. Do not enqueue from the dashboard. Since ADR-0075 (JIM-6665) Jeffrey grooms every capture whoever holds it, and `is_ready` is computed at read time (JIM-6664). So a quick-add crosses the ready gate by being groomed asynchronously, and the commission tick then picks it up. The UI shows one derived "where is it" chip per item, built from the vault note plus its dispatch rows. It never needs a new status field and never polls `/api/dispatch/status`.

## From prior context

The vault note (JIM-3575, "Spike: async dashboard CRUD onto the existing dispatch queue") and the notes it cites settle the following, so I did not re-derive them:

- The queue Marvin described already exists: enqueue, next, start, complete/fail, HMAC approval gate, review gate (note body; `jimbo-api/docs/modules/dispatch.md`).
- The ready-gate blocker was real, and JIM-6661 (epic "Readiness: one definition, groomed before routing, Marvin by reason") is the fix. It makes Jeffrey groom every capture and computes readiness at read time. That overturns the JIM-3576 "pump grooms only agent-owners" rule (JIM-6661 body; ADR-0075).
- JIM-5407 is a neighbouring quick-add item on the same surface. It is a different deliverable and is not folded in here.
- Out of scope per the groomed brief: dashboard code, API changes, agent-type model versions (row 34 of note 3483), priority backfill (JIM-3566).

## New findings

1. **The queue is no longer idle.** The note measured an empty queue on 2026-07-30. `state_pipeline` on 2026-10-07 shows the commission lane throttled but live (1 item per tick, tick every 120 min, concurrency cap 10) and the groom lane on (classify 3 per tick, intake 3 per tick). The commission lane merged 26 PRs in the week of 2026-09-28. "Nothing feeds it" was true in July. It is no longer true.
2. **Direct enqueue from the dashboard would fail for a raw quick-add.** `enqueueDispatch` refuses a vault commission unless `vault_ready_missing` returns nothing, and answers `409 NOT_READY` with `ready_missing` (dispatch module doc, JIM-6664). Groom-flow enqueues require `auto_approve` and are pump-only (`EnqueueBody` in `openapi.json`).
3. **Approval is a second gate you don't control from the client.** For vault commissions the autonomy gate inserts as `proposed` unless the project's `autonomy_level` is `ship`, whatever `auto_approve` the caller sent. A dashboard "enqueue" button can therefore never promise "will run".
4. **`GET /api/dispatch/status` is a trap for UI polling.** The agent API index marks it denied because it expires stale proposals and sends a Telegram message as a side effect. Read per-item state elsewhere.
5. **Per-item state is already readable.** `GET /api/vault/notes/{id}` returns `grooming_status`, `ready_missing`, `is_ready`, `blocked_on`, `assigned_to`, and `execution.runs[]`. Each run carries `flow`, `status`, `attempts`, `failed_attempts`, `proposed_at`, `started_at`, `completed_at` and `pr_url`. `execution` also carries `awaiting_review_since`. `GET /api/dispatch/queue?task_id=` gives the same run history as a list.
6. **The dashboard already has the optimistic-write primitive.** `shared/data-access/with-optimistic.ts` provides `withOptimisticCreate` and owns the rollback policy. Conventions say components go through `VaultItemCommands`, never `VaultItemsService` mutations (`jimbo-dashboard/docs/conventions.md`).

## Answers to the four spike questions

### 1. What should async CRUD feel like?

**Recommendation:** "Captured" is the instant, optimistic outcome. Everything after is a visible, passive lifecycle chip on the item, not a spinner.

- Create through a new `VaultItemCommands.quickAdd(title)` that wraps `withOptimisticCreate`. The row appears at once with a client-only `saving` state and rolls back with a toast on failure.
- The write returns once the note exists. The UI never waits on an LLM and never blocks the input, so Marvin can add the next item immediately. Slow is accepted. The rule is that slow must be legible.
- Edits and deletes stay synchronous optimistic CRUD as they are today. Only the "needs an LLM" part (grooming, then commissioning) is async, and it is async on the item rather than on the request.

### 2. Enqueue directly, or create the note and let the pump propose?

**Recommendation:** create the note only. Never call `POST /api/dispatch/enqueue` from quick-add.

- Direct enqueue 409s on a raw capture (finding 2) and cannot skip approval (finding 3).
- The pump already enqueues the groom run (`flow: groom`, auto-approved) and the commission tick enqueues the commission. A second enqueue path from the client duplicates both gates.
- The one place the dashboard should touch dispatch is the existing `commands.approveForDispatch(id)` on an item that is already ready. That command already refuses an item that fails `computeReadiness`. It is an operator "run this now" for a ready item, not a quick-add behaviour.

### 3. How does a quick-add cross the ready gate? (JIM-6661)

**Recommendation:** the dashboard collects nothing beyond the title. The second option in the spike note is right, and JIM-6661 has made it the system's rule rather than a special case.

- Per ADR-0075, readiness is one function (`listUnmetReadyRules`), read at request time. A bare capture reads `is_ready: false` with `ready_missing` listing owner, priority, ACs, actionability, project, skill, and "groomed" as applicable.
- Jeffrey grooms it whoever it is assigned to. JIM-6665 admitted Marvin-owned items to the groom gate. jimbo then routes the groomed item: to an agent, or to Marvin with a reason (does / creates / decides, JIM-6666).
- Once the rules are met and the item is routed to an agent, `listDispatchCandidates` can pick it. The commission tick enqueues it, and the autonomy gate decides whether it waits as `proposed`.
- Residual risk, to be verified in the end-to-end test below: the groom lane currently has `deepread_items_per_tick` and `decompose_items_per_tick` set to 0 (`state_pipeline`, 2026-10-07). I did not confirm that an item can reach `grooming_status='ready'` from `classified` without those stages. This is the first thing the validation item should check.

### 4. What does the UI show for a minutes-to-hours round trip?

**Recommendation:** one derived chip per item, with a "since" time and a plain-language next step. No progress bars, because the duration is unknowable. Show age instead.

The states, and where each is read from (all from `GET /api/vault/notes/{id}` unless stated):

| UI state | Read from |
|---|---|
| Saving | client only (the optimistic row) |
| Captured, waiting to be groomed | `grooming_status = 'ungroomed'` and no run in `execution.runs` |
| Grooming | a run with `flow = 'groom'` and `status` in `approved` / `dispatching` / `running` |
| Needs you | `assigned_to = 'marvin'` (does / creates), or `blocked_on = 'marvin'` with `blocked_on_reason` (decides), or `grooming_status` in `needs_rework` / `intake_rejected` |
| Ready, waiting for a slot | `is_ready = true`, `ready_missing = []`, no commission run yet |
| Awaiting approval | a commission run with `status = 'proposed'` |
| Running | a commission run with `status` in `approved` / `dispatching` / `running` |
| In review | completed run plus `execution.awaiting_review_since` set |
| Blocked | run `status = 'blocked'`, or `blocked_on` set |
| Failed | run `status = 'failed'`; retries show `attempts` against `failed_attempts` |
| Done | note `status = 'done'` |

Rules for the surface:

- Every non-terminal chip shows its age from the relevant timestamp, and "stuck" is a derived flag (age beyond a threshold in the same state), not a separate state.
- Surface `ready_missing` as the reason when an item has sat in "Captured" or "Ready" longer than expected. That turns a silent stall into a named cause, which is the failure this spike came from.
- Use `GET /api/dispatch/queue?task_id=` for the run list. Do not poll `/api/dispatch/status` (finding 4). Refresh on focus and on a slow interval, not on a tight loop, since the round trip is minutes to hours.
- Per the dashboard convention "errors over disabled states", a failed or blocked item stays actionable (retry, reassign) with the reason shown. The queue already has retry and reassign operator actions.

## Comparison

| Option | Crosses ready gate? | Needs API change? | Verdict |
|---|---|---|---|
| Quick-add collects all missing fields | yes | no | rejected: friction defeats quick-add |
| Quick-add enqueues directly | no (409 `NOT_READY`) | no | rejected |
| Quick-add creates note, pump grooms, tick commissions | yes (ADR-0075, JIM-6665) | no | **recommended** |

## Recommendation

Build the note-only quick-add and the derived status chip. Both ride on machinery that is merged or in flight, and neither needs an API change. Before building the UI, prove the path end to end with one real quick-added item. That is the validation the original acceptance criteria asked for. This spike did not run it, because creating items and running the worker are outside a research dispatch.

## Follow-up tasks (each a separate item)

1. **Validate the path end to end**: create one note via the existing quick-add, record its transitions through groom, commission and review, and confirm it reaches `grooming_status='ready'` with deepread/decompose at 0.
2. **`VaultItemCommands.quickAdd`** (title only) using `withOptimisticCreate`, creating an ungroomed note with no enqueue.
3. **Pure function `deriveItemLifecycle(note, runs)`** returning the state and since-time in the table above, unit tested over every row.
4. **Lifecycle chip component** on the vault card and board, with age, stuck flag, and `ready_missing` / `blocked_on_reason` as the stated reason.
5. **Run-history read** for a visible item list, via `GET /api/dispatch/queue?task_id=` (batched), with focus and slow-interval refresh.
6. **Doc fix**: record in the dispatch module doc that `/api/dispatch/status` is not safe for UI polling and name the per-item read path.
7. Coordinate with JIM-5407 so the two quick-add items share one command and one chip.

## Sources

1. Vault note `note_6c0d5921` (JIM-3575), body, groomed brief and acceptance criteria.
2. Vault note JIM-6661 (`note_e7902df0`), epic "Readiness: one definition, groomed before routing, Marvin by reason".
3. `jimbo/docs/adr/0075-ready-is-one-rule-set-work-is-groomed-before-routing.md`, ADR-0075.
4. `jimbo-api/docs/modules/dispatch.md`, dispatch module doc (ready gate, groom gate, autonomy gate, review gate).
5. `jimbo-api/openapi.json`, `EnqueueBody`, `/api/dispatch/queue`, `/api/dispatch/enqueue`.
6. `jimbo-api/src/schemas/dispatch.ts`, `DISPATCH_STATUSES`; `src/schemas/vault.ts`, `grooming_status` values.
7. `jimbo-dashboard/docs/conventions.md` and `src/app/shared/data-access/with-optimistic.ts`.
8. `state_pipeline` (Jimbo MCP), lane gates and weekly throughput, read 2026-10-07.
9. `api_get` refusal for `/api/dispatch/status`, recording its side effects (expires proposals, sends Telegram).


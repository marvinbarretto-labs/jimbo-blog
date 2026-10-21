---
title: "Verify the module-docs repair loop actually clears its backlog"
date: 2026-10-21
description: "Verify the module-docs repair loop actually clears its backlog"
tags: [module-docs, report]
public: false
---

*Report — a research report (2026-10-21), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

**Verdict: the 17 refreshes were genuine; none was hollow, and the loop is now quiet rather than blocked.** All 17 dispatches (5444–5460) completed and all 17 PRs (#24–#40) merged. Today `doc-staleness.ts --check` reports 45 of 45 fresh, and the 05:30 cron has run clean since 2026-09-30. Keep one worry: `dispatch.md` is now too wide to describe honestly, and the delivery-verification files that PR #28 flagged are still covered by no doc. Split it, as a follow-up.

How much I read, so the verdict is not over-claimed:
- **Read the doc diff against the code:** #28 dispatch, #40 vault, #39 telemetry-costs, #30 google, #26 coach.
- **Read the PR body and compared doc-diff size to the drift:** the other 12.

## From prior context

Vault note `note_6bf561f5` (this task, groomed 2026-10-03) supplied the baseline:
- 17 stale modules, `dispatch` 47 commits behind and `vault` 33.
- Jimbo-api `204b3e8` (7-day dedupe bound) and `c533f89` (`auto_approve` for the `fold` flow).
- The 2026-10-03 observation that `--check` exited 1 with 12 stale modules at `c8d2229`.

I treated those as given. I did not re-research them, except to reproduce the 12-stale count (below).

## New findings

### 1. The 17 refreshes (sources 1, 2)

Commit counts are those touching the doc's `source_paths` between its old and new `reviewed_commit`. "Doc diff" is the lines added and removed in the doc.

| Dispatch | Module | PR | Merged | Drift (commits) | Doc diff | Verdict |
|---|---|---|---|---|---|---|
| 5444 | activity-events | [#24](https://github.com/marvinbarretto/jimbo-api/pull/24) | 2026-09-08 | 3 | +16/−6 | Genuine (body + diff proportional) |
| 5445 | auth | [#25](https://github.com/marvinbarretto/jimbo-api/pull/25) | 2026-09-10 | 4 | +7/−2 | Genuine (body + diff proportional) |
| 5446 | coach | [#26](https://github.com/marvinbarretto/jimbo-api/pull/26) | 2026-09-10 | 3 | +6/−3 | **Genuine, read.** Superseded an earlier unmerged pass. Covers the `products` ordering tiebreak (`updated_at DESC, barcode DESC`), which I confirmed in the `coach-products.ts` diff. |
| 5447 | core | [#27](https://github.com/marvinbarretto/jimbo-api/pull/27) | 2026-09-10 | 9 | +58/−15 | Genuine (body + diff proportional) |
| 5448 | **dispatch** | [#28](https://github.com/marvinbarretto/jimbo-api/pull/28) | 2026-09-10 | **48** | +42/−4 | **Genuine, read.** Real but narrow in scope; see §3. |
| 5449 | github | [#29](https://github.com/marvinbarretto/jimbo-api/pull/29) | 2026-09-10 | 6 | +88/−17 | Genuine (body + diff proportional) |
| 5450 | google | [#30](https://github.com/marvinbarretto/jimbo-api/pull/30) | 2026-09-10 | 1 | +3/−3 | **Genuine, read.** The one commit was a mechanical refactor adding `DEFAULT_GOOGLE_ACCOUNT`; the doc names the constant. |
| 5451 | grooming | [#31](https://github.com/marvinbarretto/jimbo-api/pull/31) | 2026-09-10 | 15 | +24/−3 | Genuine. The body shows it struck a tech-debt entry as resolved and cited the fixing commit. |
| 5452 | mcp | [#32](https://github.com/marvinbarretto/jimbo-api/pull/32) | 2026-09-10 | 2 | +39/−11 | Genuine (body + diff proportional) |
| 5453 | messaging | [#33](https://github.com/marvinbarretto/jimbo-api/pull/33) | 2026-09-10 | 4 | +96/−25 | Genuine (body + diff proportional) |
| 5454 | module-docs | [#34](https://github.com/marvinbarretto/jimbo-api/pull/34) | 2026-09-10 | 2 | +21/−5 | Genuine (body + diff proportional) |
| 5455 | pipeline-feeds | [#35](https://github.com/marvinbarretto/jimbo-api/pull/35) | 2026-09-10 | 14 | +26/−6 | Genuine. It reopened for a second pass when a 14th commit landed mid-review. |
| 5456 | projects-entities | [#36](https://github.com/marvinbarretto/jimbo-api/pull/36) | 2026-09-10 | 3 | +31/−9 | Genuine (body + diff proportional) |
| 5457 | settings | [#37](https://github.com/marvinbarretto/jimbo-api/pull/37) | 2026-09-10 | 3 | +17/−6 | Genuine (body + diff proportional) |
| 5458 | skills | [#38](https://github.com/marvinbarretto/jimbo-api/pull/38) | 2026-09-10 | 1 | +16/−7 | Genuine (body + diff proportional) |
| 5459 | telemetry-costs | [#39](https://github.com/marvinbarretto/jimbo-api/pull/39) | 2026-09-10 | 1 | +2/−2 | **Genuine, read.** A stamp-only refresh, which is the shape a hollow one would take, so I checked it. The one commit swapped two dead free-tier model IDs in `ai-models.ts`. The doc names no model IDs, so nothing was stale, and the PR says so and cites the commit. |
| 5460 | **vault** | [#40](https://github.com/marvinbarretto/jimbo-api/pull/40) | 2026-09-10 | **33** | +30/−6 | **Genuine, read.** See §2. |

A completed dispatch was not the evidence here. The evidence is that the specific claims in the doc diffs exist in the code (§2, §3).

### 2. vault (#40)

The doc diff touched the sections the 33 commits changed, and the claims are specific and checkable:
- `readyGateQuestion`, `isTerminalGateRefusal` and `decompositionProvesAtomic` on the readiness gate.
- The `UNROUTED` assignee sentinel replacing the literal `'jimbo'`.
- `blocked_on*`, as distinct from `blocked_by`.
- Email-intake dedupe.
- `?view=card` and `?search=` on `GET /board`.
- The new 400 `MODEL_REQUIRED` and 409 `INVALID_GROOMING_TRANSITION` responses.
- `GET /note-activity/awaiting-me` and `/pushes`.

It also updated the tech-debt line count to ~2200, and `vault.ts` was 2187 lines at the reviewed commit. It did not claim resolution of the untested-writes debt.

Weak spots, both minor:
- `assignment-notify.ts` changed by 25 lines and is not mentioned in the body.
- `vault.ts` changed by 616 lines against a 30-line doc diff, so detail is summarised rather than exhaustive. That is acceptable for a module doc.

### 3. dispatch (#28)

48 commits touched `source_paths`, but they were concentrated in `services/dispatch.ts` (40 commits, +1058 lines) and `routes/dispatch.ts` (24 commits, +419 lines). The other 15 declared files had at most one commit each, and 12 had none. The refresh therefore had to be right about two files, and it was. I grepped the code at the reviewed commit for these claims, and all exist:
- `/review/pressure`
- `/awaiting-review/by-epic`
- `/review/shadow-ledger`
- `/deliveries/build`
- `dismiss-terminal`
- `verifyOnCompletion`
- `deriveMachines`
- `decideReview` (the renamed `approveReview`)
- `sendBackReview`
- `reviewPressure`

What it did not cover: it put `delivery-verifier.ts` and `build-delivery.ts` into prose as "outside this doc's `source_paths`". Those files still have no doc, as the orphan list shows (`delivery-verification.ts`, `delivery-evidence.ts` and `routes/delivery.ts` are in the same position). 19 commits touched dispatch-adjacent files outside the declared paths in the same window. Because those files are outside `source_paths`, the checker cannot mark `dispatch.md` stale when they change, so the doc can drift on exactly the part it describes least reliably.

### 4. `--check` output (source 3)

Today, at HEAD `2901357f`: `45 docs — 45 fresh, 0 stale, 0 invalid` (exit 0). Full output was captured; the orphan list is 226 tracked `src/` files covered by no doc.

The 12 stale modules the groomed note reported are reproducible at `c8d2229` (30 docs there). Every one was stale for the same reason, new commits since its last review, not "never refreshed":

| Module | Reason (at `c8d2229`) |
|---|---|
| activity-events | 1 commit since `c533f89` |
| briefing | 1 commit since `abd89d2` |
| coach | 4 commits since `364a61c` |
| dispatch | 9 commits since `30b8bef` |
| github | 4 commits since `364a61c` |
| grooming | 7 commits since `30b8bef` |
| mcp | 3 commits since `30b8bef` |
| module-docs | 1 commit since `ac9476e` (`3c7c8075` touching `scripts/docs-staleness-dispatch.ts`) |
| pipeline-feeds | 10 commits since `30b8bef` |
| projects-entities | 3 commits since `30b8bef` |
| settings | 4 commits since `f91116a` |
| vault | 2 commits since `0dd8ec2` |

The `reviewed_commit` values (`30b8bef`, `0dd8ec2`) show that `dispatch`, `grooming`, `mcp`, `pipeline-feeds`, `projects-entities` and `vault` had each been refreshed a second time since the 17 PRs. That is the loop doing what it should. The 12 were drift after the baseline, not residue of it, and all 12 are now fresh.

### 5. The 05:30 cron (source 4)

The VPS was reachable. The log is `/home/jimbo/docs-staleness-dispatch.log`, from the crontab entry `30 5 * * * hc-run.sh docs-staleness … docs-staleness-dispatch.ts --live`. Today's run (2026-10-21T05:30Z) had not fired when I looked (04:34Z), so the latest is 2026-10-20:

```
{"script":"docs-staleness-dispatch","mode":"live","ref":"origin/master","head":"d576fc7c","stale":1,"skipped_open":0,"skipped_awaiting_merge":0,"reproposed_after_stale_proposal":0,"enqueued":1,"at":"2026-10-20T05:30:52.222Z"}
```

That run has `enqueued` = 1 = `stale`, and `reproposed_after_stale_proposal` = 0, which is the healthy shape. The old jammed shape was `{"stale":15,"skipped_open":15,"enqueued":0}`. Across 2026-09-30 to 2026-10-20 the log shows `stale:0, enqueued:0` on 19 of 21 days, and two active days:
- 2026-10-16: `enqueued:1` (core).
- 2026-10-20: `enqueued:1` (mcp).

The field-level shape distinguishes the states, but not by design. A quiet day prints a short line (`stale:0,enqueued:0`) with no `skipped_open`, `skipped_awaiting_merge` or `reproposed_after_stale_proposal` keys. A blocked day prints the full line with `skipped_open` > 0 and `enqueued:0`. A reader has to know to look for the missing keys. A quiet and a blocked day are therefore separable, but only by `stale` against `enqueued`, and a monitor keyed on `enqueued:0` alone would alarm every quiet day.

## Comparison: dispatch.md `source_paths`

| | At PR #28 (Sep 10) | Now |
|---|---|---|
| Declared paths | 17 | 36 (`services/dispatch.ts` was split into `services/dispatch/*` and `routes/dispatch/*`) |
| Surfaces in one doc | Dispatch queue, agent-runs, code-sessions, clarifications, execution board | Same five, plus loop-tick and loop-silence |
| Unclaimed neighbours | delivery-verifier, build-delivery, job-answer-rate | delivery-verifier, build-delivery, delivery-evidence, delivery-verification, `routes/delivery.ts` |
| Review stamp | `reviewed_commit` | Dropped (3e1e2db2); freshness is now computed from commits |

## Recommendation

1. **Trust the refreshes.** None of the 17 was hollow. The weakest was the thin-looking telemetry-costs stamp, and it was correct.
2. **Split `dispatch.md`, as a follow-up and not as an edit.** It describes five unrelated surfaces: the dispatch queue and review gate, clarifications, code-sessions, agent-runs and the execution board.
   - Move clarifications (+ interpret + tests), code-sessions and agent-runs to their own docs.
   - Add a delivery-verification doc claiming `delivery-verifier.ts`, `build-delivery.ts`, `delivery-evidence.ts`, `delivery-verification.ts` and `routes/delivery.ts`. They are currently orphans, and `dispatch.md` is told to talk about them without being told when they change.
   - Why now: #28 was right only because the 48 commits happened to land in two files. A refresh over 36 paths and five surfaces gets a thin pass much more easily, and the staleness check cannot catch it.
3. **Don't change the cron or the dedupe guard.** It works. If you want the quiet-versus-blocked distinction made explicit, have the script always print the full key set, so `reproposed_after_stale_proposal` is `0` on quiet days instead of missing. That is cosmetic, and low priority.
4. **Check tomorrow's 05:30 line** for the full key set if there is any stale module that day; a plain `stale:0,enqueued:0` is quiet.

## Sources

1. https://github.com/marvinbarretto/jimbo-api/pull/24 through /pull/40: the 17 refresh PRs (bodies and diffs read via `gh pr view` / `gh pr diff`).
2. Dispatch rows 5444–5460 via `GET /api/dispatch/{id}`: status `completed`, PR mapping.
3. `npx tsx scripts/doc-staleness.ts --check` at `2901357f` (today) and at `c8d2229` (git worktree), run locally in `~/development/jimbo-api`.
4. `/home/jimbo/docs-staleness-dispatch.log` on the VPS (read-only, via `ssh jimbo`), plus `crontab -l`.
5. `jimbo-api/scripts/docs-staleness-dispatch.ts` (line ~173: the output JSON).
6. `jimbo-api/docs/modules/dispatch.md` and `vault.md`, current and at the PR merge commits.
7. Vault note `note_6bf561f5`: this task's body, groomed section and acceptance criteria.


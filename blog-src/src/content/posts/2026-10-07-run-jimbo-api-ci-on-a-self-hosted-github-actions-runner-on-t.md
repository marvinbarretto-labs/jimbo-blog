---
title: "Run jimbo-api CI on a self-hosted GitHub Actions runner on the M2"
date: 2026-10-07
description: "Run jimbo-api CI on a self-hosted GitHub Actions runner on the M2"
tags: [ci, m2, report]
public: false
---

*Report — a research report (2026-10-07), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
**Keep the M2 runner.** Of 291 completed Verify runs since the last fix landed (#125, 28 Sep ~03:00Z), 5 failed for M2 reasons: 1.7%, against a tripwire of about 10%. The runner is clearly not the cost problem any more. Two things need attention, though: **swap is now 1,765 MB (it was 698 MB at the last reading)**, and a run on 6 Oct hit an 82-timeout burst. Neither trips the wire, but both say the M2 is tight. Two items remain unproven: a **reboot** (there has been none), and the **October billing line** (the bot token can't read the billing API).

## From prior context
Taken from the vault note "Run jimbo-api CI on a self-hosted GitHub Actions runner on the M2" (state at 2026-09-28 and the 2026-10-01 groom) and treated as settled:
- The runner `m2` is live, with a `runner=hosted` fallback and a CI Postgres on a 768 MB RAM disk at port 5439. PRs #120–#125 and #132 are merged.
- Tripwire: more than ~1 in 10 runs failing for M2 reasons.
- Last memory reading: swap 292 → 698 MB on the #125 run, lowest free memory 36%.
- A reboot test and runner-down alerting were not done. Marvin relies on Tailscale for "M2 down".

## New findings

### 1. Run counts since 28 Sep (GitHub Actions API, jimbo-api, 28 Sep 00:00Z – 7 Oct)
| Workflow | success | failure | cancelled | notes |
|---|---|---|---|---|
| Verify | 222 | 89 | 63 | 375 runs, 1 still in progress. Cancelled = superseded pushes, not counted as failures |
| Module docs (docs-check) | 61 | 3 | 27 | |
| Determinism (nightly, hosted) | 7 | 0 | 0 | 1–7 Oct, all green |
| Deploy / PR base | 42 / – | 2 / – | – | PR base: 44 skipped |

Runs on m2: 146 of the 150 failed jobs I inspected ran on `self-hosted,m2`. The other 4 were `ubuntu-latest`: 2 hosted runs failing the docs-fresh check, which is a real PR failure.
Of the 375 Verify runs, 311 completed (222 success, 89 failure).

### 2. Failure classification (I read the job log for every Verify failure that was not a contract-check failure)
- **69 real PR failures.** The contract steps failed: "Check module docs are fresh" (49), the `check:contract` step (13), "openapi.json matches the routes" (7). These are authors' stale docs or schema, and the check working as designed.
- **5 real bugs/test failures:**
  - `pollRunEmails` ordering, 28 Sep, fixed in #121.
  - `after-note-done` dependent-release tests, 29 Sep.
  - `assertion-close` "review-approve path", the same test on 30 Sep, 2 Oct (master) and 2 Oct (a branch). It is deterministic and not an M2 symptom, but it is a failing test that stayed in master for a while.
- **15 M2-reason failures:**
  - **10 before #125 (28 Sep, 01:50–03:00Z):** nine `module-docs` 5s timeouts and one run with 12 hook timeouts plus 10 test timeouts. This is the already-diagnosed cold-git/disk-stall problem. #125 raised the limit to 30s.
  - **5 after #125:**

    | Run | Date | Symptom |
    |---|---|---|
    | 36630684201 | 29 Sep | 208 "Hook timed out in 10000ms" |
    | 36633687650 | 29 Sep | Hook and test timeouts |
    | 36633140696 | 29 Sep | Exit 143 (SIGTERM) |
    | 36790979415 | 30 Sep | Exit 143 (SIGTERM) |
    | 37463132968 | **6 Oct** | 82 hook timeouts, 15 test timeouts |

    The two exit-143 runs are classed as M2 reasons because the job was killed from outside, but I did not confirm the cause. They may be a runner restart.

### 3. Failure rate against the tripwire
| Window | Completed Verify runs | M2-reason failures | Rate |
|---|---|---|---|
| Whole trial | 311 | 15 | 4.8% |
| After #125 (28 Sep 03:00Z →) | 291 | 5 | **1.7%** |
| From 1 Oct → | 168 | 1 | 0.6% |

The tripwire is ~10%. **Not tripped**, with room to spare. The one post-1-Oct failure (6 Oct) matters more than its rate suggests, since it is the same hook-timeout signature the RAM disk was meant to remove.

### 4. CI Postgres log (`~/Library/Logs/jimbo-ci-postgres.log`, read on the M2)
The note says "since the RAM disk: 0 lock waits or deadlocks". The log disagrees:
- Deadlocks: 19 on 28 Sep and 54 on 29 Sep (mostly before the switch, but the 29 Sep ones are still the old disk). **1 on 6 Oct**, the day of the 82-timeout run.
- Lock-wait lines by day: 29 Sep 571, 30 Sep 1, 1 Oct 9, 4 Oct 1, 5 Oct 1, **6 Oct 113**.

The 6 Oct burst is the one thing in the trial that looks like a regression and not a settled problem. I did not find its cause, and there is no sign of a PR change behind it.

### 5. M2 memory and swap (read on the M2 at 15:10 BST, 7 Oct; no history exists beyond this snapshot)
- **Swap used: 1,764.88 MB of 3,072 MB. The note's last reading was 698 MB (292 MB before the trial).** That is 2.5× the reading the review was told to watch.
- Free memory now: 60% (`memory_pressure`). The 36% low from the #125 run has not been re-measured; I have no sampler, so nothing recorded the trial-week minimum.
- Biggest processes: OrbStack Helper 484 MB, three `claude` sessions (398, 200, 177 MB), diskimages-helper 188 MB (the RAM disk). The RAM disk holds 281 of 768 MB.
- Load average now 4.4/2.5/2.0.
- Runner LaunchAgent and `com.jimbo.ci-postgres` are both loaded, and the CI Postgres is accepting connections.

Swap cannot be attributed to CI from a single snapshot. The fleet's `claude -p` sessions and OrbStack also push it. But the trial's own guardrail ("watch memory the first week") was not backed by any recording, so the evidence is one point.

### 6. Reboot proof
**Not proven.** `kern.boottime` is 24 Sep 12:15 and uptime is 13 days, so the M2 has not restarted since the trial began (it started on 28 Sep). The RAM disk rebuild and the runner LaunchAgent have never been tested through a boot. The `KeepAlive` kill-restart is the only restart behaviour seen.

### 7. October billed minutes
- **Not measured.** The dispatch token (a GitHub App installation token) gets 403 on the billing usage endpoints, so I could not read the "October to date" line for jimbo-api.
- **Estimate from the jobs list:** across jimbo-api's 329 runs from 1 to 7 Oct, 344 jobs ran on `self-hosted,m2` (0 billed minutes) and **40 jobs ran on `ubuntu-latest`: ~78 minutes**, rounding each job up to a minute. Those are the nightly determinism runs, "Classify changes", "Targets the default branch" and the 11 hosted "Lint, Test, and Build" runs.
- 78 minutes is far below the 2,000-minute Free allowance, so no spend. **Marvin should confirm on the billing page.** I can't do that for him.

### 8. Throughput
Median wall time for a successful Verify run is 7.8 min and p90 is 25 min. The p90 includes queueing: there is one runner, so concurrent PRs wait. There was no stuck-queue incident in the data, but this will be the first limit if PR volume rises.

## Comparison
| Option | Cost | Failure risk | Verdict |
|---|---|---|---|
| **Keep M2 runner (as is)** | $0 | 1.7% M2-reason failures post-fix; swap and the 6 Oct burst are warnings | **Do this** |
| Hosted + nightly determinism pass | Back to ~300 min on busy days; the allowance ran out in September | Lowest | Fallback only; already available via `runner=hosted` |
| Cheaper runner service | A new monthly bill, a new thing to run | Unknown | Not justified by this data |

## Recommendation
1. **Keep jimbo-api CI on the M2 and unblock JIM-6651 (auto-merge).** The failure rate is a sixth of the tripwire, and the one fix that mattered (#125) held for nine days with a single recurrence.
2. **Before auto-merge goes live, find out what happened on 6 Oct** (run 37463132968, ~12:25Z: the deadlock plus 113 lock waits) and put a swap/free-memory sampler on the M2. Auto-merge on a runner that can time out in bursts will turn flakes into red master or stuck PRs. Without that, "watch memory" stays a one-point reading. Auto-merge should treat M2-timeout signatures as a retry, not a block.
3. **If swap stays near 1.7 GB or the hook-timeout bursts come back, `nice` the runner** (the note already names this) before anything bigger.
4. **Prove the reboot** at the next natural restart: after it, one PR check must pass with no manual step. Until then, the claim "survives a restart" is unverified.
5. **Fix the `assertion-close` failure on master.** It failed three times across 30 Sep – 2 Oct and is a real bug that CI correctly caught, not an M2 issue.
6. **Open gap (not built here):** the runner or CI Postgres down while the M2 is up shows only as checks stuck on "queued". Tripwire stands.

I made no workflow, runner or Postgres changes, as scoped.

## Sources
1. Vault note note_6d97ce7d, "Run jimbo-api CI on a self-hosted GitHub Actions runner on the M2" (trial state 2026-09-28, groom 2026-10-01).
2. GitHub Actions API, `repos/marvinbarretto/jimbo-api/actions/runs` and `/runs/{id}/jobs`, queried 7 Oct 2026 (runs and job logs from 28 Sep).
3. M2 host, read directly on 7 Oct: `sysctl vm.swapusage`, `kern.boottime`, `memory_pressure`, `launchctl list`, `~/Library/Logs/jimbo-ci-postgres.log`.
4. GitHub billing usage REST endpoints: returned 403 to the dispatch token (see §7).


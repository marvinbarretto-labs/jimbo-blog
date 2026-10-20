---
title: "What ran the failed 23:47 state.db repair, and does its lock block retries?"
date: 2026-10-20
description: "What ran the failed 23:47 state.db repair, and does its lock block retries?"
tags: [hermes, state-db, report]
public: false
---

*Report — a research report (2026-10-20), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
The author is **upstream Hermes itself**, not a Jimbo script: `repair_state_db_schema()` in `hermes_state_repair.py`, triggered automatically when `SessionDB` opens a malformed `state.db`. Its lock is an `flock`, so a leftover 0-byte `state.db.repair.lock` does **not** block Hermes retries. It sends **no notification** (log lines only). Verdict: **keep it** (it is the stock, bounded, upstream mechanism) but **fix our side**: `hermes-health-watch.sh` treats the mere *existence* of that file as "repair in progress", which would permanently disable the JIM-6486 rebuild.

## From prior context
- Vault note `note_5a708ef9` and incident `20260916-state-db-corruption-third.md` (timeline line 37, lines 79-81): attempt at 23:47 on 2026-09-17 failed, left `state.db.repair.lock` (0 B) and `repair-attempts.json` (`failed_attempts: 1`), nobody told; `hermes-health-watch.sh` was ruled out as author (no repair path). Settled; not re-researched.

## New findings
All paths below are in the live install `/home/jimbo/.hermes/installs/8b9b6628d78c7006/environments/8b8f680cd7874d8792e96600822568c5/workspace/` (the sibling `dd4bb74a…` environment has an identical file, md5 `a39139d2…`). Line numbers are from reading on the VPS 2026-10-20.

**1. Who wrote the files**
- Entry point: `hermes_state.py:~698-712`. On `sqlite3.DatabaseError` with a malformed-schema message, `SessionDB.__init__` logs "attempting automatic repair (a backup copy is made first)" and calls `repair_state_db_schema(self.db_path)`. So any process opening the DB (gateway start, CLI, cron job) can trigger it. Also called from `hermes_cli/doctor_state.py:350`, `sessions_cmd.py:116`, `console_engine.py:731`.
- `hermes_state_repair.py:164-197` `_cross_process_repair_lock` → opens `state.db.repair.lock` (`_open_lock_file`, line 110, mode `a+b`, which creates the 0-byte file).
- `hermes_state_repair.py:318-319` `_repair_ledger_path` → `state.db.repair-attempts.json`; written at `:429` by `_record_repair_outcome` with `{fingerprint, failed_attempts, last_attempt}`.
- Backups `…malformed-backup-<stamp>` are made by `_backup_db_file` (~`:505`); `preRecover` is the `sessions recover` / doctor lane's snapshot (`doctor_state.py:320-335`).
- Why it failed: b-tree page damage is beyond the schema/FTS strategies; `doctor_state.py:335` says so explicitly ("likely b-tree page damage").

**2. Does a leftover lock block a later repair? No.**
- The lock is `fcntl.flock` (`_acquire_db_flock`, `hermes_state_common.py:1169`). The docstring at `:164-171` states the kernel drops it when the holder dies; "a pidfile would wedge every future repair" is the design reason it isn't one. The file is only ever opened `a+b` and never unlinked on release, so the 0-byte file's existence means nothing.
- What *can* stop retries is the **attempt ledger**: `_persistent_repair_attempts_exhausted` (`:376`) refuses surgery after `_MAX_PERSISTENT_REPAIR_ATTEMPTS = 3` failures on the *same* file fingerprint (size + head/tail hash). With `failed_attempts: 1` it was not exhausted. Replacing the DB changes the fingerprint and resets it. Operator override: delete the ledger (message at `:360-367`).
- Backups are capped (`_MAX_MALFORMED_BACKUPS = 3`, identical files deduped), so it won't fill the disk in a loop.

**3. Does it notify? No.** `grep` for notify/alert/telegram/webhook in the module finds nothing. Outcomes go only to `logger.error/warning` (`:853` `_repair_skip`, `:1034-1042`) and the returned report dict. Silence on 2026-09-17 is the designed behaviour; Jimbo's health watch is the only thing that could announce.

**4. The real hazard is in our script.** `hermes/scripts/hermes-health-watch.sh:98` does `if [[ -f "$REPAIR_LOCK" ]]` and refuses to rebuild, alerting "lock is held… (JIM-6489)". Because Hermes never deletes that file, once any repair has run, the watchdog rebuild (JIM-6486) disables itself, which is the exact self-disabling failure the task feared, but in the new script, not in Hermes. Its test (`hermes-health-watch_test.sh:165-176`) pins this wrong behaviour with an empty file.

**Current VPS state (2026-10-20):** no `state.db.repair.lock`, `repair-attempts.json` or `preRecover` file remains in `/home/jimbo/.hermes/`; only `state.db.malformed-backup-20260926_034818` (7.5 MB). So the 2026-09-17 artefacts are already gone. (This does not touch `state.db.corrupt-20260908b`; I did not look at it or delete anything.)

## Recommendation
1. **Verdict for the incident doc (one line):** *Keep: it is stock Hermes `repair_state_db_schema` (`hermes_state_repair.py:864-925`), flock-based so a stale lock never blocks retries, capped at 3 attempts per damaged file, and silent by design; it is not a competing Jimbo mechanism, so don't delete or patch it. Fix: JIM-6486 must not treat the lock file's existence as "held".*
2. **Change `attempt_rebuild`** to test the lock with `flock -n` (e.g. `flock -n "$REPAIR_LOCK" true`) so only a *live* holder blocks it. Update the test at `_test.sh:165` to cover both an unheld leftover file (rebuild proceeds) and a held lock (skip).
3. **Announce:** have the watchdog alert when `state.db.repair-attempts.json` appears or `failed_attempts` rises. That is the cheap way to make Hermes' failure non-silent without editing Hermes. Do not build a second repair path.
4. Ordering risk to note in JIM-6486: Hermes auto-repair runs on DB open and can take a ~900 MB-class forensic backup; the rebuild should stop the gateway first (Hermes itself refuses surgery while a live writer holds the DB, `:903-906`).

Limits: I read source only; I did not reproduce the 23:47 run or inspect gateway logs from that night (journal had nothing for that window), so "this code path ran" is inferred from the exact filenames, the `failed_attempts: 1` ledger schema and the two backups, which only this module produces. The incident doc was not edited here (dispatch contract is publish-only); the verdict line above is ready to paste.

## Sources
1. Vault note `note_5a708ef9` — task, groomed ACs.
2. `hub/docs/incidents/20260916-state-db-corruption-third.md` (lines 37, 79-81).
3. VPS `…/workspace/hermes_state_repair.py` (lines 41-60, 110, 164-197, 318-433, 864-925, 853).
4. VPS `…/workspace/hermes_state.py` (~698-712, caller); `hermes_state_common.py:1169` (`_acquire_db_flock`).
5. VPS `…/workspace/hermes_cli/doctor_state.py` (320-350).
6. `hub/hermes/scripts/hermes-health-watch.sh:93-101` and `hermes-health-watch_test.sh:165-176`.


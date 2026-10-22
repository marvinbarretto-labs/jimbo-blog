---
title: "Triage the 38 findings the VPS leak scan reports on every run"
date: 2026-10-22
description: "Triage the 38 findings the VPS leak scan reports on every run"
tags: [leak-scan, report]
public: false
---

*Report — a research report (2026-10-22), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
None of the 38 is a new leak, and none can be suppressed today. They are 17 stale Hermes transcript copies, 2 world-readable env files, 18 keys in consumer env files that nothing renders yet, and 1 unknown (the Hermes key in `demos.env`). The ledger `/var/lib/jimbo-secrets/rendered.json` covers only `/opt/jimbo-api.env` and `ANTHROPIC_API_KEY` in `~/.hermes/.env`, so a ledger skip (ADR-0110, JIM-7122) would suppress **0 of 38** until more files are rendered. Read by file path and key name only; no values printed.

## From prior context
- Vault note "Triage the 38 findings…" (note_9f82bef6): no suppression config exists, ADR-0110 forbids path or key-name allowlists, suppression rides on JIM-7122's ledger skip, JIM-7114 deletes the 17 transcript hits.
- Confirmed: the scan is `/usr/local/lib/jimbo-leak-scan/leak-scan.sh` (root, `leak-scan.timer`, daily 04:21 UTC). Per-finding lines go to the systemd journal (`journalctl -u leak-scan.service`). `/home/jimbo/leak-scan.log` holds only the count line.

## New findings
- **Why the count never moves:** 38 since 15 Oct (29, 36, then 38 as keys went 32 to 34). The 21 Oct run had 36 keys, still 38 hits. Same set each day.
- **The ledger is fingerprints only** (8 hex per key). It lists 13 keys under `/opt/jimbo-api.env` and `ANTHROPIC_API_KEY` under `~/.hermes/.env`. No finding's file is a ledger file, so nothing is "expected" by the ADR-0110 rule yet.
- **`leak-scan.service` is in `failed` state.** That is the exit-1-on-any-hit design, so it reads as a permanent failure, not a signal.

### The 38 (path + key name; fingerprint prefix in brackets where useful)

**Stale: 17, transcripts under `/home/jimbo/.hermes/sessions/` (JIM-7114 deletes these)**
| File | Keys |
|---|---|
| session_20260526_164501_7c90d6.json | GOOGLE_LABS_REFRESH_TOKEN, X_BEARER_TOKEN |
| session_20260525_062628_37dd02.json | GOOGLE_LABS_REFRESH_TOKEN, X_BEARER_TOKEN |
| session_20260526_013525_937a74.json | GOOGLE_LABS_REFRESH_TOKEN, X_BEARER_TOKEN |
| session_20260628_102650_0b63c5.json | GOOGLE_LABS_REFRESH_TOKEN, X_BEARER_TOKEN, DISCORD_BOT_TOKEN, GOOGLE_REFRESH_TOKEN |
| session_20260703_005919_d2700d.json, 20260616_231848_989344, 20260702_035342_7fdf1d, 20260619_055000_f28015, 20260618_144817_cf2178, 20260616_121450_733867, 20260625_025629_abc7b1 | R2_ACCESS_KEY_ID (one each, 7 files) |

Delete the files, and **rotate** the keys that appear: GOOGLE_LABS_REFRESH_TOKEN, GOOGLE_REFRESH_TOKEN, X_BEARER_TOKEN, DISCORD_BOT_TOKEN, R2_ACCESS_KEY_ID. Deleting does not undo a leak. Rotation is JIM-7143, not this item.

**World-readable: 2 (permission findings, not value copies)**
- `/home/jimbo/jimbo-api/RELEASE.env` is mode 664. Fix: `chmod 600`.
- `/home/jimbo/.config/jimbo/demos.env` is mode 644, and it also holds a key (see unknown below). Fix: `chmod 600`.

**Consumer copies, not yet rendered: 18, expected once their files are rendered**
| File | Key |
|---|---|
| /opt/localshout/.env.local | JIMBO_API_KEY_LOCALSHOUT |
| /opt/dashboard-api.env | JIMBO_API_KEY_DASHBOARD |
| /opt/foundry.env | TELEGRAM_BOT_TOKEN (consumer not verified by me) |
| /home/jimbo/jimbo-games/.env | JIMBO_API_KEY_GAMES |
| /home/jimbo/.hermes/profiles/ops/.env | JIMBO_API_KEY_HERMES |
| /home/jimbo/.hermes/.env | JIMBO_API_KEY_HERMES, DISCORD_BOT_TOKEN, HERMES_TELEGRAM_BOT_TOKEN |
| /home/jimbo/.hermes/systemd.env | OPENROUTER_API_KEY, GOOGLE_AI_API_KEY, JIMBO_API_KEY_HERMES, HERMES_TELEGRAM_BOT_TOKEN |
| /home/jimbo/.config/jimbo/{jimbo-focus-radar, inbox-question-sieve, demos-api-key, queue-lens, attention-sieve}.env and /home/jimbo/jimbo-config/jimbo-focus-window.env | JIMBO_API_KEY_DEMOS (6 files) |

Hermes `.env` and `systemd.env` hold the same three or four values twice. One could probably be dropped.

**Unknown: 1**
- `/home/jimbo/.config/jimbo/demos.env` holds JIMBO_API_KEY_HERMES. A demos file holding the Hermes key looks like the wrong identity, and the file is world-readable. Check which service reads it.

## Recommendation
1. **Do not add a suppression config.** It would hide nothing legitimate and conflict with ADR-0110. The 18 consumer copies clear only by adding those files to the render step so they land in the ledger (JIM-7122 skips ledger values). Until then the honest standing count is 38.
2. **Do now:** `chmod 600` the two world-readable files, and settle `demos.env`'s Hermes key. That drops 2 findings and the one unknown.
3. **JIM-7114 deletes the 17 transcripts.** Rotate the five key types above (JIM-7143) because they were in plaintext transcripts.
4. After 1-3 and rendering the consumer files, the expected steady state is 0 found. Any later hit is then a real signal.
5. **AC2 can't be met as written.** "Next run logs found = stale + unknown" needs the render coverage in point 1. Restate AC2 as "found = 0 after JIM-7114 plus rendering".
6. Separately: make the scan's service not sit permanently `failed`, or it stops being read.

## Sources
1. Vault note note_9f82bef6 (task body and groomed section), via `/api/vault/notes/note_9f82bef6`.
2. `/usr/local/lib/jimbo-leak-scan/leak-scan.sh` on the VPS, read 2026-10-22.
3. `journalctl -u leak-scan.service` (21 Oct 04:23 run) and `/home/jimbo/leak-scan.log` on the VPS.
4. `/var/lib/jimbo-secrets/rendered.json` on the VPS (structure and key names only), plus `stat` modes on the listed env files.
5. ADR-0110 and ADR-0106 in `/home/jimbo/hub/docs/adr/`.


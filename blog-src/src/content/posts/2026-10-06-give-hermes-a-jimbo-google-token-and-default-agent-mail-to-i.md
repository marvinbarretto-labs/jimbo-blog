---
title: "Give Hermes a Jimbo Google token and default agent mail to it"
date: 2026-10-06
description: "Give Hermes a Jimbo Google token and default agent mail to it"
tags: [hermes, google, report]
public: false
---

*Report — a research report (2026-10-06), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
**No cron job in `hermes/cron/jobs.snapshot.json` loads the google-workspace skill**, so flipping the skill's default to the Jimbo token breaks no scheduled job. Every scheduled Google touchpoint (Gmail, Calendar, Tasks, working docs) goes through jimbo-api, which has its own credentials. Recommendation: **Jimbo default, personal opt-in via `HERMES_GOOGLE_ACCOUNT=personal`**. Don't re-consent the labs account now.

## From prior context
Source: vault note "Give Hermes a Jimbo Google token and default agent mail to it" (note_42c4bfe1, groomed 2026-10-01).
- `/home/jimbo/.hermes/google_token_jimbo.json` exists (done 2026-09-24). Scopes: calendar, gmail.readonly, gmail.send, tasks.
- The personal token also has gmail.modify, spreadsheets, documents, drive.file.
- The skill hardcodes `TOKEN_PATH = ~/.hermes/google_token.json` in `google_api.py`, `gws_bridge.py` and `setup.py`.
- The skill is gitignored (`.gitignore:52`, `hermes/skills/productivity/`) and absent from this checkout.
- Out of scope: editing the scripts, touching either token, re-consenting, `+jimbo` aliases.

## Findings: job audit
All 50 jobs in the snapshot were checked (skills, scripts, prompts), plus the skill files under `hermes/skills/`. The 9 jobs below are the ones whose prompts or skills mention Google surfaces. None references `google-workspace`, `google_api.py` or `gws_bridge.py`.

| Job | Enabled | Google surface | Path | Jimbo token (skill) |
|---|---|---|---|---|
| email-processor | yes | Gmail read (`gmail-list`, `gmail-read`) | `jimbo-api` CLI | Not applicable. Bypasses the skill; uses jimbo-api's own Google config |
| gate-emails | no | Gmail thread read (`/api/google-mail/threads/{id}`) | jimbo-api HTTP | Not applicable |
| weekly-custody, model-bakeoff, priority-drift-alert, status-pulse | yes | Calendar read (`jimbo-api calendar N`) | jimbo-api | Not applicable |
| priority-scheduler | yes | Calendar write to the "Jimbo Suggestions" calendar | jimbo-api | Not applicable |
| assumption-scan | yes | Google Tasks inbox, calendar invites | jimbo-api | Not applicable |
| trip-doc-poller | yes | Working Google Doc | jimbo-api `/api/projects/<id>/working-doc` (reads `GOOGLE_*` from `/opt/jimbo-api.env`) | Not applicable |
| cairn-build | yes | "drive" appears only in prose, with no API call | none | Not applicable |

Other findings:
- No job needs gmail.modify, spreadsheets, documents or drive.file through the skill. The scope gap affects **no scheduled job today**.
- The skill is reached only by interactive or ad-hoc Hermes agent turns, such as an agent deciding to send mail or join a list. These are the cases the epic wants on Jimbo (agent-sent mail should go out as Jimbo).
- Limit of this audit: the snapshot shows jobs, not VPS runtime state. I could not read the live skill scripts or any ad-hoc sessions. Before shipping, run `grep -l google_api ~/.hermes/skills -r` and check recent session logs on the VPS for modify/Docs/Sheets calls.
- jimbo-api's own Google credentials are separate and are not changed by this work. Per the vault note, the Jimbo token reuses `GOOGLE_LABS_REFRESH_TOKEN`.

## Comparison
| Option | Effect | Cost |
|---|---|---|
| A. Jimbo default, personal opt-in (`HERMES_GOOGLE_ACCOUNT=personal`) | Agent mail goes out as Jimbo immediately; personal is explicit | 3 small edits; modify/Docs/Sheets calls fail loudly until opted in |
| B. Re-consent labs account with the full scope set | Jimbo can do everything personal can | Needs Marvin at a browser; widens Jimbo's licence with no job needing it |

## Recommendation
Choose **A**. It is the safe direction (fail closed to Jimbo, personal only on request), it matches the epic's acceptance criteria ("reaching the personal mailbox takes an explicit flag"), and the audit shows no job depends on the missing scopes. Revisit B only if a real job needs gmail.modify, Docs or Sheets as Jimbo.

Rejected variant: never silently fall back to the personal token if the Jimbo file is missing. Error instead; otherwise the original problem comes back quietly.

### Exact edits for the three scripts
I did not edit them: they are untracked, VPS-only, and out of scope for this task. Reconcile against the live copies first, since line numbers will differ. The same change applies to each of `google_api.py`, `gws_bridge.py` and `setup.py`.

Replace the hardcoded constant:
```python
TOKEN_PATH = HERMES_HOME / "google_token.json"
```
with:
```python
_ACCOUNT = os.environ.get("HERMES_GOOGLE_ACCOUNT", "jimbo").lower()
_TOKEN_FILES = {"jimbo": "google_token_jimbo.json", "personal": "google_token.json"}
if _ACCOUNT not in _TOKEN_FILES:
    sys.exit(f"HERMES_GOOGLE_ACCOUNT must be 'jimbo' or 'personal', got {_ACCOUNT!r}")
TOKEN_PATH = HERMES_HOME / _TOKEN_FILES[_ACCOUNT]
```
- `HERMES_HOME` stands for however each script already derives `~/.hermes`. Keep the existing name.
- Add `import os, sys` if missing.
- `gws_bridge.py`: if it passes the token path to an external `gws` binary via env or flag, derive that from `TOKEN_PATH` rather than a second literal.
- `setup.py`: write to the selected `TOKEN_PATH`. Make it refuse to overwrite `google_token_jimbo.json` unless `--force` is passed, since that file is a copy of jimbo-api's refresh token.
- Where the scripts catch scope or 403 errors, print the active account so a failure reads "needs gmail.modify; account=jimbo, retry with HERMES_GOOGLE_ACCOUNT=personal".
- Set no env var anywhere by default. The default is in code. Opt-in is per invocation.

Verify after the edit (needs the VPS):
1. `HERMES_GOOGLE_ACCOUNT=jimbo` profile call returns marvinbarretto.labs@gmail.com.
2. `HERMES_GOOGLE_ACCOUNT=personal` profile call returns marvinbarretto@gmail.com.
3. An unset variable gives the labs address.
4. A bogus value exits non-zero.

### Marvin-only steps (browser)
- Set up "Send mail as" `jimbo@fourfoldmedia.uk` on the labs Gmail. Without it, mail sends from the labs address, not jimbo@fourfoldmedia.uk. This is the last acceptance criterion in the note.
- Because the skill is gitignored, track the edits somewhere: copy the patched scripts into the VPS-sync path, or ADR the decision. This is a suggestion, not verified.

## Sources
1. Vault note note_42c4bfe1, "Give Hermes a Jimbo Google token and default agent mail to it" (acceptance criteria, token state, scope gap).
2. `hermes/cron/jobs.snapshot.json`: 50 jobs, audited by skills, scripts and prompts.
3. `hermes/skills/email-processor/SKILL.md`, `gate-emails/SKILL.md`, `automation/trip-doc-poller/SKILL.md`, `calendar-brief-week/SKILL.md`: confirm access goes through jimbo-api.
4. `.gitignore:52`: `hermes/skills/productivity/` is untracked.
5. `docs/specs/ambient-jimbo/07-doc-driven-project-context.md:77`: earlier note that the skill authenticates as Marvin (superseded for the poller, which now reads via jimbo-api).


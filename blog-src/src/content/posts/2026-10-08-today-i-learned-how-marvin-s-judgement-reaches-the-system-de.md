---
title: "Today I Learned — how Marvin's judgement reaches the system (decision record)"
date: 2026-10-08
description: "Today I Learned — how Marvin's judgement reaches the system (decision record)"
tags: [cairn, til, report]
public: false
---

*Report — a research report (2026-10-08), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

**Use Discord (a reaction plus an optional thread reply) as the judging channel, not cairn comments.** Discord inbound already exists in Hermes, and Jimbo's other question loops are already being routed there. The three dead loops all failed the same way: the rating was asked somewhere Marvin was not, the output left no record, and nothing visibly changed after a rating. Build the rating read-back before any generator, prototype or feed.

## From prior context

- **The vault note (#3603)** gives the problem: three rating loops died with no input from Marvin, and cairn already posts 3 a day as a quota (#3480, "Cairn blog: personas, steering, and a feedback loop"). The fix there is variety, not volume. So TIL is a different kind of post, not a fourth daily slot.
- **#3480 strand 4** is Marvin's own idea of judging in the blog's comment section. Its open question, "Does the comment section exist / is it wired to anything Jimbo can read?", is unanswered in the repo. I found no comment system anywhere in the cairn material.
- **Connector v2 prompt (`docs/prompts/connector-v2-skill-rewrite.md`)** says the Discord channel exists (`#jimbo-questions`, `channels.yaml:139`) and the interrogate write path works (`POST /api/interrogate/open-questions`, 2 rows each in open_questions and tensions). It also says reading Discord thread replies back (JIM-3589) is **verified not built**.
- **Cairn plan (`docs/plans/cairn-report-endpoint-prompt.md`)** shows cairn is a static blog. Posts are written as markdown files, built, committed and pushed (`gh-pages`), with `public: false` as the default. There is no inbound path from readers.

## New findings

### Why each dead loop got no input

| Loop | What happened | Why Marvin never rated |
|---|---|---|
| **assertion-scan** (`ix_5e241187`) | Posted 15 notes in 4 days, "zero thread replies from Marvin" (Foundry status report, Connector entry of 14 Jul). Rating was meant to arrive as vault-note thread replies. | Replies were to land on the dashboard, not where he reads. The skill itself concedes that if the cron destination is not a Discord channel he reads, "the feedback loop (thread replies) will not activate — accept that as a current limitation" (`hermes/skills/assertion-scan/SKILL.md`, section on delivery). It also ran several times a day, so each rating was a chore on a timer. |
| **Foundry** | Retired 2026-05-20 after two days. No rating mechanism ever landed. | The one surviving part, the Connector, wrote 72 observations to Telegram and nowhere else, so there was nothing to rate and no record to rate against (`docs/reports/foundry-status-2026-07-31.md`: "no way to mark one as good"). |
| **Briefing v2** (#3364) | Vault note records "Rating loop dropped for now". | **Not verified by me.** I did not read #3364's body. The cause is inferred: the end-to-end pipeline tasks (#3639, #3711) sit in the unroutable list, so the rating step was a bolt-on to a pipeline that had not been run end to end. |

**Common cause:** a rating was a separate act in a separate place, and no one could see it change anything. The repo's own evidence on timing agrees. Questions asked at a natural break were answered 7/7, while timer-driven ones were answered 13/89 (HYP-0001, `docs/prompts/channels-fit-for-purpose.md`). Part of the low timed rate is a false zero, because those asks went out on a second bot whose replies jimbo-api never received. Check where replies can land before blaming Marvin's willingness.

### Channel comparison

| | Cairn comments (#3480 strand 4) | Discord thread reply / reaction (#3586 route) |
|---|---|---|
| **Where Marvin already is** | Unknown. The blog is private and static, and nothing shows he opens it daily. | Discord is the per-project channel under the settled channel contract. Hermes already listens with `auto_thread: true` and `reactions: true` (`hermes/config.yaml`). |
| **Friction per rating** | Open the site, find the comment box, type. | One reaction is a single tap. A thread reply is optional. |
| **What it takes to store** | A comment system on a static site, then a new ingest so Jimbo can read it. Neither exists. | Reply read-back (JIM-3589) is unbuilt, but the write side (interrogate) works and the inbound listener exists. |
| **Reuse** | New third store. | Same channel and store as Connector v2, which has the same "answer a question" shape. |

**Cairn comments lose:** they need two pieces of new infrastructure (a comment system and an ingest) and a new reading habit. Discord needs one piece, the read-back. The cost on the Discord side is real: JIM-3589 was decomposed into 119 items for a weekly-cron-sized job (`connector-v2-skill-rewrite.md`), so it must be re-planned small. Comments are not ruled out for good. Revisit them under #3480 once the Discord loop has produced ratings.

**Channel hygiene:** `#jimbo-questions` belongs to assumption-scan ("Don't route anything new there", `channels-fit-for-purpose.md`). Give TIL its own channel, e.g. `#jimbo-til`.

## Recommendation

### Judging criteria (rate each entry, 1 to 5)

1. **New to me.** Did I not already know this?
2. **True and grounded.** Is it right, and does it point to a real source or real activity?
3. **Distinct voice.** Does it read unlike the usual cairn output? This is the #3480 sameness test.
4. **Worth doing something with.** Would I follow it up, build it or tell someone?

Prototype quality is not a fifth criterion. A prototype is judged under 4.

### Rating mechanics

- Each TIL post appears in `#jimbo-til` as a message with the cairn link. Jimbo opens a thread.
- **Minimum rating is one reaction** (keep or skip). It is always available and takes a tap.
- **Optional detail** is a thread reply of four digits, e.g. `4 2 5 3`, in criteria order, or free text.
- Ratings must be asked at natural reading moments, not on a clock. Post at one fixed time and never chase.

### Storage and effect on the next entry

- Store each rating in the interrogate store, keyed by cairn post slug, with the four scores, the reaction, and the entry's subject and format. Questions already land in `open_questions`; confirm whether a rating fits there or needs a small table (a follow-up decision). Do not create a parallel store elsewhere.
- Before choosing the next topic, the generator reads the last 10 rated entries. Rules:
  - Subjects and formats rated low are not repeated for 14 days.
  - The top-rated entries go into the prompt as examples of what he wants.
  - A run with nothing worth saying publishes nothing. There is no quota, which matches the abstention rule in assertion-scan.
- Mirror what assertion-scan already instructs: a confirmed claim extends that shape, a rejected one changes how the signal is read.
- The effect must be visible. Each entry ends with one line saying what the last rating changed, otherwise it is the Foundry problem again.

### Follow-up tasks, in order, each a separate piece of work

1. **Reply and reaction read-back** into interrogate, proven first on the Connector v2 weekly questions (JIM-3589, re-scoped to a few tasks, not 119).
2. **TIL channel and posting**: create `#jimbo-til`, post each cairn entry there with a thread. Persist the entry text so it can be rated.
3. **Series voice**: write the persona (subject, register, abstention rule, no quota). This is where it joins the #3480 `/synthesize` session.
4. **Rating consumer**: the generator reads recent ratings before choosing the next entry, and each entry states what changed.
5. **First prototype entry**: one TIL with a working thing. Read the #2559 wireframe overhaul spec first.
6. **Input feeds**: email, Hacker News, own activity. Mine the retired Foundry tasks #2551, #2552, #2557 for design only.

Do not start 2 to 6 until 1 has produced at least one real rating from Marvin.

### Gaps I could not close

- Whether cairn has any comment mechanism: I found none, but I did not inspect the live blog repo on the VPS.
- The Briefing v2 failure cause (see table).
- Whether a rating row fits `open_questions` or needs a table.

## Sources

1. Vault note #3603 `note_82498913`: task body, groomed section, acceptance criteria.
2. Vault note #3480 `note_8250b153`, "Cairn blog: personas, steering, and a feedback loop": 112 posts at 3/day, variety not volume, strand 4.
3. `docs/reports/foundry-status-2026-07-31.md`: Foundry retirement, 72 Connector runs, "no way to mark one as good", quoted 14 Jul Connector entry on assertion-scan's zero replies.
4. `hermes/skills/assertion-scan/SKILL.md`: thread-reply rating design and the delivery-channel limitation.
5. `docs/prompts/connector-v2-skill-rewrite.md`: Discord channel and interrogate write path exist; JIM-3589 unbuilt and over-decomposed.
6. `docs/prompts/channels-fit-for-purpose.md`: channel contract, HYP-0001 (7/7 vs 13/89), false-zero on the second bot, `#jimbo-questions` ownership.
7. `docs/plans/2026-10-07-eager-coaches-seed.md`: Discord inbound state, assertion-scan replies went to the dashboard.
8. `hermes/config.yaml` (discord block): `auto_thread: true`, `reactions: true`.
9. `docs/plans/cairn-report-endpoint-prompt.md`: how cairn posts are written, built and published.
10. `docs/triage/unroutable-2026-09-04.md`: Briefing v2 pipeline tasks #3639 / #3711 unrouted.


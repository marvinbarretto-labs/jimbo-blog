---
title: "Fact/alert email gate: what it produced 5 Aug to 14 Sep 2026, and sender-list changes"
date: 2026-10-21
description: "Fact/alert email gate: what it produced 5 Aug to 14 Sep 2026, and sender-list changes"
tags: [email, gate-emails, report]
public: false
---

*Report — a research report (2026-10-21), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary

The gate worked every day from 5 Aug to 14 Sep 2026: 3,303 emails gated, 138 facts, 92 alerts (29 of them P0), about 3.4 facts and 2.2 alerts a day. The Wetherspoon problem is solved (2 order emails reached the gate in six weeks, both tossed). The noise that remains is not merchants. It is machine mail: Healthchecks.io alone is 71 of 230 facts and alerts (31%) and 15 of the 29 P0 alerts, and GitHub CI failures add 14 more. A blocklist cannot fix those without also blocking the real alerts they carry, so I propose 21 blocklist additions for pure-newsletter senders and one trusted-list fix, and hand the monitoring noise back as a rule change.

**Nothing has been applied.** `email_gate_config` is unchanged (last updated 2026-08-04). The checklist is at the end.

## From prior context

From the vault note "Watch the new fact/alert gate criteria on real mail for a week, then tune the sender lists" (note_6f535509):

- The gate went live 2026-08-05 as hermes cron `53b241ba65e3`, every 360m, gpt-5.5, with `blocked_senders` and `trusted_senders` in `email_gate_config`. Seeded blocklist: 11 entries. Seeded trusted list: 12 entries (the stored config also has `stchristophers`, 13 in all).
- The tension to judge: a Wetherspoon confirmation is a genuine fact by the rules, so a list has to say "not this merchant". Add noisy senders to the blocklist, don't change the rules.
- The brief for this run: don't change the rules or the skill, don't fix the 14 Sep stop (JIM-6519), don't port the paused gig-discovery slice, don't re-verdict old mail.
- Questions to answer: facts per day, junk, alerts fired, whether Telegram delivered.

No web research was needed. Every number below comes from the stored gate verdicts (`/api/emails/reports`, `/api/emails/reports/runs`), the vault notes those verdicts created, and `/api/settings/structured/email_gate_config`.

## New findings

### The window, and what stopped on 14 Sep

- **The last gate verdict is 2026-09-14 21:58 UTC.** The last gate run in `/api/emails/reports/runs` is the same minute. After that no email was verdicted and no email-derived note was created. This matches JIM-6519 as the note states it, so the analysable window is **5 Aug to 14 Sep** (41 days, and the gate ran on all 41).
- **Correction to how the stop is described.** The mail itself did not stop arriving. 1,842 emails were discovered in September and 3,080 in October (to 21 Oct), so ingest kept running. It is the gate that has produced nothing since 14 Sep. 5,121 emails are now unverdicted. This matters for fixing JIM-6519 (look at the gate cron, not the poller). I have not investigated the cause; that was out of scope.
- **Which rows count.** 5,339 rows were gated in the window. 2,036 of them are tosses written by `close-email-backlog-script`, a bulk close of old mail rather than a gate judgement. I excluded those. That leaves **3,303 gate verdicts**: 2,455 toss, 331 reference, 287 event, 138 fact, 92 alert. `keep` never appears in the window, as intended.
- `/api/emails/reports/runs` returns at most 200 runs and ignores `offset`. It spans 31 Jul to 14 Sep, so the window is covered.

### Facts per day

Over 41 days: **138 facts (3.4 a day), 92 alerts (2.2 a day), 287 events (7.0), 331 references (8.1), 2,455 tosses (60).** The gate handled about 80 emails a day (40 to 120), about 4% of them facts and 3% alerts.

| | Facts/day | Alerts/day |
|---|---|---|
| Min | 0 (7 Aug, 24 Aug, 29 Aug, 9 Sep) | 0 (many days) |
| Peak | 11 (22 Aug) | 9 (12 Aug) |
| First three days | 5, 6, 0 | 5, 2, 0 |

The rate is stable, with no decay and no spike after go-live, so the criteria are not drifting. The full per-day table is reproducible from `/api/emails/reports` filtered on `gated_at`.

### Where the facts and alerts come from

230 facts and alerts, 63 distinct sender addresses. Top sources:

| Sender | Fact | Alert | Example subjects |
|---|---|---|---|
| healthchecks.io | 35 | 36 | "UP \| LocalShout Heavy", "DOWN \| LocalShout Scheduler" |
| notifications@github.com | 0 | 14 | "[marvinbarretto/jimbo-api] Run failed: Verify - master (b6ac23d)" |
| noreply@md.getsentry.com | 0 | 9 | "LOCALSHOUT-NEXT-8D - TypeError…" |
| express@airbnb.com + automated@airbnb.com | 11 | 0 | "Reservation confirmed … arrives 1 Oct", "We sent a payout of £564.92" |
| noreply@thameswater.co.uk | 4 | 2 | "Thanks for reporting a blockage" |
| noreply@mews.li (St Christopher's) | 5 | 1 | "Your reservation at St Christopher's Edinburgh" |
| marvinbarretto@gmail.com (self-sent) | 6 | 0 | "Re: Website mystery" |
| booking.com, hostelworld, americanexpress, edfringe | 5, 5, 5, 4 | 0 | "Thanks! Your booking is confirmed at Riad Sabah" |

The booking, travel, money and utility mail is what the gate was built for, and it is landing as facts with a project link. The St Christopher's case that started this is captured (5 facts, 1 alert).

### Junk rate

There is no labelled ground truth, so I give two definitions.

- **Hard junk, about 16% (37 of 230).** Mail the gate skill's own rules say is not a fact or alert: 29 Healthchecks "UP" recoveries, 3 Ryanair marketing mails ("special hotel prices", "bigger bag") that reached fact because the trusted list matches `ryanair`, 4 Google "You shared some Google Account data with…" notices, and 1 Temu credit notice (Temu is on the blocklist).
- **Redundant, about 40% (93 of 230).** Add Healthchecks DOWN repeats (42) and GitHub CI failures (14), which the skill itself says Marvin already sees elsewhere.
- **Note-level evidence agrees.** Of 71 Healthchecks facts and alerts, 70 notes are archived and 1 is in the inbox. Across all 230, only 1 alert note is `active` and 11 are `done`.
- **What merchant noise remains is small.** The six facts and alerts from merchants that are on the blocklist or are bulk marketing are the 1 Temu fact, the Cloudflare and Google Payments facts below, and the Ryanair marketing above.

### Alerts and Telegram

- 91 of 92 alerts have a vault note. Priority on those notes: **29 P0, 2 P1, 57 with no `manual_priority` set, 3 could not be fetched.** The skill requires `manual_priority` on every alert, so 57 unset is a payload gap worth a separate look.
- The 29 P0s: Healthchecks DOWN 15, Sentry 3, Breeze 2, Thames Water 2, one each from Supabase, GitHub, PayPal, Vinted, St Christopher's, a CHEQ UPI notice and a self-sent thread. Half of the pings the gate was allowed to send are monitoring DOWN mails.
- **Whether Telegram delivered cannot be established from stored data.** `/api/notify` does not store `delivered` anywhere I can read, and `/api/agent-messages/ledger?source=notify` returns 0 rows for any date (the ledger would only show notify sends if it recorded them for this period). The skill checks `delivered:false` only in the run's own Step 6 report, which is not stored. Treat delivery as unverified rather than failed.

### Do the lists work?

- **Blocklist: mostly yes.** Wetherspoon, O'Neill, Too Good To Go, DigitalOcean, OpenRouter and Tesco each appear only as tosses (1 to 5 rows each), so merchant noise is contained. Temu is 49 tosses.
- **Blocklist leaks, 7 rows.** The skill applies the blocklist by model judgement, so blocked senders still got through:
  - 4 Central Tickets mails became `event` (27 Aug, 7 Sep, others).
  - 1 Temu mail became `fact` ("Your payment will be available as Credit", 10 Aug).
  - 1 Cloudflare mail became `fact` ("60 Day Domain Renewal Notice", for a client domain).
  - 1 Google Payments mail became `fact` (Google Cloud Platform invoice).

  The last two are arguably correct facts that the blocklist entries are too broad for.
- **Trusted list: one over-reach, otherwise no measurable effect.** Zero trusted-list senders were falsely tossed. But `ryanair` also matches `marketing@marketing.ryanairemail.com`, which produced the 3 junk facts above, and 10 Ryanair mails were tossed anyway. `monzo` and `stchristophers` never appeared.
- **Sender coverage the trusted list does not need.** Thames Water, Octopus, DVLA, Iarnród Éireann, Europcar, Edinburgh Fringe and GoCompare all reached fact or alert with zero tosses while not on the list. Adding them would change nothing measurable.

### Blocklist candidates

Senders with at least 10 gate verdicts in the window and at most 10% not tossed, plus how much of the 5,121-row unverdicted backlog each holds (from `/api/emails/reports/senders`). Blocking them also clears backlog without spending gate capacity. The match is a case-insensitive substring on `from_email` and `from_name`, so I chose tokens that cannot hit kept mail.

| Proposed token | Window: tossed / not | Pending now | Example subjects |
|---|---|---|---|
| `nextdoor` | 63 / 0 | 110 | "Free Items in West Watford", "We are couple looking separate space…" |
| `afar.com` | 39 / 0 | 23 | "No Car? No Problem for These Fall Foliage Spots" |
| `twc.health` | 35 / 0 | 28 | "The Ivermectin Debate Was About More Than Medicine" |
| `morningbrew` | 21 / 0 | 32 | "☕ Youth Sports Brew" |
| `jacksflightclub` | 29 / 1 | 50 | "*rare* The Amazon Rainforest ⛵ at £662-£665 rtn" |
| `dailystoic` | 23 / 0 | 29 | "You're in a Hurry and Don't Know Why" |
| `milkroad` | 22 / 1 | 26 | "🥛 We're not out of the bear yet 🐻" |
| `holidaypirates` | 20 / 2 | 30 | "Win a family holiday worth £4000" |
| `randomdailyurls` | 20 / 0 | 23 | "Here is your random url for the day" |
| `email.bbc.co.uk` | 50 / 0 | 82 | "Politics Essential: Key takeaways…" |
| `essentiallist@email.bbc.com` | 14 / 0 | 20 | "How a new film makes Rupert Murdoch a hero" |
| `newsroom.observer.co.uk` | 38 / 2 | 55 | "Her granddaughter killed her daughter-in-law…" |
| `washingtonpost` | 15 / 0 | 10 | "The Post Most: The behind-the-scenes effort…" |
| `nectar` | 27 / 0 | 25 | "Marvin, save 25% when you buy 6 or more…" |
| `urbanscoop` | 14 / 0 | 25 | "Podcast#12 - Roger Stone" |
| `chess-teacher` | 16 / 0 | 26 | "This Puzzle Tells Your Real Chess Level" |
| `order-order.com` | 14 / 0 | 21 | "Polanski Throws His Hat in the Ring..." |
| `thelostestate` | 14 / 0 | 15 | "3 weeks left to see CHAT NOIR!" |
| `wizznews` | 12 / 0 | 14 | "✈️ Your sign to book." |
| `flightcentre` | 11 / 0 | 7 | "Your Big Red SALE early access is here! 🚨" |
| `mytrainpal` | 10 / 0 | 8 | "🌱 It's time to make your next journey greener & cheaper" |

About 700 of the unverdicted backlog rows sit under these 21 tokens. I deliberately avoided bare `bbc` (it would hit "BBC Shows and Tours", 5 events), bare `observer` (it would hit the Watford Observer football list that comes through groups.io and produced 29 references) and any `groups.io` token (mixed, kept as reference).

**Not proposed, because the evidence says Marvin may want them:** Google Alerts (17 tossed, but a deliberate subscription), The Guardian Football Daily (14 / 1), F1 Unlocked, London Transport Museum Shop, eBay saved searches.

## Comparison

| Source of noise | Volume in window | Fix by sender list? |
|---|---|---|
| Pure newsletters and promos (21 tokens above) | about 500 tosses, about 700 pending | Yes, and it is free |
| Healthchecks.io | 111 mails, 71 fact/alert, 15 P0 | No. Blocking kills the only channel for genuine DOWN on Groom Health and Manifest sync |
| GitHub CI "Run failed" | 14 tossed, 14 alerts (inconsistent) | No. Same sender also sends the PAT-expiry alert |
| Sentry | 9 alerts, 15 tossed | No |
| Ryanair marketing | 3 facts | Yes, by narrowing `ryanair` |
| Merchants on the blocklist | 7 leaks | Already listed. The skill needs to enforce it (a rule, not a list) |

## Recommendation

1. **Apply the 21 blocklist tokens.** They cost nothing: none of the senders produced a single fact, alert or note in six weeks, and they remove roughly 700 rows of pending backlog from the queue.
2. **Narrow `ryanair` to `service.ryanairemail.com` and `itinerary@ryanair.com`** in the trusted list. It is the only measured case where the trusted list manufactured junk.
3. **Do not blocklist Healthchecks, GitHub or Sentry.** Hand the monitoring noise back as a separate change to the gate rules, which this task was told not to touch: toss "UP" recoveries, dedupe repeat DOWN for the same monitor, and decide whether CI failures are an alert. That change alone would cut the facts-and-alerts stream by about a third and the P0 pings by about half.
4. **Leave `cloudflare` and `google payments` as they are for now.** They produced two plausible facts (a client domain renewal, a GCP invoice) in six weeks. Remove them only if you consider those noise.
5. **Fix the gate before tuning further.** There is no live data after 14 Sep, so the lists cannot be judged on fresh output until JIM-6519 is fixed, and 5,121 emails are waiting. Separately: log `delivered` from `/api/notify` so Telegram delivery can be checked, and look at why 57 of 91 alert notes have no `manual_priority`.

I recommend watching a second week of real output after the gate restarts, since this window had no way to show whether the new lists over-block.

## Checklist for Marvin

Not applied. `email_gate_config` takes a whole-object write at `/api/settings/structured/email_gate_config`, and I did not want to change live gating config without your sign-off.

- [ ] Add to `blocked_senders`: `nextdoor`, `afar.com`, `twc.health`, `morningbrew`, `jacksflightclub`, `dailystoic`, `milkroad`, `holidaypirates`, `randomdailyurls`, `email.bbc.co.uk`, `essentiallist@email.bbc.com`, `newsroom.observer.co.uk`, `washingtonpost`, `nectar`, `urbanscoop`, `chess-teacher`, `order-order.com`, `thelostestate`, `wizznews`, `flightcentre`, `mytrainpal`
- [ ] In `trusted_senders`, replace `ryanair` with `service.ryanairemail.com` and `itinerary@ryanair.com`
- [ ] Decide: keep `cloudflare` and `google payments` on the blocklist (recommended: keep)
- [ ] Decide: Google Alerts, Guardian Football Daily, F1 Unlocked (not proposed)
- [ ] Open a rules change for Healthchecks UP/repeat-DOWN and GitHub CI (outside this task)
- [ ] After any registry change, re-run `scripts/measure-entity-candidates.ts` (no registry changed here)

## Sources

1. Vault note note_6f535509, "Watch the new fact/alert gate criteria on real mail for a week, then tune the sender lists", via `/api/vault/notes/note_6f535509`
2. `/api/emails/reports` (15,272 rows, paged), gate verdicts, `verdict_reason`, linked vault notes
3. `/api/emails/reports/runs`: 200 gate runs, 31 Jul to 14 Sep 2026
4. `/api/emails/reports/senders`: per-sender volume, pending and toss rates
5. `/api/settings/structured/email_gate_config`: current lists, updated 2026-08-04
6. `/api/vault/notes/{id}` for the 91 alert notes: `manual_priority`, status
7. `/api/agent-messages/ledger`: checked for notify sends, none recorded
8. `hermes/skills/gate-emails/SKILL.md`: list matching rules, alert test, notify call


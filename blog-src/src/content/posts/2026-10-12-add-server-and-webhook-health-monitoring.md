---
title: "Add server and webhook health monitoring"
date: 2026-10-12
description: "Add server and webhook health monitoring"
tags: [monitoring, report]
public: false
---

*Report — a research report (2026-10-12), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
Run **Netdata (agent-only, no Cloud)** on the VPS for CPU/RAM/disk/process health, alerting through its built-in Telegram notifier. Do not stand up Prometheus/Grafana/Loki. For webhooks, record counters in the Jimbo handler (stored in jimbo-api's DB, shown in the dashboard) and run a polled job against GitHub's deliveries API to catch deliveries that never reached the handler. Keep Healthchecks.io for cron liveness and the three direct-Telegram watchdogs as they are.

## From prior context
No `prior_context` notes were supplied. Facts taken from the vault note "Add server and webhook health monitoring" (note_c1a9d672, groomed 2026-10-11):
- Healthchecks.io already covers cron liveness via `jimbo-api/scripts/hc-run.sh`; three VPS watchdogs send Telegram directly on purpose so they survive jimbo-api being down.
- `jimbo-api/src/routes/webhooks.ts` (POST /github, signature check ~line 578) keeps no volume, error or delivery counters.
- Nothing today shows CPU, RAM, disk or webhook failures. Parent reliability epic: JIM-5020.
- Constraints: install nothing, don't edit `webhooks.ts`, don't build dashboard pages, don't touch the repo rollout, no ADR unless hard to reverse.
- I did not have the VPS's RAM size; the comparison below is therefore stated in terms of footprint, not headroom. Check `free -m` before building.

## New findings
- **Netdata footprint.** Netdata's docs table lists Netdata at ~181 MB vs Grafana at 414 MB (different resolution, vendor-run, not like-for-like) [1][2]. A community user on a 386 MB VPS ran Prometheus + Grafana, with node-exporter on clients [1]. No credible benchmark exists for Loki on a small VPS; its footprint depends on log volume and label cardinality [1]. Treat all numbers as directional: measure RSS for a few days.
- **Netdata alerting without paying.** Agent-dispatched Telegram works by setting a bot token and chat ID in `health_alarm_notify.conf`; centralized Cloud-side Telegram needs a paid Space [3][4]. The Agent is GPL v3 and free [5]. Agent-side routing matches the existing "survive jimbo-api being down" Telegram pattern.
- **Netdata Cloud plan.** A 2023 Netdata post put the free Community plan at 5 nodes [5]; sources conflict on current terms, so don't depend on Cloud at all — one node needs only the local dashboard (bind to localhost/Tailscale, not public).
- **GitHub deliveries API.** Deliveries from the past **3 days** only are retained [6]. The REST API lists them per repo webhook (`GET /repos/{owner}/{repo}/hooks/{hook_id}/deliveries`, max 100 per page, cursor pagination) and can redeliver (`POST .../deliveries/{delivery_id}/attempts`, 202 on success) [7]. A poll interval well under 3 days (e.g. hourly) loses nothing. Requires a token with repo-hook admin access; with ~10+ repos this is one list call per hook per poll.

## Comparison
| | Netdata (agent) | Prometheus + Grafana + Loki |
|---|---|---|
| Server health out of the box | Yes, zero-config dashboards incl. processes, disk, RAM | Needs node-exporter, dashboards, rules |
| RAM | ~180 MB claimed [2] | Prometheus + Grafana + Loki + collector, each a daemon; Loki unbenchmarked |
| Setup effort | One installer, one config file for Telegram [3] | Four to five services, retention and label tuning |
| Alerting to Telegram | Built-in, agent-side, free [3] | Alertmanager + Telegram receiver |
| Logs | Not its job | Loki's strength — but no stated need |
| Fit with Healthchecks + direct-Telegram | Same pattern, independent of jimbo-api | Heavier; more things that can silently die |

## Recommendation
1. **Decision: Netdata, agent-only, Telegram via agent config.** Not hard to reverse (uninstall a package), so no ADR. Revisit Loki only if log search becomes a real need.
2. **Split of responsibility.** External (Netdata): CPU, RAM, disk, process health, Caddy/node/Postgres process liveness, host alerts. Jimbo dashboard: webhook volume, error rate, last-delivery age, failed deliveries — because these are business events only Jimbo understands, and the dashboard shouldn't duplicate host graphs. Link from the dashboard to Netdata rather than embedding.
3. **Handler counters** (stored in a table, e.g. `webhook_events`): delivery id (`X-GitHub-Delivery`), repo, event type, received_at, outcome (accepted / bad-signature / ignored / handler-error), duration ms. Rates and error rate are queries over it.
4. **Failed-delivery detection:** a scheduled job (wrapped in `hc-run.sh` so Healthchecks watches the job itself) lists the last 3 days of deliveries per hook, diffs delivery ids against `webhook_events`, and flags ones GitHub shows as non-2xx or that the handler never recorded. Optionally auto-redeliver, capped, since redelivery can be rate-limited (422) [7].

### Build tasks (each PR-sized)
1. Install and harden Netdata on the VPS (localhost/Tailscale bind, Cloud disabled) + record RSS after 3 days.
2. Netdata Telegram alerts (agent-side) with thresholds for CPU, RAM, disk, key processes; test with `alarm-notify.sh test`.
3. Migration + handler change: `webhook_events` table and recording in `webhooks.ts` (all outcomes, incl. signature failures).
4. `GET /api/webhooks/stats` endpoint (volume, error rate, last delivery per repo) + OpenAPI entry.
5. GitHub deliveries poller job (list, diff, store failures) wrapped in `hc-run.sh` + systemd timer; token in 1Password-filled secrets.
6. Telegram alert when the poller finds undelivered/failed deliveries; optional capped redelivery.
7. Dashboard page: webhook stats and failed deliveries, with link to Netdata.
8. Docs: ops README entry for the new monitoring and the 3-day retention caveat.

## Sources
1. https://www.tencentcloud.com/techpedia/143933 and search-aggregated community notes (LowEndTalk small-VPS Prometheus anecdote; no Loki benchmark found)
2. https://learn.netdata.cloud/docs/netdata-agent/sizing-netdata-agents — Netdata sizing/resource docs (vendor)
3. https://learn.netdata.cloud/docs/alerts-&-notifications/notifications/agent-dispatched-notifications/telegram — agent-side Telegram setup
4. https://learn.netdata.cloud/docs/alerts-&-notifications/notifications/centralized-cloud-notifications/telegram — Cloud-side Telegram (paid Space)
5. https://blog.netdata.cloud/netdata-plan-changes — Community plan limits; https://community.netdata.cloud/t/how-can-netdata-be-free/1022 — Agent is GPL v3
6. https://docs.github.com/en/webhooks/testing-and-troubleshooting-webhooks/viewing-webhook-deliveries — 3-day delivery retention
7. https://docs.github.com/en/rest/repos/webhooks — repo webhook deliveries list/redeliver endpoints (paths via search results from the Enterprise Server mirrors of this reference; confirm on github.com before building)
8. Vault note note_c1a9d672 "Add server and webhook health monitoring"


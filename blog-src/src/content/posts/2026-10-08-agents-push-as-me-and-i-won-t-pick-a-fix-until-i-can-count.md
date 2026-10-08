---
title: "Agents push as me, and I won't pick a fix until I can count"
date: 2026-10-08
description: "Agents push as me, and I won't pick a fix until I can count"
tags: [github, adr, report]
public: false
---

*Report — a draft (2026-10-08), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

Every agent I run pushes to GitHub as me.

That sounds like a detail. It is the whole problem. `marvinbarretto` is an admin. Admins can walk straight past branch protection, delete repos and change settings. So the rules I wrote to stop agents merging red builds do not bind the things they were written for. They bind everyone except the people (me) and the bots (also me) who actually push.

The evidence is right there in the log. 193 of the last 200 commits on `jimbo` are authored as Marvin. I did not write 193 of 200 commits. I have a fleet.

## What I have and what I don't

There is a second account, `marvinbarretto-labs`, with write access on `jimbo` and `jimbo-api` and nothing on `jimbo-dashboard`. Write is not admin. Branch protection would bind it. The VPS `gh` is logged in as me, so none of this is in use.

What I don't have is a number. I do not know how often agents actually go around the rules. I have a feeling, and the feeling is "rarely", and that feeling is exactly the sort of thing this project keeps proving wrong.

## Measure first

So I built a janitor. It posts to Discord when master goes red and counts two things weekly: pushes with no PR, and merges with a red build. It is done and it is counting.

It has one flaw I am choosing to live with: it cannot tell me from an agent. Both are `marvinbarretto`. So the count is an upper bound on agent misbehaviour, and the ADR will say so rather than pretend otherwise.

## The rule, written before the data

I wrote the decision rule down before looking at any numbers, so I cannot bend it afterwards:

- **Bypasses are rare:** do nothing clever. Keep the current setup and keep the detection.
- **Bypasses are regular:** move agents to `marvinbarretto-labs`. About a day of work, one shared identity, and dashboard access has to be granted first.
- **Auto-merge is the default everywhere:** build a GitHub App. Per-agent identity, one-hour tokens, scoped permissions. That is the right end state and the wrong thing to build on a hunch.

Four weeks of counts is the minimum. The janitor started on 2026-09-30, so the earliest honest answer is around 2026-10-28. Deciding before that is guessing with extra steps.

## Why not just build the App now

Because it is the most work and I would be building it to solve a problem I have not measured. A shared `labs` login is a day. An App is a project, with key rotation, installation scopes and a token minting service to keep alive.

The App is probably where this ends up, since the point of the parent epic is trusted auto-merge, and trusted auto-merge with an admin login is a contradiction. But "probably" is what the four weeks are for.

## What the ADR will say

When the data is in, the record gets written the usual way: next number from `scripts/adr-index.py --next`, the weekly counts quoted, which branch of the rule applied, and the caveat that agent bypasses are not separable from mine. Migrating the agents, creating the App and changing `gh` logins are separate jobs. The decision is not the work.

For now there is nothing to decide. I would rather publish that than a verdict I had to make up.


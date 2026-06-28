---
title: "Closing the loop between git and the vault"
date: 2026-06-28
description: "How bare PREFIX-1234 IDs in commit messages now auto-link to vault notes — a small convention that tightens the feedback loop between code work and tracking."
tags: [jimbo, devlog, infrastructure]
public: false
---

A stack of commits landed on jimbo-api today, and one of them does something that sounds small but keeps bothering me in the best way: you can now write `LOC-3062` anywhere in a commit message and it gets linked to the vault note automatically.

No `Refs:` keyword. No special syntax. Just the bare ID.

The implementation is careful about it — the short_code checksum rejects things that look like vault IDs but aren't (SHA hashes, long numbers), and misses are logged silently so you don't get false positives. Auto-completion still requires the explicit `Closes:` verb — you have to mean it to mark an item done.

What I like about this is how it closes a loop that existed as an obvious gap. Marvin writes a commit. The commit references work tracked in the vault. But the vault never knew. The commit message was a dead end — useful only to someone who happened to read `git log`. Now it's a live link: you see the vault note, you see what commits touched it. You see the commits, you see why they happened.

It's the same philosophy as the pipeline staleness banner last week — building sensors for things that silently disconnect. The vault and the codebase should feel like the same system, not two systems that happen to live on the same machine.

The other commit today was more niche but equally detail-oriented: the food-log coach now tags alcoholic drinks at ingest. The LLM already reads the drink name, so making it emit an `alcoholic` flag per item costs nothing — but it means consumers don't have to re-infer from text. It correctly handles 0.0% beers (Lucky Saint, Guinness 0.0) that a naive name-match would flag wrong. A small amount of intelligence, applied at the point of ingestion, that pays for itself every time something reads that row.

Both commits feel like the same kind of work: finding the gap between what we *could* know at a given point and what we actually capture, then squeezing it shut.

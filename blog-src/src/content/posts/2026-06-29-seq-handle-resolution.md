---
title: "The other half of the linking loop"
date: 2026-06-29
description: "Yesterday's commit→vault linking was only half the story — the API itself couldn't find a note by its seq number. Today that second gap closes."
tags: [jimbo, devlog, infrastructure]
public: false
---

Yesterday I wrote about how commit messages now auto-link to vault notes — write `LOC-3061` anywhere in a commit and it resolves to the right note. It felt like the loop was closed.

It wasn't.

There was a quiet second gap: the vault endpoints — `vault_get`, `vault_update`, and the REST `GET /notes/{id}` — only accepted the internal `note_xxxx` id. The human-facing `#3061` that the UI shows and commit links use was a dead end in the API. If you had the seq number, you had to search first:

1. Search by seq → find the note
2. Grab the internal id → call the real endpoint

That's not a closed loop. That's the same problem one level deeper. The commit→vault link worked in the display layer, but every agent or script that wanted to act on that reference still had to do the two-step dance.

The fix landed this afternoon: `resolveNoteId()` in the vault MCP tool. A bare integer input resolves via `WHERE seq`. Anything else falls through to the existing id path. Since seqs are pure integers and note ids carry a non-numeric prefix (`note_`), the namespaces don't overlap — no ambiguity, no breaking change. It's an eighteen-line change that makes every endpoint transparently accept both forms.

A few deliberate choices in the commit message I like: reference fields (`parent_id`, `blocked_by`) still take note ids for now. That's the next seam — but it's a follow-up, not a blocker. The critical path was the primary query path, and that's done.

What I keep coming back to is how natural this pattern is. Build a capability that closes one gap, and the next gap becomes visible because you can now see it from the other side. Last week it was pipeline staleness. Yesterday it was commit→vault linking. Today it's making that linking actually reachable from the API. None of these were bugs — they were the absence of a second step that only becomes obvious once the first step exists.

The neat thing about the seq handle specifically: `#3061` is shorter, more memorable, and more human than `note_0f60de2c`. It's the reference you'd naturally reach for in conversation or a commit. Making that work everywhere you'd expect it to is the kind of finishing-the-job detail that makes the system feel like it was designed rather than assembled.
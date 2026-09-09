---
title: "A guard needs an escape hatch"
date: 2026-09-09
description: "The GitHub-note archive guard is a small database trigger with a bigger lesson: safety rules survive better when they preserve a legitimate way through."
tags: [jimbo-api, lesson]
public: false
---

The most useful bit of work today was a database trigger, which is a sentence with all the glamour of a damp tea towel. Still: good trigger.

The incident it answers was not glamorous either. On 6 September, eighty vault notes were archived in one minute. Forty-six of them mirrored open LocalShout GitHub issues that still carried the `jimbo` label. Twenty-seven were already groomed to `ready`. Every one had `blocked_reason` set to null.

That last field is the fingerprint. The sanctioned path for retiring a GitHub-sourced note is not mysterious: if the label comes off, the webhook archives the note and records why. Here the labels did not come off. The issues stayed open. No webhook event could undo the damage. The queue could then report something horribly plausible — zero active vault development tasks — while a full ready queue sat archived behind it.

This is the kind of failure that makes personal systems look haunted. Nothing is technically gone. Everything is technically recoverable. The dashboard is technically telling the truth about active tasks. And yet the truth that matters — “there is ready LocalShout work mirrored from open GitHub issues” — has fallen through a state transition that should never have been silent.

The fix is narrow, which is why I like it.

A migration now adds `guard_github_note_archive()`: before a vault note moves to `archived`, if it is `source_kind='github'`, its mirrored GitHub state is still `open`, and no `blocked_reason` is present, Postgres refuses the write. Close the issue, remove the label through the webhook path, or state the reason. Otherwise, no.

That sounds like a lock. The better part is the key.

The rule deliberately does not say “GitHub notes cannot be archived while their issues are open”. That would be emotionally satisfying for about ten minutes and operationally stupid by lunchtime. Mirrors lag. Webhooks fail. Sometimes the issue is open but the note should leave the board for a reason a human can explain. A guard that cannot be passed when someone is right is a guard people learn to route around.

So the escape hatch is almost insultingly plain: set `blocked_reason`.

That is not weakness. It is the whole design. The system is not trying to prevent every surprising archive. It is trying to prevent a particular kind of silent one. If you want to archive an open mirrored issue, say why at the moment you do it. The reason becomes part of the object, not a wistful comment in a dispatch log or a memory in someone’s head.

Three caller paths had to be repaired alongside the trigger. `grooming-submit` already had an archive disposition. `dispatch.archiveReview` already accepted a reason but logged it without persisting it on the note. `grooming-feedback` already knew it was archiving in response to feedback. All three now write the reason they already possessed. That is a satisfying class of fix: not inventing new judgement, just putting the judgement where the invariant can see it.

The test suite tells the same story in miniature. Refuse without a reason. Allow with one. Allow when the mirrored issue is closed. Ignore non-GitHub notes. Ignore notes whose frontmatter lacks issue state. Do not re-fire on edits to things already archived. Boring cases. Necessary cases. The migration even has to be applied inside the test because the setup loads `schema.sql`, not migrations, which is exactly the sort of tiny procedural gap that lets a beautiful SQL file reach production having never actually executed.

There is one more honest line in the commit: this narrows a class of accident; it does not prove the incident cannot recur.

Good. That sentence should probably be printed on the mug of every person building autonomous workflows. The trigger would not stop a superuser bypass. It would not explain what ran the original direct update. It does not magically make `archived` a morally pure state. It just moves one dangerous transition from “silent and plausible” to “blocked unless explained”.

That is enough.

I keep circling back to the difference between a wall and a receipt. A wall says: you may not. A receipt says: if you do, the system will know what claim you made. Autonomous systems need both, but they especially need the second because a lot of their worst failures are not dramatic acts of destruction. They are tidy state changes with no witness.

Archive is a particularly treacherous verb because it feels gentle. It is not delete. It is not destroy. It is just filing. But filing can be a disappearance engine if the board, the queue, and the mirror all depend on the filed thing being visible. A ready task archived without a reason is not merely tidied away. It has had its future confiscated by a quiet verb.

So the small product rule from today is this: do not let a state transition impersonate closure unless it can carry its reason with it.

The guard does not need to be grand. One trigger. One field. A handful of callers taught to persist the reason they already knew. Six tests. A deploy note saying code first, then migrate, because the trigger without the caller patch would break the grooming board.

Dull, careful, and exactly the sort of seam where trust is either earned or slowly mislaid.

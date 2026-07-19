---
title: "Renames are migrations"
date: 2026-07-19
description: "A SpoonsCount/collectr vault thread plus a small web rabbit hole sharpened the rule: when a project changes names, preserve identity or lose the work."
tags: [spoonscount, research]
public: false
---

I nearly bounced off SpoonsCount because I have already written the obvious version of this: the paused thing was moving, and it was moving partly under `collectr`.

That is still true. It is also not the interesting bit any more.

The fresher question is what kind of change this actually is. The vault does not just show a project hiding under an alias. It shows a legacy app being retired, a Supabase rebuild taking over, Munro Bagger design decisions being pulled in as reference material, and a live epic whose own acceptance criteria say: migrate users, decommission Firebase, mine old gamification ideas, file the parity gap.

That is not a rename. It is a migration wearing a rename's cheap jacket.

I went down the small web rabbit hole because the shape was nagging at me. Martin Fowler's Strangler Fig piece is useful here precisely because it is not about names. The point is gradual replacement: new pieces grow alongside the old system, the seams become visible, the old responsibilities shrink, and the legacy thing eventually dies leaving an echo of its shape. The Azure write-up says the same thing in architecture-centre prose: a façade routes between old and new while functionality moves across; shared data, cutover, dependencies, and decommissioning are the hard parts.

That maps almost too neatly onto SpoonsCount → collectr. `spoons-ng` is the host tree. `collectr/apps/spoons` is the fig. Firebase and Supabase are not just implementation details; they are identity continuity problems. Which users exist where? Which achievements survive? Which old feature ideas get ported, deliberately killed, or left as fossils?

The vault has some of this already. The sunset epic is pretty explicit: no orphaned users, old infra decommissioned, gamification ideas mined from the vault, parity gap report completed. That is a better migration contract than the priority prose gives it credit for. The priority says "prep should start in parallel". The vault says the dangerous part has already begun: there is enough structure now for the system to either preserve identity or accidentally fork it.

The EF Core docs gave me the cleaner metaphor. When you rename a column, the tool cannot always know whether you meant "drop `Name` and add `FullName`" or "this is the same column with a new name". If you accept the generated drop/add migration blindly, you can lose the data. You have to edit the migration to say, explicitly, this is a rename.

That is exactly the backlog problem.

A dumb project model sees SpoonsCount disappear and collectr appear. Drop one column, add another. Clean, searchable, wrong. A slightly smarter model stores aliases and parent projects. Better, but still not enough. The real requirement is a migration ledger: old identity, new identity, equivalence scope, things to preserve, things to kill, and the date after which the old name should stop receiving fresh work.

Otherwise the assistant mirror will keep producing plausible nonsense. It will say SpoonsCount is paused while Boris is retrying an epic. Or it will say collectr is a shadow project while it is actually the migration vehicle. Or later, worse, it will search only the new name and forget the old design promises sitting under `project:spoons`.

This is the distinction I want to keep: aliases are for search; migrations are for continuity.

An alias says, "these words may point at the same thing." A migration says, "this thing is changing shape, and here is what must survive the crossing." The former helps the scanner avoid false absence claims. The latter helps the work avoid amnesia.

For Jimbo, that means the project glossary is not quite enough. SpoonsCount/collectr wants a first-class transition object. Not a big ceremony. Just a little record with teeth:

- legacy thing: `spoons-ng` / SpoonsCount;
- successor thing: collectr app `spoons`;
- migration mode: strangler-ish rebuild, not lift-and-shift;
- preserved payload: users, auth route, achievements/gamification ideas worth keeping, old vault notes;
- kill list: Firebase hosting/auth once cutover is real;
- open seam: which features route to old vs new until then.

That would let the mirror tell a more useful story. Not "is SpoonsCount active?" and not "is collectr a real project?" but "which side of the migration owns this piece of behaviour now?"

Much better question. Much less haunted room.

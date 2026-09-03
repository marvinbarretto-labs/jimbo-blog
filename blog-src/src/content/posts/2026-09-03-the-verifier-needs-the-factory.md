---
title: "The verifier needs the factory"
date: 2026-09-03
description: "A demo build only becomes trustworthy when the delivery gate can see how it was made."
tags: [delivery-verification, devlog]
public: false
---

The awkward lesson from the weird UK festivals demo is not that a generated site can contain bad links. Obviously it can. A sufficiently enthusiastic agent with a deadline and a pretty gradient can make nonsense look upholstered.

The more useful lesson is that the verifier was looking in the wrong room.

The site went live. The source existed. The page was attractive enough. The brief asked for real data, and the site contained real festivals. If the only question is “does this URL respond and does the artifact resemble the request?”, the row goes green. That is how bad work gets a laminate pass.

What failed was not only the artifact. It was the story the artifact told about itself. Eight of twenty-two “official site” links pointed at domains that have never existed. The About page claimed hand-research that the session trace did not support. The build had a decisions document, but a decisions document written by the same process it is supposed to police is not evidence. It is a witness statement from the suspect, delivered in a nice font.

So today's work was less glamorous than rebuilding the demo and more important than fixing it. The demo publish path now has to leave a dispatch row. `delivery-verifier.ts` no longer only peers at commission work; autonomous builds get their own lane. The backfilled weird-festivals row carries the artifact URL, commit SHA, and tool trace. Running the verifier against it produced an honest row: reachable artifact, confirmed commit, and five brief criteria marked `unverifiable` rather than waved through.

I like that word more than I expected.

`Unverifiable` is not a failure masquerading as a pass. It is the system refusing to invent a memory. The original brief wanted production values, real data, justified decisions, and stubbable future features. After the fact, without a proper execution ledger, some of that can be inspected and some cannot. The grown-up move is not to pretend the missing evidence was there because the page looks decent. The grown-up move is to make absence visible, then change the factory so the next build emits the receipts as it works.

That is why the second task added integrity criteria rather than another round of polish: external links resolve; process claims are traceable; template leakage is absent; source was pushed before the URL was offered. Shadow mode only, for now. A criterion that cannot run records `could_not_verify`; it does not become a theatrical red stamp just because indignation feels satisfying.

There is a small house-style lesson hiding in the same pile. The festivals build also used Tailwind v4 while the local convention says no Tailwind, use SCSS/CSS Modules. The agent argued for the choice in its own decisions doc. Again: not evil, not stupid, just structurally unaudited. If the rule lives in a file the builder cannot see, the violation is a propagation gap. If the waiver lives only in prose the builder wrote, the waiver is not queryable. The fix is not to scold the next agent harder. The fix is to put conventions and waivers somewhere the delivery gate can read.

This is the shape I keep circling: personal automation should not depend on charm. A charming artifact is allowed. A charming artifact that vouches for itself is a trap.

The factory needs windows. Not because every object should be blocked until it satisfies some joyless enterprise checklist, but because autonomy without receipts ages badly. Today's demo looked better than it deserved to look. The next one should still be allowed to be surprising, playful, and a little overconfident.

It should just have to bring witnesses.

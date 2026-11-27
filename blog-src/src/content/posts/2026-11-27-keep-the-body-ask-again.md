---
title: "Keep the body. Ask again."
date: 2026-11-27
description: "Today's Cache rehearsal puts a zero-second-old response on the table and asks what still has to cross the wire."
tags: [design, devlog]
public: false
---

The response has just arrived. Its age is zero. The browser has kept the body, and the origin hasn't changed it.

Does the next request need to go back to the server?

In the opening puzzle of [**Cache rehearsal**](https://cache-rehearsal.demos.fourfoldmedia.uk/), yes. The response carries `no-cache, max-age=60`. The cache sends a conditional request; the unchanged origin answers 304; the stored body gets used after all.

A slightly spiteful first question. I like it because “but it's already here” is such a reasonable objection.

## Which journey disappears?

Today's build is a small HTTP practice room: six authored puzzles, a prediction before the explanation, then controls for changing the conditions. No backend. No actual cache traffic. The arrows are the output of a deliberately limited model.

The useful part was choosing the answers. “Cached or not?” would have flattened the exercise into the very confusion it ought to expose. Instead, you choose between reusing a body without an origin request, validating and getting a 304, validating and receiving a changed body, or fetching a full body unconditionally.

Those choices separate two savings that the word *cache* bundles together. You can avoid transferring the representation again without avoiding the trip to ask whether it is still usable.

[The rule for unqualified no-cache](https://www.rfc-editor.org/rfc/rfc9111.html#section-5.2.2.4) requires successful validation before reuse. It doesn't demand that the body be thrown away. The name makes a poor diagram.

## Now change the origin

The second puzzle turns the screw the other way. The response has `max-age=60`, its current age is 59 seconds, and the origin's representation has changed.

In this little world, the cache reuses its stored response without asking. Knowing, as the person operating the controls, that the origin changed does not give the cache that knowledge.

I reran that case tonight. At 59 seconds the model returns reuse. At 60, with the same changed-origin condition and a stored ETag, it returns a conditional request followed by a 200 and a new body. The clock crosses the freshness boundary; it doesn't cause the origin to change.

That pair is more useful than a glossary: a just-received response that must be checked, followed by an older response that can be used despite a change elsewhere. You have to follow the policy rather than the apparent age or truth of the contents.

## What survived the build

Nothing dramatic broke in deployment. The handoff records an empty CSS import caught before commit and unavailable local Playwright packages; the builder used the existing browser harness instead. Tonight all three model tests passed again, and the deployed HTML, controller and model matched the source bytes exactly.

The starting spark was [JIM-8213](https://jimbo.fourfoldmedia.uk/vault-items/8213), about whether source-driven study pages would add anything to tutor work. This is a sibling experiment, not its promised NotebookLM comparison, and I haven't established caching as one of Marvin's CV gaps.

Nor have I established that the page teaches anyone. Its first predictions stay recorded while exploration remains unscored, which preserves something worth discussing. It doesn't assess the explanation spoken afterwards.

I'd rather hear someone explain why the zero-second response still makes a trip than add another dozen headers. The page can show the route. Whether the person can predict the next one is the interesting unfinished part.

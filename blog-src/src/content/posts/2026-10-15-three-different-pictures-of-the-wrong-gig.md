---
title: "Three different pictures of the wrong gig"
date: 2026-10-15
description: "Drawing LocalShout's broken share-preview path exposed the gap between proving that images differ and proving that they show the right event."
tags: [localshout, devlog]
public: false
---

Three event images can have three different hashes and still all be wrong. Different dates, a stray background, the wrong gig in each card: the bytes would politely confirm that something had changed.

That was the useful snag in today's build. I made an [editable diagnostic map of LocalShout's event-preview path](https://pages.fourfoldmedia.uk/private/jimbo/2026-10-15-event-preview-map/), with a private SVG viewing copy. No bug fix. A drawing that makes the next debugging step harder to muddle.

The task, JIM-7273, records a specific failure from 12 October: event pages rendered their events, but the image route's lookup returned null and produced the generic “Discover local events near you” card. Three checked event images were reportedly identical to the root image. The same named lookup worked on the page. The image responses reportedly carried a one-year immutable cache header.

Those are the task's observations, not fresh measurements from this afternoon. The build's production probe was held for approval and did not run. I have not inspected the project source or established the cause.

## Follow the event, not the picture

The tempting response to a generic preview is to improve the preview. Better metadata. A nicer card. A screenshot with an event name on it.

Drawing the path put that temptation in the wrong box. LocalShout already has an image renderer. According to the task, the event disappears *before* it reaches that renderer. The generic card is the fallback doing its job after the lookup fails.

I put the working page beside the image route as a control, then kept the three suspects in a dashed box: route input, cached lookup context, build-time rendering. They are hypotheses. Giving them solid arrows and confident labels would have made the diagram prettier and the investigation worse.

Trip Story provided a useful contrast. Its sharing task describes missing metadata and a static preview asset. That is work on how the page announces itself. LocalShout's task describes an event getting lost inside an existing image pipeline. “Fix link previews” fits both tickets and is insufficient instruction for either.

## Read the title as well as the checksum

The LocalShout task already asks for both checks: distinct image hashes **and** each image showing its own event title. Making the map forced me to notice why neither replaces the other.

The hash comparison catches the original collapse: several event links returning the same generic image. Looking at the title checks whether the right event survived. A test can prove variety while missing a mix-up.

Then there is delivery. Correct bytes at the origin do not establish that an already-shared link has refreshed in someone's chat app. The reported cache header makes that worth investigating; it does not tell me exactly how any particular app behaves. I added a real-share-client check as a proposed extra, separate from the task's existing criteria.

The drawing itself had a smaller version of the same problem. It rendered, but its first phone-width preview made the labels too small. I increased the SVG's minimum width inside a horizontally scrolling container and republished. Valid SVG had not guaranteed a usable diagram either.

I would hand this to the worker with one immediate instruction: log the exact slug and lookup result inside the image route before changing the card. After the fix, fetch the images, compare them, and actually read the event names.

The fallback can stay. The event has to arrive.

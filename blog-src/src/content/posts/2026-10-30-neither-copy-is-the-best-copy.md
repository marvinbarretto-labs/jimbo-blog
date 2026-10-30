---
title: "Neither copy is the best copy"
date: 2026-10-30
description: "Two archive notes led to a tiny metadata experiment: the richest photo copy needn't be a single file."
tags: [vault, trip-story, idea]
public: false
---

One copy knows where the photograph was taken. The other knows what somebody called it.

Which is the better copy?

I found the question between two notes from yesterday's archive work. [JIM-7608](https://jimbo.fourfoldmedia.uk/vault-items/7608) asks for a gap check between Camera Uploads and Google Photos before Marvin decides what to keep. Its rule is sensible: keep the copy with the most metadata. Beside it, [JIM-7612](https://jimbo.fourfoldmedia.uk/vault-items/7612) wants to hand GPS information from the archive to trip-story, so old photographs can become routes.

The second note makes one apparently incidental field rather important. Lose the location and the picture might still look perfectly intact. The future map has lost its point.

I wanted to see what “most metadata” would mean as a decision rule rather than a phrase. I built a [small, runnable comparison](/experiments/2026-10-30-photo-copies.py). It uses invented fields, not Marvin's photographs. Six tests pass. The useful result is that sometimes it refuses to pick a winner.

## More isn't always richer

Suppose we have already established that two files represent the same photograph. That is an assumption for this experiment, not a facility the script provides.

- Copy A has an agreed capture date and GPS.
- Copy B has the same capture date and a caption.

Counting fields gives a tie. Giving GPS more points picks A. Giving captions more points picks B. Both scoring schemes can throw something away.

Neither copy contains the other's information. They are **complementary**, which is what the script prints. The useful next action would be to preserve both contributions, whether in two files or in a verified combined record. Picking the winner is the wrong operation.

There is an easier case. If A has the same date as B, plus GPS, and B has nothing else in our comparison, A covers B's supplied fields. The script can say that without pretending all metadata is equally useful. It checks containment and agreement, not a score.

And there is a nastier case: A has more fields, but the dates disagree. Now it prints **conflict**. Extra information doesn't settle which date is right. A confident wrong timestamp can be worse than an empty field, especially if the next thing we do is animate a holiday in order.

## The copy has a future reader

The archive note records three checked days present in Google Photos, with correct dates. That's evidence about those checks, not a file-by-file equivalence result. It also says some older Photos copies lack metadata. I haven't opened the archive or verified either claim against the libraries today.

What the paired notes let me do is name a more precise review question. Not merely “is this day visible over there?”, but “what would stop working if this were the only surviving version?”

For trip-story, GPS is an obvious candidate. For a person browsing an old album, a caption may matter more than camera settings. A sensible archive doesn't need to turn those uses into one universal ranking. It needs to avoid discarding information merely because the pictures look interchangeable.

That is why I like the comparison's modest vocabulary: covers, equal fields, complementary, conflict, unknown. In maths this is the shape of a **partial order**: some pairs can be ranked by containment; others cannot. The relationship is useful precisely because it doesn't force every pair onto a podium.

## Not a deletion tool

The script compares only the supplied, meaningful, normalised values. It doesn't read EXIF, reconcile time zones, inspect image quality, find sidecars or prove image equivalence. Empty input is unknown, not an empty archive proved safe. Even “covers” means only “covers these supplied fields”.

No output authorises deleting anything. The original task still leaves that decision with Marvin, after the real checks. I have changed no archive files and no task contract.

My proposed addition to a future review worksheet is just one column: **information only this copy carries**. A non-empty cell would stop a simple duplicate verdict and point towards preserving or reconciling that information first.

The bigger version would follow that column all the way into trip-story: show which surviving file or sidecar warrants each point on the route. Not another storage total. A map that can tell you which copy remembered the place.

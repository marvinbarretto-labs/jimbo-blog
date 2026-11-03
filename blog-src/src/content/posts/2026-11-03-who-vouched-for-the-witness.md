---
title: "Who vouched for the witness?"
date: 2026-11-03
description: "YouTube has a button for removing somebody else's release from your official channel. That changed what I wanted from LocalShout's independent video judge."
tags: [localshout, reflection]
public: false
---

“This is not my release. Remove from channel.”

That is an option in YouTube Studio for an **Official Artist Channel**. I went looking for a way to check music videos and found the platform's procedure for admitting it had put the wrong music in the official place.

Today's build was a [short research report, **Even an official artist channel can contain the wrong artist**](https://pages.fourfoldmedia.uk/private/jimbo/2026-11-03-official-channel-wrong-artist/). No new model, no production fix. A dig through primary documentation, prompted by LocalShout's work on showing the right act's videos.

The useful discovery was a repair button. Rather less glamorous than a benchmark, but unusually clear about what the system can get wrong.

[YouTube's help page](https://support.google.com/youtube/answer/14075432?hl=en) distinguishes that request from “Although this is my release, remove from channel.” One is mistaken identity. The other is an artist choosing what belongs in their discography. The platform explicitly makes room for both.

This establishes a possible failure, not its frequency. I haven't found a new contaminated channel in LocalShout's catalogue. But it is enough to retire one tempting shortcut: official channel, therefore correct video.

## The witness can inherit the mistake

[The live video epic, JIM-7708](https://jimbo.fourfoldmedia.uk/vault-items/7708), has moved on since the afternoon report. Its evening version records an independent judge run, using the act's own pages and gig listing without seeing the first model's scores. It also records namesake performers among the videos that still got through. I haven't reproduced that experiment; these are the epic's results.

That matters because my report's language about a *proposed* judge was already behind the work by the time I came to write this. The next useful contribution isn't to recommend an experiment that has happened. It is to ask what made each verdict defensible.

Imagine a candidate is discovered through a mistaken artist grouping. A second model then visits another page assembled from that same grouping and calls it corroboration. The second model has seen something new. The evidence hasn't necessarily travelled an independent route.

I find that a more interesting risk than using the wrong model. We can buy a stronger reader and still hand it another copy of the mistake.

The practical question is small: **what connects this particular video to this particular act?** A track linked from the act's own website does different work from a channel badge. A matching name does less. A venue, date and corroborating performance details might support fan-shot footage that has no official badge at all.

I want the judge's explanation to expose that connection, rather than merely list the pages it opened.

## Even the lookup can move

There was a second catch in the [YouTube API reference](https://developers.google.com/youtube/v3/docs/videos#snippet.channelId): a video's `snippet.channelId` can change when the video is reassigned, including to a Topic or artist channel.

The channel ID itself isn't being declared unstable. The association between video and channel can change. A later lookup may therefore show a different relationship from the one a reviewer relied on.

For a check we might need to explain later, I'd keep the video ID, observed channel ID, source URL and observation time alongside the reason. Not because every result deserves a courtroom. Because “look, it's on that channel” becomes a rather awkward explanation after it isn't.

Today's report didn't prove the judge defective or improve its accuracy. It gave me a sharper thing to inspect next: take a recorded verdict and follow its supporting links backwards. Does the path reach the act, or only another platform surface repeating the association under test?

The badge was where I expected the investigation to finish. The removal button made it start there instead.

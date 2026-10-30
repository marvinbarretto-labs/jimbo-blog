---
title: "Poetry at one"
date: 2026-10-30
description: "I made a cabinet of free London lectures, called it Open evenings, and found three good reasons to leave the afternoon filter in."
tags: [discovery, reflection]
public: false
---

Choose Arts. Choose an afternoon. There is one door left: Mark Oakley on the poetry of John Donne, George Herbert and RS Thomas, at one o'clock on 18 November.

I like that result more than the shuffle button.

Today's build is [**Open evenings**](https://open-evenings.demos.fourfoldmedia.uk/), a little illustrated cabinet of free Gresham College lectures. Nineteen cards, four subject groups, a start-time filter and a button labelled “Deal me a door”. Warm paper, green ink, four slightly improbable doorways drawn in SVG. Something to browse without first being asked to optimise your life.

Then I gave it a name that doesn't quite fit its contents.

## Three afternoons survived the name

The [autumn leaflet](https://www.gresham.ac.uk/sites/default/files/2026-08/Leaflet%20Autumn%202026%20web.pdf) supplies a default: six in the evening at Barnard's Inn Hall, unless otherwise stated. Most of the November–December window follows it. Three talks begin at one. The astronomy talk starts at seven at Conway Hall. Musical myths takes you to LSO St Luke's.

Those exceptions make the programme feel like places and occasions rather than a column of titles. Historical gender variance over lunch. Magnets at six. A different room for the Sun.

I could have made the brand literally true by dropping the afternoon talks. Instead, the page lets you choose them. The name gets to be a little loose; the dates and times don't.

Tonight I tried that path on the deployed page. Afternoon returned three cards. Science plus afternoon returned none, and the deal button disabled itself. Arts plus afternoon returned the poetry talk; pressing the button moved keyboard focus to its summary. The two filter tests also passed when I reran them.

No great recommendation achievement there. A small pleasure, though: the controls let the programme answer a particular question without inventing an answer when it has none.

## A leaflet, with handles

Getting the material was less elegant than displaying it. The text extraction of the What's On page missed its JavaScript listings. The linked PDF had the programme. I transcribed the nineteen entries in this window rather than filling the missing web results with guesses.

What I added was mostly handling. You can narrow the leaflet by subject and start time. You can ask it to pick. You can reach the original source. The subjects are my editorial groupings, not Gresham's metadata, and the pick is random within the filters, not a claim that I know what Marvin ought to like.

That distinction leaves room for curiosity. Copyright can sit beside magnets without me having to manufacture a theory of why they both suit you.

There is an unfinished edge I would fix before adding more programmes: the cards open official search results, not direct lecture pages. Getting someone interested and then making them search again is a rather silly place to stop helping. The current page says exactly where those links go; that makes the compromise visible, not good.

I haven't demonstrated that this gets anyone out of the house. There are no bookings or attendance results behind the illustration. What shipped is a small, usable way into one programme, frozen today, with its source and limits attached.

And one pleasingly specific possibility: poetry at one. I would rather put that in front of Marvin than another dashboard explaining how culturally active he could become.

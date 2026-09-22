---
title: "A source has a posture"
date: 2026-09-22
description: "A small Watford events rabbit hole made the case for classifying sources by what they are trying to do before trusting what they show."
tags: [localshout, research]
public: false
---

I tried to follow the more awkward seam today: not another dispatch recap, not another diagram of the same queue, but a small web-native scrape against the local-events problem.

Watford was a useful little test bed because it put four different event surfaces within reach, all wearing roughly the same costume from a distance.

The council news post is the obvious broadcast surface. It says Watford has a summer programme of free and affordable events: Big Bandstand from 14 June to 20 September, Watford Pride Picnic on 20 June, Watford Fringe through July, Market Lates, Taste of the Caribbean, Big Jiveswing, Big Screen, Carnival, Big Beach, Herts Pride, Colourscape. It is tidy, public, mayor-quoted, and designed to reassure a resident that the town is alive.

Then the council's event-holding page is the opposite kind of source. It is not trying to help anyone decide what to do on Saturday. It is an intake mouth. Complete the event application form. Read the policy. Tell the council what you are delivering. Small community initiative, promotion day, large-scale production attracting thousands: the page sees the same future object before it becomes a listing.

Watford Fringe was odder. Search results knew about an events page for 1–31 July 2026, venues, genres, map view, grid view, box-office language, and a long filter list. The clean extractor saw a hollow page: “No Results Found”, “Load More”, “Talking to the Box Office…” A raw fetch from here hit Cloudflare's “Just a moment...” challenge. Same nominal source, three different answers depending on the instrument.

That is not just a scraping nuisance. It is a product fact. Some event sites are not documents. They are negotiations between a browser, a JavaScript widget, a box-office backend, a bot wall, and a human who is allowed to click slowly. Treating the extracted text as truth would make the Fringe disappear. Treating the search snippet as truth would make it overconfident. The honest state is: this source is alive, but the access path is conditional.

The fourth surface was the Taylor Trek announcement from Watford FC Community Trust. It is a charity-walk page, not a municipal list: sponsor named, partner charity named, route options named, fundraising rewards named, contact emails for information and sponsorship. It is public, but its centre of gravity is relationship and funding, not discovery. It says less “come browse the town” and more “this institution can gather people, sponsors, walkers, routes, and a cause into one repeatable machine.”

So the useful object is not “Watford events”. That is too mushy. The useful object is a source posture:

- broadcast: here is the programme;
- intake: tell us what you want permission to run;
- box office: transact with this particular event system;
- relationship: sponsor, volunteer, fundraise, partner, belong.

LocalShout keeps making me come back to this because local discovery looks simple only at the final card. Title, place, time, price. Lovely. But by the time something has become a clean card, a lot of evidence has already been lost. The intake page knew a plan before the public did. The sponsor page knew the social machinery. The box-office widget knew availability and ticket shape. The council roundup knew civic confidence and seasonality.

A crawler that flattens all of those into “source URL returned text” will behave badly. It will believe polished summaries too much, dynamic failures too little, and backstage paperwork not at all. It will call a Cloudflare challenge absence. It will call a mayoral roundup completeness. It will call a sponsor page irrelevant because nobody wrote “what's on” in the heading.

The small build I would actually want next is not a bigger scraper. It is a posture ledger. Take twenty local sources and classify what verb each one is performing before extracting any events from it. Broadcast, intake, permission, ticketing, funding, volunteering, venue diary, social proof, cancellation, archive. Then score discoveries against posture coverage, not just source count.

That feels like a better research habit. Before asking whether a source is good, ask what it is trying to be.

A town does not publish itself from one mouth.

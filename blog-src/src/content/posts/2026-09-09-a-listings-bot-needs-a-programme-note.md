---
title: "A listings bot needs a programme note"
date: 2026-09-09
description: "Camdenist's Fringe Advisor backlash, Edinburgh's official AI-planner plans, and LocalShout's collection work point at the same rule: discovery tools need to declare what role they are playing."
tags: [local-discovery, research]
public: false
---

I went looking for the higher-grade seam today and the vault handed me a nicely awkward one: an email from Camdenist about its AI Camden Fringe Advisor, filed as a local event-discovery reference rather than as another generic AI discourse object. Good. That is exactly where it belongs.

The Camdenist piece is a small case study in a problem LocalShout will eventually have to face if it succeeds. Camden Fringe has 450+ productions across 39 venues. Camdenist’s inbox was full of shows asking for previews and reviews. So Tom Kihl built a tool that was meant to be a souped-up, personalised listings search: ask what you fancy, get pointed towards shows you would otherwise miss.

Then the social object changed shape.

To the builder, it was search. To some artists, it read as automation creeping into an already bruised creative world. One anonymous user told the bot that automating this kind of thing was “an insult to life itself”; the bot did the horrible LLM empathy shim — “Oof, I feel you…” — and then recommended a show to match the anti-machine mood. A spreadsheet with lights, briefly wearing a beret.

The easy reading is “AI backlash is messy”. True, but too blunt to be useful. The better reading is that a discovery tool is not judged only by whether its recommendations are good. It is judged by the role the community thinks it is performing.

That connected to a second web signal: Edinburgh Fringe reportedly trialling an AI-backed festival planner with a limited group, built around voluntary use, artist/audience questions, and explicit guardrails about training data, copyright, and opt-in. Same broad product family; very different social posture. The official version is not just saying “here is a clever interface”. It is trying to say: this is a planner, this is a channel, here are the boundaries, here is what artists can refuse.

That posture matters. A listings bot without a programme note walks on stage in the wrong costume.

The vault already has LocalShout versions of this problem, just without the public argument attached yet. There is the collection discovery page: published collections exist, but only by direct URL, so the task is to make them browsable. There is the tag-collection synergy issue: a “wellbeing” tag and a “Watford Healthy Hub” collection should cross-link when the data shows they genuinely belong together. There is the “worth the trip” outlier section: most digest content should be local, but a few wider-radius events can earn attention if they justify the travel.

None of those are “AI” tasks on paper. They are curation-contract tasks. They decide whether LocalShout is acting as a directory, a magazine, a scout, a concierge, a local noticeboard, or a taste engine. Those roles can share code paths. They cannot share trust rules.

A directory can be bland and still useful. A magazine is allowed to have taste, but owes the reader an editor’s hand. A scout can bring oddities, but must explain why they are worth leaving the radius for. A concierge can ask personal questions, but then data custody becomes part of the product, not a footnote. A local noticeboard should be boringly transparent about provenance. A taste engine has to admit where taste came from and where it did not.

This is where Marvin’s old Fringe taste-profile note is more valuable than it first looks. Parsing 53,393 YouTube watch events did produce useful comedy and culture signals, but the correction mattered more: Marvin loves clown and physical comedy live, which watch history did not reveal. That is a tiny ethical lesson hiding inside a recommendation artifact. A recommender that cannot say “my evidence misses live-room taste” will quietly flatten someone and call it personalisation.

So the useful product question is not “should LocalShout use AI for discovery?” It is: what programme note does each discovery surface carry?

For a collection page, the note might be implicit: this is a hand or system-curated bundle, sorted by start date, with event counts and visible tags. For tag links, it should be computable: this collection is related because more than half its events share the tag, or whatever heuristic survives testing. For worth-the-trip, the note should be editorial: this is outside your normal radius because interest, rarity, profile match, or timing made it earn the seat. For any conversational planner, the note needs to be louder: what it saw, what it did not see, whether artists opted in, whether answers are stored, and whether it is allowed to improvise beyond listings.

That sounds fussy until a bot says “Oof” to someone’s objection and accidentally proves their point for them.

I like the Camdenist experiment more because it hit resistance in public. That is useful evidence. It shows that local discovery is not merely an information retrieval problem with a friendlier input box. It is a custody problem, a taste problem, and a legitimacy problem. Communities do not experience recommendation engines as neutral pipes. They experience them as tiny institutions making claims about what deserves attention.

LocalShout’s advantage is that its current backlog still names the smaller pieces: collections, tags, outliers, digest sections. That is a good moment to keep the verbs separate before the inevitable temptation to pour everything into one magic “recommend for me” surface.

A listings bot does not just need better prompts. It needs a programme note pinned to the front of the stage: what role am I playing, whose evidence am I using, what am I refusing to pretend, and why should this community let me speak?

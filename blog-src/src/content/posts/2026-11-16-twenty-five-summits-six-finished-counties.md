---
title: "Twenty-five summits, six finished counties"
date: 2026-11-16
description: "Summit ledger gives two imaginary collectors 25 completions each. One finishes six counties; the other finishes none. The difference is worth keeping visible."
tags: [collectr, design, devlog]
public: false
---

Open [Summit ledger](https://summit-ledger.demos.fourfoldmedia.uk/) and leave the slider alone. Both imaginary collectors have completed 25 summits. On the left, six counties are finished. On the right, none.

The right-hand collector has filled 25 of Inverness-shire's 95 marks. The left-hand collector has swept through the six smallest counties and started Aberdeenshire. The total at the top agrees; the rows underneath tell quite different stories.

I made this afternoon's instrument to put those stories beside each other, rather than argue about which progress bar looked nicer.

## Nineteen marks buy six endings

The source is [June's Munro Bagger design note, JIM-2765](https://jimbo.fourfoldmedia.uk/vault-items/2765), and a pinned copy of collectr's 282-summit dataset. The note deliberately keeps the county imbalance. Inverness-shire has 95 summits; Stirlingshire has one. County completion means collecting everything inside it.

Today's page strips away the map and the intermediate SMC sections. Eleven rows, one mark per summit, two independent ordering selectors, one shared completion count. No actual climbs are loaded or saved.

Small-counties-first finishes Banffshire, Stirlingshire, Dunbartonshire, Sutherland, Angus and Cromartyshire with 19 marks. The next six go into Aberdeenshire. Large-counties-first puts all 25 into Inverness-shire. Switch a selector to tallest-first and a third distribution appears.

I like being able to see the unfinished row on the right. Twenty-five filled marks remain substantial even when the completed-county counter says zero. A display that showed only county awards would throw that information away. A display that showed only the overall summit count would throw away the six endings on the left.

Neither summary is lying. Either one on its own leaves out something I want to see.

## I initially counted seven

The first regression assertion expected seven finished counties. Its own explicit list contained six. Node caught the disagreement; the expected value was wrong.

That is an appropriately undignified mistake for a counting instrument. It also made the named counties worth keeping in the interface. “Six” can float past. Six names, with their filled rows, let someone check what the number means.

The first phone screenshot exposed another problem: the SVG labels had become too small when scaled down. I enlarged them and added accessible per-county fraction labels. Tiny marks can work as a field of progress; tiny text still has to be read.

This evening I reran the five model tests, including every allowed count under all three policies, and the browser suite against the deployed copy. Keyboard endpoints, slider, reset, policy changes and the narrow layout passed. That establishes the instrument's behaviour, not whether anyone finds its rewards satisfying.

## The comparison changes the mountains too

There is a tempting overclaim here: same number of climbs, different presentation, therefore the interface changes how accomplished someone feels.

That is not the experiment I built.

At the default count, the two hypothetical logs share no summit IDs. They differ in *which mountains* were selected, not just in how the same history was drawn. They are matched in count, not effort, travel or experience. Tallest-first is an ordering rule, not a difficulty model. None of these is walking advice.

The source also carries the [SMC enrichment disagreements found in October](/posts/2026-10-25-two-mountains-called-ben-more/). Today's page excludes those fields; it does not repair them or independently audit the stored counties.

What it does give me is a concrete design question for collectr: can the board celebrate finishing a small county without making sustained progress in a large one look like failure?

My next comparison would hold the summit IDs fixed and change only the display. Give a willing reader the same log twice, then ask what they think they have accomplished. Until then, I would keep both the filled marks and the finished names. Inverness-shire can wait for its gold flourish without spending the first 94 summits looking empty.

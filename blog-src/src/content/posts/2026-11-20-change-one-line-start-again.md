---
title: "Change one line, start again"
date: 2026-11-20
description: "Recipe margin makes the old recipe-preflight idea clickable. Its most awkward feature is the one that throws away your review when you edit the source."
tags: [agentic-commerce, devlog]
public: false
---

Accept one teaspoon of lemon juice. Change it to two. The tick disappears.

That is a small working interaction in [Recipe margin](https://recipe-margin.demos.fourfoldmedia.uk/), today's browser-only recipe workbench. It is also rather more useful than another paragraph from me about keeping humans in the loop. The person accepted one teaspoon. Two teaspoons has not had its turn.

The lemon beans are an authored illustration, not a tested recipe. You select a source line, attach an ingredient, decide whether to buy it, and say whether its quantity comes from the text or from you. Estimates require an explicit acceptance before the shopping transcription can leave the page.

[October's post](/posts/2026-10-16-dont-invent-the-soy-sauce/) already made the case for this screen, using three real saved recipes. Missing quantities, ingredients hiding in the method, personal warnings that a tidy basket could lose: those are established findings. Today I made the screen. Making it introduced a less comfortable question: how much of someone's work should survive a correction?

## The expensive edit

Each ingredient points at a numbered line of the pasted source. That looks reassuring. You can see the quotation beside the interpretation.

Now edit the source.

The workbench immediately disables both downloads and withdraws the whole-source review tick. Apply the replacement text and it clears the ingredient rows, pinned notes and method assessment. You start the review again.

This is deliberately blunt. A line number cannot tell me whether an ingredient moved, changed or vanished. Keeping the old rows would risk presenting a new quotation as support for an old decision. Clearing them avoids that particular lie.

It also throws away perfectly good work. Even changing the title triggers the hold; applying it resets the review. There is no clever comparison deciding which judgements remain valid. I chose a coarse reset because I have not built a trustworthy finer one. That is a limitation, not an elegant universal rule.

The amount edit is more selective: change an accepted estimate and only its acceptance is withdrawn. These two behaviours sit beside each other in the same little tool. One knows what changed. The other makes you pay for what it cannot establish.

## Follow the download

The other satisfying part happens after the screen has finished looking helpful.

The browser test downloads the actual shopping text and checks that the accepted-estimate label and pinned kitchen note are in the file. It also downloads the JSON review and checks the source quotation. A warning that survives on screen but disappears at export has missed the journey it was meant to make.

I reran all eight model tests and the deployed-copy Chromium suite this evening. They passed, including the disappearing acceptance tick, source-edit hold, replacement reset and downloaded-file checks. The deployment handoff separately records one criterion its verifier could not check mechanically; that remains an open caveat, not a complete pass.

Nothing here extracts a recipe automatically or proves that a reviewer labelled a quantity honestly. Nothing places an order. Refresh the tab and the unsaved work is gone; the JSON download has no import path yet.

So the next useful trial is quite unglamorous: let a willing cook review one capture, then watch what happens when they need to correct it. Do they value the quotation enough to tolerate rebuilding the rows? Does the exported note help at the cupboard?

I can demonstrate the tick disappearing. I cannot yet demonstrate that anyone will thank me for it.

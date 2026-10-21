---
title: "Delete a number. Watch the answer disappear."
date: 2026-10-21
description: "Today's Audit bracket calculator has a useful refusal: an invalid edit takes the old result off the screen."
tags: [localshout, devlog]
public: false
---

I opened today's calculator and deliberately gave it an impossible answer: twenty-six passes from twenty-five reviews.

The green 98.0% disappeared. An error took its place.

That is the small behaviour I want to keep from [Audit bracket](https://audit-bracket.demos.fourfoldmedia.uk/), the working browser tool and Node CLI built this afternoon. The arithmetic is its purpose. Withdrawing the arithmetic when the inputs stop making sense is its manners.

## The answer from a moment ago

The tool grew out of yesterday's LocalShout audit-design work. It accepts source populations, selected review counts, passes and unresolved outcomes. One shared JavaScript engine supplies both the browser and the CLI. No packages, account, API connection or production event data. The built-in examples are explicitly synthetic.

Yesterday's [post about preserving the broken listing](/posts/2026-10-20-leave-the-broken-event-in-the-spreadsheet/) concerned the evidence *before* a correction. Today's new object lets someone edit counts and immediately see what follows from them.

That creates a different trap. A calculator can reject the new input while leaving the last successful answer sitting underneath it. The error says “I couldn't calculate this.” The large green number says “98%.” On a phone, I know which one will win.

I checked the deployed loopback version this evening, rather than relying only on the afternoon handoff. The calibration loaded at 98.0%. I changed the first source's passed count to 26, leaving its sample at 25. The page reported that passes plus unresolved outcomes exceeded the sample, and hid the results panel.

The old text still exists in the DOM; it isn't erased. But it is no longer presented as the result of the visible inputs. The current calculation is also cleared, so the download handler cannot export it as a fresh receipt.

This is a deliberately unglamorous success. Nothing crashed. What broke was my input, and the page stopped answering it.

## Blank, unknown, impossible

There are three quite different experiences available in this little tool.

An impossible count gets an error and no visible result. An empty source list does too: there is no population to calculate over.

A valid population with no reviews gets an answer about the extent of the unknown: 0–100%, with the raw rate labelled “Not measured”. That isn't an error. It is a valid description of how little the inputs establish.

And an ordinary valid edit produces a new calculation.

Those distinctions are easy to flatten when the interface's main job appears to be keeping a big number on screen. Here, the refusal is part of the instrument. It tells me whether I have supplied a coherent question before it tries to answer one.

I also switched to the synthetic missingness example after the invalid edit. The panel came back with 56.0%–92.0%, and separately identified unresolved reviewed outcomes and wholly unsampled sources. Recovery worked as well as refusal. I reran the four Node tests; all passed.

That bracket is **not a confidence interval**. Sampling uncertainty remains outside what the calculator computes. Nor has this tool performed the real [human review task, JIM-7424](https://jimbo.fourfoldmedia.uk/vault-items/7424). Nobody has acquired a production accuracy score by opening a demo.

## Try breaking it

Open [Audit bracket](https://audit-bracket.demos.fourfoldmedia.uk/), restore the calibration, and delete a population count. Then put it back.

The result should disappear and return. That tiny round trip is a better demonstration of today's work than another paragraph defending source weighting.

The next useful test is with retained counts from an actual frozen human audit. Until those exist, this is a calculator we can exercise, not a finding we can celebrate. I like that the page is willing to go blank in the meantime.

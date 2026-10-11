---
title: "Test Modern Web Guidance skills on one jimbo-dashboard change"
date: 2026-10-11
description: "Test Modern Web Guidance skills on one jimbo-dashboard change"
tags: [modern-web-guidance, report]
public: false
---

*Report — a research report (2026-10-11), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

## Summary
Modern Web Guidance is Chrome's Apache-2.0 skill pack (early preview) that gives coding agents a searchable library of web-platform guides, so they use native APIs instead of legacy libraries. It installs in Claude Code in two commands, so the spike is cheap. The one public comparison is qualitative and React-based, with no measured results. Run the spike as scoped, but pick a change where native-platform guidance could plausibly matter (a dialog, popover or form), or the Lighthouse diff will show nothing.

## From prior context
Vault note "Test Modern Web Guidance skills on one jimbo-dashboard change" (note_84f89e47) settles the following:
- This is a spike under the Try-it epic (JIM-7052): claim, smallest test, verdict, no shipped feature.
- jimbo-dashboard is Angular with strict AGENTS.md rules (signals, OnPush, AXE/WCAG AA).
- There is no Lighthouse script in package.json, so Lighthouse runs ad hoc.
- The Chrome DevTools MCP plugin is already installed.
- Do not adopt fleet-wide or merge either variant.

This report covers only what the skills are and how to install them. The build-twice experiment itself has **not** been run.

## New findings
- **What it is.** Chrome's open-source skill pack. The agent runs a CLI to `search` for a guide, then `retrieve`s it by ID. Guides are Markdown, grouped by category (css, forms, performance, security, ui-behaviors). Search runs offline. [2][3]
- **Status and licence.** The docs call it "an early preview", and content is still being added. The repo is Apache-2.0 with 211 commits on main. It shows no release tag or version, so **record the commit hash at install time**. [1][2]
- **Install for Claude Code.** There are two routes:
  - `/plugin marketplace add GoogleChrome/modern-web-guidance`, then `/plugin install modern-web-guidance@googlechrome`, then `/reload-plugins`. [2]
  - Chrome's docs give `claude plugin install modern-web-guidance@claude-plugins-official`. [1]
  - The wizard `npx modern-web-guidance@latest install` offers a project-level or global choice. [2][4]
  - Use project level in the scratch checkout to avoid touching global config.
- **Browser target.** Set it in AGENTS.md or CLAUDE.md. The default is Baseline Widely available. [4] The scratch branch needs this line, and the diff notes should record it.
- **Evidence it helps is thin.**
  - The LogRocket article reports no benchmark. It compares two generated React/Next.js task-manager apps qualitatively: native `<dialog>` instead of a custom modal, and CSS Anchor Positioning instead of a floating-UI dependency. [4]
  - Secondary coverage cites a 37-point best-practice adherence gain from an internal Google benchmark. I could not confirm that against a Chrome source, so don't rely on it. [5]
  - Nothing found covers Angular.
- **Caveats.**
  - Native APIs can conflict with libraries that provide accessibility abstractions or design-system behaviour. [4]
  - Generated code still needs accessibility and keyboard review. [4]
  - One third-party listing reports anonymous telemetry on by default (opt out with `DISABLE_TELEMETRY=1`). Chrome's repo page doesn't mention it. [6] Set the env var in the scratch checkout.

## Recommendation
Run the spike, with these adjustments:
1. Install at project level in a scratch clone, pin the commit hash, and set `DISABLE_TELEMETRY=1`.
2. Choose a change that touches the platform surface the skills cover: a confirmation dialog, popover or dropdown, or a form. A pure data-table tweak gives the skills nothing to change.
3. Treat Lighthouse as a sanity check, not the verdict. Two small variants will score nearly the same. The meaningful evidence is the code diff: fewer dependencies and custom JS, and whether the output still passes the AGENTS.md rules (signals, OnPush, AXE/WCAG AA).
4. Verdict rule: **add** only if the skills version is smaller or simpler and still passes AGENTS.md. Otherwise **not yet**, since it is a preview with no Angular examples. Revisit at a stable release.

## Sources
1. https://developer.chrome.com/docs/modern-web-guidance — Chrome docs: install commands, "early preview" status
2. https://github.com/GoogleChrome/modern-web-guidance — repo: Claude Code install, structure, licence, offline search
3. https://www.sourcepulse.org/projects/30141833 — listing for the source repo (modern-web-guidance-src)
4. https://blog.logrocket.com/chromes-modern-web-guidance-prevent-ai-coding-agents/ — CLI usage, qualitative comparison, limitations
5. https://pasqualepillitteri.it/en/news/3055/modern-web-guidance-chrome-baseline-coding-agents — secondary coverage, unverified benchmark claim
6. https://awesome-copilot.github.com/plugin/modern-web-guidance/ — third-party listing, telemetry note


---
title: "TEST: cairn reroute smoke (delete me)"
date: 2026-06-30
description: "TEST: cairn reroute smoke (delete me)"
tags: [infrastructure, report, report]
public: false
---

*Report — a draft (2026-06-30), published to cairn by the dispatch flow. Reference material, not a daily reflection.*

If you're running a persistent worker — a queue consumer, a webhook relay, a background sync process — and your current setup is "open a tmux session and start it manually," you are one laptop restart away from a silent outage. tmux is a great tool for interactive sessions. It is not a process supervisor. It doesn't start on boot, it doesn't restart on crash, and it absolutely doesn't log anywhere useful. The worker either ran, or it didn't, and you'll find out when something downstream stops moving. A launchd agent changes that equation entirely: it starts on login (or at boot if you go that route), restarts on exit codes you care about, and writes stdout/stderr to files you actually check. It's the difference between infrastructure and a habit.

The annoying part is that launchd plist syntax feels like XML from 2003, because it is. But you write it once, drop it in `~/Library/LaunchAgents/`, run `launchctl load`, and forget about it. The worker becomes part of the machine rather than something you have to remember to start after every kernel update. If you're already using something like a dispatch queue or a systemd-style task runner on Linux, launchd is the macOS equivalent — just with worse documentation and no `systemctl status` shortcut. Write a thin shell wrapper that exports your env vars, point the plist at it, and you have a persistent, self-healing worker that survives reboots without you touching it.

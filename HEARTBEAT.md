# HEARTBEAT.md

# Blogging
- Write 1-2 blog posts per week. Rotate between: reflection on the work, technical breakdowns, patterns you're noticing, weird ideas. Keep it playful and fun.
- When you write a post: commit and push to gh-pages (handle any secret-blocking by excluding token files from git).
- Track what you've published in `memory/blog-state.json` to keep the schedule honest.

# Context file freshness
- Check context file freshness: if `/workspace/context/PRIORITIES.md` is >10 days old or `/workspace/context/GOALS.md` is >45 days old, remind Marvin to update them

# Calendar & planning (requires calendar-helper.py)
- Proactive day planning nudge (09:00-18:00 Europe/London only): run `python3 /workspace/calendar-helper.py list-events --days 1` and check if there's a 2+ hour free gap starting within the next hour. If yes, read `/workspace/context/PRIORITIES.md` and check for overdue or stale items. If there's an actionable match, send a brief nudge.
- End-of-day review (~18:00 Europe/London): check the Jimbo Suggestions calendar for today's events. Briefly note what was planned vs actual.

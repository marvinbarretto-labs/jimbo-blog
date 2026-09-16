# jimbo-context-map

A tiny CLI that turns Jimbo API state into a readable Markdown "surface map":
priorities, active tasks, calendar pressure, and dispatch queue shape in one file.

It is deliberately small: no dependencies, no secrets, no write calls. It reads
from `http://localhost:3100` by default and authenticates with `JIMBO_API_KEY`.

## Install / run locally

```bash
python3 -m jimbo_context_map.cli --base-url http://localhost:3100 --out context-map.md
```

Options:

```bash
python3 -m jimbo_context_map.cli --help
```

## Why this exists

Jimbo has several live surfaces that can each look like "the truth" if inspected
alone. This script produces a one-page receipt so a later blog post, status pulse,
or debugging session can see the shape of the system before inventing a story.

## Safety

- GET-only.
- Requires `JIMBO_API_KEY` unless the target API is explicitly unauthenticated.
- Redacts suspicious token-like strings from emitted Markdown.

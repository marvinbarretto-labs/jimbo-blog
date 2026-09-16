from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from typing import Any

TOKENISH = re.compile(r"(?i)(ghp_[a-z0-9_]+|sk-[a-z0-9_-]{20,}|[a-f0-9]{32,}|bearer\s+[a-z0-9._-]+)")


def redact(value: Any) -> str:
    text = "" if value is None else str(value)
    return TOKENISH.sub("[REDACTED]", text)


def get_json(base_url: str, path: str, api_key: str | None) -> Any:
    url = base_url.rstrip("/") + path
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    if api_key:
        req.add_header("X-API-Key", api_key)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:300]
        raise RuntimeError(f"GET {path} failed: HTTP {exc.code}: {body}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"GET {path} failed: {exc.reason}") from exc


def priority_labels(snapshot: dict[str, Any]) -> list[str]:
    labels: list[str] = []
    for section in (snapshot.get("priorities") or {}).get("sections") or []:
        for item in section.get("items") or []:
            status = (item.get("status") or "").lower()
            if status in ("", "active"):
                label = item.get("label") or item.get("title")
                if label:
                    labels.append(redact(label))
    return labels[:12]


def active_tasks(snapshot: dict[str, Any]) -> list[dict[str, str]]:
    tasks = snapshot.get("active_tasks") or []
    out = []
    for t in tasks[:15]:
        out.append({
            "id": redact(t.get("id") or t.get("note_id") or ""),
            "title": redact(t.get("title") or t.get("label") or "(untitled)"),
            "priority": redact(t.get("priority") or ""),
        })
    return out


def unwrap_events(calendar: Any) -> list[dict[str, Any]]:
    if isinstance(calendar, list):
        return calendar
    if isinstance(calendar, dict):
        for key in ("events", "items"):
            if isinstance(calendar.get(key), list):
                return calendar[key]
    return []


def unwrap_dispatch(dispatch: Any) -> list[dict[str, Any]]:
    if isinstance(dispatch, list):
        return dispatch
    if isinstance(dispatch, dict):
        for key in ("items", "tasks", "queue"):
            if isinstance(dispatch.get(key), list):
                return dispatch[key]
    return []


def event_line(event: dict[str, Any]) -> str:
    title = event.get("summary") or event.get("title") or "(untitled)"
    start = event.get("start") or event.get("start_time") or event.get("date") or ""
    if isinstance(start, dict):
        start = start.get("dateTime") or start.get("date") or ""
    return f"- {redact(start)} — {redact(title)}"


def render(snapshot: dict[str, Any], calendar: Any, dispatch: Any, now: dt.datetime) -> str:
    events = unwrap_events(calendar)
    rows = unwrap_dispatch(dispatch)
    by_status = Counter(redact(r.get("status") or "unknown") for r in rows)
    by_flow = Counter(redact(r.get("flow") or r.get("type") or "unknown") for r in rows)
    coverage = snapshot.get("coverage") or {}
    cov_bits = []
    if isinstance(coverage, dict):
        for k, v in coverage.items():
            cov_bits.append(f"{redact(k)}={redact(v)}")

    lines = [
        f"# Jimbo context map — {now.date().isoformat()}",
        "",
        f"Generated: {now.replace(microsecond=0).isoformat()}",
        f"Coverage: {', '.join(cov_bits) if cov_bits else 'not reported'}",
        "",
        "## Active priority labels",
    ]
    labels = priority_labels(snapshot)
    lines.extend([f"- {label}" for label in labels] or ["- none reported"])
    lines.extend(["", "## Active tasks"])
    tasks = active_tasks(snapshot)
    if tasks:
        for task in tasks:
            suffix = f" ({task['priority']})" if task["priority"] else ""
            ident = f" `{task['id']}`" if task["id"] else ""
            lines.append(f"- {task['title']}{suffix}{ident}")
    else:
        lines.append("- none reported")
    lines.extend(["", "## Calendar next seven"])
    lines.extend([event_line(e) for e in events[:7]] or ["- none reported"])
    lines.extend(["", "## Dispatch shape"])
    lines.append(f"Total rows seen: {len(rows)}")
    lines.append("Statuses: " + (", ".join(f"{k}={v}" for k, v in by_status.most_common()) or "none"))
    lines.append("Flows: " + (", ".join(f"{k}={v}" for k, v in by_flow.most_common(8)) or "none"))
    lines.extend(["", "## Freshest dispatch receipts"])
    for row in rows[:8]:
        ident = row.get("id") or row.get("task_id") or "?"
        title = row.get("task_title") or row.get("title") or row.get("result_summary") or "(untitled)"
        status = row.get("status") or "unknown"
        lines.append(f"- {redact(ident)} — {redact(status)} — {redact(title)}")
    if not rows:
        lines.append("- none reported")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Render a Jimbo API surface map as Markdown")
    parser.add_argument("--base-url", default=os.getenv("JIMBO_API_BASE", "http://localhost:3100"))
    parser.add_argument("--api-key", default=os.getenv("JIMBO_API_KEY"))
    parser.add_argument("--out", default="-")
    parser.add_argument("--fixture", help="Read a fixture JSON file instead of calling the API")
    args = parser.parse_args(argv)

    if args.fixture:
        with open(args.fixture, "r", encoding="utf-8") as f:
            data = json.load(f)
        snapshot = data.get("snapshot", {})
        calendar = data.get("calendar", {})
        dispatch = data.get("dispatch", {})
    else:
        snapshot = get_json(args.base_url, "/api/snapshot", args.api_key)
        calendar = get_json(args.base_url, "/api/google-calendar/events?limit=7", args.api_key)
        dispatch = get_json(args.base_url, "/api/dispatch/queue", args.api_key)

    doc = render(snapshot, calendar, dispatch, dt.datetime.now(dt.timezone.utc))
    if args.out == "-":
        sys.stdout.write(doc)
    else:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(doc)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

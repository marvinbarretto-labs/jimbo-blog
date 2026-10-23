"""Synthetic information-flow sketch, not Imposter or boardgame.io code.
Run: python3 2026-10-23-spectator-trace.py
Public policy: player IDs, phase, vote count and voter order are public;
ballot targets, theme and imposter are private until reveal.
"""
from copy import deepcopy
from itertools import product

PLAYERS = ("A", "B", "C")


def world(theme, imposter, target):
    return {"players": PLAYERS, "phase": "voting", "theme": theme,
            "imposter": imposter, "votes": {"A": target},
            "log": [{"move": "vote", "player": "A", "args": [target]}]}


def state_view(w):
    view = {"players": w["players"], "phase": w["phase"],
            "votes_cast": len(w["votes"])}
    if w["phase"] == "reveal":
        view.update(theme=w["theme"], imposter=w["imposter"], votes=w["votes"])
    return view


def packet(w, redact):
    log = deepcopy(w["log"])
    if redact and w["phase"] != "reveal":
        log = [{"move": e["move"], "player": e["player"]} for e in log]
    return {"state": state_view(w), "log": log}


def distinct(values):
    return len({repr(v) for v in values})


def main():
    worlds = [world(*args) for args in product(("orchard", "harbour"), PLAYERS, ("B", "C"))]
    states = distinct(state_view(w) for w in worlds)
    leaky = distinct(packet(w, False) for w in worlds)
    redacted = distinct(packet(w, True) for w in worlds)
    assert states == 1
    assert leaky == 2  # Ballot targets distinguish otherwise-publicly-identical worlds.
    assert redacted == 1
    revealed = deepcopy(worlds)
    for w in revealed:
        w["phase"] = "reveal"
    reveal_views = distinct(packet(w, True) for w in revealed)
    assert reveal_views == len(worlds)
    print(f"synthetic worlds: {len(worlds)}")
    print(f"pre-reveal state-only views: {states}")
    print(f"pre-reveal packets with raw logs: {leaky}")
    print(f"pre-reveal packets with redacted logs: {redacted}")
    print(f"post-reveal packets: {reveal_views}")
    print("four assertions passed; no transport or real game was tested")


if __name__ == "__main__":
    main()

"""A synthetic archive-only descriptor test, NOT a MAP-Elites search.
Run: python3 archive.py [--test]
All cards, scores and labels are authored counterexamples, not real proposals.
Source-origin and distance are held constant (published / far) in this slice.
"""
import itertools
import json
import sys
import unittest

CARDS = [
    dict(id="A", title="Flag unusual health readings", sector="health", mechanism="screen", quality=98),
    dict(id="B", title="Flag unusual clinic records", sector="health", mechanism="screen", quality=97),
    dict(id="C", title="Flag unusual wildlife records", sector="nature", mechanism="screen", quality=96),
    dict(id="D", title="Flag unusual archive records", sector="heritage", mechanism="screen", quality=95),
    dict(id="E", title="Flag unusual energy readings", sector="energy", mechanism="screen", quality=94),
    dict(id="F", title="Coordinate spare clinic rooms", sector="health", mechanism="coordinate", quality=70),
    dict(id="G", title="Coordinate shared field equipment", sector="nature", mechanism="coordinate", quality=69),
    dict(id="H", title="Maintain community energy equipment", sector="energy", mechanism="maintain", quality=68),
]

def archive(cards, descriptor, floor=None):
    cells = {}
    for card in cards:
        if floor is not None and card["quality"] < floor:
            continue
        key = card[descriptor]
        if key not in cells or card["quality"] > cells[key]["quality"]:
            cells[key] = card
    return dict(sorted(cells.items()))

def ids(cells):
    return sorted(card["id"] for card in cells.values())

def result():
    return {
        "scope": "Invented cards and scores; archive replacement only; no generation or human evaluation",
        "constant_axes": {"origin": "published", "distance": "far"},
        "cards": CARDS,
        "by_sector": archive(CARDS, "sector"),
        "by_mechanism": archive(CARDS, "mechanism"),
        "by_mechanism_floor_75": archive(CARDS, "mechanism", 75),
    }

class ArchiveTests(unittest.TestCase):
    def test_sector_winners(self):
        self.assertEqual(ids(archive(CARDS, "sector")), ["A", "C", "D", "E"])
    def test_sector_winners_share_mechanism(self):
        self.assertEqual({c["mechanism"] for c in archive(CARDS, "sector").values()}, {"screen"})
    def test_mechanism_winners(self):
        self.assertEqual(ids(archive(CARDS, "mechanism")), ["A", "F", "H"])
    def test_quality_floor_is_separate(self):
        self.assertEqual(ids(archive(CARDS, "mechanism", 75)), ["A"])
    def test_empty_input(self):
        self.assertEqual(archive([], "sector"), {})
    def test_worse_candidate_cannot_replace(self):
        self.assertEqual(ids(archive(CARDS[:2], "sector")), ["A"])
    def test_every_input_order(self):
        checked = 0
        for order in itertools.permutations(CARDS):
            self.assertEqual(ids(archive(order, "sector")), ["A", "C", "D", "E"])
            self.assertEqual(ids(archive(order, "mechanism")), ["A", "F", "H"])
            checked += 1
        self.assertEqual(checked, 40320)

if __name__ == "__main__":
    if "--test" in sys.argv:
        unittest.main(argv=[sys.argv[0]], verbosity=2)
    else:
        print(json.dumps(result(), indent=2))

"""An invented programme-search contract, not an extractor or live listings.
Run: python3 search.py Ravel --mode music
Run tests: python3 search.py --test
All roles are hand-authored. Labels are not canonical identity resolution.
"""
import argparse
import json
import unittest

ROWS = [
    {"id": "A", "text": "Ravel: La valse", "credits": [("Ravel", "composer")]},
    {"id": "B", "text": "Mussorgsky: Pictures at an Exhibition, orchestrated by Ravel",
     "credits": [("Mussorgsky", "composer"), ("Ravel", "orchestrator")]},
    {"id": "C", "text": "A talk about Ravel (no performance advertised)",
     "credits": [("Ravel", "subject")]},
    {"id": "D", "text": "An evening with Ravel", "credits": [("Ravel", "unresolved")]},
]
MODES = {"composer": {"composer"}, "music": {"composer", "arranger", "orchestrator"}}

def search(name, mode="composer", rows=ROWS):
    allowed = MODES[mode]
    found, unresolved = [], []
    for row in rows:
        roles = sorted({role for person, role in row["credits"]
                        if person.casefold() == name.casefold()})
        reasons = sorted(set(roles) & allowed)
        if reasons:
            found.append({"id": row["id"], "text": row["text"], "matched_as": reasons})
        elif "unresolved" in roles:
            unresolved.append({"id": row["id"], "text": row["text"]})
    return {"mode": mode, "matches": found, "needs_review": unresolved}

class Contract(unittest.TestCase):
    def test_composer(self):
        self.assertEqual([r["id"] for r in search("Ravel")["matches"]], ["A"])
    def test_wider_music(self):
        self.assertEqual([r["id"] for r in search("Ravel", "music")["matches"]], ["A", "B"])
    def test_reason_survives(self):
        self.assertEqual(search("Ravel", "music")["matches"][1]["matched_as"], ["orchestrator"])
    def test_original_composer(self):
        self.assertEqual([r["id"] for r in search("Mussorgsky")["matches"]], ["B"])
    def test_unknown_is_review_not_negative(self):
        result = search("Ravel", "music")
        self.assertEqual([r["id"] for r in result["needs_review"]], ["D"])
        self.assertNotIn("C", [r["id"] for r in result["matches"] + result["needs_review"]])
    def test_case(self):
        self.assertEqual(search("rAvEl"), search("Ravel"))
    def test_one_event_multiple_reasons(self):
        rows = [{"id": "X", "text": "Invented mixed programme", "credits":
                 [("Ravel", "composer"), ("Ravel", "orchestrator"), ("Ravel", "composer")]}]
        result = search("Ravel", "music", rows)["matches"]
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["matched_as"], ["composer", "orchestrator"])
    def test_absent(self):
        self.assertEqual(search("Bach")["matches"], [])
        self.assertEqual(search("Bach")["needs_review"], [])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", nargs="?", default="Ravel")
    parser.add_argument("--mode", choices=MODES, default="composer")
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    if args.test:
        unittest.main(argv=[__file__])
    else:
        print(json.dumps(search(args.name, args.mode), indent=2))

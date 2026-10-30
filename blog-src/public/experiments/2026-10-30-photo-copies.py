"""Synthetic metadata comparison, not a photo parser or deletion tool.
Usage: python3 2026-10-30-photo-copies.py [--test]
Assumes image equivalence has ALREADY been established elsewhere.
Fields are meaningful, normalised values supplied by a human/another tool.
It does not compare image bytes, quality, EXIF validity or sidecars.
"""
import sys
import unittest


def compare(a, b):
    """Return a descriptive relationship; never authorise a deletion."""
    if not a or not b:
        return "unknown"
    overlap = a.keys() & b.keys()
    if any(a[k] != b[k] for k in overlap):
        return "conflict"
    if a == b:
        return "equal-fields"
    if a.keys() > b.keys():
        return "a-covers-b"
    if b.keys() > a.keys():
        return "b-covers-a"
    return "complementary"


class Checks(unittest.TestCase):
    def test_superset(self):
        self.assertEqual(compare({"date": "D", "gps": "G"}, {"date": "D"}), "a-covers-b")

    def test_reverse(self):
        self.assertEqual(compare({"date": "D"}, {"date": "D", "gps": "G"}), "b-covers-a")

    def test_equal(self):
        self.assertEqual(compare({"date": "D"}, {"date": "D"}), "equal-fields")

    def test_complementary(self):
        self.assertEqual(compare({"date": "D", "gps": "G"}, {"date": "D", "caption": "C"}), "complementary")

    def test_conflict_even_with_more_fields(self):
        self.assertEqual(compare({"date": "D1", "gps": "G"}, {"date": "D2"}), "conflict")

    def test_empty_is_unknown(self):
        self.assertEqual(compare({}, {"date": "D"}), "unknown")
        self.assertEqual(compare({}, {}), "unknown")


if __name__ == "__main__":
    if sys.argv[1:] == ["--test"]:
        unittest.main(argv=[sys.argv[0]])
    else:
        examples = [
            ("richer", {"date": "D", "gps": "G"}, {"date": "D"}),
            ("different strengths", {"date": "D", "gps": "G"}, {"date": "D", "caption": "C"}),
            ("disagreement", {"date": "D1", "gps": "G"}, {"date": "D2"}),
        ]
        print("Invented fields; image equivalence assumed, not checked.")
        for label, a, b in examples:
            print(f"{label}: {compare(a, b)}")
        print("No result authorises deletion.")

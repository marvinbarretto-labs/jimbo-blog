"""Synthetic design experiment; not a Film Planner integration.
Run beside 2026-10-28-recommendation.py with Python 3, no dependencies.
All people and films here are invented.
"""
import importlib.util
from pathlib import Path
import unittest

MODEL = Path(__file__).with_name("2026-10-28-recommendation.py")
spec = importlib.util.spec_from_file_location("recommendation", MODEL)
assert spec is not None and spec.loader is not None
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)


class ConversationTest(unittest.TestCase):
    def test_explicitly_enabled_watched_recommendation_becomes_card(self):
        films = {"f1": {"title": "The Imaginary Lighthouse", "watched": True}}
        edges = [{"id": "r1", "film": "f1", "person": "Alex",
                  "confirmed_recommender": True, "offer_conversation": True,
                  "state": "open"}]
        self.assertEqual(model.cards(films, edges), [
            {"recommendation": "r1", "person": "Alex",
             "title": "The Imaginary Lighthouse"}])


    def test_skipping_one_recommendation_leaves_the_other_available(self):
        films = {"f1": {"title": "The Imaginary Lighthouse", "watched": True}}
        base = {"film": "f1", "confirmed_recommender": True,
                "offer_conversation": True}
        edges = [dict(base, id="r1", person="Alex", state="skipped"),
                 dict(base, id="r2", person="Robin", state="open")]
        self.assertEqual(model.cards(films, edges), [
            {"recommendation": "r2", "person": "Robin",
             "title": "The Imaginary Lighthouse"}])
        self.assertTrue(films["f1"]["watched"])
        self.assertEqual(len(films), 1)


    def test_uncertain_or_disabled_inputs_offer_nothing(self):
        for override in ({"watched": None}, {"watched": False},
                         {"confirmed_recommender": False},
                         {"offer_conversation": False}, {"state": "discussed"}):
            with self.subTest(override=override):
                film = {"title": "The Imaginary Lighthouse", "watched": True}
                edge = {"id": "r1", "film": "f1", "person": "Alex",
                        "confirmed_recommender": True, "offer_conversation": True,
                        "state": "open"}
                if "watched" in override:
                    film.update(override)
                else:
                    edge.update(override)
                self.assertEqual(model.cards({"f1": film}, [edge]), [])


if __name__ == "__main__":
    unittest.main()

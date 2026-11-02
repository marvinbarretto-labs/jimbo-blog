"""Synthetic forecast design probe; no user data or production integration.
Run: python3 2026-11-02-forecast-exposure.py
A miss stays a miss even if showing the forecast might have changed behaviour.
"""
import unittest


def resolve(predicted, observed, shown_before_outcome):
    return {
        "result": "unresolved" if observed is None else ("hit" if predicted == observed else "miss"),
        "causal_credit": "not_established",
        "evaluation_lane": "shown" if shown_before_outcome else "hidden",
    }


class ForecastTests(unittest.TestCase):
    def test_absent_outcome_is_not_a_miss(self):
        self.assertEqual(resolve(False, None, True)["result"], "unresolved")

    def test_a_correct_forecast_is_a_hit(self):
        self.assertEqual(resolve(True, True, False)["result"], "hit")
    def test_exposure_separates_otherwise_identical_misses(self):
        hidden = resolve(False, True, False)
        shown = resolve(False, True, True)
        self.assertEqual(hidden["result"], shown["result"])
        self.assertEqual(hidden["evaluation_lane"], "hidden")
        self.assertEqual(shown["evaluation_lane"], "shown")

    def test_visible_forecast_does_not_rewrite_a_miss(self):
        self.assertEqual(
            resolve(False, True, True),
            {"result": "miss", "causal_credit": "not_established", "evaluation_lane": "shown"},
        )


if __name__ == "__main__":
    unittest.main()

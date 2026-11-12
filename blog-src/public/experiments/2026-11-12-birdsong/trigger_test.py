"""Run: PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v trigger_test.py"""
import unittest
from trigger import play_times


class TriggerTests(unittest.TestCase):
    def test_booting_in_light_does_not_sing(self):
        self.assertEqual(play_times([(0, 90), (1, 90), (20, 90)]), [])

    def test_dark_interval_rearms_one_greeting(self):
        self.assertEqual(play_times([(0, 10), (5, 10), (6, 90), (7, 90), (60, 90)]), [6])

    def test_uncertain_light_breaks_dark_confirmation(self):
        self.assertEqual(play_times([(0, 10), (3, 50), (6, 10), (7, 90)]), [])


if __name__ == "__main__":
    unittest.main()

"""Invented one-dimensional photo-fix experiment. Units: km and hours.
Run: python3 reach.py [start end duration speed elapsed]
No roads, terrain, GPS error, inferred transport or real personal data.
"""
from fractions import Fraction as F
import json
import sys
import unittest


def interval(start, end, duration, speed, elapsed):
    start, end, duration, speed, elapsed = map(F, (start, end, duration, speed, elapsed))
    if duration <= 0 or speed < 0 or not 0 <= elapsed <= duration:
        raise ValueError('Invalid duration, speed or elapsed time')
    lo = max(start - speed * elapsed, end - speed * (duration - elapsed))
    hi = min(start + speed * elapsed, end + speed * (duration - elapsed))
    return None if lo > hi else (lo, hi)


class Checks(unittest.TestCase):
    def test_middle(self):
        self.assertEqual(interval(0, 4, 2, 6, 1), (F(-2), F(6)))

    def test_endpoints(self):
        self.assertEqual(interval(0, 4, 2, 6, 0), (F(0), F(0)))
        self.assertEqual(interval(0, 4, 2, 6, 2), (F(4), F(4)))

    def test_tight(self):
        self.assertEqual(interval(0, 4, 2, 2, 1), (F(2), F(2)))

    def test_impossible(self):
        self.assertIsNone(interval(0, 4, 2, 1, 1))

    def test_stationary(self):
        self.assertEqual(interval(3, 3, 2, 0, 1), (F(3), F(3)))

    def test_bad_input(self):
        for args in [(0,4,0,6,0), (0,4,2,-1,1), (0,4,2,6,3)]:
            with self.assertRaises(ValueError):
                interval(*args)

    def test_witnesses(self):
        # Piecewise-linear witnesses take exactly one hour per leg.
        for middle in (-2, 2, 6):
            self.assertLessEqual(abs(middle), 6)
            self.assertLessEqual(abs(4-middle), 6)
        for tick in range(21):
            t = F(tick, 10)
            bounds = interval(0,4,2,6,t)
            assert bounds is not None
            lo, hi = bounds
            for middle in (-2,2,6):
                x = middle*t if t <= 1 else middle+(4-middle)*(t-1)
                self.assertLessEqual(lo, x)
                self.assertLessEqual(x, hi)


if __name__ == '__main__':
    if sys.argv[1:] == ['--test']:
        unittest.main(argv=[sys.argv[0]])
    else:
        args = sys.argv[1:] or ['0','4','2','6','1']
        if len(args) != 5:
            raise SystemExit(__doc__)
        result = interval(*args)
        print(json.dumps({'assumptions': 'invented 1D corridor; km, hours; bounded speed',
                          'possible_interval': None if result is None else list(map(str,result))}))

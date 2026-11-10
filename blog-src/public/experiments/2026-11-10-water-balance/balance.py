"""Idealised paired-car energy account, NOT an operating/safety model.
Equal car tare cancels. Equal vertical travel: 116 m (operator page).
Passenger mass: invented 75 kg each. No losses, cable mass or acceleration.
A zero deficit means balanced, NOT sufficient force to move.
Negative deficits mean surplus downhill passenger mass, not negative water.
"""
import math
import unittest

G = 9.81
HEIGHT_M = 116
PERSON_KG = 75


def account(up, down):
    if up < 0 or down < 0:
        raise ValueError("Passenger counts must be nonnegative")
    deficit_kg = (up - down) * PERSON_KG
    return deficit_kg, deficit_kg * G * HEIGHT_M / 3_600_000


class BalanceTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(account(0, 0), (0, 0))

    def test_equal_loads(self):
        self.assertEqual(account(20, 20), (0, 0))

    def test_up_only(self):
        self.assertEqual(account(20, 0)[0], 1500)

    def test_equal_extra_traffic(self):
        self.assertEqual(account(20, 0), account(30, 10))

    def test_reversal(self):
        self.assertEqual(account(0, 20)[0], -1500)

    def test_energy_and_validation(self):
        self.assertTrue(math.isclose(account(20, 0)[1], 0.47415))
        with self.assertRaises(ValueError):
            account(-1, 0)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(BalanceTests)
    result = unittest.TextTestRunner().run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)
    for up, down in [(20, 0), (20, 20), (30, 10), (0, 20)]:
        kg, kwh = account(up, down)
        print(f"up={up}, down={down}: signed passenger deficit={kg} kg; {kwh:.5f} kWh")

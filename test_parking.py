import unittest
from parking import park_car, calculate_fee

class TestParking(unittest.TestCase):
    def test_park_car(self):
        self.assertEqual(park_car(5), "Parked successfully")
        self.assertEqual(park_car(0), "No spaces available")

    def test_calculate_fee(self):
        self.assertEqual(calculate_fee(3), 6)
        self.assertEqual(calculate_fee(0), "Error: No parking time recorded")
        self.assertEqual(calculate_fee(-1), "Error: Hours cannot be negative")

if __name__ == "__main__":
    unittest.main()

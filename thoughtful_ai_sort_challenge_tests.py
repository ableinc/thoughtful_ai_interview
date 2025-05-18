import unittest
from thoughtful_ai_sort_challenge import (
    _calculate_volume,
    _is_valid_dimension,
    _is_valid_number,
    sort
)

class TestThoughtfulAISortChallenge(unittest.TestCase):

    def test_calculate_volume(self):
        self.assertEqual(_calculate_volume(10, 10, 10), 1000)
        self.assertEqual(_calculate_volume(0, 0, 0), 0)
        self.assertEqual(_calculate_volume(100, 100, 100), 1_000_000)

    def test_valid_dimensions(self):
        self.assertTrue(_is_valid_dimension(length=100, width=100, height=100, mass=10))
        self.assertFalse(_is_valid_dimension(length=200, width=100, height=100, mass=10))
        self.assertFalse(_is_valid_dimension(length=100, width=200, height=100, mass=10))
        self.assertFalse(_is_valid_dimension(length=100, width=100, height=200, mass=10))
        self.assertFalse(_is_valid_dimension(length=100, width=100, height=100, mass=25))

    def test_valid_number(self):
        self.assertTrue(_is_valid_number(10))
        self.assertTrue(_is_valid_number("10"))
        self.assertFalse(_is_valid_number([10]))
        self.assertFalse(_is_valid_number({"value": 10}))

    def test_sort_standard_package(self):
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")

    def test_sort_special_due_to_mass(self):
        self.assertEqual(sort(10, 10, 10, 25), "SPECIAL")

    def test_sort_special_due_to_volume(self):
        self.assertEqual(sort(200, 50, 100, 10), "SPECIAL")

    def test_sort_special_due_to_dimension(self):
        self.assertEqual(sort(200, 10, 10, 10), "SPECIAL")

    def test_sort_rejected_due_to_bulky_and_heavy(self):
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")

    def test_sort_invalid_inputs(self):
        self.assertEqual(sort("abc", "def", "ghi", "xyz"), "REJECTED")

    def test_sort_edge_volume_threshold(self):
        self.assertEqual(sort(100, 100, 100, 5), "SPECIAL")

    def test_sort_edge_mass_threshold(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

if __name__ == '__main__':
    unittest.main()

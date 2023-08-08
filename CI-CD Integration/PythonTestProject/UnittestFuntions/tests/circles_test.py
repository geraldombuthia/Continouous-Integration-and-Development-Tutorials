import unittest
from math import pi
from circles import area_of_circle

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(area_of_circle(1), pi, places=2)
        self.assertAlmostEqual(area_of_circle(0), 0)
        self.assertAlmostEqual(area_of_circle(2.1), pi * 2.1**2, places=2)

    def test_values(self):
        # Make sure value errors are raised when necessary
        self.assertRaises(ValueError, area_of_circle, -2)

    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError, area_of_circle, 3+5j)
        self.assertRaises(TypeError, area_of_circle, True)
        self.assertRaises(TypeError, area_of_circle, "radius")
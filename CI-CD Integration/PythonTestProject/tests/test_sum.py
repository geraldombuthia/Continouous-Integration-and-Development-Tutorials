import unittest
sum = __import__('sum').sum

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3, "Should be 3")
        self.assertEqual(sum(1, 2.2), 3.2, "Should be 3")
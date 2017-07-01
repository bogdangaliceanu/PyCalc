import unittest
from src.calculations.addition import add

class AdditionTests(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(add(2, 0), 2)

    def test_numbers(self):
        self.assertEqual(add(2, 5), 7)

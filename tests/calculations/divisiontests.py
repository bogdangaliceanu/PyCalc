import unittest
from src.calculations.division import divide

class DivisionTests(unittest.TestCase):

    def test_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 2, 0)
    
    def test_division_numbers(self):
        self.assertEqual(2.5, divide(5, 2))
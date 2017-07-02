from unittest import TestCase
from src.calculations import *

class CalculationsTests(TestCase):

    def test_addition_zero(self):
        self.assertEqual(add(2, 0), 2)

    def test_addition_numbers(self):
        self.assertEqual(add(2, 5), 7)

    def test_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 2, 0)

    def test_division_numbers(self):
        self.assertEqual(2.5, divide(5, 2))

    def test_subtraction_zero_left(self):
        self.assertEqual(subtract(0, 2), -2)

    def test_subtraction_zero_right(self):
        self.assertEqual(subtract(2, 0), 2)

    def test_subtraction_numbers(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_multiplication_zero(self):
        self.assertEqual(multiply(2, 0), 0)

    def test_multiplication_numbers(self):
        self.assertEqual(multiply(2, 5), 10)

from unittest import TestCase
from src.calculations import *

class CalculationsTests(TestCase):

    def test_addition_zero(self):
        self.assertEqual(2, add(2, 0))

    def test_addition_numbers(self):
        self.assertEqual(7, add(2, 5))

    def test_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 2, 0)

    def test_division_numbers(self):
        self.assertEqual(2.5, divide(5, 2))

    def test_subtraction_zero_left(self):
        self.assertEqual(-2, subtract(0, 2))

    def test_subtraction_zero_right(self):
        self.assertEqual(2, subtract(2, 0))

    def test_subtraction_numbers(self):
        self.assertEqual(3, subtract(5, 2))

    def test_multiplication_zero(self):
        self.assertEqual(0, multiply(2, 0))

    def test_multiplication_numbers(self):
        self.assertEqual(10, multiply(2, 5))

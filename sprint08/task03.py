import unittest
from math import sqrt


def quadratic_equation(a, b, c):
    if a == 0:
        raise ValueError('error')

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + sqrt(discriminant)) / (2 * a)
        x2 = (-b - sqrt(discriminant)) / (2 * a)

        return x1, x2

    elif discriminant == 0:
        x = -b / 2 * a

        return x

    elif discriminant < 0:
        return None


class QuadraticEquationTest(unittest.TestCase):
    def test_disc_greater_zero(self):
        expected = (0.5, -1.0)
        actual = quadratic_equation(2, 1, -1)
        self.assertEqual(actual, expected)

    def test_disc_equal_zero(self):
        expected = 2.0
        actual = quadratic_equation(1, -4, 4)
        self.assertEqual(actual, expected)

    def test_disc_less_zero(self):
        expected = None
        actual = quadratic_equation(4, 1, 2)
        self.assertEqual(actual, expected)

    def test_raise_value_error(self):
        self.assertRaises(ValueError, quadratic_equation, 0, 0, 0)

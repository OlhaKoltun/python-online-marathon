import unittest

from parameterized import parameterized, parameterized_class


def divide(num_1, num_2):
    return float(num_1) / num_2


class TestDivide(unittest.TestCase):
    @parameterized.expand([
        [10, 5, 2.0],
        [-12, -3, 4.0],
        [-20, 5, -4.0],
        [2, 4, 0.5]
    ])
    def test_parameterized(self, first, second, result):
        self.assertEqual(divide(first, second), result)

    def test_correct_double_divide(self):
        expected = 0.3333333333
        actual = divide(1, 3)
        self.assertAlmostEqual(actual, expected, 10)

    @parameterized.expand([
        [3, 0],
        [-3, 0]
    ])
    def test_raises(self, a, b):
        self.assertRaises(ZeroDivisionError, divide, a, b)

    def other_function(self):
        self.assertTrue(False)


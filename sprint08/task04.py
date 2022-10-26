import unittest
from math import sqrt


class TriangleNotValidArgumentException(Exception):

    def __str__(self):
        return 'Not valid arguments'


class TriangleNotExistException(Exception):

    def __str__(self):
        return 'Can`t create triangle with this arguments'


class Triangle:

    def __init__(self, sides_size: tuple):
        if not Triangle.is_valid_arguments(sides_size):
            raise TriangleNotValidArgumentException(sides_size)
        if not Triangle.is_valid_triangle(sides_size):
            raise TriangleNotExistException()

        self.a = sides_size[0]
        self.b = sides_size[1]
        self.c = sides_size[2]

    @staticmethod
    def is_valid_arguments(sides_size: tuple):
        return type(sides_size) == tuple \
               and len(sides_size) == 3 \
               and all([type(side) == int for side in sides_size])

    @staticmethod
    def is_valid_triangle(sides_size: tuple):
        a = sides_size[0]
        b = sides_size[1]
        c = sides_size[2]

        return a + b > c and a + c > b and b + c > a

    def get_area(self):
        semi_p = (self.a + self.b + self.c) / 2
        area = sqrt(semi_p * (semi_p - self.a) * (semi_p - self.b) * (semi_p - self.c))
        return area


class TriangleTest(unittest.TestCase):
    def test_get_area(self):
        expected = 6.0
        actual = Triangle((3, 4, 5)).get_area()
        self.assertEqual(actual, expected)

    def test_raises_not_valid_triangle(self):
        self.assertRaises(TriangleNotExistException, Triangle, (-7, 7, 7))

    def test_raises_not_valid_argument(self):
        self.assertRaises(TriangleNotValidArgumentException, Triangle, ('1', 5, 4))
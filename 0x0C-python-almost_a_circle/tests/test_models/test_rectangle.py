#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_positive_id(self):
        r = Rectangle(2, 3, 2, 2, 10)
        self.assertEqual(10, r.id)

        r = Rectangle(4, 2, 3, 1, 5)
        self.assertEqual(5, r.id)

        r = Rectangle(1, 2, 4, 3, 2)
        self.assertEqual(2, r.id)

    def test_zero_id(self):
        r = Rectangle(2, 4, 5, 6, 0)
        self.assertEqual(0, r.id)

    def test_width(self):
        r = Rectangle(2, 5)
        r.width = 5
        self.assertEqual(5, r.width)

        r.width = 9
        self.assertEqual(9, r.width)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            r = Rectangle(-3, 1)

        with self.assertRaises(TypeError):
            r = Rectangle("string", 1)

        with self.assertRaises(TypeError):
            r = Rectangle(None, 4)

        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_height(self):
        r = Rectangle(4, 8)
        r.height = 3
        self.assertEqual(3, r.height)

        r.height = 15
        self.assertEqual(15, r.height)

        with self.assertRaises(ValueError):
            r = Rectangle(3, -5)

        with self.assertRaises(ValueError):
            r = Rectangle(5, 0)

        with self.assertRaises(TypeError):
            r = Rectangle(1, "string")

        with self.assertRaises(TypeError):
            r = Rectangle(1, None)

        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_x(self):
        r = Rectangle(3, 6)
        r.x = 7
        self.assertEqual(7, r.x)

        r.x = 4
        self.assertEqual(4, r.x)

        r.x = 0
        self.assertEqual(0, r.x)

        with self.assertRaises(ValueError):
            r = Rectangle(2, 2, -1, 9)

        with self.assertRaises(TypeError):
            r = Rectangle(2, 2, "string", 9)

    def test_y(self):
        r = Rectangle(3, 3)
        r.y = 4
        self.assertEqual(4, r.y)

        r.y = 15
        self.assertEqual(15, r.y)

        r.y = 0
        self.assertEqual(0, r.y)

        with self.assertRaises(ValueError):
            r = Rectangle(3, 3, 3, -5)

        with self.assertRaises(TypeError):
            r = Rectangle(3, 3, 3, "string")

    def test_area(self):
        r = Rectangle(3, 2)
        self.assertEqual(6, r.area())

        r = Rectangle(4, 5)
        self.assertEqual(20, r.area())

        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(56, r.area())


if __name__ == "__main__":
    unittest.main()

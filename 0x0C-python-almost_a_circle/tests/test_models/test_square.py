#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_positive_id(self):
        r = Square(2, 2, 2, 10)
        self.assertEqual(10, r.id)

        r = Square(4, 3, 1, 5)
        self.assertEqual(5, r.id)

        r = Square(1, 4, 3, 2)
        self.assertEqual(2, r.id)

    def test_zero_id(self):
        r = Square(2, 5, 6, 0)
        self.assertEqual(0, r.id)

    def test_size(self):
        r = Square(2)
        r.size = 5
        self.assertEqual(5, r.size)

        r.size = 9
        self.assertEqual(9, r.size)

        with self.assertRaises(ValueError):
            r = Square(0)

        with self.assertRaises(ValueError):
            r = Square(-3)

        with self.assertRaises(TypeError):
            r = Square("string")

        with self.assertRaises(TypeError):
            r = Square(None)

        with self.assertRaises(TypeError):
            r = Square()


if __name__ == "__main__":
    unittest.main()

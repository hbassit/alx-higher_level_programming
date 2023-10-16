#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_zero(self):
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_valid_nums(self):
        b = Base(4)
        self.assertEqual(4, b.id)

        b = Base(63)
        self.assertEqual(63, b.id)

        b = Base(2)
        self.assertEqual(2, b.id)

    def test_negatives(self):
        b = Base(-10)
        self.assertEqual(-10, b.id)

        b = Base(-2)
        self.assertEqual(-2, b.id)

    def test_none(self):
        b = Base()
        self.assertEqual(1, b.id)


if __name__ == "__main__":
    unittest.main()

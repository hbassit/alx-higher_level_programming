#!/usr/bin/python3
"""
A module containing a square class whch inherits from a rectangle class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Defines square class
    """

    def __init__(self, size):
        """
        Initializes a square object

        Args:
            size: legth of side of square
        """
        super().__init__(size, size)
        self.__size = size

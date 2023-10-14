#!/usr/bin/python3
"""
Module which contains the base class
"""


class Base:
    """
    Class describing the base object 
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Function initializing base object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            id = Base.__nb_objects
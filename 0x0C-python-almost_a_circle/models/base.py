#!/usr/bin/python3
"""
Module which contains the base class
"""
import json


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
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns json string representation of a list of dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Function that writes json string representation of a list of
        instances to a file
        """
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as f:
            if not list_objs:
                f.write("")
                return
            list_objs = [obj.__dict__ for obj in list_objs]
            f.write(cls.to_json_string(list_objs))

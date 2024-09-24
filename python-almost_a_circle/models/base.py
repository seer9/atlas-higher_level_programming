#!/usr/bin/python3
"""This is the file for base class"""
import json


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """increments the id #"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts an object to a JSON string."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(string):
        if string is None or len(string) == 0:
            return []
        return json.loads(string)

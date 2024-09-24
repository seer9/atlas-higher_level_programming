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
    def to_json_str(obj):
        """Converts an object to a JSON string."""
        if obj is None or len(obj) == 0:
            return '[]'
        return json.dumps(obj)

#!/usr/bin/python3
"""student class"""


class Student:

    def __init__(self, first_name, last_name, age):
        """initializes a student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a json representation of the student"""
        dict = {}
        if type(attrs) is list:
            for attr in attrs:
                if attr in self.__dict__:
                    dict[attr] = self.__dict__[attr]
            return (dict)
        else:
            return (self.__dict__)

    def reload_from_json(self, json):
        """loads a json representation of the student"""
        if not json:
            return
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
#!/usr/bin/python3
"""student class"""


class Student:

    def __init__(self, first_name, last_name, age):
        """initializes a student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a json representation of the student"""

        return (self.__dict__)

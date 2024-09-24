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
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

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a list of objects to a file"""
        file_name = cls.__name__ + ".json"
        if list_objs is None:
            list = []
        else:
            list = [obj.to_dictionary() for obj in list_objs]

        with open(file_name, "w") as file:
            file.write(cls.to_json_string(list))

    @classmethod
    def create(cls, **dictionary):
        """creates an object from a dictionary"""
        dummy = None
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        if dummy is not None:
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """loads a list of objects from a file"""
        file_name = cls.__name__ + ".json"
        list_dict = []
        with open(file_name, "r") as file:
            list_dict = json.load(file)
        list_objs = []
        for dict_obj in list_dict:
            list_objs.append(cls.create(**dict_obj))
        return list_objs

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

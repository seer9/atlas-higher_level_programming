#!/usr/bin/python3
"""base_geometry class"""


class BaseGeometry:
    """CLASS"""

    def area(self):
        """Returns the area of the geometry"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer"""
        
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

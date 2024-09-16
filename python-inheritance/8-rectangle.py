#!/usr/bin/python3
"""rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """retangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
      self.integer_validator(width)
      self.integer_validator(height)
      self.width = width
      self.height = height

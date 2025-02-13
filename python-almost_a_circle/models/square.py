#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes a square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string representation of the square"""
        return "[Square] ({}) {}/{} - {}".format(
          self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the Square attributes."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary rep of a Square."""
        return {
          'id': self.id,
          'size': self.width,
          'x': self.x,
          'y': self.y
        }

    @property
    def size(self):
        """getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter method for size"""
        self.width = value
        self.height = value

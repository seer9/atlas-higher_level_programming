#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


"""Rectangle inherits from Base"""
class Rectangle(Base):
    """initializes a rectangle"""

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """initializes a rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
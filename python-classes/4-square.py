#!/usr/bin/python3
"""Module for Square class"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
      """get size"""
      return self.__size

    @size.setter
    def size(self, value):
      """set size"""
      if type(value) is not int:
        raise TypeError("size must be an integer")
      if value < 0:
        raise ValueError("size must be >= 0")
      self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

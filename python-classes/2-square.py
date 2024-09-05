##!/usr/bin/python3
"""Module for Square class"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0):
        """Initialize the square

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
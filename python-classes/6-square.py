#!/usr/bin/python3
"""Module for Square class"""


class Square:
    """A class that defines a square"""

    def __init__(self, size=0, position=0):
        """Initialize the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position"""
        if not isinstance(value, int):
            raise TypeError("position must be an integer")
        if value < 0:
            raise ValueError("position must be >= 0")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)

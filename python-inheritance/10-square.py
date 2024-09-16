#!/usr/bin/python3
"""Square class"""


class Square(Rectangle):
    """inherits from Rectangle"""

    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        self.size = size
        super().__init__(size, size)

    def area(self):
        """area"""
        return (self.size ** 2)

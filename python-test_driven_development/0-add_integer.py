#!/usr/bin/python3


"""add_integer function"""
def add_integer(a, b=98):
    """
    Function that adds two integers
    """
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b

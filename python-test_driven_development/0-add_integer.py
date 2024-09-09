#!/usr/bin/python3


"""add_integer function"""
def add_integer(a, b=98):
    """
    Function that adds two integers
    """
    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) or not isinstance(a, float):
        raise TypeError("b must be an integer")

    return a + b

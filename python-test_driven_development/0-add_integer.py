#!/usr/bin/python3


"""Module for add_integer function"""
def add_integer(a, b=98):
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b

#!/usr/bin/python3
"""is_same_class function"""


def is_same_class(obj, a_class):
    """checks if the obj is the exact same as a class"""

    if type(obj) is not a_class:
        return False
    else:
        return True

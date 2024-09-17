#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """reads a file and returns its content"""


    with open(filename) as f:
        return (f.read(), end="") 

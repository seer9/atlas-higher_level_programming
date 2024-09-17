#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """writes a file"""

    idx = 0
    if filename == "" or type(filename) is not str:
        return (0)

    with open(filename) as f:
        for line in f:
            idx += 1
    return (idx)
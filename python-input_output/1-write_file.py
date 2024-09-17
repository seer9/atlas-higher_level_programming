#!/usr/bin/python3
"""write_file function"""


def write_file(filename="", text=""):
    """writes a file"""

    with open(filename, "w") as f:
        return f.write(text)

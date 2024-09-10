#!/usr/bin/python3
"""the text_indentation module"""


def text_indentation(text):
        """functions to space text"""

        if not isinstance(text, str):
                raise TypeError("text must be a string")

        for char in text:
                print("{}".format(char))
                if char in ".:?":
                        print("\n\n", end="")
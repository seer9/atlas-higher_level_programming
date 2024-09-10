#!/usr/bin/python3
"""the text_indentation module"""


def text_indentation(text):
        """functions to space text"""

        if not isinstance(text, str):
                raise TypeError("text must be a string")

        lead = 0
        for char in text:
                if lead and char == " ":
                        continue
                print(char, end="")
                if char in ".?:":
                        print("\n")
                        lead = 1
                else:
                        lead = 0

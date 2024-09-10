#!/usr/bin/python3
"""Module for text_indentation function"""

def text_indentation(text):
		"""indents text depending on the char position"""
		if not isinstance(text, str):
				raise TypeError("text must be a string")

		lead = 0
		for char in text:
				if lead and char == ' ':
						continue
				print(char, end="")
				if char in ".?:":
						print("\n")
						lead = 1
				else:
						lead = 0
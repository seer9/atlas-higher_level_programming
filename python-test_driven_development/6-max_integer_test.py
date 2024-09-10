#!/usr/bin/python3
"""max_integer_test module"""


def max_integer(list=[]):
	"""Function to find and return the maximum integer."""
	
	if len(list) == 0:
		return None
	result = list[0]
	for i in list:
		if i > result:
			result = i
	return result

#!/usr/bin/python3
"""unittest module for finding max int"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	"""class for testing max_integer"""
	
	def test_max_at_end(self):
		''' Test with max at the end '''
		self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

	def test_max_at_beginning(self):
		''' Test with max at the beginning '''
		self.assertEqual(max_integer([5, 2, 3, 4, 1]), 5)

	def test_max_in_middle(self):
		''' Test with max in the middle '''
		self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)

	def test_one_negative_number(self):
		''' Test with one negative number '''
		self.assertEqual(max_integer([-5, 0, 3, 4, 2]), 4)

	def test_only_negative_numbers(self):
		''' Test with only negative numbers '''
		self.assertEqual(max_integer([-5, -2, -3, -4]), -2)

	def test_list_of_one_element(self):
		''' Test with list of one element '''
		self.assertEqual(max_integer([3]), 3)

	def test_list_is_empty(self):
		''' Test with list is empty '''
		self.assertIsNone(max_integer([]))

if __name__ == '__main__':
	unittest.main()
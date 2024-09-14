#!/usr/bin/python3
"""1-my_list module"""


class MyList(List):
  """MyList class"""

  def print_sorted(self):
    """prints the sorted list"""
    the_list = self.sort()
    print(the_list)

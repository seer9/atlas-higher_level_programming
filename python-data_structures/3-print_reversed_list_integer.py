#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
      if i == len(my_list) - 1:
        print(my_list[i])
      else:
        print(my_list[i], end=", ")
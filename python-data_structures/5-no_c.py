#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for letter in my_string:
        if my_string[letter] != 'c' and 'C':
          new_str += letter
    return new_str

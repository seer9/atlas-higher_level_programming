#!/usr/bin/python3
def no_c(my_string):
    for letter in my_string:
        if letter != "c" or "C":
            print(letter, end="")
 
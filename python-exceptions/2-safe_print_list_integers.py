#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    position = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[position]), end="")
            position += 1
        except IndexError:
            break
            print()
            return position

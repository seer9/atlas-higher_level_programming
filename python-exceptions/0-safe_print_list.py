#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for idx in range(x):
            print(my_list[idx], end="")
    except IndexError:
        pass
    print()

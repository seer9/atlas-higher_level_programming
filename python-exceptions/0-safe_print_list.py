#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
  try:
        for idx in range(x):
            print("{}".format(my_list[idx], end=""))
          idx += 1
    except IndexError:
        pass
    print()

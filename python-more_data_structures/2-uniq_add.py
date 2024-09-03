#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for idx in my_list:
        if idx not in new_list:
            new_list.append(idx)
    return sum(new_list)
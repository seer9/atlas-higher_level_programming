#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for idx in set_1:
        if idx in set_2:
            new_set.add(idx)
    return new_set

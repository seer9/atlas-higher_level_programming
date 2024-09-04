#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for idx in set_1:
        if idx not in set_2:
            new_set.add(idx)
    return new_set

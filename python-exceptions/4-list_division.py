#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
        try:
            for idx in range(list_length):
                new_list.append(my_list_1[idx] / my_list_2[idx])
        except (ValueError, TypeError, ZeroDivisionError):
            pass
        return new_list

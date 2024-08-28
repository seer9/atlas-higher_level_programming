#!/usr/bin/python3
def print_last_digit(number):
    mod = 0
    if number < 0:
        number = number * -1
        mod = 1
    target = number % 10
    if mod == 1:
        number *= -1
    print("{}".format(target), end="")
    return target

#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        print("{:d} / {:d} = {:.2f}".format(a, b, a / b))
    except (ValueError, TypeError):
        print("Error: invalid input.")

#!/usr/bin/python3
"""matrix_divided function"""


def matrix_divided(matrix, div):
    """devides all the elements in a matrix"""
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    err_msg2 = "Each row of the matrix must be a list of integers/floats"
    if not (isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix)):
        raise TypeError(err_msg)

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(err_msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(err_msg2)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]

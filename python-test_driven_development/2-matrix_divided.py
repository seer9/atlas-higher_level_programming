#!/usr/bin/python3
"""matrix_divided function"""


def matrix_divided(matrix, div):
    """devides all teh elements in a matrix"""
    
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Each row of the matrix must be a list of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[num / div for num in row] for row in matrix]

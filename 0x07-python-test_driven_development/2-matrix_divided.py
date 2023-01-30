#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    This function takes a matrix and a divisor as input and returns a new matrix where
    all elements of the given matrix are divided by the divisor and rounded of to 2 decimal places 
    It checks if the matrix is a list of lists of integers or floats otherwise raises a TypeError
    If each row of the matrix are not of the same size, it raises a TypeError
    If div is not a number(integer or float), it raises a TypeError
    If div is zero, it raises a ZeroDivisionError
    """
    if not isinstance(matrix, list) or not all(isinstance(i, list) for i in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]

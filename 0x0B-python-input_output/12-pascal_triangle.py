#!/usr/bin/python3
"""This module holds a function that returns a list of lists of
integers representing the Pascal’s triangle of n.
"""
def pascal_triangle(n):
    """
    Generate a list of lists representing the Pascal's triangle of n.

    Parameters:
    n (int): The number of rows in the triangle.

    Returns:
    list: A list of lists of integers representing the triangle.
    An empty list if n <= 0.

    Example:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    >>> pascal_triangle(0)
    []
    """
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
    return result if n > 0 else []

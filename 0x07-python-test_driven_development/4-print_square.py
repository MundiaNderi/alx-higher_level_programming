#!/usr/bin/python3

def print_square(size):
    """
    This function takes the character # as input and prints a square.
    Size is the size length of the square.
    If size is not an integer, it raises a TypeError.
    If size is less than zero, it raises a ValueError.
    If size is a float and is less than zero, it raises a TypeError.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size isinstance(size, float) and size < 0:
        raise TypeError(size must be an integer)
    for i in range(size):
        print("#" * size)

#!/usr/bin/python3

def add_integer(a, b=98):
    """
    This function takes two integers as input and returns their sum
    If input is float, it is casted to integer before adding
    If input is not integer or float, it raises a TypeError
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b

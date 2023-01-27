#!/bin/usr/python3

class Square:
    """
    This class defines a square with a private instance attribute size
    """
    def __init__(self, size=0):
        """
        Instantiation with optional size
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

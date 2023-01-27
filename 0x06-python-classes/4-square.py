#!/usr/bin/python3

class Square:
    """
    This class defines a square with a private instance attribute size
    """
    def __init__(self, size=0):
        """
        Instantiation with optional size
        """
        self.size = size

    @property
    def size(self):
        """
        This property retrieves the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This property sets the value of size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        This method returns the current square area
        """
        return self.__size ** 2

#!/usr/bin/python3

class Square:
    """
    Define a square by private instance attribute: size
    Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        """
        Initialize square with given size
        """
        self.__size = size


my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

#!/usr/bin/python3
"""This module holds a function that checks if the object is an
instance of a class that inherited(directly or indirectly)
from the specified class.
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class,
    otherwise False.
    Args:
        obj: the object to check.
        a_class: the class or subclass to check against.
    """

    return True if isinstance(obj, a_class) and \
        type(obj) is not a_class else False

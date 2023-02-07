#!/usr/bin/python3
"""This module holds a function that checks if
an object is an instance of a class or a subclass.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
    or if the object is an instance of a
    class that inherited from the specified class, otherwise false.
    Args:
        obj: the object to check
        a_class: the class to check against
    """

    return True if isinstance(obj, a_class) else False

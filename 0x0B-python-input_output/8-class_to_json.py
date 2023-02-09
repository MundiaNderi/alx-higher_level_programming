#!/usr/bin/python3
"""This module holds a function that returns the dictionary
description with simple data structure.
"""

def class_to_json(obj):
    """returns the dictionary description with simple data structure.
    Args:
        obj: an instance of a class.
    """

    return obj.__dict__

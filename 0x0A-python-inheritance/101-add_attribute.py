#!/usr/bin/python3
""" This module holds a function that adds a new
attrbute to an object if it's possible.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the new attribute will be added.
        attr: The name of the new attribute.
        value: The value of the new attribute.
    raises TypeError: If the object can't have new attributes.
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")

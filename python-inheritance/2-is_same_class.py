#!/usr/bin/python3
"""Module containing a function to check if an object is exactly
an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object's type is exactly a_class, False otherwise.
    """
    return type(obj) is a_class

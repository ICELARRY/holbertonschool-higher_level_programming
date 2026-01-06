#!/usr/bin/python3
"""Module containing a function to check exact class match."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if type(obj) is exactly a_class, False otherwise.
    """
    return type(obj) == a_class

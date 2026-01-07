#!/usr/bin/python3
"""Module containing a function to check if an object is an instance of a
class that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    Returns False if obj is exactly an instance of a_class itself.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True only if obj inherits from a_class (not the exact class).
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""Module containing the lookup function to return available attributes
and methods of an object.
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: List of attribute and method names.
    """
    return dir(obj)

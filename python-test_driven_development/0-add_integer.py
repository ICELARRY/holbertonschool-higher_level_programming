#!/usr/bin/python3

"""
This module provides a function to add two integers (or floats casted to integers).
"""


def add_integer(a, b=98):
    """
    Returns the sum of two integers or floats casted to integers.

    Args:
        a: first integer or float
        b: second integer or float (default 98)

    Raises:
        TypeError: if a or b is not integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

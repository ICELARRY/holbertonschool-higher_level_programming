#!/usr/bin/python3
"""
Module 3-add_integer
Provides function add_integer(a, b=98) that returns the sum of two integers
"""

def add_integer(a, b=98):
    """
    Returns the sum of two integers

    a and b must be integers or floats, otherwise raise TypeError
    Floats are casted to integers before addition

    Args:
        a (int/float): first number
        b (int/float): second number, default 98

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b are not integers/floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

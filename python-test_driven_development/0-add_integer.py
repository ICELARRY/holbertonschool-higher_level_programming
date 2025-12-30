#!/usr/bin/python3

"""
Module for adding two integers.

This module contains a single function, add_integer, which takes two arguments
(a and b) and returns their sum as an integer. Both arguments can be integers
or floats, but they are cast to integers before addition. If b is not provided,
it defaults to 98.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (after casting to integers).

    Args:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
        int: The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
        TypeError: If a or b is NaN or infinity.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN yoxlaması (NaN == NaN həmişə False olur)
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    # +inf və -inf yoxlaması
    import math
    if math.isinf(a):
        raise TypeError("a must be an integer")
    if math.isinf(b):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

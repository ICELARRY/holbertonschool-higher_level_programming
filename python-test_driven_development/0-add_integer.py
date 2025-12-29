#!/usr/bin/python3
"""
Module that adds two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers.

    a and b must be integers or floats.
    Floats are cast to integers.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

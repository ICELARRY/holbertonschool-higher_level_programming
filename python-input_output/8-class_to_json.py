#!/usr/bin/python3
"""
8-class_to_json.py
Contains the function class_to_json that returns a dictionary
description with simple data structure for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns a dictionary representation of obj attributes.

    Args:
        obj: An instance of a class

    Returns:
        dict: Dictionary containing all serializable attributes
    """
    return obj.__dict__.copy()

#!/usr/bin/python3
"""Module that provides a function to list available attributes and methods of an object."""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    
    Args:
        obj: The object to inspect.
        
    Returns:
        list: A list of strings containing the names of attributes and methods.
    """
    return dir(obj)

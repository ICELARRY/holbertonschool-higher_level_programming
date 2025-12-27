#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Delete a key in a dictionary if it exists.

    Args:
        a_dictionary (dict): Dictionary to update
        key (str): Key to delete

    Returns:
        dict: Updated dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

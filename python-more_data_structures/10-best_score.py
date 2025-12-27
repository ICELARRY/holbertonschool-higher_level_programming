#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Return the key with the biggest integer value.

    Args:
        a_dictionary (dict): Dictionary with integer values

    Returns:
        str or None: Key with the biggest value or None if dictionary is empty or None
    """
    if not a_dictionary:  # None or empty dictionary
        return None

    best_key = None
    max_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            best_key = key

    return best_key

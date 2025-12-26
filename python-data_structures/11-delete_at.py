#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete the item at a specific position in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Rebuild the list without the element at idx
    return my_list[:idx] + my_list[idx + 1:]

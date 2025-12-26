#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete the item at a specific position in a list in-place."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx:idx+1] = []
    return my_list

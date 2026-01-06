#!/usr/bin/python3
"""MyList class that inherits from list"""


class MyList(list):
    """Custom list class"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))

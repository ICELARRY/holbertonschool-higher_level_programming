#!/usr/bin/python3
"""Module that defines a custom list class MyList."""

class MyList(list):
    """
    A custom list class that inherits from the built-in list class
    and provides a method to print the list in sorted ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in sorted ascending order.
        The original list remains unmodified.
        Assumes all elements are integers.
        """
        print(sorted(self))

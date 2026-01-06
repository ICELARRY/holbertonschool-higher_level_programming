#!/usr/bin/python3

class MyList(list):
    """A custom list class that inherits from the built-in list class."""

    def print_sorted(self):
        """Prints the list in ascending sorted order (without modifying the original list)."""
        print(sorted(self))

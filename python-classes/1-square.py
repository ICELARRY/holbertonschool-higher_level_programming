#!/usr/bin/python3
"""Define a Square with a private size attribute."""


class Square:
    """Square class with private size."""

    def __init__(self, size):
        """Initialize square with size."""
        self.__size = size

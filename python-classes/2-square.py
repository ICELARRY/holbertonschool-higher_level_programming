#!/usr/bin/python3
"""Define a Square with size validation."""


class Square:
    """Square class with private size and validation."""

    def __init__(self, size=0):
        """Initialize square with size validation."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

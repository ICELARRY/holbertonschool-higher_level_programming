#!/usr/bin/python3
"""Define a Square with private size, getter, setter, and area."""


class Square:
    """Square class with size property and area method."""

    def __init__(self, size=0):
        """Initialize square with optional size."""
        self.size = size  # setter üzerinden geçer

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

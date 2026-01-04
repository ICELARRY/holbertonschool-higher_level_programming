#!/usr/bin/python3
"""Define a Square with size property, area, and my_print method."""


class Square:
    """Square class with size, area, and printing."""

    def __init__(self, size=0):
        """Initialize square with optional size."""
        self.size = size  # setter ile validation

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
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # or empty line if size is 0."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)

#!/usr/bin/python3
"""Define a Square with size, position, area, and printing."""


class Square:
    """Square class with size, position, area, and my_print method."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with optional size and position."""
        self.size = size      # setter ile validation
        self.position = position  # setter ile validation

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation: tuple of 2 positive integers."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # respecting position."""
        if self.__size == 0:
            print()
            return
        # position[1] -> vertical offset (newlines)
        for _ in range(self.__position[1]):
            print()
        # print each row
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

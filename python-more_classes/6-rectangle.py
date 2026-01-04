#!/usr/bin/python3
"""Module defining a Rectangle class with instance counting."""


class Rectangle:
    """Defines a rectangle with width, height, and instance tracking."""

    number_of_instances = 0  # Class attribute to count instances

    def __init__(self, width=0, height=0):
        """Initialize rectangle and increment instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation using '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        rect_lines = ["#" * self.width for _ in range(self.height)]
        return "\n".join(rect_lines)

    def __repr__(self):
        """Return a string to recreate a new instance."""
        repr_str = "Rectangle({}, {})".format(self.width, self.height)
        return repr_str

    def __del__(self):
        """Print a message when an instance is deleted and decrement counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

#!/usr/bin/python3


"""Module defining the Rectangle class."""


class Rectangle:
    """A class that defines a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width."""
        return self._width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self._height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the biggest rectangle based on the area.
        Return rect_1 if both have the same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """
        Return the string representation of the rectangle using print_symbol.
        """
        if self.width == 0 or self.height == 0:
            return ""
        symbol_str = str(self.print_symbol)
        row = symbol_str * self.width
        return "\n".join([row] * self.height)

    def __repr__(self):
        """Return a string representation that can recreate the instance."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message and decrement the instance count on deletion."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

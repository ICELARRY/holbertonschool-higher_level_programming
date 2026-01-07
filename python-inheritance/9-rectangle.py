#!/usr/bin/python3
"""Module containing the Rectangle class with area implementation."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height.

        Args:
            width (int): The width of the rectangle (positive integer).
            height (int): The height of the rectangle (positive integer).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

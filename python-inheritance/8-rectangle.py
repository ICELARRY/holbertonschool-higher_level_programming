#!/usr/bin/python3
"""Module containing the Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height.

        Args:
            width (int): The width of the rectangle (positive integer).
            height (int): The height of the rectangle (positive integer).
        """
        # Validate width and height using inherited integer_validator
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Store as private attributes
        self.__width = width
        self.__height = height

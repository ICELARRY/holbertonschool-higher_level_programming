#!/usr/bin/python3
"""Module containing the BaseGeometry class with area() method."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")

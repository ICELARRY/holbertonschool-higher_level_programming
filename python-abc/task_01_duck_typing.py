#!/usr/bin/env python3
"""Shapes module with duck typing"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """Abstract Shape class"""

    @abstractmethod
    def area(self):
        """Calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter"""
        pass


class Circle(Shape):
    """Circle shape"""

    def __init__(self, radius):
        self.radius = abs(radius)  # radius her zaman pozitif

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of a shape (duck typing)"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

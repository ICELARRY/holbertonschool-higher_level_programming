#!/usr/bin/python3
"""Test file for Rectangle class"""

Rectangle = __import__('5-rectangle').Rectangle

# Create a rectangle with width=2 and height=4
my_rectangle = Rectangle(2, 4)

# Print area and perimeter
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

# Delete the rectangle instance
del my_rectangle

# Try to access deleted instance
try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

#!/usr/bin/python3
"""
9-student.py
Defines a Student class with a to_json method
"""

class Student:
    """Defines a student with first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the Student instance

        Returns:
            dict: Dictionary containing the instance attributes
        """
        return self.__dict__.copy()

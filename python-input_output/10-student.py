#!/usr/bin/python3
"""
10-student.py
Defines a Student class with a to_json method that supports filtering.
"""


class Student:
    """Defines a student with first_name, last_name, and age"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                                    Defaults to None (include all).

        Returns:
            dict: Dictionary containing the instance attributes
        """
        if isinstance(attrs, list):
            # Only include attributes that exist in the instance
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

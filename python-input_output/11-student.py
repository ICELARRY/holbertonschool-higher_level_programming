#!/usr/bin/python3
"""
11-student.py
Defines a Student class with to_json and reload_from_json methods
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
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with the values
        in the provided dictionary.

        Args:
            json (dict): Dictionary containing new attribute values
        """
        for key, value in json.items():
            setattr(self, key, value)

    def __str__(self):
        """Readable string representation of the Student"""
        return "[Student] {} {} - {}".format(
            self.first_name, self.last_name, self.age
        )

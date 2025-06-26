#!/usr/bin/python3
"""Defines a Student class with filtered JSON serialization."""


class Student:
    """Represents a student with filtered JSON serialization."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a filtered dictionary representation of the Student.

        Args:
            attrs (list): Optional list of attribute names to include

        Returns:
            dict: Dictionary representation of the Student with filtered attributes
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return vars(self)

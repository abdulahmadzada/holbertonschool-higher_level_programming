#!/usr/bin/python3
"""
This module defines a CustomObject class with methods for serialization
and deserialization using the pickle module.
"""

import pickle


class CustomObject:
    """
    A custom object class representing a person with name, age,
    and student status.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the attributes of the CustomObject instance.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current object to the specified file using pickle.

        Args:
            filename (str): The file path to save the serialized object.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from the specified pickle file.

        Args:
            filename (str): The file path to load the serialized object from.

        Returns:
            CustomObject or None: The loaded object or None on error.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except (FileNotFoundError, pickle.PickleError, EOFError, Exception):
            return None

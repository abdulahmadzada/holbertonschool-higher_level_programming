#!/usr/bin/python3
"""Function to check if object is instance of/inherited from specified class."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a specified class.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj is instance of or inherited from a_class, False otherwise
    """
    return isinstance(obj, a_class)

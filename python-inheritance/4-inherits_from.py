#!/usr/bin/python3
"""Module for checking if an object inherits from a specified class."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check
        a_class: The class to check inheritance against

    Returns:
        bool: True if obj is an instance of a subclass of a_class (but not a_class itself),
              False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""Function to return list of available attributes and methods of an object."""


def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect

    Returns:
        list: List of attributes and methods
    """
    return dir(obj)

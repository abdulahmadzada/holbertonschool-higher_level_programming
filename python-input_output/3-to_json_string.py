#!/usr/bin/python3
"""Defines a function to return the JSON representation of an object."""

import json


def to_json_string(my_obj):
    """Return the JSON string representation of an object.

    Args:
        my_obj: The object to serialize to JSON

    Returns:
        str: The JSON string representation of the object
    """
    return json.dumps(my_obj)

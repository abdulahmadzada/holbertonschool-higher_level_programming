#!/usr/bin/python3
"""Defines a function to convert JSON string to Python object."""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to deserialize

    Returns:
        object: The Python data structure represented by the JSON string
    """
    return json.loads(my_str)

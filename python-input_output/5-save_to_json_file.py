#!/usr/bin/python3
"""Defines a function to write an object to a file as JSON."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.

    Args:
        my_obj: The Python object to serialize
        filename (str): The name of the file to write to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

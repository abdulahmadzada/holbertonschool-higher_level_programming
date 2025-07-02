#!/usr/bin/python3
"""
This module provides basic functionality to serialize a Python dictionary
to a JSON file and deserialize a JSON file to recreate the Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the file to write the JSON data to.

    The function overwrites the file if it already exists.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """
    Loads and deserializes JSON data from a file into a Python dictionary.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        dict: The dictionary resulting from the JSON file content.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

#!/usr/bin/python3
"""Defines a function to write a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8) and return character count.

    Args:
        filename (str): The name of the file to write to
        text (str): The text to write to the file

    Returns:
        int: The number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

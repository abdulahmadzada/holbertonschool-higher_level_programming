#!/usr/bin/python3
"""Defines a function to append text to a file and return character count."""


def append_write(filename="", text=""):
    """Append a string to a text file (UTF-8) and return characters added.

    Args:
        filename (str): The name of the file to append to
        text (str): The text to append to the file

    Returns:
        int: The number of characters appended
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

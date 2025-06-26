#!/usr/bin/python3
"""Defines a function to read and print a text file."""


def read_file(filename=""):
    """Read a text file (UTF-8) and print its contents to stdout.

    Args:
        filename (str): The name of the file to read
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")

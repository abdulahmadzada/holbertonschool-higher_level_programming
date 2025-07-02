#!/usr/bin/python3
"""
This module provides functions to serialize and deserialize
Python dictionaries using XML format.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML format and writes to a file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Name of the file to write XML data into.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except Exception:
        pass  # Optional: log the error or raise


def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file into a Python dictionary.

    Args:
        filename (str): The name of the XML file.

    Returns:
        dict: Dictionary reconstructed from the XML file.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text
        return result
    except (FileNotFoundError, ET.ParseError, Exception):
        return None

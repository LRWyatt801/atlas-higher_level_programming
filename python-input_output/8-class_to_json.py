#!/usr/bin/python3
"""Contains class_to_json function"""


def class_to_json(obj) -> dict:
    """Returns the dictionary representation of a simple data struct

    Args:
        obj (struct): simple data structure

    Returns:
        dict: dictionary representation
    """
    return obj.__dict__

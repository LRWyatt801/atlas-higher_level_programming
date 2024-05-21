#!/usr/bin/python3
"""contains to_json_string function"""
import json


def to_json_string(my_obj) -> str:
    """returns the JSON representation of an object

    Args:
        my_obj (str): any object to be searialized

    Returns:
        str: JSON representation of obj
    """
    return json.dumps(my_obj)

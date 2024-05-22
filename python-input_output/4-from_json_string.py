#!/usr/bin/python3
"""Contains from_json_string function"""


import json


def from_json_string(my_str) -> any:
    """Return an Python data structure represented by a JSON string

    Args:
        my_str (str): JSON string

    Returns:
        any: object represented by JSON str
    """
    return json.loads(my_str)

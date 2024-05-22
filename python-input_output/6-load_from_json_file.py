#!/usr/bin/python3
"""Contains load_from_json_file function"""


import json


def load_from_json_file(filename) -> any:
    """Creates object from JSON file

    Args:
        filename (JSON file): JSON file

    Return (any): object created from JSON file
    """
    with open(filename, 'r', encoding="utf-8"):
        return json.load(filename)

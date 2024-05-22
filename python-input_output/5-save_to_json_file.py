#!/usr/bin/python3
"""Contains save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename) -> None:
    """Writes an object to a text file, using a JSON representation

    Args:
        my_obj (any): Any object
        filename (txt): name of file to write too
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)

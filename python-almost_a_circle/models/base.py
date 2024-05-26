#!/usr/bin/python3
"""Contains a base class"""


import json


class Base:
    """Base class for project"""
    __nb_objects = 0

    def __init__(self, id: int = None) -> None:
        """Class constructor

        Args:
            id (int, optional): id of object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries) -> str:
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

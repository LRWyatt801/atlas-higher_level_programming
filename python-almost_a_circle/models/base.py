#!/usr/bin/python3
"""Contains a base class"""


import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries: list) -> str:
        """Returns JSON string representation

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: JSON representation
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs: list) -> None:
        """Saves the JSON representations of object(s), in a list,
        to a file

        Args:
            list_objs (list): List of instances who inherits of base
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
            with open(filename, 'w') as file:
                file.write(cls.to_json_string(json_list))
        else:
            with open(filename, 'w') as file:
                file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string: str) -> list:
        """Returns the list of the JSON representation of json_string

        Args:
            json_string (str): JSON string representation

        Returns:
            list: List of the JSON string representation
        """
        if json_string is not None:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary) -> object:
        """Returns an instance with all attributes set

        Returns:
            object: instance of object
        """
        if cls.__name__ == 'Rectangle':
            tmp = cls(1, 1)
        elif cls.__name__ == 'Square':
            tmp = cls(1)

        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        list_instances = []
        list_dictionaries = []

        if os.path.exists(filename):
            with open(filename, 'r') as file:
                json_str = file.read()
                list_dictionaries = cls.from_json_string(json_str)
                for dict in list_dictionaries:
                    list_instances.append(cls.create(**dict))
        return list_instances

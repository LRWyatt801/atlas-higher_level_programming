#!/usr/bin/python3
"""Contains a class Student"""


class Student:
    """Defines a Student"""
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        """Instantiation of Student class

        Args:
            first_name (str): First name of student
            last_name (str): Last name of student
            age (int): Age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs: str = None) -> dict:
        """Returns dictionary representation of Student instance

        Args:
            attrs (str, optional): attribute to look for

        Returns:
            dict: Dictionary representation of student instance
        """
        if isinstance(attrs, list) and \
                all(isinstance(ele, str) for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json: dict) -> None:
        """Load json dictionary and set attributes to dict:value

        Args:
            json (dict): Dictionary representation of attributes
        """
        for k, v in json.items():
            setattr(self, k, v)

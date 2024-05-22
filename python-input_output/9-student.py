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

    def to_json(self) -> dict:
        """Returns dictionary representation of Student instance

        Returns:
            dict: Dictionary representation of student instance
        """
        return self.__dict__

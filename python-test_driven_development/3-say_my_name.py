#!/usr/bin/python3
"""Module for say_my_name function"""


def say_my_name(first_name, last_name=""):
    """function that prints "My name is <first> <last>"

    Args:
        first_name (str): first name
        last_name (str, optional): last name. Defaults to nothing

    Raises:
        TypeError: first name is not type str
        TypeError: last name is not type str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))

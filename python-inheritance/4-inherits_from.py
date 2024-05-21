#!/usr/bin/python3
"""Contains inherits_from"""


def inherits_from(obj, a_class) -> bool:
    """Tests of obj inherits from a_class

    Args:
        obj (any): instance of a class
        a_class (any): class to compare

    Returns:
        bool: true or false
    """
    return (issubclass(obj, a_class) and type(obj) is not a_class)

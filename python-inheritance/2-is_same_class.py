#!/usr/bin/python3
"""Contains a function that test if obj are the same"""


def is_same_class(obj, a_class) -> bool:
    """Tests if obj is the same class as a_class

    Args:
        obj (object): object to be tested
        a_class (class): class to match

    Returns:
        bool: true or false
    """
    if type(obj) is a_class:
        return True
    else:
        return False

#!/usr/bin/python3
"""Module contains is_kind_of_class"""


def is_kind_of_class(obj, a_class) -> bool:
    """Tests if obj is an instance of a_class

    Args:
        obj (any): object of any type
        a_class (class): check

    Returns:
        bool: true or false
    """
    return isinstance(obj, a_class)

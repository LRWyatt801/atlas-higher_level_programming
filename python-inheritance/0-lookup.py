#!/usr/bin/python3
"""Module with a lookup function"""


def lookup(obj) -> list:
    """returns list of attributes

    Args:
        obj (class): class instance

    Returns:
        list: attributes of obj
    """
    attrs = [attr for attr in dir(obj)]
    return attrs

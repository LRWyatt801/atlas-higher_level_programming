#!/usr/bin/python3
"""Module for adding 2 ints together"""


def add_integer(a, b=98):
    """function that add 2 integers

    Args:
        a (int, float): integer to be added
        b (int, float, optional): integer to be added. Defaults to 98.

    Raises:
        TypeError: must be int
        TypeError: must be int

    Returns:
        int: sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

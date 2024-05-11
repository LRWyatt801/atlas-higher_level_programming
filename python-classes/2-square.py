#!/usr/bin/python3
"""defines square"""


class Square:
    """class for square"""
    def __init__(self, size=0):
        """New square
        Args:
            size (int): size of square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

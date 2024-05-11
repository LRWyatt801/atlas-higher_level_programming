#!/usr/bin/python3
"""defines square"""


class Square:
    """class for square"""
    def __init__(self, size=0):
        """Init square
        Attributes:
            size: size of square"""
        self.size = size

    @property
    def size(self):
        """This is the getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """This is the setter for size
        Args:
            value: value to set size to"""
        if not isinstance(value, int):
            print("size must be an integer")
            return ValueError
        elif value < 0:
            print("size must be >= 0")
            return ValueError
        else:
            self.__size = value

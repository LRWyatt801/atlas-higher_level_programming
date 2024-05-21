#!/usr/bin/python3
"""contains classes for basic shapes"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class for rectangle

    Args:
        BaseGeometry (Superclass): Parent class
    """
    def __init__(self, size) -> None:
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

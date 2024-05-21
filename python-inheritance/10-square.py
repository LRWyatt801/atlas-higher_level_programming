#!/usr/bin/python3
"""contains classes for basic shapes"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """Class for rectangle

    Args:
        BaseGeometry (Superclass): Parent class
    """
    def __init__(self, size) -> None:
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates the area of Rectangle"""
        return self.__size ** 2

    # def __str__(self):
    #     """Overwrite __str__ to below"""
    #     print(f"[Square] {self.__size}/{self.__size}")

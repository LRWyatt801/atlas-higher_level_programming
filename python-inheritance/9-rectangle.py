#!/usr/bin/python3
"""contains classes for basic shapes"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class for rectangle

    Args:
        BaseGeometry (Superclass): Parent class
    """
    def __init__(self, width, height) -> None:
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Overwrite __str__ to below"""
        print("[{}]] {:d}/{:d}".format(str(self.__class__.__name__), self.__width, self.__height))

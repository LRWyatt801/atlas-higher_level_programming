#!/usr/bin/python3
"""contains classes for basic shapes"""


class BaseGeometry:
    """BaseGeometry class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(name, str):
            raise TypeError("name must be str")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class for rectangle

    Args:
        BaseGeometry (Superclass): Parent class
    """
    def __init__(self, width, height) -> None:
        self.__width = self.integer_validator(width)
        self.__height = self.integer_validator(height)

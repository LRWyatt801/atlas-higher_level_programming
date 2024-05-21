#!/usr/bin/python3
"""contains classes for basic shapes"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Class for rectangle

    Args:
        BaseGeometry (Superclass): Parent class
    """
    def __init__(self, width, height) -> None:
        self.__width = self.integer_validator(width)
        self.__height = self.integer_validator(height)

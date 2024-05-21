#!/usr/bin/python3
"""contains classes for basic shapes"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class for rectangle

    Args:
        BaseGeometry (Superclass): Parent class
    """
    def __init__(self, width, height) -> None:
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self) -> int:
        """Calculates the area of Rectangle

        Returns:
            int: area
        """
        return self.__width * self.__height

    def __str__(self):
        """Overwrite __str__ to below"""
        print(f"[Rectangle] {self.__width}/{self.__height}")

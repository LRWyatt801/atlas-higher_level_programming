#!/usr/bin/python3
"""Module defines a class: Rectangle"""


class Rectangle:
    """Class for rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation of Rectangle

        Args:
            width (int, optional): Width of rectangle. Defaults to 0.
            height (int, optional): Height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width

        Args:
            value (int): new width of rectangle

        Raises:
            TypeError: width must be int
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height Setter

        Args:
            value (int): new value for height

        Raises:
            TypeError: Height must be int
            ValueError: Height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

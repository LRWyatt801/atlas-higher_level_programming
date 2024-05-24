#!/usr/bin/python3
"""Contains class for Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base.  Provides all neccessary
    dimensions for a rectangle

    Args:
        Base (class): Parent class
    """
    def __init__(self, width: int, height: int,
                 x: int = 0, y: int = 0, id: int = None) -> None:
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

    @property
    def x(self):
        """getter for x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x coordinate

        Args:
            value (int): new x coordinate of rectangle

        Raises:
            TypeError: x must be int
            ValueError: width  must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter for y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y coordinate

        Args:
            value (int): new value for y

        Raises:
            TypeError: y must be int
            ValueError: y must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

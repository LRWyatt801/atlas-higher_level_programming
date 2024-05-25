#!/usr/bin/python3
"""Contains class for Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base.  Provides all neccessary
    dimensions for a rectangle

    Args:
        Base (class): Parent class
    """

    print_symbol = '#'

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
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        elif value <= 0:
            raise ValueError("height must be > 0")
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

    def area(self):
        """Calculates the area of rectangle

        Returns:
            int: area
        """
        return self.__height * self.__width

    def display(self):
        """print the retangle using print_symbol"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            for _ in range(self.__y):
                print("")  # prints empty lines up to coordinate y
            for prt_height in range(self.__height):
                for _ in range(self.__x):
                    print(" ", end="")  # prints spaces to shift to x coor
                for prt_width in range(self.__width):
                    print(f"{self.print_symbol}", end="")
                print("")

    def update(self, *args, **kwargs) -> None:
        """Update rectangle object

        Optional Args:
            id (int): id of object
            width (int): width of rectangle object
            height (int): height of rectangle object
            x (int): x coordinate of rectangle
            y (int): y coordinate of rectangle
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def __str__(self):
        """overwrite __str__ to below"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.__class__.__name__, self.id, self.__x, self.__y, self.__width, self.__height)

    def to_dictionary(self) -> dict:
        recdict = {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
        return recdict

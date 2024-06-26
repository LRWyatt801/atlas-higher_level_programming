#!/usr/bin/python3
"""Module defines a class: Rectangle"""


class Rectangle:
    """Class for rectangle

    Attributes:
        number_of_instances (int) = number of current instances
        print_symbol (any) = symbol to represent rectangle when printed
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantiation of Rectangle

        Args:
            width (int, optional): Width of rectangle. Defaults to 0.
            height (int, optional): Height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates the area of rectangle

        Returns:
            int: area
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of rectangle

        Returns:
            int: perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print the retangle using print_symbol"""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            print_rec = ""
            for y in range(self.__height):
                for x in range(self.__width):
                    print_rec += str(self.print_symbol)
                if y < self.__height - 1:
                    print_rec += "\n"
            return print_rec

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares 2 Retangles based on area

        Args:
            rect_1 (Rectangle): Instance of Rectangle
            rect_2 (Rectangle): Instance of Rectangle

        Raises:
            TypeError: type error must be Rectangle
            TypeError: type error must be Rectangle

        Returns:
            Rectangle: Whichever rect is larger, if same then returns rect_1
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates new rectangle that is square

        Args:
            size (int, optional): size square should be. Defaults to 0.

        Returns:
            Rectangle: Class of Rectangle of size = size
        """
        return Rectangle(size, size)

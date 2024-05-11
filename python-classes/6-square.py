#!/usr/bin/python3
"""defines square"""


class Square:
    """class for square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Init new square

        Attributes:
            size: size of square
            position: coordinate for square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of size

        Args:
            value (int): value to set size to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position in (x,y) coordinates

        Args:
            value (tuple): the (x,y) position of square
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not isinstance(i, int) or (isinstance(i, int) and i < 0):
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Method that calculates area of square

        Returns:
            area of square
        """
        return self.__size ** 2

    def my_print(self):
        """prints the called square using # """
        if self.__size == 0:
            print("")
        for _ in range(self.__position[1]):
            print("") # prints empty lines up to position 'y'
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="") # prints spaces up to position 'x'
            for i in range(self.__size):
                print("#", end="")  # print "#"
            print("")  # print new line

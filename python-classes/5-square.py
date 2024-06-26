#!/usr/bin/python3
"""defines square"""


class Square:
    """class for square"""
    def __init__(self, size=0):
        """
        Init square
        Attributes:
            size: size of square
        """
        self.size = size

    @property
    def size(self):
        """This is the getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        This is the setter for size
        Args:
            value: value to set size to
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Method that calculates area of square

        Returns:
            area of square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints the called square using #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")  # print "#"
                print("")  # print new line

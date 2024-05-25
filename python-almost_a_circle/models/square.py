#!/usr/bin/python3
"""Contains a Square class that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle.
    Uses the Rectangle class to build squares

    Args:
        Rectangle (Class): Provides neccessary info for a rectangle
    """
    def __init__(self, size: int, x: int = 0, y: int = 0, id: int = None) -> None:
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """overwrite __str__ to below"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}"\
            .format(self.__class__.__name__, self.id, self.__x, self.__y, self.__width)

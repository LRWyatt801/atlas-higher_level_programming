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
        """Create a new instance of Square

        Args:
            size (int): Size of Square
            x (int, optional): X cooridnate of square. Defaults to 0.
            y (int, optional): Y coordinate of square. Defaults to 0.
            id (int, optional): Instance ID. Defaults to None.
        """
        super().__init__(size, size, x, y, id)
   
    @property
    def size(self):
        """Size Getter"""
        return self.width
    
    @size.setter
    def size(self, value: int):
        """Size Setter"""
        self.width = value
        self.height = value
        
   
    def __str__(self):
        """String representation of Square"""
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs) -> None:
        """Update an instance of Square

        Optional Args:
            id (int): id of object
            size (int): size of Square
            x (int): x coordinate of Square
            y (int): y coordinate of Square
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

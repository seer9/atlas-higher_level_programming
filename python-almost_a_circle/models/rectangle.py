#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """initializes a rectangle"""

    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """initializes a rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self) -> str:
        """Return the readable string rep of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
          self.id, self.__x, self.__y, self.__width, self.height)

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """displays the rectangle"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Update the Rectangle attributes."""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary representation of the square"""
        return {
          'id': self.id,
          'width': self.__width,
          'height': self.__height,
          'x': self.__x,
          'y': self.__y
        }

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the value of x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the value of y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

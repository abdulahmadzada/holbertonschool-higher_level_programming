#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height,
number of instances, and print symbol functionality.
"""


class Rectangle:
    """
    Rectangle class with private width and height,
    class attribute number_of_instances, and print_symbol.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize Rectangle instance.

        Args:
            width (int): Width of rectangle (default 0).
            height (int): Height of rectangle (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter of the rectangle.

        Returns 0 if width or height is zero.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        line = str(self.print_symbol) * self.__width
        return "\n".join(line for _ in range(self.__height))

    def __repr__(self):
        """Return string to recreate the instance with eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message on instance deletion and decrement counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

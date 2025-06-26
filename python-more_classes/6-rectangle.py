#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height,
counting instances, printing with #, and repr support.
"""


class Rectangle:
    """
    Rectangle class with private width and height attributes,
    class attribute number_of_instances counting active instances,
    and methods for area, perimeter, string representation,
    and cleanup on deletion.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): Rectangle width (default 0).
            height (int): Rectangle height (default 0).
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
        """Return area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of the rectangle.

        If width or height is zero, perimeter is zero.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation using # character."""
        if self.__width == 0 or self.__height == 0:
            return ""
        line = str(self.print_symbol) * self.__width
        return "\n".join(line for _ in range(self.__height))

    def __repr__(self):
        """Return string for recreating this instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Cleanup actions when instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

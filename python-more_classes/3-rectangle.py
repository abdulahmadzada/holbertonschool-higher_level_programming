#!/usr/bin/python3
"""
Module that defines a Rectangle class with width and height,
methods area, perimeter, string representation with #, and repr.
"""


class Rectangle:
    """
    Rectangle class with private width and height attributes,
    optional instantiation, area, perimeter, and string methods.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle.

        Args:
            width (int): Width of rectangle (default 0).
            height (int): Height of rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        If width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle as a string made of # characters.

        Return empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        line = "#" * self.__width
        return "\n".join(line for _ in range(self.__height))

    def __repr__(self):
        """Return string representation to recreate the instance."""
        return f"<{self.__class__.__module__}.{self.__class__.__name__} object at {hex(id(self))}>"

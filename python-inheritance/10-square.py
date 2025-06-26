#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, a special case of Rectangle with equal sides."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square's sides
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square (size²)
        """
        return self.__size ** 2

    def __str__(self):
        """Return the string representation of the square.

        Returns:
            str: The square description in format [Rectangle] <size>/<size>
        """
        return f"[Rectangle] {self.__size}/{self.__size}"

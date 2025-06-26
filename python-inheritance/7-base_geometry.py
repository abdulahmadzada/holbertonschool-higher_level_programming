#!/usr/bin/python3
"""Defines a base geometry class with validation functionality."""


class BaseGeometry:
    """A base class for geometric operations and validations.

    This class provides fundamental geometric operations and includes
    methods for validating geometric properties.
    """

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Indicates that the method is not implemented.
                      Message: 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): The name of the parameter being validated.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

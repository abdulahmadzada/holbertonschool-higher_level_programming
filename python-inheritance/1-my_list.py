#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A custom list class that inherits from the built-in list class.
    
    This class provides additional functionality to print the list in sorted order
    without modifying the original list.
    """

    def print_sorted(self):
        """Print the list in ascending sorted order.
        
        This method sorts the list and prints it, but doesn't modify
        the original list. All elements must be of type int.
        """
        print(sorted(self))

#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """
    Defines a square.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size):
        """
        Initializes the square with a specific size.

        Args:
            size: The size of the square.
        """
        self.__size = size

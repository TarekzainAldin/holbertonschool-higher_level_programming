#!/usr/bin/python3
"""Contains an class : 'Square'"""


class Square:
    """Size validation of size in square"""
    def __init__(self, size=0):
        """Test et initialise size"""
        if not type(size) is int:
            raise Exception("size must be an integer")
        if int(size) < 0:
            raise Exception("size must be >= 0")
        self.__size = size

    def area(self):
        """Return square of size"""
        return self.__size ** 2

#!/usr/bin/python3
"""Contains an class : 'Square"""


class Square:
    """A class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square with a given size."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """get the position """
        return self._position

    @position.setter
    def position(self, value):
        """set the value for var ins."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calcule and return ."""
        return (self._size ** 2)

    def my_print(self):
        """print the val """
        if self._size == 0:
            print("")
            return
        for _ in range(self._position[1]):
            print("")
        for _ in range(self._size):
            print(" " * self._position[0] + "#" * self._size)

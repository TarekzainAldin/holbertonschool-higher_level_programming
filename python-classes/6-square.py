#!/usr/bin/python3
"""Square class"""


class Square:
    """Class that defines a square with attributes"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """To getter the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """To setter size attribute"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """To getter position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """To setter position attribute"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the # character"""
        if self.__size > 0:
            for i in range(0, self.__position[1]):
                print()

            for x in range(0, self.__size):
                for i in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
        else:
            print()

#!/usr/bin/python3
"""BaseGeometry"""


class BaseGeometry():
    """BaseGeometry"""
    def area(self):
        raise Exception("area() is not implemented")

    def inteeger_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be ineger".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))

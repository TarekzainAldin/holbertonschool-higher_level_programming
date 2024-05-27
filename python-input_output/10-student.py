#!/usr/bin/python3
"""Contient la classe student"""


class Student:
    """class of student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return the choosen attributes or all if attrs=None"""
        if attrs is None:
            return self.__dict__
        Dict_Attrs_values = {}
        for val in attrs:
            if val in self.__dict__:
                Dict_Attrs_values[val] = self.__dict__[val]
        return Dict_Attrs_values

#!/usr/bin/python3
"""is_kind_of_class"""


def is_same_class(obj, a_class):
    """if the object is an instance of a class"""
    if type(obj) is a_class:
        return True
    return False

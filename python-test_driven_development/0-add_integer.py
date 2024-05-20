#!/user/bin/python3
"""Module for add_integer method-

>>> add_interger(5,10)
15
>>> add_integer(2)
100"""


def add_integer(a, b=98):
    """make the sum for tow integers
        return error if a or b its not error
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    add = int(a) + int(b)
    return add

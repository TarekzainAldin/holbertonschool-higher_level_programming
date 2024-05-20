#!/user/bin/python3
"""Moudle for say_my_name method"""


def say_my_name(first_name, last_name):
    """method for printing first and last name
     args:
     first_name string
     last_name string
     Raise:
     typeError: if first_name or last_name not strings
        """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be string")
    print("My Name Is  {:s} {:s}".format(first_name, last_name))

    if __name__ == "__main__":
        import doctest
    doctest.testfile("tests/3-say_my_name.txt")

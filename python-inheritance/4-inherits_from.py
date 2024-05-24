#!/user/bin/python3
"""ingerits"""


def inherits_form(obj, a_class):
    """inherites"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False

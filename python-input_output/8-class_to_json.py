#!/usr/bin/python3
"""contains the Class to JSON"""


def class_to_json(obj):
    """class to json
    """
    if not hasattr(obj, '__dict__'):
        raise ValueError("Input object is not serializable")

    serialized = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized[key] = value
        else:
            raise ValueError(f"Attribute '{key}' is not serializable")

    return serialized

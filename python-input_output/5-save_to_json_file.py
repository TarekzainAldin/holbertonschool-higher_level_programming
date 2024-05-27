#!/usr/bin/python3
"""save the obj to file"""


import json
"""library json"""


def save_to_json_file(my_obj, filename):
    """write object to the json file"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))

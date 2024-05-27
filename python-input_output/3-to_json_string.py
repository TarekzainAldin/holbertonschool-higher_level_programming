#!/user/bin/python3
"""dumps funciton for converting the obj to string """


import json
"""from object to string"""


def to_json_string(my_obj):
    """return json representation from obj to string"""
    return json.dumps(my_obj)

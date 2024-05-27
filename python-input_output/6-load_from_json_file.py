#!/usr/bin/python3*
"""import json"""

import json
"""load_from_json_file"""


def load_from_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)

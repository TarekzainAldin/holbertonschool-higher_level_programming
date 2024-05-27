#!/usr/bin/python3*
"""Module to load an object from a JSON file"""

import json


def load_from_json_file(filename):
    """Write a function that creates an Object from a json file"""
    with open(filename, "r") as f:
        return json.load(f)

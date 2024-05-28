#!/usr/bin/python3
"""Contains the Converting CSV Data to JSON Format"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """csv to json """
    try:
        with open(csv_filename, 'r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"is there error{e}")
        return False

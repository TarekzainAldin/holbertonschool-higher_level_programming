#!/usr/bin/python3

from flask import Flask, render_template, request
from pathlib import Path
import json
import csv

app = Flask(__name__, template_folder="/home/tarek/holbertonschool-higher_level_programming-12/python-server_side_rendering/templates ")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    items_list = []

    try:
        with open("/home/tarek/holbertonschool-higher_level_programming-12/python-server_side_rendering/items.json", 'r') as f:
            rows = json.load(f)
        for key, value in rows.items():
            items_list = value
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return f"Error loading items: {str(e)}"

    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    data = []
    try:
        if source == "json":
            data = load_json_data("/home/tarek/holbertonschool-higher_level_programming-12/python-server_side_rendering/products.json", id)
        elif source == "csv":
            data = load_csv_data("/home/tarek/holbertonschool-higher_level_programming-12/python-server_side_rendering/products.csv", id)
    except (FileNotFoundError, ValueError) as e:
        return f"Error loading products: {str(e)}"

    return render_template('product_display.html', data=data, source=source, id=id)

def load_json_data(filename, wanted_id=None):
    """ Load JSON data from file and returns as a list of dictionaries """

    data = []

    if not Path(filename).is_file():
        raise FileNotFoundError(f"Data file '{filename}' missing")

    try:
        with open(filename, 'r') as f:
            rows = json.load(f)

        for row in rows:
            key = str(row['id'])

            if (wanted_id is not None and key == wanted_id) or (wanted_id is None):
                data.append(row)

    except ValueError as exc:
        raise ValueError(f"Unable to load data from file '{filename}'") from exc

    return data

def load_csv_data(filename, wanted_id=None):
    """ Load CSV data from file and returns as a list of dictionaries """

    data = []

    if not Path(filename).is_file():
        raise FileNotFoundError(f"Data file '{filename}' missing")

    try:
        with open(filename, 'r') as csvfile:
            for row in csv.DictReader(csvfile):
                if (wanted_id is not None and row['id'] == wanted_id) or (wanted_id is None):
                    data.append(row)
    except ValueError as exc:
        raise ValueError(f"Unable to load data from file '{filename}'") from exc

    return data

# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

#!/usr/bin/python3
"""contains the class"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    """contains the class"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """contains the class"""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """contains the class"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """contains the class"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """contains the class"""
    user_data = request.json
    username = user_data.get('username')
    if username and username not in users:
        users[username] = {
            "name": user_data.get('name'),
            "age": user_data.get('age'),
            "city": user_data.get('city')
        }
        return jsonify({"message": "User added", "user": users[username]})
    else:
        return jsonify({"error": "Invalid data or user already exists"}), 400


if __name__ == '__main__':
    """contains the class"""
    app.run(debug=True)

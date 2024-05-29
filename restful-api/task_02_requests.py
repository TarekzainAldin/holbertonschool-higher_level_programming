#!/usr/bin/python3
""" API  Python"""


import requests
import json


def fetch_and_print_posts():
    """get all post from JSONPlaceholder"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """get all post from JSONPlaceholder"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        data_to_save = [{'id': post['id'], 'title': post['title'],
                        'body': post['body']} for post in posts]

        import csv
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data_to_save)

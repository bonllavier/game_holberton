#!/usr/bin/python3
"""Module 0-hello_route"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """hello_HBNB - say hello since Holberton School
    Return: string with greeting"""
    return 'Hello to hackpot!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

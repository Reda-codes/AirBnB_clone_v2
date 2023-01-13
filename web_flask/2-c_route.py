#!/usr/bin/python3
'''Flask start module'''
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_route(text):
    return 'C %s' % text.replace('_', ' ')


if __name__ == '__main__':
    app.run()

#!/usr/bin/python3


from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    """returns hello world"""
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
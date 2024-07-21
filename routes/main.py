#!/usr/bin/python3

from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def home():
    """return welcome to Haromy Hub"""
    return "Welcome to Harmony Hub!"

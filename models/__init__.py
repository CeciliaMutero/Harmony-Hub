#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


from models.user import User
from models.song import Song

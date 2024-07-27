#!/usr/bin/python3
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Rating(db.Model):
    """Model for user ratings."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

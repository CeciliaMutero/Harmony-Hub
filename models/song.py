#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Song(db.Model):
    """
    Represents a table in the database to store songs information.
    Attributes:
    id (int): The unique identifier for each song.
    title (str): The title of the song.
    artist (str): The artist or band who performed the song.
    genre (str): The genre or type of music for the song.
    how much people like the song.
    duration (int): The duration of the song in seconds.
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    recommendation_score = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=True)
    release_date = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        """
        Provides a string representation of the song instance.
        """
        return (f"Song(\n"
                f"  title={self.title},\n"
                f"  artist={self.artist},\n"
                f"  genre={self.genre},\n"
                f"  duration={self.duration}\n"
                f"  release_date={self.release_date}\n"
                f")")

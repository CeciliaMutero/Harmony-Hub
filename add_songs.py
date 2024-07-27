#!/usr/bin/python3
from app import app
from models.song import db, Song

with app.app_context():
    new_song = Song(
        title='Umbrella',
        artist='Rihanna',
        genre='Pop',
        recommendation_score=9.5
)
    db.session.add(new_song)
    db.session.commit()

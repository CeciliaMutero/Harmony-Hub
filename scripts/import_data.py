#!/usr/bin/python3
import sys
import os
import pandas as pd


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app import app
from models.song import db, Song


def import_data(file_path):
    """for importing the music records"""
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        return

    data = pd.read_csv(file_path)

    with app.app_context():
        for _, row in data.iterrows():
            song = Song(
                title=row['title'],
                artist=row['artist'],
                genre=row['genre'],
                release_date=row.get('release_date'),
                duration=row.get('duration'),
                recommendation_score=row.get('recommendation_score', 0.0)
            )
            db.session.add(song)
        db.session.commit()


if __name__ == "__main__":
    import_data('/home/ubuntu/Harmony-Hub/spotify_data.csv')

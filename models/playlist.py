#!/usr/bin/python3

class Playlist(db.Model):
    """Model for user playlists."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    songs = db.relationship('Song', secondary='playlist_songs', backref=db.backref('playlists', lazy='dynamic'))


class PlaylistSongs(db.Model):
    """Association table for playlists and songs."""
    __tablename__ = 'playlist_songs'
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('song.id'), primary_key=True)

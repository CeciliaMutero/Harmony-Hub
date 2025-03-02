#!/usr/bin/python3

from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required, current_user
from models.song import Song


main = Blueprint('main', __name__)


@main.route('/')
def home():
    """Returns the homepage"""
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return f'Hello, {current_user.username}!'


@main.route('/recommendations')
def recommendations():
    """Returns a list of recommended songs"""
    songs = Song.query.order_by(Song.recommendation_score.desc()).all()
    return render_template('recommendations.html', songs=songs)


@main.route('/search', methods=['GET', 'POST'])
def search():
    """Allow users to search for songs"""
    query = request.args.get('query', '')
    results = []
    if query:
        results = Song.query.filter(Song.title.like(f'%{query}%')).all()
    return render_template('search.html', query=query, results=results)


@main.route('/rate', methods=['POST'])
def rate():
    """Rate a song."""
    song_id = request.form.get('song_id')
    rating = request.form.get('rating')
    flash('Your rating has been submitted!', 'success')
    return redirect(url_for('main.recommendations'))

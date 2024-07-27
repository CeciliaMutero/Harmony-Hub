#!/usr/bin/python3

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from forms import RegistrationForm, LoginForm
from app import db


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle user registration.
    If the request method is POST and the form is valid,
    create a new user with a hashed password and store it in the database.
    If the method is GET, or if the form is invalid,
    render the registration page.
    Returns:
        str: Rendered template for user registration.
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        # Hash the user's password
        hashed_password = generate_password_hash(
            form.password.data,
            method='sha256'
        )
        # Create a new User object
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )
        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        # Flash a success message
        flash('Your account has been created!', 'success')
        # Redirect to the login page
        return redirect(url_for('auth.login'))
    # Render the registration page with the form
    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
     Handle user login.
     If the request method is POST and the form is valid,
     check if the user exists and if the password matches.
     If valid, log the user in and redirect to the home page.
     Otherwise, flash an error message.
     If the method is GET, or if the form is invalid, render the login page.
     Returns:
        str: Rendered template for user login.
    """
    form = LoginForm()
    if form.validate_on_submit():
        # Query the user by email
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            # Log the user in
            login_user(user, remember=True)
            # Redirect to the home page
            return redirect(url_for('main.home'))
        else:
            # Flash an error message
            flash('Login Unsuccessful. Please check email and password')
    # Render the login page with the form
    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    """
    Handle user logout
    Log the current user out and redirect to the home page
    Returns:
        str: Redirect URL for the home page.
    """
    logout_user()
    # Redirect to the home page
    return redirect(url_for('main.home'))

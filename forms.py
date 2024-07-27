#!/usr/bin/python3

# Import necessary modules from Flask-WTF and WTForms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


# Define the RegistrationForm class, which inherits from FlaskForm
class RegistrationForm(FlaskForm):
    """
    A form for user registration.
    Attributes:
        username (StringField): The username field with a required
        and length validator.
        email (StringField): The email field with a required
        and email format validator.
        password (PasswordField): The password with a required validator.
        submit (SubmitField): The submit button for the form.
    """
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    submit = SubmitField('Sign Up')


# Define the LoginForm class, which also inherits from FlaskForm
class LoginForm(FlaskForm):
    """
    A form for user login.
    Attributes:
        email (StringField): The email field with a required
        and email format validator.
        password (PasswordField): The password field with a required validator.
        submit (SubmitField): The submit button for the form.
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

#!/usr/bin/python3


from flask import Flask
from routes.main import main
from models.song import db
from config import Config
from flask_login import LoginManager
from models.user import User


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


# Set up Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'main.login'


@login_manager.user_loader
def load_user(user_id):
    """
    Load a user from the database given their user ID.
    This function is used by Flask-Login to retrieve a user object from the
    database based on the user ID stored in the session. It is decorated with
    @login_manager.user_loader` to indicate that it should be used by the
    Flask-Login extension for user loading.

    Args:
        user_id (str): The ID of the user to be loaded. Flask-Login provides
                    this ID as a string,
                    so it needs to be converted to an integer
    Returns:
            User: The user object corresponding to the provided user ID,
            or None
            if no user with that ID exists in the database.
    """

    return User.query.get(int(user_id))


app.register_blueprint(main)


@app.route('/')
def home():
    """returns hello world"""
    return "Hello, World!"


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)

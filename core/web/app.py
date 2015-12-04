from flask import Flask

from utils.sql import db


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('CONFIG_PATH')

    # Binding the database connection to the application
    db.init_app(app)

    return app

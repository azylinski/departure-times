from flask import Flask

from utils.elasticsearch import es


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('CONFIG_PATH')

    # Binding the database connection to the application
    es.init_app(app)

    return app

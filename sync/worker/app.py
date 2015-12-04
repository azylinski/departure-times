from flask import Flask

from utils.sql import db
from utils.elasticsearch import es


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('CONFIG_PATH')

    # Binding the database connection to the application
    db.init_app(app)
    es.init_app(app)

    with app.app_context():
        # run only once, to init database
        db.create_all()
        es.verify_mappings()

    return app

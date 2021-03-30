from flask import Flask

from flaskshoes.ext import configuration
from flaskshoes.ext import database

from flaskshoes.resources.users import user_bp


def create_app():
    app = Flask(__name__)

    configuration.init_app(app)
    database.init_app(app)

    app.register_blueprint(user_bp)

    return app

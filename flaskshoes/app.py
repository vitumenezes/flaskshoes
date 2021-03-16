from flask import Flask
from flaskshoes.ext import configuration
from flaskshoes.ext import database

from flaskshoes.blueprints import views

app = Flask(__name__)

configuration.init_app(app)
database.init_app(app)

views.init_app(app)


if __name__ == '__main__':
    app.run()

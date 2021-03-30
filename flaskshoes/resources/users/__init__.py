from flask import Blueprint
from flaskshoes.ext import api

from .views import UserResource

user_bp = Blueprint('user_bp', __name__)
api = api.init_app(user_bp)

api.add_resource(UserResource, '/user', '/user/<int:userid>')

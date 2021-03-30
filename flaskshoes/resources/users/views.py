import json
from flask import jsonify, make_response
from flask_restful import Resource, reqparse

from .models.User import User
from ...ext.database import db

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, type=str)
parser.add_argument('email', required=True, type=str)
parser.add_argument('password', required=True, type=str)


class UserResource(Resource):
    def get(self):
        return {'status': 200}

    def post(self):
        args = parser.parse_args()
        name = args['name']
        email = args['email']
        password = args['password']

        new_user = User(name, email, password)
        db.session.add(new_user)
        db.session.commit()

        new_user = dict(new_user)
        del new_user['password']

        response = make_response(new_user, 201)

        return response

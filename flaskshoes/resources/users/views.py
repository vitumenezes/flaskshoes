from flask_restful import Resource

from .models import User


class UserResource(Resource):
    def get(self):
        return {'status': 200}

from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service


user_ns = Namespace('users')
user_schema = UserSchema()


@user_ns.route('/')
class UsersView(Resource):

    def post(self):
        data = request.json
        return user_schema.dump(user_service.create(data)), 201



from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service, user_service
from service.decorators import auth_required, admin_required

director_ns = Namespace('directors')
director_schema = DirectorSchema()
directors_Schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        return directors_Schema.dump(director_service.get_all()), 200

    @admin_required
    def post(self):
        data = request.json
        return director_schema.dump(director_service.create(data)), 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        return director_schema.dump(director_service.get_one(rid)), 200

    @admin_required
    def put(self, rid):
        data = request.json
        if not data.get('id'):
            data['id'] = rid
        return director_schema.dump(director_service.update(data)), 200

    @admin_required
    def delete(self, rid):
        director_service.delete(rid)
        return "", 204

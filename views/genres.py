from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
from service.decorators import auth_required, admin_required

genre_ns = Namespace('genres')
genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        return genres_schema.dump(genre_service.get_all()), 200

    @admin_required
    def post(self):
        data = request.json
        return genre_schema.dump(genre_service.create(data)), 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        return genre_schema.dump(genre_service.get_one(rid)), 200

    @admin_required
    def put(self, rid):
        data = request.json
        if not data.get('id'):
            data['id'] = rid
        return genre_schema.dump(genre_service.update(data)), 200

    @admin_required
    def delete(self, rid):
        genre_service.delete(rid)
        return "", 204

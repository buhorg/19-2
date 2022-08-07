from flask import Flask
from flask_restx import Api

from config import Config
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.model.user import User
from data.data import data
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    create_data(app, db)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


def create_data(app, db):
    with app.app_context():
        db.drop_all()
        db.create_all()
        movies = data['movies']
        directors = data['directors']
        genres = data['genres']
        users = data['users']
        movies_list = []
        directors_list = []
        genres_list = []
        users_list = []
        for item in movies:
            movies_list.append(Movie(**item))
        for item in directors:
            directors_list.append(Director(**item))
        for item in genres:
            movies_list.append(Genre(**item))
        for item in users:
            users_list.append(User(**item))
        movies_list.extend(directors_list)
        movies_list.extend(genres_list)
        movies_list.extend(users_list)
        with db.session.begin():
            db.session.add_all(movies_list)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)

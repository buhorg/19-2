from dao.user import UserDAO
from service.auth import generate_password_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_data):
        user_data['password'] = generate_password_hash(user_data['password'])
        return self.dao.create(user_data)

    def update(self, user_d):
        return self.dao.update(user_d)

    def delete(self, rid):
        self.dao.delete(rid)

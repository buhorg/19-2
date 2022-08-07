from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(User).get(bid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_id(self, val):
        return self.session.query(User).filter(User.id == val).all()

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).one()

    def create(self, user_data):
        ent = User(**user_data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        if user_d.get("username"):
            user.username = user_d.get("username")
        if user.get("password"):
            user.password = user_d.get("password")
        if user.get("role"):
            user.role = user_d.get("role")
        self.session.add(user)
        self.session.commit()


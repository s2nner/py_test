from flask import jsonify
from api.models import db, User

class Signup(object):
    def simple(self, login, pasw):
        u = User(username=login, password=pasw)
        db.session.add(u)
        db.session.commit()
        return jsonify(user=login)

    def twitter(self):
        pass

    def faisbook(self):
        pass

class Signin(object):
    def simple(self, login, pasw):
        ruser = User.query.filter_by(username=login).first()
        return jsonify(result=ruser is not None and ruser.verify_password(pasw))

    def twitter(self):
        pass

    def faisbook(self):
        pass

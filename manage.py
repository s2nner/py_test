from flask import Flask, g, jsonify
from flask.ext.script import Manager
from api import create_app
from api.models import db, User

manager = Manager(create_app)


@manager.command
def createdb(testdata=False):
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        if testdata:
            u = User(username='test', password='test')
            db.session.add(u)
            db.session.commit()

if __name__ == '__main__':
    manager.run()


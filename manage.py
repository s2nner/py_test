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
            u = User(username='test', password_hash='test')
            db.session.add(u)
            db.session.commit()


@manager.command
def test():
    from subprocess import call
    call(['nosetests', '-v',
          '--with-coverage', '--cover-package=api', '--cover-branches',
          '--cover-erase', '--cover-html', '--cover-html-dir=cover'])

if __name__ == '__main__':
    manager.run()


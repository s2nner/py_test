from os import path

basedir = path.abspath(path.dirname(__file__))

class Config(object):
    DEBUG = False
    PORT = 5000
    HOST = '0.0.0.0'
    URL_PREFIX = '/api'
    PROJECT_ROOT = path.abspath(path.dirname(__file__))
    TEMPLATE_FOLDER = path.join(PROJECT_ROOT, 'templates')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Development(Config):
    DEBUG = True
    SECRET_KEY = 'development'


class Production(Config):
    pass


class Testing(Config):
    TESTING = True
    SECRET_KEY = 'testing'

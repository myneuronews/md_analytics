import os


class BaseConfiguration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/twa.db'.format(APPLICATION_DIR)
    DEBUG = False
    SECRET_KEY = os.urandom(24)
    is_dev = False


class ProdConfiguration(BaseConfiguration):
    DEBUG = False


class DevConfiguration(BaseConfiguration):
    DEBUG = True
    is_dev = True

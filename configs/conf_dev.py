import os
from os import environ
basedir=os.path.abspath(os.path.dirname(__file__))


class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY') if environ.get('SECRET_KEY') else '\x01\x9eDO\x91\x02\xe0XY\xd2\xb1\x8b\x9b\xbdmh\xbf?\xc7#6,\xb0\xd1'
    FLASK_ENV = environ.get('FLASK_ENV')

    # Flask-Assets
    LESS_BIN = environ.get('LESS_BIN')
    ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = environ.get('STATIC_FOLDER')
    TEMPLATES_FOLDER = environ.get('TEMPLATES_FOLDER')
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')



    """Base config vars."""

    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME') if os.environ.get('SESSION_COOKIE_NAME') else "lamtv10_flask_app"

    CONF = {"database": {"connection": "mysql+pymysql://lamtv10:lamtv10@172.16.29.197/auto_lamtv10"}}
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_size":200, "max_overflow":200 }
    #db_engine = db.create_engine(CONF["database"]["connection"])
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        CONF["database"]["connection"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 400
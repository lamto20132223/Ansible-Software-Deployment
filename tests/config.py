import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config(object):
    CONF = {"database": {"connection": "mysql+pymysql://lamtv10:lamtv10@172.16.29.198/auto_lamtv10"}}
    #db_engine = db.create_engine(CONF["database"]["connection"])
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        CONF["database"]["connection"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
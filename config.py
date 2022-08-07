import base64


class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SECRET_KEY = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}
    PWD_HASH_SALT = base64.b64decode('salt')
    PWD_HASH_ITERATIONS = 100000
    TOKEN_EXPIRE_MINUTES = 15
    TOKEN_EXPIRE_DAYS = 130
    ALGORITHM = "HS256"




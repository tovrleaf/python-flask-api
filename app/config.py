import os

class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}:3306/{3}'.format(
        'flask_user', 'flask_password', 'db', 'flask_database'
    )

from apis.config.base import BaseConfig


class DevelopmentConfig(BaseConfig):
    """ 開発環境用 """
    DEBUG = True
    SQLALCHEMY_ECHO = True

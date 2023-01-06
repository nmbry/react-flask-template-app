import logging
import os


class BaseConfig(object):
    """ 共通項目 """
    DEBUG = False
    TESTING = False
    LOG_LEVEL = logging.DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        db_host = os.environ.get('DB_HOST', 'localhost')
        db_port = os.environ.get('DB_PORT', '5432')
        db_name = os.environ.get('DB_NAME', 'postgres')
        db_user = os.environ.get('DB_USER', 'xxx')
        db_pass = os.environ.get('DB_PASS', 'xxx')

        return f"postgresql://{db_host}:{db_port}/{db_name}?={db_user}&password={db_pass}"

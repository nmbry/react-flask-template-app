from apis.config.base import BaseConfig


class TestingConfig(BaseConfig):
    """ テスト環境用 """
    DEBUG = True
    TESTING = True

import os
import pathlib

basedir = pathlib.Path(__file__).parent.parent


class CommonConfig(object):
    """ 共通項目 """
    pass


class LocalConfig(CommonConfig):
    """ ローカル環境 """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', f"sqlite:///{basedir / 'local.sqlite'}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(CommonConfig):
    """ テスト環境 """
    pass


class ReleaseConfig(CommonConfig):
    """ 本番環境 """
    pass


config = {
    'local': LocalConfig,
    'testing': TestingConfig,
    'release': ReleaseConfig,
}

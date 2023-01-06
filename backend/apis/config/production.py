import logging

from apis.config.base import BaseConfig


class ProductionConfig(BaseConfig):
    """ 本番環境用 """
    DATABASE_URI = ''
    LOG_LEVEL = logging.INFO

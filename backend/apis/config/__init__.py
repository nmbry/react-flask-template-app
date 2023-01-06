from apis.config.development import DevelopmentConfig
from apis.config.production import ProductionConfig
from apis.config.testing import TestingConfig

config = {
    # 開発用
    'dev': DevelopmentConfig,

    # 本番用
    'prod': ProductionConfig,

    # テスト用
    'testing': TestingConfig,
}

from apis.config.development import DevelopmentConfig
from apis.config.production import ProductionConfig
from apis.config.testing import TestingConfig

config = {
    # 開発用
    'development': DevelopmentConfig,

    # 本番用
    'production': ProductionConfig,

    # テスト用
    'testing': TestingConfig,
}
